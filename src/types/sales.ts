export interface SaleRecord {
  id: string | number;
  order_id: string;
  date: string;
  amount: number;
  customer_name?: string;
  customer_email?: string;
  customer_city?: string;
  product_name?: string;
  product_id?: string;
  category?: string;
  salesperson?: string;
  quantity?: number;
  unit_price?: number;
  status: 'completed' | 'pending' | 'cancelled' | 'refunded' | string;
  payment_method?: 'Credit Card' | 'UPI' | 'Net Banking' | 'Debit Card' | 'Cash' | string;
  region?: string;
  discount?: number;
  notes?: string;
  [key: string]: unknown;
}

export interface DashboardMetrics {
  totalSales: number;
  totalOrders: number;
  averageOrderValue: number;
  totalUnits: number;
  salesChange: number; // percentage change
  ordersChange: number;
  aovChange: number;
  unitsChange: number;
  topProduct: { name: string; sales: number; units: number } | null;
  topCategory: { name: string; sales: number; percentage: number } | null;
  topSalesperson: { name: string; sales: number; deals: number } | null;
}

export interface FilterState {
  search: string;
  dateRange: 'all' | '7d' | '30d' | '90d' | 'this_month' | 'last_month' | 'this_year' | 'custom';
  startDate: string;
  endDate: string;
  category: string;
  status: string;
  salesperson: string;
  paymentMethod: string;
  region: string;
}

export interface TimeSeriesPoint {
  date: string;
  label: string;
  sales: number;
  orders: number;
  aov: number;
  units: number;
}

export interface CategoryBreakdown {
  name: string;
  sales: number;
  count: number;
  percentage: number;
  color: string;
}

export interface ProductPerformance {
  id: string;
  name: string;
  category: string;
  sales: number;
  units: number;
  averagePrice: number;
  orderCount: number;
}

export interface SalespersonPerformance {
  name: string;
  sales: number;
  deals: number;
  aov: number;
  target: number;
  completion: number;
}

export interface StatusDistribution {
  name: string;
  count: number;
  sales: number;
  percentage: number;
  color: string;
}

export interface PaymentMethodDistribution {
  name: string;
  count: number;
  sales: number;
  percentage: number;
}

export interface DimensionAvailability {
  hasCustomers: boolean;
  hasSalespersons: boolean;
  hasCategories: boolean;
  hasProducts: boolean;
  hasStatus: boolean;
  hasPaymentMethods: boolean;
  hasRegions: boolean;
  hasQuantity: boolean;
}

export interface ApiStatus {
  source: 'live' | 'demo';
  isConnected: boolean;
  isConnecting: boolean;
  lastFetched: Date | null;
  error: string | null;
  endpoint: string;
  statusMessage: string;
  rawSample?: unknown;
}
