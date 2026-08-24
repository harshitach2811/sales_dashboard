import React from 'react';
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
