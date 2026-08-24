import React from 'react';
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
