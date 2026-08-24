import React from 'react';
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
