import React from 'react';

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
