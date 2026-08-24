import React from 'react';

export const LoadingSkeleton: React.FC = () => {
  return (
    <div className="space-y-6 animate-pulse p-6">
      {/* Top Banner Skeleton */}
      <div className="h-10 bg-slate-800/60 rounded-xl w-1/3" />

      {/* KPI Cards Skeleton */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {[1, 2, 3, 4].map(i => (
          <div key={i} className="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-5 space-y-3">
            <div className="flex justify-between items-center">
              <div className="h-4 bg-slate-800 rounded w-24" />
              <div className="w-8 h-8 rounded-lg bg-slate-800" />
            </div>
            <div className="h-8 bg-slate-800 rounded w-36" />
            <div className="h-3 bg-slate-800 rounded w-20" />
          </div>
        ))}
      </div>

      {/* Charts Grid Skeleton */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 bg-slate-900/60 border border-slate-800/80 rounded-2xl p-5 h-80 flex flex-col justify-between">
          <div className="h-5 bg-slate-800 rounded w-40" />
          <div className="h-48 bg-slate-800/40 rounded-xl" />
        </div>
        <div className="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-5 h-80 flex flex-col justify-between">
          <div className="h-5 bg-slate-800 rounded w-36" />
          <div className="w-40 h-40 mx-auto rounded-full bg-slate-800/40" />
        </div>
      </div>

      {/* Table Skeleton */}
      <div className="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-5 space-y-4">
        <div className="h-5 bg-slate-800 rounded w-48" />
        <div className="space-y-2">
          {[1, 2, 3, 4, 5].map(i => (
            <div key={i} className="h-12 bg-slate-800/40 rounded-lg" />
          ))}
        </div>
      </div>
    </div>
  );
};
