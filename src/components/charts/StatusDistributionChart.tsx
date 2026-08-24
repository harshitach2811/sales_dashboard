import React from 'react';
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
