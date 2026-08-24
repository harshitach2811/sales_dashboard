import React from 'react';
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
