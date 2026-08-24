import React, { useState } from 'react';
import {
  DashboardMetrics,
  TimeSeriesPoint,
  CategoryBreakdown,
  ProductPerformance,
  SalespersonPerformance,
  StatusDistribution,
  PaymentMethodDistribution,
  SaleRecord,
  DimensionAvailability
} from '@/types/sales';
import { KPICards } from '@/components/dashboard/KPICards';
import { SalesTrendChart } from '@/components/charts/SalesTrendChart';
import { CategoryChart } from '@/components/charts/CategoryChart';
import { TopProductsChart } from '@/components/charts/TopProductsChart';
import { SalespersonPerformanceChart } from '@/components/charts/SalespersonPerformanceChart';
import { StatusDistributionChart } from '@/components/charts/StatusDistributionChart';
import { SalesTable } from '@/components/dashboard/SalesTable';
import { SalesDetailModal } from '@/components/dashboard/SalesDetailModal';

interface DashboardViewProps {
  metrics: DashboardMetrics;
  timeSeries: TimeSeriesPoint[];
  timeInterval: 'daily' | 'weekly' | 'monthly';
  onTimeIntervalChange: (interval: 'daily' | 'weekly' | 'monthly') => void;
  categoryBreakdown: CategoryBreakdown[];
  topProducts: ProductPerformance[];
  salespersons: SalespersonPerformance[];
  statusDistribution: StatusDistribution[];
  paymentDistribution: PaymentMethodDistribution[];
  filteredData: SaleRecord[];
  dimensions: DimensionAvailability;
  onExportCSV: () => void;
}

export const DashboardView: React.FC<DashboardViewProps> = ({
  metrics,
  timeSeries,
  timeInterval,
  onTimeIntervalChange,
  categoryBreakdown,
  topProducts,
  salespersons,
  statusDistribution,
  paymentDistribution,
  filteredData,
  dimensions,
  onExportCSV,
}) => {
  const [selectedRecord, setSelectedRecord] = useState<SaleRecord | null>(null);

  return (
    <div className="space-y-6">
      {/* KPI Cards Header */}
      <KPICards metrics={metrics} />

      {/* Main Charts Row */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2">
          <SalesTrendChart
            data={timeSeries}
            interval={timeInterval}
            onIntervalChange={onTimeIntervalChange}
          />
        </div>
        <div>
          <CategoryChart data={categoryBreakdown} />
        </div>
      </div>

      {/* Secondary Row: Products & Sales Team */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className={dimensions.hasSalespersons ? 'lg:col-span-2' : 'lg:col-span-3'}>
          <TopProductsChart products={topProducts} />
        </div>
        {dimensions.hasSalespersons && (
          <div>
            <SalespersonPerformanceChart salespersons={salespersons} />
          </div>
        )}
      </div>

      {/* Fulfillment Status & Payment Distribution */}
      <StatusDistributionChart
        statusData={statusDistribution}
        paymentData={paymentDistribution}
      />

      {/* Full Underlying Sales Table */}
      <SalesTable
        data={filteredData}
        onSelectRecord={setSelectedRecord}
        onExport={onExportCSV}
      />

      {/* Record Inspection Modal */}
      <SalesDetailModal
        record={selectedRecord}
        onClose={() => setSelectedRecord(null)}
      />
    </div>
  );
};
