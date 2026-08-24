import os

def write_file(rel_path, content):
    full_path = os.path.join(os.path.dirname(__file__), rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Wrote {rel_path}')

# 1. src/components/ui/StatusBadge.tsx
write_file('src/components/ui/StatusBadge.tsx', '''import React from 'react';

interface StatusBadgeProps {
  status: string;
  size?: 'sm' | 'md';
}

export const StatusBadge: React.FC<StatusBadgeProps> = ({ status, size = 'md' }) => {
  const s = (status || 'completed').toLowerCase();

  let bg = 'bg-slate-800/80 text-slate-300 border-slate-700';
  let dot = 'bg-slate-400';

  if (s === 'completed' || s === 'success' || s === 'delivered' || s === 'paid') {
    bg = 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20';
    dot = 'bg-emerald-400';
  } else if (s === 'pending' || s === 'processing' || s === 'in_transit') {
    bg = 'bg-amber-500/10 text-amber-400 border-amber-500/20';
    dot = 'bg-amber-400';
  } else if (s === 'refunded' || s === 'returned') {
    bg = 'bg-indigo-500/10 text-indigo-400 border-indigo-500/20';
    dot = 'bg-indigo-400';
  } else if (s === 'cancelled' || s === 'failed') {
    bg = 'bg-rose-500/10 text-rose-400 border-rose-500/20';
    dot = 'bg-rose-400';
  }

  const padding = size === 'sm' ? 'px-2 py-0.5 text-xs' : 'px-2.5 py-1 text-xs';

  return (
    <span className={`inline-flex items-center gap-1.5 font-medium rounded-full border ${bg} ${padding}`}>
      <span className={`w-1.5 h-1.5 rounded-full ${dot}`} />
      <span className="capitalize">{s}</span>
    </span>
  );
};
''')

# 2. src/components/ui/LoadingSkeleton.tsx
write_file('src/components/ui/LoadingSkeleton.tsx', '''import React from 'react';

export const LoadingSkeleton: React.FC = () => {
  return (
    <div className="space-y-6 animate-pulse p-6">
      {/* Top Banner Skeleton */}
      <div className="h-10 bg-slate-800/60 rounded-xl w-1/3" />

      {/* KPI Cards Skeleton */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {[1, 2, 3, 4].map(i => (
          <div key={i} className="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-5 space-y-3">
            <div className="flex justify-between items-center">
              <div className="h-4 bg-slate-800 rounded w-24" />
              <div className="w-8 h-8 rounded-lg bg-slate-800" />
            </div>
            <div className="h-8 bg-slate-800 rounded w-36" />
            <div className="h-3 bg-slate-800 rounded w-20" />
          </div>
        ))}
      </div>

      {/* Charts Grid Skeleton */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 bg-slate-900/60 border border-slate-800/80 rounded-2xl p-5 h-80 flex flex-col justify-between">
          <div className="h-5 bg-slate-800 rounded w-40" />
          <div className="h-48 bg-slate-800/40 rounded-xl" />
        </div>
        <div className="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-5 h-80 flex flex-col justify-between">
          <div className="h-5 bg-slate-800 rounded w-36" />
          <div className="w-40 h-40 mx-auto rounded-full bg-slate-800/40" />
        </div>
      </div>

      {/* Table Skeleton */}
      <div className="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-5 space-y-4">
        <div className="h-5 bg-slate-800 rounded w-48" />
        <div className="space-y-2">
          {[1, 2, 3, 4, 5].map(i => (
            <div key={i} className="h-12 bg-slate-800/40 rounded-lg" />
          ))}
        </div>
      </div>
    </div>
  );
};
''')

# 3. src/components/ui/EmptyState.tsx
write_file('src/components/ui/EmptyState.tsx', '''import React from 'react';
import { ShoppingBag, RotateCcw } from 'lucide-react';

interface EmptyStateProps {
  title?: string;
  description?: string;
  onResetFilters?: () => void;
}

export const EmptyState: React.FC<EmptyStateProps> = ({
  title = 'No sales records found',
  description = 'There are no sales transactions matching the currently active filter criteria. Try expanding your date range or clearing search filters.',
  onResetFilters,
}) => {
  return (
    <div className="flex flex-col items-center justify-center p-12 text-center bg-slate-900/40 border border-slate-800/80 rounded-2xl">
      <div className="w-16 h-16 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400 mb-4 shadow-inner">
        <ShoppingBag className="w-8 h-8" />
      </div>
      <h3 className="text-lg font-semibold text-slate-100 mb-1">{title}</h3>
      <p className="text-sm text-slate-400 max-w-md mb-6">{description}</p>
      {onResetFilters && (
        <button
          onClick={onResetFilters}
          className="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-slate-200 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded-xl transition-all shadow-sm"
        >
          <RotateCcw className="w-4 h-4" />
          Reset All Filters
        </button>
      )}
    </div>
  );
};
''')

# 4. src/components/ui/ErrorState.tsx
write_file('src/components/ui/ErrorState.tsx', '''import React from 'react';
import { AlertCircle, RefreshCw, Settings, ShieldAlert } from 'lucide-react';

interface ErrorStateProps {
  message: string;
  endpoint?: string;
  onRetry: () => void;
  onOpenSettings?: () => void;
}

export const ErrorState: React.FC<ErrorStateProps> = ({
  message,
  endpoint,
  onRetry,
  onOpenSettings,
}) => {
  return (
    <div className="p-6">
      <div className="bg-rose-950/20 border border-rose-800/30 rounded-2xl p-6 md:p-8 max-w-3xl mx-auto shadow-xl">
        <div className="flex items-start gap-4">
          <div className="p-3 bg-rose-500/10 rounded-xl border border-rose-500/20 text-rose-400 shrink-0">
            <ShieldAlert className="w-7 h-7" />
          </div>
          <div className="space-y-3 flex-1">
            <div>
              <h3 className="text-lg font-semibold text-rose-200">Supabase RPC Connection Alert</h3>
              <p className="text-sm text-rose-300/80 mt-1">
                Unable to establish a direct connection to the Supabase RPC endpoint.
              </p>
            </div>

            <div className="p-3.5 bg-slate-900/80 border border-slate-800 rounded-xl font-mono text-xs text-slate-300 break-all space-y-1">
              {endpoint && <div className="text-slate-400"><span className="text-slate-500">Target:</span> {endpoint}</div>}
              <div><span className="text-slate-500">Details:</span> {message}</div>
            </div>

            <div className="text-xs text-slate-400 space-y-1 bg-slate-900/40 p-3 rounded-lg border border-slate-800/50">
              <p className="font-semibold text-slate-300">Potential Causes:</p>
              <ul className="list-disc list-inside space-y-0.5 text-slate-400">
                <li>The Supabase free-tier project is currently paused due to inactivity.</li>
                <li>Custom network/firewall policies blocking direct DNS resolution.</li>
                <li>The RPC function name or schema signature differs on the target project.</li>
              </ul>
            </div>

            <div className="flex flex-wrap items-center gap-3 pt-2">
              <button
                onClick={onRetry}
                className="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-500 rounded-xl shadow-lg shadow-indigo-600/20 transition-all"
              >
                <RefreshCw className="w-4 h-4" />
                Retry Connection
              </button>

              {onOpenSettings && (
                <button
                  onClick={onOpenSettings}
                  className="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-slate-200 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded-xl transition-all"
                >
                  <Settings className="w-4 h-4" />
                  Configure Supabase Endpoint
                </button>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
''')

# 5. src/components/layout/Sidebar.tsx
write_file('src/components/layout/Sidebar.tsx', '''import React from 'react';
import {
  BarChart3,
  ShoppingBag,
  Package,
  Users,
  FileText,
  Settings,
  ChevronLeft,
  ChevronRight,
  TrendingUp,
  Database,
  X
} from 'lucide-react';
import { ApiStatus } from '@/types/sales';

export type TabType = 'dashboard' | 'sales' | 'products' | 'customers' | 'reports' | 'settings';

interface SidebarProps {
  activeTab: TabType;
  setActiveTab: (tab: TabType) => void;
  collapsed: boolean;
  setCollapsed: (collapsed: boolean) => void;
  mobileOpen: boolean;
  setMobileOpen: (open: boolean) => void;
  apiStatus: ApiStatus | null;
  hasCustomers: boolean;
}

export const Sidebar: React.FC<SidebarProps> = ({
  activeTab,
  setActiveTab,
  collapsed,
  setCollapsed,
  mobileOpen,
  setMobileOpen,
  apiStatus,
  hasCustomers,
}) => {
  const navItems = [
    { id: 'dashboard' as TabType, label: 'Dashboard', icon: BarChart3 },
    { id: 'sales' as TabType, label: 'Sales Transactions', icon: ShoppingBag },
    { id: 'products' as TabType, label: 'Products', icon: Package },
    ...(hasCustomers ? [{ id: 'customers' as TabType, label: 'Customers & Team', icon: Users }] : []),
    { id: 'reports' as TabType, label: 'Reports', icon: FileText },
    { id: 'settings' as TabType, label: 'API & Settings', icon: Settings },
  ];

  const sidebarContent = (
    <div className="flex flex-col h-full bg-slate-950 border-r border-slate-800/80 text-slate-300 select-none">
      {/* Brand Header */}
      <div className="flex items-center justify-between p-4 border-b border-slate-800/80 h-16">
        <div className="flex items-center gap-3 overflow-hidden">
          <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-indigo-600 to-violet-500 flex items-center justify-center text-white shadow-lg shadow-indigo-600/30 shrink-0">
            <TrendingUp className="w-5 h-5" />
          </div>
          {!collapsed && (
            <div className="truncate">
              <span className="font-bold text-base tracking-tight text-white block leading-none">SalesPulse</span>
              <span className="text-[11px] font-medium text-indigo-400 uppercase tracking-wider block mt-1">Analytics BI</span>
            </div>
          )}
        </div>

        {/* Mobile close */}
        <button
          onClick={() => setMobileOpen(false)}
          className="lg:hidden p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Desktop Collapse Toggle */}
        <button
          onClick={() => setCollapsed(!collapsed)}
          className="hidden lg:flex p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800/80 transition-colors"
          title={collapsed ? 'Expand Sidebar' : 'Collapse Sidebar'}
        >
          {collapsed ? <ChevronRight className="w-4 h-4" /> : <ChevronLeft className="w-4 h-4" />}
        </button>
      </div>

      {/* Navigation Links */}
      <nav className="flex-1 p-3 space-y-1.5 overflow-y-auto">
        <div className={`text-[11px] font-semibold tracking-wider text-slate-500 uppercase px-3 py-1.5 ${collapsed ? 'text-center' : ''}`}>
          {collapsed ? '•••' : 'Main Navigation'}
        </div>
        {navItems.map(item => {
          const Icon = item.icon;
          const isActive = activeTab === item.id;
          return (
            <button
              key={item.id}
              onClick={() => {
                setActiveTab(item.id);
                setMobileOpen(false);
              }}
              className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl font-medium text-sm transition-all ${
                isActive
                  ? 'bg-indigo-600/15 text-indigo-400 border border-indigo-500/20 shadow-sm shadow-indigo-500/10'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900 border border-transparent'
              } ${collapsed ? 'justify-center px-0' : ''}`}
              title={collapsed ? item.label : undefined}
            >
              <Icon className={`w-5 h-5 shrink-0 ${isActive ? 'text-indigo-400' : 'text-slate-400'}`} />
              {!collapsed && <span className="truncate">{item.label}</span>}
              {!collapsed && isActive && (
                <div className="w-1.5 h-1.5 rounded-full bg-indigo-400 ml-auto" />
              )}
            </button>
          );
        })}
      </nav>

      {/* Connection Pill Status */}
      <div className="p-3 border-t border-slate-800/80 bg-slate-950/80">
        <div className={`p-3 rounded-xl border ${
          apiStatus?.source === 'live'
            ? 'bg-emerald-500/5 border-emerald-500/20 text-emerald-400'
            : 'bg-indigo-500/5 border-indigo-500/20 text-indigo-300'
        } flex items-center gap-2.5`}>
          <div className="relative shrink-0">
            <Database className="w-4 h-4" />
            <span className={`absolute -top-0.5 -right-0.5 w-2 h-2 rounded-full ${
              apiStatus?.source === 'live' ? 'bg-emerald-400 ring-2 ring-emerald-950 animate-pulse' : 'bg-indigo-400 ring-2 ring-indigo-950'
            }`} />
          </div>
          {!collapsed && (
            <div className="overflow-hidden">
              <div className="text-xs font-semibold truncate">
                {apiStatus?.source === 'live' ? 'Live Supabase RPC' : 'Active Demo Mode'}
              </div>
              <div className="text-[10px] text-slate-400 truncate">
                {apiStatus?.source === 'live' ? 'Connected & Verified' : 'Free tier paused (demo active)'}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );

  return (
    <>
      {/* Desktop Sidebar */}
      <aside className={`hidden lg:block h-screen sticky top-0 transition-all duration-300 z-30 ${
        collapsed ? 'w-20' : 'w-64'
      }`}>
        {sidebarContent}
      </aside>

      {/* Mobile Drawer Overlay */}
      {mobileOpen && (
        <div className="lg:hidden fixed inset-0 z-50 flex">
          <div
            className="fixed inset-0 bg-slate-950/80 backdrop-blur-sm transition-opacity"
            onClick={() => setMobileOpen(false)}
          />
          <div className="relative w-72 max-w-[80vw] h-full shadow-2xl z-10 animate-in slide-in-from-left duration-200">
            {sidebarContent}
          </div>
        </div>
      )}
    </>
  );
};
''')

# 6. src/components/layout/Header.tsx
write_file('src/components/layout/Header.tsx', '''import React from 'react';
import {
  RefreshCw,
  Download,
  Settings,
  Menu,
  Database,
  Calendar,
  Layers,
  Sparkles
} from 'lucide-react';
import { ApiStatus, FilterState } from '@/types/sales';

interface HeaderProps {
  title: string;
  subtitle?: string;
  isRefreshing: boolean;
  onRefresh: () => void;
  onExport: () => void;
  onOpenSettings: () => void;
  onOpenApiInspector: () => void;
  onOpenMobileMenu: () => void;
  apiStatus: ApiStatus | null;
  filters: FilterState;
  totalFilteredCount: number;
}

export const Header: React.FC<HeaderProps> = ({
  title,
  subtitle = 'Real-time sales intelligence & revenue analytics',
  isRefreshing,
  onRefresh,
  onExport,
  onOpenSettings,
  onOpenApiInspector,
  onOpenMobileMenu,
  apiStatus,
  filters,
  totalFilteredCount,
}) => {
  const getFilterDateLabel = () => {
    switch (filters.dateRange) {
      case '7d': return 'Last 7 Days';
      case '30d': return 'Last 30 Days';
      case '90d': return 'Last 90 Days';
      case 'this_month': return 'This Month';
      case 'last_month': return 'Last Month';
      case 'this_year': return 'This Year';
      case 'custom': return 'Custom Range';
      default: return 'All Time';
    }
  };

  return (
    <header className="sticky top-0 z-20 bg-slate-950/80 backdrop-blur-md border-b border-slate-800/80 px-4 lg:px-8 py-3.5 flex flex-col md:flex-row md:items-center justify-between gap-4">
      {/* Title & Mobile Hamburger */}
      <div className="flex items-center gap-3">
        <button
          onClick={onOpenMobileMenu}
          className="lg:hidden p-2 text-slate-400 hover:text-white rounded-xl bg-slate-900 border border-slate-800"
        >
          <Menu className="w-5 h-5" />
        </button>

        <div>
          <div className="flex items-center gap-2.5">
            <h1 className="text-xl font-bold text-white tracking-tight">{title}</h1>
            <span className="text-xs px-2.5 py-0.5 rounded-full font-medium bg-slate-800 text-slate-300 border border-slate-700">
              {totalFilteredCount} records
            </span>
          </div>
          <p className="text-xs text-slate-400 hidden sm:block mt-0.5">{subtitle}</p>
        </div>
      </div>

      {/* Action Buttons & Status Indicators */}
      <div className="flex items-center flex-wrap gap-2.5">
        {/* Date preset indicator */}
        <div className="hidden sm:flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-slate-300 bg-slate-900 border border-slate-800 rounded-xl">
          <Calendar className="w-3.5 h-3.5 text-indigo-400" />
          <span>{getFilterDateLabel()}</span>
        </div>

        {/* API Status Badge */}
        <button
          onClick={onOpenApiInspector}
          className={`flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium rounded-xl border transition-all ${
            apiStatus?.source === 'live'
              ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20 hover:bg-emerald-500/20'
              : 'bg-indigo-500/10 text-indigo-300 border-indigo-500/20 hover:bg-indigo-500/20'
          }`}
          title="Inspect API Payload & Schema"
        >
          <span className={`w-2 h-2 rounded-full ${apiStatus?.source === 'live' ? 'bg-emerald-400 animate-pulse' : 'bg-indigo-400'}`} />
          <span>{apiStatus?.source === 'live' ? 'Live Supabase' : 'Demo Dataset'}</span>
        </button>

        {/* Refresh Button */}
        <button
          onClick={onRefresh}
          disabled={isRefreshing}
          className="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-slate-200 bg-slate-900 hover:bg-slate-800 border border-slate-800 hover:border-slate-700 rounded-xl transition-all disabled:opacity-60 shadow-sm"
          title="Re-query Supabase RPC"
        >
          <RefreshCw className={`w-3.5 h-3.5 text-indigo-400 ${isRefreshing ? 'animate-spin' : ''}`} />
          <span>{isRefreshing ? 'Refreshing...' : 'Refresh'}</span>
        </button>

        {/* Export CSV Button */}
        <button
          onClick={onExport}
          className="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-slate-200 bg-slate-900 hover:bg-slate-800 border border-slate-800 hover:border-slate-700 rounded-xl transition-all shadow-sm"
          title="Export Filtered Transactions to CSV"
        >
          <Download className="w-3.5 h-3.5 text-slate-400" />
          <span className="hidden sm:inline">Export CSV</span>
        </button>

        {/* Settings Button */}
        <button
          onClick={onOpenSettings}
          className="p-1.5 text-slate-400 hover:text-white bg-slate-900 hover:bg-slate-800 border border-slate-800 rounded-xl transition-colors"
          title="API Connection Settings"
        >
          <Settings className="w-4 h-4" />
        </button>
      </div>
    </header>
  );
};
''')

# 7. src/components/dashboard/KPICards.tsx
write_file('src/components/dashboard/KPICards.tsx', '''import React from 'react';
import {
  DollarSign,
  ShoppingBag,
  TrendingUp,
  TrendingDown,
  Layers,
  Award,
  Sparkles,
  ArrowUpRight,
  ArrowDownRight,
  Tag
} from 'lucide-react';
import { DashboardMetrics } from '@/types/sales';
import { formatCurrency, formatNumber, formatPercentage } from '@/utils/formatters';

interface KPICardsProps {
  metrics: DashboardMetrics;
}

export const KPICards: React.FC<KPICardsProps> = ({ metrics }) => {
  const cards = [
    {
      id: 'total_sales',
      name: 'Total Revenue',
      value: formatCurrency(metrics.totalSales, 'INR'),
      change: metrics.salesChange,
      subtext: 'vs previous period',
      icon: DollarSign,
      color: 'from-indigo-500/20 to-blue-500/5',
      iconColor: 'text-indigo-400 bg-indigo-500/10 border-indigo-500/20',
      accentColor: 'border-indigo-500/30',
    },
    {
      id: 'total_orders',
      name: 'Total Orders',
      value: `${formatNumber(metrics.totalOrders)} Orders`,
      change: metrics.ordersChange,
      subtext: 'completed transactions',
      icon: ShoppingBag,
      color: 'from-sky-500/20 to-cyan-500/5',
      iconColor: 'text-sky-400 bg-sky-500/10 border-sky-500/20',
      accentColor: 'border-sky-500/30',
    },
    {
      id: 'average_order',
      name: 'Average Order Value (AOV)',
      value: formatCurrency(metrics.averageOrderValue, 'INR'),
      change: metrics.aovChange,
      subtext: 'per transaction average',
      icon: TrendingUp,
      color: 'from-emerald-500/20 to-teal-500/5',
      iconColor: 'text-emerald-400 bg-emerald-500/10 border-emerald-500/20',
      accentColor: 'border-emerald-500/30',
    },
    {
      id: 'total_units',
      name: 'Units Sold',
      value: `${formatNumber(metrics.totalUnits)} Items`,
      change: metrics.unitsChange,
      subtext: 'product volume delivered',
      icon: Layers,
      color: 'from-purple-500/20 to-pink-500/5',
      iconColor: 'text-purple-400 bg-purple-500/10 border-purple-500/20',
      accentColor: 'border-purple-500/30',
    },
    ...(metrics.topProduct ? [{
      id: 'top_product',
      name: 'Top Grossing Product',
      value: metrics.topProduct.name,
      subtext: `${formatCurrency(metrics.topProduct.sales, 'INR')} (${metrics.topProduct.units} units)`,
      icon: Award,
      color: 'from-amber-500/20 to-orange-500/5',
      iconColor: 'text-amber-400 bg-amber-500/10 border-amber-500/20',
      accentColor: 'border-amber-500/30',
      isSpecial: true,
    }] : []),
    ...(metrics.topCategory ? [{
      id: 'top_category',
      name: 'Top Category',
      value: metrics.topCategory.name,
      subtext: `${formatPercentage(metrics.topCategory.percentage)} total volume`,
      icon: Tag,
      color: 'from-rose-500/20 to-pink-500/5',
      iconColor: 'text-rose-400 bg-rose-500/10 border-rose-500/20',
      accentColor: 'border-rose-500/30',
      isSpecial: true,
    }] : []),
  ];

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-4">
      {cards.map(card => {
        const Icon = card.icon;
        const isPositive = card.change !== undefined && card.change >= 0;

        return (
          <div
            key={card.id}
            className={`relative overflow-hidden rounded-2xl bg-slate-900/80 border ${card.accentColor} p-4 flex flex-col justify-between shadow-lg shadow-black/20 hover:border-slate-700 transition-all group`}
          >
            {/* Ambient background glow */}
            <div className={`absolute top-0 right-0 w-32 h-32 bg-gradient-to-bl ${card.color} rounded-full blur-2xl pointer-events-none -mr-10 -mt-10 opacity-70 group-hover:opacity-100 transition-opacity`} />

            {/* Top row */}
            <div className="flex items-center justify-between mb-3 relative z-10">
              <span className="text-xs font-medium text-slate-400 truncate max-w-[130px]">{card.name}</span>
              <div className={`w-8 h-8 rounded-xl flex items-center justify-center border ${card.iconColor}`}>
                <Icon className="w-4 h-4" />
              </div>
            </div>

            {/* Main Value */}
            <div className="relative z-10 my-1">
              <div className="text-lg font-bold text-white tracking-tight truncate" title={String(card.value)}>
                {card.value}
              </div>
            </div>

            {/* Bottom Row / Metric change */}
            <div className="flex items-center justify-between mt-2 pt-2 border-t border-slate-800/60 relative z-10 text-[11px]">
              {card.change !== undefined ? (
                <div className="flex items-center gap-1">
                  <span className={`inline-flex items-center font-semibold ${isPositive ? 'text-emerald-400' : 'text-rose-400'}`}>
                    {isPositive ? <ArrowUpRight className="w-3 h-3" /> : <ArrowDownRight className="w-3 h-3" />}
                    {formatPercentage(Math.abs(card.change), false)}
                  </span>
                  <span className="text-slate-500 truncate">{card.subtext}</span>
                </div>
              ) : (
                <span className="text-slate-400 truncate font-medium">{card.subtext}</span>
              )}
            </div>
          </div>
        );
      })}
    </div>
  );
};
''')

# 8. src/components/dashboard/FilterToolbar.tsx
write_file('src/components/dashboard/FilterToolbar.tsx', '''import React from 'react';
import {
  Search,
  RotateCcw,
  SlidersHorizontal,
  X,
  Calendar,
  Filter,
  Check
} from 'lucide-react';
import { FilterState, DimensionAvailability } from '@/types/sales';

interface FilterToolbarProps {
  filters: FilterState;
  onUpdateFilter: <K extends keyof FilterState>(key: K, value: FilterState[K]) => void;
  onResetFilters: () => void;
  filterOptions: {
    categories: string[];
    statuses: string[];
    salespersons: string[];
    paymentMethods: string[];
    regions: string[];
  };
  dimensions: DimensionAvailability;
  totalResults: number;
}

export const FilterToolbar: React.FC<FilterToolbarProps> = ({
  filters,
  onUpdateFilter,
  onResetFilters,
  filterOptions,
  dimensions,
  totalResults,
}) => {
  const datePresets: Array<{ id: FilterState['dateRange']; label: string }> = [
    { id: 'all', label: 'All Time' },
    { id: '7d', label: '7D' },
    { id: '30d', label: '30D' },
    { id: '90d', label: '90D' },
    { id: 'this_month', label: 'This Month' },
    { id: 'this_year', label: 'This Year' },
  ];

  const hasActiveFilters = 
    filters.search !== '' ||
    filters.dateRange !== 'all' ||
    filters.category !== 'all' ||
    filters.status !== 'all' ||
    filters.salesperson !== 'all' ||
    filters.paymentMethod !== 'all' ||
    filters.region !== 'all';

  return (
    <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-4 shadow-lg shadow-black/20 space-y-3">
      {/* Top Filter Controls */}
      <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-3">
        {/* Search Input */}
        <div className="relative flex-1 min-w-[240px]">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            placeholder="Search order ID, customer, product, category, rep..."
            value={filters.search}
            onChange={(e) => onUpdateFilter('search', e.target.value)}
            className="w-full pl-9 pr-8 py-2 bg-slate-950/80 border border-slate-800 rounded-xl text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition-colors"
          />
          {filters.search && (
            <button
              onClick={() => onUpdateFilter('search', '')}
              className="absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-500 hover:text-slate-300"
            >
              <X className="w-4 h-4" />
            </button>
          )}
        </div>

        {/* Date Presets */}
        <div className="flex items-center gap-1 bg-slate-950/80 p-1 border border-slate-800 rounded-xl overflow-x-auto">
          {datePresets.map(preset => (
            <button
              key={preset.id}
              onClick={() => onUpdateFilter('dateRange', preset.id)}
              className={`px-3 py-1.5 text-xs font-medium rounded-lg transition-all whitespace-nowrap ${
                filters.dateRange === preset.id
                  ? 'bg-indigo-600 text-white shadow-sm shadow-indigo-600/30'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
              }`}
            >
              {preset.label}
            </button>
          ))}
        </div>
      </div>

      {/* Secondary Row: Dropdowns */}
      <div className="flex flex-wrap items-center gap-2.5 pt-2 border-t border-slate-800/60">
        {/* Category Dropdown */}
        {dimensions.hasCategories && filterOptions.categories.length > 0 && (
          <select
            value={filters.category}
            onChange={(e) => onUpdateFilter('category', e.target.value)}
            className="px-3 py-1.5 bg-slate-950/80 border border-slate-800 rounded-xl text-xs font-medium text-slate-300 focus:outline-none focus:border-indigo-500 cursor-pointer"
          >
            <option value="all">All Categories</option>
            {filterOptions.categories.map(c => (
              <option key={c} value={c}>{c}</option>
            ))}
          </select>
        )}

        {/* Status Dropdown */}
        {dimensions.hasStatus && filterOptions.statuses.length > 0 && (
          <select
            value={filters.status}
            onChange={(e) => onUpdateFilter('status', e.target.value)}
            className="px-3 py-1.5 bg-slate-950/80 border border-slate-800 rounded-xl text-xs font-medium text-slate-300 focus:outline-none focus:border-indigo-500 cursor-pointer"
          >
            <option value="all">All Statuses</option>
            {filterOptions.statuses.map(s => (
              <option key={s} value={s}>{s.toUpperCase()}</option>
            ))}
          </select>
        )}

        {/* Salesperson Dropdown */}
        {dimensions.hasSalespersons && filterOptions.salespersons.length > 0 && (
          <select
            value={filters.salesperson}
            onChange={(e) => onUpdateFilter('salesperson', e.target.value)}
            className="px-3 py-1.5 bg-slate-950/80 border border-slate-800 rounded-xl text-xs font-medium text-slate-300 focus:outline-none focus:border-indigo-500 cursor-pointer"
          >
            <option value="all">All Sales Reps</option>
            {filterOptions.salespersons.map(rep => (
              <option key={rep} value={rep}>{rep}</option>
            ))}
          </select>
        )}

        {/* Payment Method */}
        {dimensions.hasPaymentMethods && filterOptions.paymentMethods.length > 0 && (
          <select
            value={filters.paymentMethod}
            onChange={(e) => onUpdateFilter('paymentMethod', e.target.value)}
            className="px-3 py-1.5 bg-slate-950/80 border border-slate-800 rounded-xl text-xs font-medium text-slate-300 focus:outline-none focus:border-indigo-500 cursor-pointer"
          >
            <option value="all">All Payments</option>
            {filterOptions.paymentMethods.map(pm => (
              <option key={pm} value={pm}>{pm}</option>
            ))}
          </select>
        )}

        {/* Region */}
        {dimensions.hasRegions && filterOptions.regions.length > 0 && (
          <select
            value={filters.region}
            onChange={(e) => onUpdateFilter('region', e.target.value)}
            className="px-3 py-1.5 bg-slate-950/80 border border-slate-800 rounded-xl text-xs font-medium text-slate-300 focus:outline-none focus:border-indigo-500 cursor-pointer"
          >
            <option value="all">All Regions</option>
            {filterOptions.regions.map(r => (
              <option key={r} value={r}>{r}</option>
            ))}
          </select>
        )}

        {/* Reset Filters button */}
        {hasActiveFilters && (
          <button
            onClick={onResetFilters}
            className="ml-auto inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-rose-400 hover:text-rose-300 bg-rose-500/10 hover:bg-rose-500/20 border border-rose-500/20 rounded-xl transition-all"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            Clear Filters
          </button>
        )}
      </div>

      {/* Active Filter Chips */}
      {hasActiveFilters && (
        <div className="flex flex-wrap items-center gap-1.5 pt-1">
          <span className="text-[11px] text-slate-500 font-medium mr-1">Active:</span>
          {filters.search && (
            <span className="inline-flex items-center gap-1 px-2.5 py-0.5 text-xs font-medium bg-slate-800 text-slate-300 rounded-lg border border-slate-700">
              Keyword: "{filters.search}"
              <button onClick={() => onUpdateFilter('search', '')} className="text-slate-400 hover:text-white">
                <X className="w-3 h-3" />
              </button>
            </span>
          )}
          {filters.dateRange !== 'all' && (
            <span className="inline-flex items-center gap-1 px-2.5 py-0.5 text-xs font-medium bg-slate-800 text-slate-300 rounded-lg border border-slate-700">
              Range: {filters.dateRange}
              <button onClick={() => onUpdateFilter('dateRange', 'all')} className="text-slate-400 hover:text-white">
                <X className="w-3 h-3" />
              </button>
            </span>
          )}
          {filters.category !== 'all' && (
            <span className="inline-flex items-center gap-1 px-2.5 py-0.5 text-xs font-medium bg-slate-800 text-slate-300 rounded-lg border border-slate-700">
              Category: {filters.category}
              <button onClick={() => onUpdateFilter('category', 'all')} className="text-slate-400 hover:text-white">
                <X className="w-3 h-3" />
              </button>
            </span>
          )}
          {filters.status !== 'all' && (
            <span className="inline-flex items-center gap-1 px-2.5 py-0.5 text-xs font-medium bg-slate-800 text-slate-300 rounded-lg border border-slate-700">
              Status: {filters.status}
              <button onClick={() => onUpdateFilter('status', 'all')} className="text-slate-400 hover:text-white">
                <X className="w-3 h-3" />
              </button>
            </span>
          )}
          {filters.salesperson !== 'all' && (
            <span className="inline-flex items-center gap-1 px-2.5 py-0.5 text-xs font-medium bg-slate-800 text-slate-300 rounded-lg border border-slate-700">
              Rep: {filters.salesperson}
              <button onClick={() => onUpdateFilter('salesperson', 'all')} className="text-slate-400 hover:text-white">
                <X className="w-3 h-3" />
              </button>
            </span>
          )}
        </div>
      )}
    </div>
  );
};
''')

# 9. src/components/charts/SalesTrendChart.tsx
write_file('src/components/charts/SalesTrendChart.tsx', '''import React from 'react';
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  BarChart,
  Bar
} from 'recharts';
import { TimeSeriesPoint } from '@/types/sales';
import { formatCurrency, formatNumber } from '@/utils/formatters';

interface SalesTrendChartProps {
  data: TimeSeriesPoint[];
  interval: 'daily' | 'weekly' | 'monthly';
  onIntervalChange: (interval: 'daily' | 'weekly' | 'monthly') => void;
}

export const SalesTrendChart: React.FC<SalesTrendChartProps> = ({
  data,
  interval,
  onIntervalChange,
}) => {
  return (
    <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 shadow-lg shadow-black/20 flex flex-col justify-between">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-6">
        <div>
          <h2 className="text-base font-semibold text-white">Sales Performance Over Time</h2>
          <p className="text-xs text-slate-400 mt-0.5">Revenue trend & order volume trajectory</p>
        </div>

        {/* Interval Buttons */}
        <div className="flex items-center gap-1 bg-slate-950 p-1 border border-slate-800 rounded-xl self-start sm:self-auto">
          {(['daily', 'weekly', 'monthly'] as const).map(mode => (
            <button
              key={mode}
              onClick={() => onIntervalChange(mode)}
              className={`px-3 py-1 text-xs font-medium rounded-lg capitalize transition-all ${
                interval === mode
                  ? 'bg-indigo-600 text-white shadow-sm shadow-indigo-600/30'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
              }`}
            >
              {mode}
            </button>
          ))}
        </div>
      </div>

      {/* Chart */}
      <div className="h-72 w-full">
        {data.length === 0 ? (
          <div className="h-full flex items-center justify-center text-sm text-slate-500">
            No time series data available for the selected filters.
          </div>
        ) : (
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={data} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
              <defs>
                <linearGradient id="salesGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#6366f1" stopOpacity={0.4} />
                  <stop offset="95%" stopColor="#6366f1" stopOpacity={0.0} />
                </linearGradient>
                <linearGradient id="ordersGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#38bdf8" stopOpacity={0.3} />
                  <stop offset="95%" stopColor="#38bdf8" stopOpacity={0.0} />
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
              <XAxis
                dataKey="label"
                stroke="#64748b"
                fontSize={11}
                tickLine={false}
                axisLine={false}
              />
              <YAxis
                stroke="#64748b"
                fontSize={11}
                tickLine={false}
                axisLine={false}
                tickFormatter={(val) => formatCurrency(val, 'INR', true)}
              />
              <Tooltip
                content={({ active, payload, label }) => {
                  if (active && payload && payload.length) {
                    const d = payload[0].payload as TimeSeriesPoint;
                    return (
                      <div className="bg-slate-900 border border-slate-700/80 rounded-xl p-3.5 shadow-xl text-xs space-y-2">
                        <div className="font-semibold text-slate-200 border-b border-slate-800 pb-1">
                          {label || d.date}
                        </div>
                        <div className="space-y-1">
                          <div className="flex items-center justify-between gap-4">
                            <span className="text-indigo-400 font-medium">Revenue:</span>
                            <span className="text-white font-bold">{formatCurrency(d.sales, 'INR')}</span>
                          </div>
                          <div className="flex items-center justify-between gap-4">
                            <span className="text-sky-400 font-medium">Orders:</span>
                            <span className="text-white font-bold">{formatNumber(d.orders)} orders</span>
                          </div>
                          <div className="flex items-center justify-between gap-4">
                            <span className="text-emerald-400 font-medium">AOV:</span>
                            <span className="text-white font-bold">{formatCurrency(d.aov, 'INR')}</span>
                          </div>
                        </div>
                      </div>
                    );
                  }
                  return null;
                }}
              />
              <Area
                type="monotone"
                dataKey="sales"
                stroke="#6366f1"
                strokeWidth={2.5}
                fillOpacity={1}
                fill="url(#salesGrad)"
              />
            </AreaChart>
          </ResponsiveContainer>
        )}
      </div>
    </div>
  );
};
''')

# 10. src/components/charts/CategoryChart.tsx
write_file('src/components/charts/CategoryChart.tsx', '''import React, { useState } from 'react';
import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Tooltip,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid
} from 'recharts';
import { CategoryBreakdown } from '@/types/sales';
import { formatCurrency, formatPercentage } from '@/utils/formatters';

interface CategoryChartProps {
  data: CategoryBreakdown[];
}

export const CategoryChart: React.FC<CategoryChartProps> = ({ data }) => {
  const [chartType, setChartType] = useState<'donut' | 'bar'>('donut');

  return (
    <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 shadow-lg shadow-black/20 flex flex-col justify-between">
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <div>
          <h2 className="text-base font-semibold text-white">Sales by Category</h2>
          <p className="text-xs text-slate-400 mt-0.5">Revenue distribution across categories</p>
        </div>

        <div className="flex items-center gap-1 bg-slate-950 p-1 border border-slate-800 rounded-xl">
          <button
            onClick={() => setChartType('donut')}
            className={`px-2.5 py-1 text-xs font-medium rounded-lg transition-all ${
              chartType === 'donut' ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            Donut
          </button>
          <button
            onClick={() => setChartType('bar')}
            className={`px-2.5 py-1 text-xs font-medium rounded-lg transition-all ${
              chartType === 'bar' ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            Bar
          </button>
        </div>
      </div>

      {/* Chart Canvas */}
      <div className="h-64 w-full">
        {data.length === 0 ? (
          <div className="h-full flex items-center justify-center text-sm text-slate-500">
            No category data available.
          </div>
        ) : chartType === 'donut' ? (
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie
                data={data}
                cx="50%"
                cy="50%"
                innerRadius={55}
                outerRadius={80}
                paddingAngle={4}
                dataKey="sales"
              >
                {data.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} stroke="#0f172a" strokeWidth={2} />
                ))}
              </Pie>
              <Tooltip
                content={({ active, payload }) => {
                  if (active && payload && payload.length) {
                    const d = payload[0].payload as CategoryBreakdown;
                    return (
                      <div className="bg-slate-900 border border-slate-700/80 rounded-xl p-3 shadow-xl text-xs space-y-1">
                        <div className="font-semibold text-slate-200 flex items-center gap-2">
                          <span className="w-2 h-2 rounded-full" style={{ backgroundColor: d.color }} />
                          {d.name}
                        </div>
                        <div className="text-white font-bold">{formatCurrency(d.sales, 'INR')}</div>
                        <div className="text-slate-400">{formatPercentage(d.percentage)} share ({d.count} orders)</div>
                      </div>
                    );
                  }
                  return null;
                }}
              />
            </PieChart>
          </ResponsiveContainer>
        ) : (
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={data} layout="vertical" margin={{ top: 5, right: 20, left: 20, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" horizontal={false} />
              <XAxis type="number" stroke="#64748b" fontSize={10} tickFormatter={(v) => formatCurrency(v, 'INR', true)} />
              <YAxis dataKey="name" type="category" stroke="#64748b" fontSize={11} width={80} tickLine={false} />
              <Tooltip
                content={({ active, payload }) => {
                  if (active && payload && payload.length) {
                    const d = payload[0].payload as CategoryBreakdown;
                    return (
                      <div className="bg-slate-900 border border-slate-700 rounded-xl p-2.5 shadow-xl text-xs">
                        <div className="font-semibold text-slate-200">{d.name}</div>
                        <div className="text-indigo-400 font-bold">{formatCurrency(d.sales, 'INR')}</div>
                        <div className="text-slate-400">{d.count} orders ({formatPercentage(d.percentage)})</div>
                      </div>
                    );
                  }
                  return null;
                }}
              />
              <Bar dataKey="sales" radius={[0, 6, 6, 0]}>
                {data.map((entry, index) => (
                  <Cell key={`cell-bar-${index}`} fill={entry.color} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        )}
      </div>

      {/* Legend list */}
      <div className="grid grid-cols-2 gap-2 mt-3 pt-3 border-t border-slate-800/60 max-h-24 overflow-y-auto">
        {data.slice(0, 6).map(item => (
          <div key={item.name} className="flex items-center justify-between text-xs">
            <div className="flex items-center gap-1.5 truncate pr-2">
              <span className="w-2 h-2 rounded-full shrink-0" style={{ backgroundColor: item.color }} />
              <span className="text-slate-300 truncate">{item.name}</span>
            </div>
            <span className="font-medium text-slate-400">{formatPercentage(item.percentage)}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
''')

# 11. src/components/charts/TopProductsChart.tsx
write_file('src/components/charts/TopProductsChart.tsx', '''import React from 'react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Cell
} from 'recharts';
import { ProductPerformance } from '@/types/sales';
import { formatCurrency, formatNumber } from '@/utils/formatters';

interface TopProductsChartProps {
  products: ProductPerformance[];
}

export const TopProductsChart: React.FC<TopProductsChartProps> = ({ products }) => {
  const topList = products.slice(0, 6);

  return (
    <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 shadow-lg shadow-black/20 flex flex-col justify-between">
      <div>
        <h2 className="text-base font-semibold text-white">Top Performing Products</h2>
        <p className="text-xs text-slate-400 mt-0.5">Highest revenue-generating catalog items</p>
      </div>

      <div className="h-72 w-full mt-4">
        {topList.length === 0 ? (
          <div className="h-full flex items-center justify-center text-sm text-slate-500">
            No product data available.
          </div>
        ) : (
          <ResponsiveContainer width="100%" height="100%">
            <BarChart
              data={topList}
              layout="vertical"
              margin={{ top: 5, right: 30, left: 10, bottom: 5 }}
            >
              <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" horizontal={false} />
              <XAxis
                type="number"
                stroke="#64748b"
                fontSize={10}
                tickLine={false}
                axisLine={false}
                tickFormatter={(val) => formatCurrency(val, 'INR', true)}
              />
              <YAxis
                dataKey="name"
                type="category"
                stroke="#94a3b8"
                fontSize={11}
                tickLine={false}
                axisLine={false}
                width={120}
                tickFormatter={(val) => val.length > 16 ? `${val.substring(0, 16)}...` : val}
              />
              <Tooltip
                content={({ active, payload }) => {
                  if (active && payload && payload.length) {
                    const d = payload[0].payload as ProductPerformance;
                    return (
                      <div className="bg-slate-900 border border-slate-700/80 rounded-xl p-3 shadow-xl text-xs space-y-1.5">
                        <div className="font-semibold text-slate-200">{d.name}</div>
                        <div className="text-indigo-400 font-bold text-sm">{formatCurrency(d.sales, 'INR')}</div>
                        <div className="flex items-center justify-between gap-3 text-slate-400">
                          <span>Category:</span>
                          <span className="text-slate-200">{d.category}</span>
                        </div>
                        <div className="flex items-center justify-between gap-3 text-slate-400">
                          <span>Units Sold:</span>
                          <span className="text-slate-200">{formatNumber(d.units)} units</span>
                        </div>
                        <div className="flex items-center justify-between gap-3 text-slate-400">
                          <span>Avg Unit Price:</span>
                          <span className="text-slate-200">{formatCurrency(d.averagePrice, 'INR')}</span>
                        </div>
                      </div>
                    );
                  }
                  return null;
                }}
              />
              <Bar dataKey="sales" fill="#6366f1" radius={[0, 6, 6, 0]}>
                {topList.map((_, index) => (
                  <Cell
                    key={`cell-${index}`}
                    fill={index === 0 ? '#6366f1' : index === 1 ? '#818cf8' : '#a5b4fc'}
                  />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        )}
      </div>
    </div>
  );
};
''')

# 12. src/components/charts/SalespersonPerformanceChart.tsx
write_file('src/components/charts/SalespersonPerformanceChart.tsx', '''import React from 'react';
import { SalespersonPerformance } from '@/types/sales';
import { formatCurrency, formatNumber } from '@/utils/formatters';
import { UserCheck, Award, Target } from 'lucide-react';

interface SalespersonPerformanceChartProps {
  salespersons: SalespersonPerformance[];
}

export const SalespersonPerformanceChart: React.FC<SalespersonPerformanceChartProps> = ({
  salespersons,
}) => {
  return (
    <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 shadow-lg shadow-black/20">
      <div className="flex items-center justify-between mb-4">
        <div>
          <h2 className="text-base font-semibold text-white">Sales Team Leaderboard</h2>
          <p className="text-xs text-slate-400 mt-0.5">Performance against quota & closed deal volume</p>
        </div>
        <div className="p-2 rounded-xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400">
          <Award className="w-4 h-4" />
        </div>
      </div>

      <div className="space-y-3.5">
        {salespersons.length === 0 ? (
          <div className="text-center py-8 text-sm text-slate-500">
            No salesperson metrics available.
          </div>
        ) : (
          salespersons.map((rep, idx) => (
            <div key={rep.name} className="p-3 bg-slate-950/60 border border-slate-800/80 rounded-xl space-y-2">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <span className={`w-5 h-5 rounded-full flex items-center justify-center text-[10px] font-bold ${
                    idx === 0 ? 'bg-amber-400 text-slate-950' : idx === 1 ? 'bg-slate-300 text-slate-950' : 'bg-slate-800 text-slate-400'
                  }`}>
                    {idx + 1}
                  </span>
                  <span className="text-sm font-semibold text-slate-200">{rep.name}</span>
                </div>
                <span className="text-sm font-bold text-indigo-400">
                  {formatCurrency(rep.sales, 'INR')}
                </span>
              </div>

              <div className="flex items-center justify-between text-xs text-slate-400">
                <span>{rep.deals} deals closed</span>
                <span>Avg Deal: {formatCurrency(rep.aov, 'INR')}</span>
              </div>

              {/* Progress bar */}
              <div className="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
                <div
                  className="bg-indigo-500 h-full rounded-full transition-all duration-500"
                  style={{ width: `${rep.completion}%` }}
                />
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};
''')

# 13. src/components/charts/StatusDistributionChart.tsx
write_file('src/components/charts/StatusDistributionChart.tsx', '''import React from 'react';
import { StatusDistribution, PaymentMethodDistribution } from '@/types/sales';
import { formatCurrency, formatNumber, formatPercentage } from '@/utils/formatters';

interface StatusDistributionChartProps {
  statusData: StatusDistribution[];
  paymentData: PaymentMethodDistribution[];
}

export const StatusDistributionChart: React.FC<StatusDistributionChartProps> = ({
  statusData,
  paymentData,
}) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
      {/* Status Breakdown */}
      <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 shadow-lg shadow-black/20">
        <h3 className="text-sm font-semibold text-white mb-1">Order Fulfillment Status</h3>
        <p className="text-xs text-slate-400 mb-4">Breakdown of orders by fulfillment stage</p>

        <div className="space-y-3">
          {statusData.map(item => (
            <div key={item.name} className="space-y-1">
              <div className="flex items-center justify-between text-xs">
                <div className="flex items-center gap-2">
                  <span className="w-2.5 h-2.5 rounded-full" style={{ backgroundColor: item.color }} />
                  <span className="font-medium text-slate-200">{item.name}</span>
                </div>
                <span className="text-slate-400">{item.count} ({formatPercentage(item.percentage)})</span>
              </div>
              <div className="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
                <div
                  className="h-full rounded-full transition-all"
                  style={{ width: `${item.percentage}%`, backgroundColor: item.color }}
                />
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Payment Method Breakdown */}
      <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 shadow-lg shadow-black/20">
        <h3 className="text-sm font-semibold text-white mb-1">Payment Method Distribution</h3>
        <p className="text-xs text-slate-400 mb-4">Transaction channel split & volume</p>

        <div className="space-y-3">
          {paymentData.slice(0, 4).map((item, idx) => (
            <div key={item.name} className="space-y-1">
              <div className="flex items-center justify-between text-xs">
                <span className="font-medium text-slate-200">{item.name}</span>
                <span className="text-slate-400">{formatCurrency(item.sales, 'INR')} ({formatPercentage(item.percentage)})</span>
              </div>
              <div className="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
                <div
                  className="h-full bg-sky-500 rounded-full transition-all"
                  style={{ width: `${item.percentage}%` }}
                />
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
''')

# 14. src/components/dashboard/SalesDetailModal.tsx
write_file('src/components/dashboard/SalesDetailModal.tsx', '''import React from 'react';
import { X, ShoppingBag, User, Calendar, CreditCard, Tag, DollarSign, MapPin } from 'lucide-react';
import { SaleRecord } from '@/types/sales';
import { StatusBadge } from '@/components/ui/StatusBadge';
import { formatCurrency, formatDate } from '@/utils/formatters';

interface SalesDetailModalProps {
  record: SaleRecord | null;
  onClose: () => void;
}

export const SalesDetailModal: React.FC<SalesDetailModalProps> = ({ record, onClose }) => {
  if (!record) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      {/* Backdrop */}
      <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-sm transition-opacity" onClick={onClose} />

      {/* Dialog */}
      <div className="relative w-full max-w-lg bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl p-6 overflow-hidden z-10 animate-in zoom-in-95 duration-150">
        {/* Header */}
        <div className="flex items-center justify-between border-b border-slate-800 pb-4 mb-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400">
              <ShoppingBag className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base font-bold text-white">{record.order_id}</h3>
              <p className="text-xs text-slate-400">{formatDate(record.date, 'long')}</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content Details */}
        <div className="space-y-4 text-sm">
          {/* Status & Amount Highlight */}
          <div className="flex items-center justify-between p-4 bg-slate-950/70 border border-slate-800 rounded-xl">
            <div>
              <span className="text-xs text-slate-400 block mb-1">Status</span>
              <StatusBadge status={record.status} />
            </div>
            <div className="text-right">
              <span className="text-xs text-slate-400 block mb-1">Total Transaction</span>
              <span className="text-xl font-extrabold text-emerald-400">
                {formatCurrency(record.amount, 'INR')}
              </span>
            </div>
          </div>

          {/* Product & Quantity */}
          <div className="space-y-2">
            <h4 className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Product Info</h4>
            <div className="p-3 bg-slate-950/50 border border-slate-800/80 rounded-xl space-y-1.5">
              <div className="flex justify-between">
                <span className="text-slate-400">Product Name:</span>
                <span className="font-semibold text-slate-200">{record.product_name || 'Standard Catalog Item'}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-400">Category:</span>
                <span className="text-indigo-400 font-medium">{record.category || 'General'}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-400">Quantity:</span>
                <span className="text-slate-200">{record.quantity || 1} units</span>
              </div>
              {record.discount ? (
                <div className="flex justify-between text-amber-400">
                  <span>Discount Applied:</span>
                  <span>- {formatCurrency(record.discount, 'INR')}</span>
                </div>
              ) : null}
            </div>
          </div>

          {/* Customer & Rep */}
          <div className="space-y-2">
            <h4 className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Customer & Sales Team</h4>
            <div className="p-3 bg-slate-950/50 border border-slate-800/80 rounded-xl space-y-1.5">
              {record.customer_name && (
                <div className="flex justify-between">
                  <span className="text-slate-400">Customer:</span>
                  <span className="font-semibold text-slate-200">{record.customer_name}</span>
                </div>
              )}
              {record.customer_email && (
                <div className="flex justify-between">
                  <span className="text-slate-400">Email:</span>
                  <span className="text-slate-300 font-mono text-xs">{record.customer_email}</span>
                </div>
              )}
              {record.customer_city && (
                <div className="flex justify-between">
                  <span className="text-slate-400">Location:</span>
                  <span className="text-slate-300">{record.customer_city} ({record.region || 'HQ'})</span>
                </div>
              )}
              {record.salesperson && (
                <div className="flex justify-between">
                  <span className="text-slate-400">Account Executive:</span>
                  <span className="text-indigo-400 font-medium">{record.salesperson}</span>
                </div>
              )}
              {record.payment_method && (
                <div className="flex justify-between">
                  <span className="text-slate-400">Payment Channel:</span>
                  <span className="text-slate-200">{record.payment_method}</span>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="mt-6 pt-4 border-t border-slate-800 flex justify-end">
          <button
            onClick={onClose}
            className="px-4 py-2 text-sm font-medium text-slate-200 bg-slate-800 hover:bg-slate-700 rounded-xl transition-colors"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
};
''')

# 15. src/components/dashboard/SalesTable.tsx
write_file('src/components/dashboard/SalesTable.tsx', '''import React, { useState, useMemo } from 'react';
import {
  ArrowUpDown,
  ChevronUp,
  ChevronDown,
  ChevronLeft,
  ChevronRight,
  Eye,
  Download,
  Filter,
  Columns
} from 'lucide-react';
import { SaleRecord } from '@/types/sales';
import { StatusBadge } from '@/components/ui/StatusBadge';
import { formatCurrency, formatDate } from '@/utils/formatters';

interface SalesTableProps {
  data: SaleRecord[];
  onSelectRecord: (record: SaleRecord) => void;
  onExport: () => void;
}

type SortField = 'date' | 'order_id' | 'amount' | 'customer_name' | 'product_name' | 'category' | 'status';

export const SalesTable: React.FC<SalesTableProps> = ({ data, onSelectRecord, onExport }) => {
  const [sortField, setSortField] = useState<SortField>('date');
  const [sortAsc, setSortAsc] = useState<boolean>(false);
  const [page, setPage] = useState<number>(1);
  const [pageSize, setPageSize] = useState<number>(10);

  // Sorting
  const sortedData = useMemo(() => {
    return [...data].sort((a, b) => {
      let aVal = a[sortField];
      let bVal = b[sortField];

      if (sortField === 'amount') {
        aVal = Number(aVal) || 0;
        bVal = Number(bVal) || 0;
      } else if (sortField === 'date') {
        aVal = new Date(String(aVal)).getTime() || 0;
        bVal = new Date(String(bVal)).getTime() || 0;
      } else {
        aVal = String(aVal || '').toLowerCase();
        bVal = String(bVal || '').toLowerCase();
      }

      if (aVal < bVal) return sortAsc ? -1 : 1;
      if (aVal > bVal) return sortAsc ? 1 : -1;
      return 0;
    });
  }, [data, sortField, sortAsc]);

  // Pagination
  const totalPages = Math.max(1, Math.ceil(sortedData.length / pageSize));
  const paginatedData = useMemo(() => {
    const start = (page - 1) * pageSize;
    return sortedData.slice(start, start + pageSize);
  }, [sortedData, page, pageSize]);

  const handleSort = (field: SortField) => {
    if (sortField === field) {
      setSortAsc(!sortAsc);
    } else {
      setSortField(field);
      setSortAsc(false);
    }
  };

  const getSortIcon = (field: SortField) => {
    if (sortField !== field) {
      return <ArrowUpDown className="w-3.5 h-3.5 text-slate-600" />;
    }
    return sortAsc ? <ChevronUp className="w-3.5 h-3.5 text-indigo-400" /> : <ChevronDown className="w-3.5 h-3.5 text-indigo-400" />;
  };

  return (
    <div className="bg-slate-900/80 border border-slate-800 rounded-2xl shadow-lg shadow-black/20 overflow-hidden flex flex-col">
      {/* Table Header Controls */}
      <div className="p-4 border-b border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div>
          <h2 className="text-base font-semibold text-white">Underlying Sales Transactions</h2>
          <p className="text-xs text-slate-400 mt-0.5">Showing {paginatedData.length} of {data.length} records</p>
        </div>

        <div className="flex items-center gap-2 self-start sm:self-auto">
          {/* Rows per page selector */}
          <select
            value={pageSize}
            onChange={(e) => {
              setPageSize(Number(e.target.value));
              setPage(1);
            }}
            className="px-2.5 py-1.5 bg-slate-950 border border-slate-800 rounded-xl text-xs font-medium text-slate-300 focus:outline-none focus:border-indigo-500"
          >
            <option value={10}>10 rows</option>
            <option value={25}>25 rows</option>
            <option value={50}>50 rows</option>
            <option value={100}>100 rows</option>
          </select>

          <button
            onClick={onExport}
            className="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-slate-200 bg-slate-950 hover:bg-slate-800 border border-slate-800 rounded-xl transition-all"
          >
            <Download className="w-3.5 h-3.5 text-slate-400" />
            <span>Export CSV</span>
          </button>
        </div>
      </div>

      {/* Table Container */}
      <div className="overflow-x-auto min-h-[300px]">
        <table className="w-full text-left border-collapse text-xs">
          <thead>
            <tr className="border-b border-slate-800/80 bg-slate-950/60 text-slate-400 font-semibold uppercase tracking-wider">
              <th className="py-3.5 px-4 cursor-pointer hover:text-white" onClick={() => handleSort('order_id')}>
                <div className="flex items-center gap-1.5">
                  <span>Order ID</span>
                  {getSortIcon('order_id')}
                </div>
              </th>
              <th className="py-3.5 px-4 cursor-pointer hover:text-white" onClick={() => handleSort('date')}>
                <div className="flex items-center gap-1.5">
                  <span>Date</span>
                  {getSortIcon('date')}
                </div>
              </th>
              <th className="py-3.5 px-4 cursor-pointer hover:text-white" onClick={() => handleSort('customer_name')}>
                <div className="flex items-center gap-1.5">
                  <span>Customer</span>
                  {getSortIcon('customer_name')}
                </div>
              </th>
              <th className="py-3.5 px-4 cursor-pointer hover:text-white" onClick={() => handleSort('product_name')}>
                <div className="flex items-center gap-1.5">
                  <span>Product / Category</span>
                  {getSortIcon('product_name')}
                </div>
              </th>
              <th className="py-3.5 px-4 cursor-pointer hover:text-white" onClick={() => handleSort('amount')}>
                <div className="flex items-center gap-1.5">
                  <span>Amount</span>
                  {getSortIcon('amount')}
                </div>
              </th>
              <th className="py-3.5 px-4 cursor-pointer hover:text-white" onClick={() => handleSort('status')}>
                <div className="flex items-center gap-1.5">
                  <span>Status</span>
                  {getSortIcon('status')}
                </div>
              </th>
              <th className="py-3.5 px-4 text-right">Action</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800/60">
            {paginatedData.length === 0 ? (
              <tr>
                <td colSpan={7} className="py-12 text-center text-slate-500">
                  No sales transactions match the current filter selection.
                </td>
              </tr>
            ) : (
              paginatedData.map((row) => (
                <tr
                  key={row.id}
                  onClick={() => onSelectRecord(row)}
                  className="hover:bg-slate-800/40 transition-colors cursor-pointer group"
                >
                  <td className="py-3 px-4 font-mono font-medium text-indigo-400 group-hover:text-indigo-300">
                    {row.order_id}
                  </td>
                  <td className="py-3 px-4 text-slate-300 whitespace-nowrap">
                    {formatDate(row.date, 'medium')}
                  </td>
                  <td className="py-3 px-4 text-slate-200 font-medium">
                    <div className="truncate max-w-[180px]" title={row.customer_name}>
                      {row.customer_name || 'Direct Customer'}
                    </div>
                    {row.customer_city && (
                      <span className="text-[10px] text-slate-500 block">{row.customer_city}</span>
                    )}
                  </td>
                  <td className="py-3 px-4 text-slate-300">
                    <div className="truncate max-w-[200px] font-medium text-slate-200" title={row.product_name}>
                      {row.product_name || 'Catalog Item'}
                    </div>
                    <span className="text-[10px] text-indigo-400/80">{row.category || 'General'}</span>
                  </td>
                  <td className="py-3 px-4 font-semibold text-white whitespace-nowrap">
                    {formatCurrency(row.amount, 'INR')}
                  </td>
                  <td className="py-3 px-4">
                    <StatusBadge status={row.status} size="sm" />
                  </td>
                  <td className="py-3 px-4 text-right">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        onSelectRecord(row);
                      }}
                      className="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800"
                      title="Inspect record"
                    >
                      <Eye className="w-4 h-4" />
                    </button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>

      {/* Pagination Controls */}
      <div className="p-4 border-t border-slate-800 flex items-center justify-between text-xs text-slate-400">
        <div>
          Page <span className="font-semibold text-slate-200">{page}</span> of{' '}
          <span className="font-semibold text-slate-200">{totalPages}</span>
        </div>

        <div className="flex items-center gap-1.5">
          <button
            onClick={() => setPage(p => Math.max(1, p - 1))}
            disabled={page === 1}
            className="p-1.5 rounded-lg bg-slate-950 border border-slate-800 hover:bg-slate-800 text-slate-300 disabled:opacity-40 disabled:cursor-not-allowed"
          >
            <ChevronLeft className="w-4 h-4" />
          </button>
          <button
            onClick={() => setPage(p => Math.min(totalPages, p + 1))}
            disabled={page === totalPages}
            className="p-1.5 rounded-lg bg-slate-950 border border-slate-800 hover:bg-slate-800 text-slate-300 disabled:opacity-40 disabled:cursor-not-allowed"
          >
            <ChevronRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
};
''')

# 16. src/components/settings/SettingsModal.tsx
write_file('src/components/settings/SettingsModal.tsx', '''import React, { useState } from 'react';
import { X, Settings, Database, Key, CheckCircle2, AlertCircle, RefreshCw, RotateCcw } from 'lucide-react';
import {
  getActiveConfig,
  saveCustomConfig,
  clearCustomConfig,
  testConnection,
  DEFAULT_SUPABASE_URL,
  DEFAULT_SUPABASE_ANON_KEY
} from '@/services/supabase';

interface SettingsModalProps {
  isOpen: boolean;
  onClose: () => void;
  onRefreshData: () => void;
}

export const SettingsModal: React.FC<SettingsModalProps> = ({
  isOpen,
  onClose,
  onRefreshData,
}) => {
  if (!isOpen) return null;

  const currentConfig = getActiveConfig();
  const [url, setUrl] = useState<string>(currentConfig.url);
  const [anonKey, setAnonKey] = useState<string>(currentConfig.anonKey);
  const [testing, setTesting] = useState<boolean>(false);
  const [testResult, setTestResult] = useState<{ success: boolean; message: string } | null>(null);

  const handleSave = () => {
    saveCustomConfig(url, anonKey);
    onRefreshData();
    onClose();
  };

  const handleReset = () => {
    clearCustomConfig();
    setUrl(DEFAULT_SUPABASE_URL);
    setAnonKey(DEFAULT_SUPABASE_ANON_KEY);
    setTestResult(null);
  };

  const handleTest = async () => {
    setTesting(true);
    setTestResult(null);
    const res = await testConnection(url, anonKey);
    setTestResult({ success: res.success, message: res.message });
    setTesting(false);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      {/* Backdrop */}
      <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-sm transition-opacity" onClick={onClose} />

      {/* Modal Dialog */}
      <div className="relative w-full max-w-lg bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl p-6 overflow-hidden z-10 animate-in zoom-in-95 duration-150">
        <div className="flex items-center justify-between border-b border-slate-800 pb-4 mb-4">
          <div className="flex items-center gap-2.5">
            <div className="p-2 rounded-xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400">
              <Settings className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base font-bold text-white">Supabase RPC Configuration</h3>
              <p className="text-xs text-slate-400">Manage target Supabase URL and client Anon Key</p>
            </div>
          </div>
          <button onClick={onClose} className="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800">
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Inputs */}
        <div className="space-y-4 text-xs">
          <div>
            <label className="block text-slate-300 font-semibold mb-1">Supabase Project URL</label>
            <input
              type="text"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="https://your-project.supabase.co"
              className="w-full px-3 py-2 bg-slate-950 border border-slate-800 rounded-xl text-slate-200 font-mono focus:outline-none focus:border-indigo-500"
            />
          </div>

          <div>
            <label className="block text-slate-300 font-semibold mb-1">Public Anon Key</label>
            <textarea
              rows={3}
              value={anonKey}
              onChange={(e) => setAnonKey(e.target.value)}
              placeholder="eyJhbGciOi..."
              className="w-full px-3 py-2 bg-slate-950 border border-slate-800 rounded-xl text-slate-200 font-mono focus:outline-none focus:border-indigo-500 break-all"
            />
          </div>

          {/* Test Status Banner */}
          {testResult && (
            <div className={`p-3 rounded-xl border flex items-start gap-2.5 ${
              testResult.success
                ? 'bg-emerald-500/10 border-emerald-500/20 text-emerald-300'
                : 'bg-rose-500/10 border-rose-500/20 text-rose-300'
            }`}>
              {testResult.success ? <CheckCircle2 className="w-4 h-4 shrink-0 mt-0.5" /> : <AlertCircle className="w-4 h-4 shrink-0 mt-0.5" />}
              <div className="space-y-0.5">
                <div className="font-semibold">{testResult.success ? 'Connection Success' : 'Connection Failed'}</div>
                <div className="text-[11px] opacity-90">{testResult.message}</div>
              </div>
            </div>
          )}
        </div>

        {/* Action Buttons */}
        <div className="mt-6 pt-4 border-t border-slate-800 flex items-center justify-between">
          <button
            onClick={handleReset}
            className="inline-flex items-center gap-1.5 px-3 py-2 text-xs font-medium text-slate-400 hover:text-slate-200 bg-slate-950 hover:bg-slate-800 border border-slate-800 rounded-xl transition-colors"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            Reset Defaults
          </button>

          <div className="flex items-center gap-2">
            <button
              onClick={handleTest}
              disabled={testing}
              className="inline-flex items-center gap-1.5 px-3.5 py-2 text-xs font-medium text-slate-200 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded-xl transition-all"
            >
              <RefreshCw className={`w-3.5 h-3.5 ${testing ? 'animate-spin' : ''}`} />
              <span>{testing ? 'Testing...' : 'Test Connection'}</span>
            </button>

            <button
              onClick={handleSave}
              className="px-4 py-2 text-xs font-semibold text-white bg-indigo-600 hover:bg-indigo-500 rounded-xl shadow-lg shadow-indigo-600/20 transition-all"
            >
              Save & Apply
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
''')

# 17. src/components/settings/ApiInspectorModal.tsx
write_file('src/components/settings/ApiInspectorModal.tsx', '''import React from 'react';
import { X, Database, CheckCircle2, ShieldCheck, Terminal, Copy } from 'lucide-react';
import { ApiStatus } from '@/types/sales';

interface ApiInspectorModalProps {
  isOpen: boolean;
  onClose: () => void;
  apiStatus: ApiStatus | null;
}

export const ApiInspectorModal: React.FC<ApiInspectorModalProps> = ({
  isOpen,
  onClose,
  apiStatus,
}) => {
  if (!isOpen) return null;

  const copyToClipboard = (text: string) => {
    navigator.clipboard.writeText(text);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      {/* Backdrop */}
      <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-sm transition-opacity" onClick={onClose} />

      {/* Dialog */}
      <div className="relative w-full max-w-2xl bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl p-6 overflow-hidden z-10 animate-in zoom-in-95 duration-150">
        <div className="flex items-center justify-between border-b border-slate-800 pb-4 mb-4">
          <div className="flex items-center gap-2.5">
            <div className="p-2 rounded-xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400">
              <Terminal className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base font-bold text-white">API Diagnostic Inspector</h3>
              <p className="text-xs text-slate-400">Telemetry & Supabase RPC response telemetry</p>
            </div>
          </div>
          <button onClick={onClose} className="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800">
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Telemetry info */}
        <div className="space-y-4 text-xs">
          <div className="grid grid-cols-2 gap-3">
            <div className="p-3 bg-slate-950 border border-slate-800 rounded-xl space-y-1">
              <span className="text-slate-500 block">Data Source</span>
              <span className="font-semibold text-slate-200 capitalize">{apiStatus?.source || 'Demo'}</span>
            </div>
            <div className="p-3 bg-slate-950 border border-slate-800 rounded-xl space-y-1">
              <span className="text-slate-500 block">Last Queried</span>
              <span className="font-semibold text-slate-200">
                {apiStatus?.lastFetched ? apiStatus.lastFetched.toLocaleTimeString() : 'Just now'}
              </span>
            </div>
          </div>

          <div className="p-3 bg-slate-950 border border-slate-800 rounded-xl space-y-1">
            <span className="text-slate-500 block">Endpoint Target</span>
            <span className="font-mono text-slate-300 break-all">{apiStatus?.endpoint}</span>
          </div>

          <div className="space-y-1.5">
            <div className="flex items-center justify-between text-slate-400">
              <span>Telemetry Sample Payload</span>
              <button
                onClick={() => copyToClipboard(JSON.stringify(apiStatus?.rawSample, null, 2))}
                className="inline-flex items-center gap-1 text-[11px] text-indigo-400 hover:text-indigo-300"
              >
                <Copy className="w-3 h-3" />
                Copy JSON
              </button>
            </div>
            <pre className="p-3 bg-slate-950 border border-slate-800 rounded-xl font-mono text-[11px] text-indigo-300 max-h-48 overflow-y-auto">
              {JSON.stringify(apiStatus?.rawSample, null, 2) || '// No raw response payload'}
            </pre>
          </div>
        </div>

        {/* Footer */}
        <div className="mt-6 pt-4 border-t border-slate-800 flex justify-end">
          <button
            onClick={onClose}
            className="px-4 py-2 text-xs font-semibold text-white bg-indigo-600 hover:bg-indigo-500 rounded-xl transition-all"
          >
            Done
          </button>
        </div>
      </div>
    </div>
  );
};
''')

# 18. src/components/views/DashboardView.tsx
write_file('src/components/views/DashboardView.tsx', '''import React, { useState } from 'react';
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
''')

# 19. src/components/views/TransactionsView.tsx
write_file('src/components/views/TransactionsView.tsx', '''import React, { useState } from 'react';
import { SaleRecord } from '@/types/sales';
import { SalesTable } from '@/components/dashboard/SalesTable';
import { SalesDetailModal } from '@/components/dashboard/SalesDetailModal';

interface TransactionsViewProps {
  data: SaleRecord[];
  onExportCSV: () => void;
}

export const TransactionsView: React.FC<TransactionsViewProps> = ({ data, onExportCSV }) => {
  const [selectedRecord, setSelectedRecord] = useState<SaleRecord | null>(null);

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-lg font-bold text-white">All Sales Transactions</h2>
        <p className="text-xs text-slate-400">Complete historical transactional ledger</p>
      </div>

      <SalesTable
        data={data}
        onSelectRecord={setSelectedRecord}
        onExport={onExportCSV}
      />

      <SalesDetailModal
        record={selectedRecord}
        onClose={() => setSelectedRecord(null)}
      />
    </div>
  );
};
''')

# 20. src/components/views/ProductsView.tsx
write_file('src/components/views/ProductsView.tsx', '''import React from 'react';
import { ProductPerformance } from '@/types/sales';
import { TopProductsChart } from '@/components/charts/TopProductsChart';
import { formatCurrency, formatNumber } from '@/utils/formatters';
import { Package, Tag, Layers, DollarSign } from 'lucide-react';

interface ProductsViewProps {
  products: ProductPerformance[];
}

export const ProductsView: React.FC<ProductsViewProps> = ({ products }) => {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-lg font-bold text-white">Product Catalog Intelligence</h2>
        <p className="text-xs text-slate-400">Unit volume, revenue contribution, and pricing performance</p>
      </div>

      {/* Product Chart */}
      <TopProductsChart products={products} />

      {/* Products Grid Table */}
      <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 shadow-lg shadow-black/20">
        <h3 className="text-sm font-semibold text-white mb-4">Product Catalog Breakdown</h3>
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse text-xs">
            <thead>
              <tr className="border-b border-slate-800 bg-slate-950/60 text-slate-400 font-semibold uppercase">
                <th className="py-3 px-4">Product Name</th>
                <th className="py-3 px-4">Category</th>
                <th className="py-3 px-4">Units Sold</th>
                <th className="py-3 px-4">Avg Selling Price</th>
                <th className="py-3 px-4">Total Revenue</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {products.map(p => (
                <tr key={p.id} className="hover:bg-slate-800/40 transition-colors">
                  <td className="py-3 px-4 font-semibold text-white">{p.name}</td>
                  <td className="py-3 px-4 text-indigo-400">{p.category}</td>
                  <td className="py-3 px-4 text-slate-300">{formatNumber(p.units)} units</td>
                  <td className="py-3 px-4 text-slate-300">{formatCurrency(p.averagePrice, 'INR')}</td>
                  <td className="py-3 px-4 font-bold text-emerald-400">{formatCurrency(p.sales, 'INR')}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
''')

# 21. src/components/views/CustomersView.tsx
write_file('src/components/views/CustomersView.tsx', '''import React from 'react';
import { SalespersonPerformance, SaleRecord } from '@/types/sales';
import { SalespersonPerformanceChart } from '@/components/charts/SalespersonPerformanceChart';
import { formatCurrency, formatNumber } from '@/utils/formatters';
import { Users, Building, MapPin } from 'lucide-react';

interface CustomersViewProps {
  salespersons: SalespersonPerformance[];
  records: SaleRecord[];
}

export const CustomersView: React.FC<CustomersViewProps> = ({ salespersons, records }) => {
  // Aggregate Top Customers
  const customerMap = new Map<string, { name: string; city: string; sales: number; count: number }>();
  for (const r of records) {
    if (!r.customer_name) continue;
    const cur = customerMap.get(r.customer_name) || {
      name: r.customer_name,
      city: r.customer_city || 'India',
      sales: 0,
      count: 0,
    };
    cur.sales += Number(r.amount) || 0;
    cur.count += 1;
    customerMap.set(r.customer_name, cur);
  }

  const topCustomers = Array.from(customerMap.values()).sort((a, b) => b.sales - a.sales).slice(0, 8);

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-lg font-bold text-white">Accounts & Sales Team Performance</h2>
        <p className="text-xs text-slate-400">Enterprise accounts and sales executive rankings</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <SalespersonPerformanceChart salespersons={salespersons} />

        {/* Top Enterprise Customers */}
        <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 shadow-lg shadow-black/20">
          <div className="flex items-center justify-between mb-4">
            <div>
              <h3 className="text-base font-semibold text-white">Top Enterprise Clients</h3>
              <p className="text-xs text-slate-400 mt-0.5">Highest lifetime purchase volume</p>
            </div>
            <div className="p-2 rounded-xl bg-sky-500/10 border border-sky-500/20 text-sky-400">
              <Building className="w-4 h-4" />
            </div>
          </div>

          <div className="space-y-3">
            {topCustomers.map((cust, idx) => (
              <div key={cust.name} className="flex items-center justify-between p-3 bg-slate-950/60 border border-slate-800 rounded-xl">
                <div className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-xl bg-slate-800 flex items-center justify-center font-bold text-xs text-slate-300">
                    {cust.name.substring(0, 2).toUpperCase()}
                  </div>
                  <div>
                    <span className="text-sm font-semibold text-slate-200 block">{cust.name}</span>
                    <span className="text-xs text-slate-400 flex items-center gap-1">
                      <MapPin className="w-3 h-3 text-slate-500" />
                      {cust.city} • {cust.count} orders
                    </span>
                  </div>
                </div>
                <span className="text-sm font-bold text-emerald-400">
                  {formatCurrency(cust.sales, 'INR')}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
''')

# 22. src/components/views/ReportsView.tsx
write_file('src/components/views/ReportsView.tsx', '''import React from 'react';
import { DashboardMetrics, CategoryBreakdown, TimeSeriesPoint } from '@/types/sales';
import { formatCurrency, formatNumber, formatPercentage } from '@/utils/formatters';
import { FileText, Download, TrendingUp, DollarSign, Calendar } from 'lucide-react';

interface ReportsViewProps {
  metrics: DashboardMetrics;
  categories: CategoryBreakdown[];
  timeSeries: TimeSeriesPoint[];
  onExportCSV: () => void;
}

export const ReportsView: React.FC<ReportsViewProps> = ({
  metrics,
  categories,
  timeSeries,
  onExportCSV,
}) => {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-lg font-bold text-white">Executive Sales Brief & Reports</h2>
          <p className="text-xs text-slate-400">Period financial summary and performance indicators</p>
        </div>

        <button
          onClick={onExportCSV}
          className="inline-flex items-center gap-2 px-4 py-2 text-xs font-semibold text-white bg-indigo-600 hover:bg-indigo-500 rounded-xl shadow-lg shadow-indigo-600/20 transition-all"
        >
          <Download className="w-4 h-4" />
          Download Complete CSV Report
        </button>
      </div>

      {/* Summary Highlights */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="p-5 bg-slate-900/80 border border-slate-800 rounded-2xl space-y-2">
          <span className="text-xs text-slate-400">Gross Period Revenue</span>
          <div className="text-2xl font-extrabold text-white">{formatCurrency(metrics.totalSales, 'INR')}</div>
          <div className="text-xs text-emerald-400 font-medium">{formatPercentage(metrics.salesChange)} vs previous baseline</div>
        </div>

        <div className="p-5 bg-slate-900/80 border border-slate-800 rounded-2xl space-y-2">
          <span className="text-xs text-slate-400">Total Transactions Closed</span>
          <div className="text-2xl font-extrabold text-white">{formatNumber(metrics.totalOrders)}</div>
          <div className="text-xs text-sky-400 font-medium">Avg Value: {formatCurrency(metrics.averageOrderValue, 'INR')}</div>
        </div>

        <div className="p-5 bg-slate-900/80 border border-slate-800 rounded-2xl space-y-2">
          <span className="text-xs text-slate-400">Top Revenue Driver</span>
          <div className="text-lg font-extrabold text-indigo-400 truncate">{metrics.topProduct?.name || 'N/A'}</div>
          <div className="text-xs text-slate-400">{formatCurrency(metrics.topProduct?.sales || 0, 'INR')} recorded</div>
        </div>
      </div>

      {/* Category Performance Table */}
      <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 shadow-lg shadow-black/20">
        <h3 className="text-base font-semibold text-white mb-4">Category Revenue Breakdown Report</h3>
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-slate-800 bg-slate-950/60 text-slate-400 uppercase font-semibold">
                <th className="py-3 px-4">Category</th>
                <th className="py-3 px-4">Order Volume</th>
                <th className="py-3 px-4">Gross Revenue</th>
                <th className="py-3 px-4">Revenue Contribution</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {categories.map(cat => (
                <tr key={cat.name} className="hover:bg-slate-800/40">
                  <td className="py-3 px-4 font-semibold text-white flex items-center gap-2">
                    <span className="w-2.5 h-2.5 rounded-full" style={{ backgroundColor: cat.color }} />
                    {cat.name}
                  </td>
                  <td className="py-3 px-4 text-slate-300">{formatNumber(cat.count)} orders</td>
                  <td className="py-3 px-4 font-bold text-slate-200">{formatCurrency(cat.sales, 'INR')}</td>
                  <td className="py-3 px-4 text-indigo-400 font-semibold">{formatPercentage(cat.percentage)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
''')

# 23. src/App.tsx
write_file('src/App.tsx', '''import React, { useState } from 'react';
import { useSalesDashboard } from '@/hooks/useSalesDashboard';
import { Sidebar, TabType } from '@/components/layout/Sidebar';
import { Header } from '@/components/layout/Header';
import { FilterToolbar } from '@/components/dashboard/FilterToolbar';
import { DashboardView } from '@/components/views/DashboardView';
import { TransactionsView } from '@/components/views/TransactionsView';
import { ProductsView } from '@/components/views/ProductsView';
import { CustomersView } from '@/components/views/CustomersView';
import { ReportsView } from '@/components/views/ReportsView';
import { LoadingSkeleton } from '@/components/ui/LoadingSkeleton';
import { EmptyState } from '@/components/ui/EmptyState';
import { ErrorState } from '@/components/ui/ErrorState';
import { SettingsModal } from '@/components/settings/SettingsModal';
import { ApiInspectorModal } from '@/components/settings/ApiInspectorModal';

export function App() {
  const [activeTab, setActiveTab] = useState<TabType>('dashboard');
  const [sidebarCollapsed, setSidebarCollapsed] = useState<boolean>(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState<boolean>(false);
  const [settingsOpen, setSettingsOpen] = useState<boolean>(false);
  const [apiInspectorOpen, setApiInspectorOpen] = useState<boolean>(false);

  const {
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
    refetch,
    exportCSV,
  } = useSalesDashboard();

  const renderActiveView = () => {
    if (loading) {
      return <LoadingSkeleton />;
    }

    if (rawData.length === 0) {
      return (
        <EmptyState
          title="No Sales Records"
          description="Supabase RPC did not return any records. Check your database connection or refresh."
          onResetFilters={refetch}
        />
      );
    }

    switch (activeTab) {
      case 'sales':
        return (
          <TransactionsView
            data={filteredData}
            onExportCSV={exportCSV}
          />
        );
      case 'products':
        return <ProductsView products={topProducts} />;
      case 'customers':
        return (
          <CustomersView
            salespersons={salespersons}
            records={filteredData}
          />
        );
      case 'reports':
        return (
          <ReportsView
            metrics={metrics}
            categories={categoryBreakdown}
            timeSeries={timeSeries}
            onExportCSV={exportCSV}
          />
        );
      case 'settings':
        return (
          <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 max-w-2xl">
            <h2 className="text-base font-bold text-white mb-2">Endpoint Management</h2>
            <p className="text-xs text-slate-400 mb-6">
              Configure your Supabase endpoint and manage real-time RPC integration credentials.
            </p>
            <button
              onClick={() => setSettingsOpen(true)}
              className="px-4 py-2 text-sm font-semibold text-white bg-indigo-600 hover:bg-indigo-500 rounded-xl shadow-lg shadow-indigo-600/20 transition-all"
            >
              Open API Configuration
            </button>
          </div>
        );
      case 'dashboard':
      default:
        return (
          <DashboardView
            metrics={metrics}
            timeSeries={timeSeries}
            timeInterval={timeInterval}
            onTimeIntervalChange={setTimeInterval}
            categoryBreakdown={categoryBreakdown}
            topProducts={topProducts}
            salespersons={salespersons}
            statusDistribution={statusDistribution}
            paymentDistribution={paymentDistribution}
            filteredData={filteredData}
            dimensions={dimensions}
            onExportCSV={exportCSV}
          />
        );
    }
  };

  return (
    <div className="flex min-h-screen bg-slate-950 text-slate-100 antialiased font-sans">
      {/* Sidebar */}
      <Sidebar
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        collapsed={sidebarCollapsed}
        setCollapsed={setSidebarCollapsed}
        mobileOpen={mobileMenuOpen}
        setMobileOpen={setMobileMenuOpen}
        apiStatus={apiStatus}
        hasCustomers={dimensions.hasCustomers || dimensions.hasSalespersons}
      />

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col min-w-0">
        <Header
          title={
            activeTab === 'dashboard'
              ? 'Sales Dashboard'
              : activeTab === 'sales'
              ? 'Sales Transactions'
              : activeTab === 'products'
              ? 'Products'
              : activeTab === 'customers'
              ? 'Customers & Team'
              : activeTab === 'reports'
              ? 'Reports'
              : 'API Settings'
          }
          isRefreshing={isRefreshing}
          onRefresh={refetch}
          onExport={exportCSV}
          onOpenSettings={() => setSettingsOpen(true)}
          onOpenApiInspector={() => setApiInspectorOpen(true)}
          onOpenMobileMenu={() => setMobileMenuOpen(true)}
          apiStatus={apiStatus}
          filters={filters}
          totalFilteredCount={filteredData.length}
        />

        <main className="flex-1 p-4 lg:p-8 max-w-7xl mx-auto w-full space-y-6">
          {/* Universal Filter Toolbar */}
          <FilterToolbar
            filters={filters}
            onUpdateFilter={updateFilter}
            onResetFilters={resetFilters}
            filterOptions={filterOptions}
            dimensions={dimensions}
            totalResults={filteredData.length}
          />

          {/* Active View Container */}
          {renderActiveView()}
        </main>
      </div>

      {/* Settings Modal */}
      <SettingsModal
        isOpen={settingsOpen}
        onClose={() => setSettingsOpen(false)}
        onRefreshData={refetch}
      />

      {/* API Inspector Modal */}
      <ApiInspectorModal
        isOpen={apiInspectorOpen}
        onClose={() => setApiInspectorOpen(false)}
        apiStatus={apiStatus}
      />
    </div>
  );
}

export default App;
''')

# 24. src/main.tsx
write_file('src/main.tsx', '''import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
''')

print('All React components and application code written successfully!')

