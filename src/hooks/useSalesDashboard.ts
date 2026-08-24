import { useState, useEffect, useMemo, useCallback } from 'react';
import { fetchSalesDashboardData } from '@/services/salesDashboard';
import {
  SaleRecord,
  FilterState,
  ApiStatus,
  DashboardMetrics,
  TimeSeriesPoint,
  CategoryBreakdown,
  ProductPerformance,
  SalespersonPerformance,
  StatusDistribution,
  PaymentMethodDistribution,
  DimensionAvailability
} from '@/types/sales';
import {
  filterSalesData,
  calculateMetrics,
  aggregateTimeSeries,
  aggregateCategories,
  aggregateTopProducts,
  aggregateSalespersons,
  aggregateStatusDistribution,
  aggregatePaymentMethods,
  detectDimensions,
  exportToCSV
} from '@/utils/dataProcessor';

const INITIAL_FILTERS: FilterState = {
  search: '',
  dateRange: 'all',
  startDate: '',
  endDate: '',
  category: 'all',
  status: 'all',
  salesperson: 'all',
  paymentMethod: 'all',
  region: 'all',
};

export function useSalesDashboard() {
  const [rawData, setRawData] = useState<SaleRecord[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [isRefreshing, setIsRefreshing] = useState<boolean>(false);
  const [apiStatus, setApiStatus] = useState<ApiStatus | null>(null);
  const [filters, setFilters] = useState<FilterState>(INITIAL_FILTERS);
  const [timeInterval, setTimeInterval] = useState<'daily' | 'weekly' | 'monthly'>('daily');

  const loadData = useCallback(async (isManualRefresh = false) => {
    if (isManualRefresh) {
      setIsRefreshing(true);
    } else {
      setLoading(true);
    }

    try {
      const result = await fetchSalesDashboardData();
      setRawData(result.data);
      setApiStatus(result.status);
    } catch (err: unknown) {
      console.error('Error fetching dashboard data:', err);
    } finally {
      setLoading(false);
      setIsRefreshing(false);
    }
  }, []);

  useEffect(() => {
    loadData();
  }, [loadData]);

  const updateFilter = useCallback(<K extends keyof FilterState>(key: K, value: FilterState[K]) => {
    setFilters(prev => ({ ...prev, [key]: value }));
  }, []);

  const resetFilters = useCallback(() => {
    setFilters(INITIAL_FILTERS);
  }, []);

  // Filtered dataset
  const filteredData = useMemo(() => {
    return filterSalesData(rawData, filters);
  }, [rawData, filters]);

  // Dimension capabilities
  const dimensions: DimensionAvailability = useMemo(() => {
    return detectDimensions(rawData);
  }, [rawData]);

  // Derived filter choices
  const filterOptions = useMemo(() => {
    const categories = Array.from(new Set(rawData.map(r => r.category).filter(Boolean))) as string[];
    const statuses = Array.from(new Set(rawData.map(r => r.status).filter(Boolean))) as string[];
    const salespersons = Array.from(new Set(rawData.map(r => r.salesperson).filter(Boolean))) as string[];
    const paymentMethods = Array.from(new Set(rawData.map(r => r.payment_method).filter(Boolean))) as string[];
    const regions = Array.from(new Set(rawData.map(r => r.region).filter(Boolean))) as string[];

    return {
      categories: categories.sort(),
      statuses: statuses.sort(),
      salespersons: salespersons.sort(),
      paymentMethods: paymentMethods.sort(),
      regions: regions.sort(),
    };
  }, [rawData]);

  // Metrics
  const metrics: DashboardMetrics = useMemo(() => {
    return calculateMetrics(filteredData);
  }, [filteredData]);

  // Time Series
  const timeSeries: TimeSeriesPoint[] = useMemo(() => {
    return aggregateTimeSeries(filteredData, timeInterval);
  }, [filteredData, timeInterval]);

  // Category breakdown
  const categoryBreakdown: CategoryBreakdown[] = useMemo(() => {
    return aggregateCategories(filteredData);
  }, [filteredData]);

  // Top products
  const topProducts: ProductPerformance[] = useMemo(() => {
    return aggregateTopProducts(filteredData, 10);
  }, [filteredData]);

  // Salespersons
  const salespersons: SalespersonPerformance[] = useMemo(() => {
    return aggregateSalespersons(filteredData);
  }, [filteredData]);

  // Status Distribution
  const statusDistribution: StatusDistribution[] = useMemo(() => {
    return aggregateStatusDistribution(filteredData);
  }, [filteredData]);

  // Payment Distribution
  const paymentDistribution: PaymentMethodDistribution[] = useMemo(() => {
    return aggregatePaymentMethods(filteredData);
  }, [filteredData]);

  const handleExportCSV = useCallback(() => {
    const timestamp = new Date().toISOString().split('T')[0];
    exportToCSV(filteredData, `salespulse_export_${timestamp}.csv`);
  }, [filteredData]);

  return {
    rawData,
    filteredData,
    loading,
    isRefreshing,
    apiStatus,
    filters,
    filterOptions,
    dimensions,
    metrics,
    timeSeries,
    timeInterval,
    categoryBreakdown,
    topProducts,
    salespersons,
    statusDistribution,
    paymentDistribution,
    setTimeInterval,
    updateFilter,
    resetFilters,
    refetch: () => loadData(true),
    exportCSV: handleExportCSV,
  };
}
