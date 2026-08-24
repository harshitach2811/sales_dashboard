import React from 'react';
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
