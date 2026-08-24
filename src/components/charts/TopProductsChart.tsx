import React from 'react';
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
