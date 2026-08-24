import React from 'react';
import { SalespersonPerformance, SaleRecord } from '@/types/sales';
import { SalespersonPerformanceChart } from '@/components/charts/SalespersonPerformanceChart';
import { formatCurrency, formatNumber } from '@/utils/formatters';
import { Users, Building, MapPin } from 'lucide-react';

interface CustomersViewProps {
  salespersons: SalespersonPerformance[];
  records: SaleRecord[];
}

export const CustomersView: React.FC<CustomersViewProps> = ({ salespersons, records }) => {
  // Aggregate Top Customers
  const customerMap = new Map<string, { name: string; city: string; sales: number; count: number }>();
  for (const r of records) {
    if (!r.customer_name) continue;
    const cur = customerMap.get(r.customer_name) || {
      name: r.customer_name,
      city: r.customer_city || 'India',
      sales: 0,
      count: 0,
    };
    cur.sales += Number(r.amount) || 0;
    cur.count += 1;
    customerMap.set(r.customer_name, cur);
  }

  const topCustomers = Array.from(customerMap.values()).sort((a, b) => b.sales - a.sales).slice(0, 8);

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-lg font-bold text-white">Accounts & Sales Team Performance</h2>
        <p className="text-xs text-slate-400">Enterprise accounts and sales executive rankings</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <SalespersonPerformanceChart salespersons={salespersons} />

        {/* Top Enterprise Customers */}
        <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 shadow-lg shadow-black/20">
          <div className="flex items-center justify-between mb-4">
            <div>
              <h3 className="text-base font-semibold text-white">Top Enterprise Clients</h3>
              <p className="text-xs text-slate-400 mt-0.5">Highest lifetime purchase volume</p>
            </div>
            <div className="p-2 rounded-xl bg-sky-500/10 border border-sky-500/20 text-sky-400">
              <Building className="w-4 h-4" />
            </div>
          </div>

          <div className="space-y-3">
            {topCustomers.map((cust, idx) => (
              <div key={cust.name} className="flex items-center justify-between p-3 bg-slate-950/60 border border-slate-800 rounded-xl">
                <div className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-xl bg-slate-800 flex items-center justify-center font-bold text-xs text-slate-300">
                    {cust.name.substring(0, 2).toUpperCase()}
                  </div>
                  <div>
                    <span className="text-sm font-semibold text-slate-200 block">{cust.name}</span>
                    <span className="text-xs text-slate-400 flex items-center gap-1">
                      <MapPin className="w-3 h-3 text-slate-500" />
                      {cust.city} • {cust.count} orders
                    </span>
                  </div>
                </div>
                <span className="text-sm font-bold text-emerald-400">
                  {formatCurrency(cust.sales, 'INR')}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
