import React from 'react';
import { ProductPerformance } from '@/types/sales';
import { TopProductsChart } from '@/components/charts/TopProductsChart';
import { formatCurrency, formatNumber } from '@/utils/formatters';
import { Package, Tag, Layers, DollarSign } from 'lucide-react';

interface ProductsViewProps {
  products: ProductPerformance[];
}

export const ProductsView: React.FC<ProductsViewProps> = ({ products }) => {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-lg font-bold text-white">Product Catalog Intelligence</h2>
        <p className="text-xs text-slate-400">Unit volume, revenue contribution, and pricing performance</p>
      </div>

      {/* Product Chart */}
      <TopProductsChart products={products} />

      {/* Products Grid Table */}
      <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 shadow-lg shadow-black/20">
        <h3 className="text-sm font-semibold text-white mb-4">Product Catalog Breakdown</h3>
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse text-xs">
            <thead>
              <tr className="border-b border-slate-800 bg-slate-950/60 text-slate-400 font-semibold uppercase">
                <th className="py-3 px-4">Product Name</th>
                <th className="py-3 px-4">Category</th>
                <th className="py-3 px-4">Units Sold</th>
                <th className="py-3 px-4">Avg Selling Price</th>
                <th className="py-3 px-4">Total Revenue</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {products.map(p => (
                <tr key={p.id} className="hover:bg-slate-800/40 transition-colors">
                  <td className="py-3 px-4 font-semibold text-white">{p.name}</td>
                  <td className="py-3 px-4 text-indigo-400">{p.category}</td>
                  <td className="py-3 px-4 text-slate-300">{formatNumber(p.units)} units</td>
                  <td className="py-3 px-4 text-slate-300">{formatCurrency(p.averagePrice, 'INR')}</td>
                  <td className="py-3 px-4 font-bold text-emerald-400">{formatCurrency(p.sales, 'INR')}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
