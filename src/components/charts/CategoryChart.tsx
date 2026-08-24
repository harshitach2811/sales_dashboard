import React, { useState } from 'react';
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
