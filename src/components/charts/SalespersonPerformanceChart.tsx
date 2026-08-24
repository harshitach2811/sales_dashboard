import React from 'react';
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
