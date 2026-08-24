import React, { useState, useMemo } from 'react';
import {
  ArrowUpDown,
  ChevronUp,
  ChevronDown,
  ChevronLeft,
  ChevronRight,
  Eye,
  Download,
  Filter,
  Columns
} from 'lucide-react';
import { SaleRecord } from '@/types/sales';
import { StatusBadge } from '@/components/ui/StatusBadge';
import { formatCurrency, formatDate } from '@/utils/formatters';

interface SalesTableProps {
  data: SaleRecord[];
  onSelectRecord: (record: SaleRecord) => void;
  onExport: () => void;
}

type SortField = 'date' | 'order_id' | 'amount' | 'customer_name' | 'product_name' | 'category' | 'status';

export const SalesTable: React.FC<SalesTableProps> = ({ data, onSelectRecord, onExport }) => {
  const [sortField, setSortField] = useState<SortField>('date');
  const [sortAsc, setSortAsc] = useState<boolean>(false);
  const [page, setPage] = useState<number>(1);
  const [pageSize, setPageSize] = useState<number>(10);

  // Sorting
  const sortedData = useMemo(() => {
    return [...data].sort((a, b) => {
      let aVal = a[sortField];
      let bVal = b[sortField];

      if (sortField === 'amount') {
        aVal = Number(aVal) || 0;
        bVal = Number(bVal) || 0;
      } else if (sortField === 'date') {
        aVal = new Date(String(aVal)).getTime() || 0;
        bVal = new Date(String(bVal)).getTime() || 0;
      } else {
        aVal = String(aVal || '').toLowerCase();
        bVal = String(bVal || '').toLowerCase();
      }

      if (aVal < bVal) return sortAsc ? -1 : 1;
      if (aVal > bVal) return sortAsc ? 1 : -1;
      return 0;
    });
  }, [data, sortField, sortAsc]);

  // Pagination
  const totalPages = Math.max(1, Math.ceil(sortedData.length / pageSize));
  const paginatedData = useMemo(() => {
    const start = (page - 1) * pageSize;
    return sortedData.slice(start, start + pageSize);
  }, [sortedData, page, pageSize]);

  const handleSort = (field: SortField) => {
    if (sortField === field) {
      setSortAsc(!sortAsc);
    } else {
      setSortField(field);
      setSortAsc(false);
    }
  };

  const getSortIcon = (field: SortField) => {
    if (sortField !== field) {
      return <ArrowUpDown className="w-3.5 h-3.5 text-slate-600" />;
    }
    return sortAsc ? <ChevronUp className="w-3.5 h-3.5 text-indigo-400" /> : <ChevronDown className="w-3.5 h-3.5 text-indigo-400" />;
  };

  return (
    <div className="bg-slate-900/80 border border-slate-800 rounded-2xl shadow-lg shadow-black/20 overflow-hidden flex flex-col">
      {/* Table Header Controls */}
      <div className="p-4 border-b border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div>
          <h2 className="text-base font-semibold text-white">Underlying Sales Transactions</h2>
          <p className="text-xs text-slate-400 mt-0.5">Showing {paginatedData.length} of {data.length} records</p>
        </div>

        <div className="flex items-center gap-2 self-start sm:self-auto">
          {/* Rows per page selector */}
          <select
            value={pageSize}
            onChange={(e) => {
              setPageSize(Number(e.target.value));
              setPage(1);
            }}
            className="px-2.5 py-1.5 bg-slate-950 border border-slate-800 rounded-xl text-xs font-medium text-slate-300 focus:outline-none focus:border-indigo-500"
          >
            <option value={10}>10 rows</option>
            <option value={25}>25 rows</option>
            <option value={50}>50 rows</option>
            <option value={100}>100 rows</option>
          </select>

          <button
            onClick={onExport}
            className="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-slate-200 bg-slate-950 hover:bg-slate-800 border border-slate-800 rounded-xl transition-all"
          >
            <Download className="w-3.5 h-3.5 text-slate-400" />
            <span>Export CSV</span>
          </button>
        </div>
      </div>

      {/* Table Container */}
      <div className="overflow-x-auto min-h-[300px]">
        <table className="w-full text-left border-collapse text-xs">
          <thead>
            <tr className="border-b border-slate-800/80 bg-slate-950/60 text-slate-400 font-semibold uppercase tracking-wider">
              <th className="py-3.5 px-4 cursor-pointer hover:text-white" onClick={() => handleSort('order_id')}>
                <div className="flex items-center gap-1.5">
                  <span>Order ID</span>
                  {getSortIcon('order_id')}
                </div>
              </th>
              <th className="py-3.5 px-4 cursor-pointer hover:text-white" onClick={() => handleSort('date')}>
                <div className="flex items-center gap-1.5">
                  <span>Date</span>
                  {getSortIcon('date')}
                </div>
              </th>
              <th className="py-3.5 px-4 cursor-pointer hover:text-white" onClick={() => handleSort('customer_name')}>
                <div className="flex items-center gap-1.5">
                  <span>Customer</span>
                  {getSortIcon('customer_name')}
                </div>
              </th>
              <th className="py-3.5 px-4 cursor-pointer hover:text-white" onClick={() => handleSort('product_name')}>
                <div className="flex items-center gap-1.5">
                  <span>Product / Category</span>
                  {getSortIcon('product_name')}
                </div>
              </th>
              <th className="py-3.5 px-4 cursor-pointer hover:text-white" onClick={() => handleSort('amount')}>
                <div className="flex items-center gap-1.5">
                  <span>Amount</span>
                  {getSortIcon('amount')}
                </div>
              </th>
              <th className="py-3.5 px-4 cursor-pointer hover:text-white" onClick={() => handleSort('status')}>
                <div className="flex items-center gap-1.5">
                  <span>Status</span>
                  {getSortIcon('status')}
                </div>
              </th>
              <th className="py-3.5 px-4 text-right">Action</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800/60">
            {paginatedData.length === 0 ? (
              <tr>
                <td colSpan={7} className="py-12 text-center text-slate-500">
                  No sales transactions match the current filter selection.
                </td>
              </tr>
            ) : (
              paginatedData.map((row) => (
                <tr
                  key={row.id}
                  onClick={() => onSelectRecord(row)}
                  className="hover:bg-slate-800/40 transition-colors cursor-pointer group"
                >
                  <td className="py-3 px-4 font-mono font-medium text-indigo-400 group-hover:text-indigo-300">
                    {row.order_id}
                  </td>
                  <td className="py-3 px-4 text-slate-300 whitespace-nowrap">
                    {formatDate(row.date, 'medium')}
                  </td>
                  <td className="py-3 px-4 text-slate-200 font-medium">
                    <div className="truncate max-w-[180px]" title={row.customer_name}>
                      {row.customer_name || 'Direct Customer'}
                    </div>
                    {row.customer_city && (
                      <span className="text-[10px] text-slate-500 block">{row.customer_city}</span>
                    )}
                  </td>
                  <td className="py-3 px-4 text-slate-300">
                    <div className="truncate max-w-[200px] font-medium text-slate-200" title={row.product_name}>
                      {row.product_name || 'Catalog Item'}
                    </div>
                    <span className="text-[10px] text-indigo-400/80">{row.category || 'General'}</span>
                  </td>
                  <td className="py-3 px-4 font-semibold text-white whitespace-nowrap">
                    {formatCurrency(row.amount, 'INR')}
                  </td>
                  <td className="py-3 px-4">
                    <StatusBadge status={row.status} size="sm" />
                  </td>
                  <td className="py-3 px-4 text-right">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        onSelectRecord(row);
                      }}
                      className="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800"
                      title="Inspect record"
                    >
                      <Eye className="w-4 h-4" />
                    </button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>

      {/* Pagination Controls */}
      <div className="p-4 border-t border-slate-800 flex items-center justify-between text-xs text-slate-400">
        <div>
          Page <span className="font-semibold text-slate-200">{page}</span> of{' '}
          <span className="font-semibold text-slate-200">{totalPages}</span>
        </div>

        <div className="flex items-center gap-1.5">
          <button
            onClick={() => setPage(p => Math.max(1, p - 1))}
            disabled={page === 1}
            className="p-1.5 rounded-lg bg-slate-950 border border-slate-800 hover:bg-slate-800 text-slate-300 disabled:opacity-40 disabled:cursor-not-allowed"
          >
            <ChevronLeft className="w-4 h-4" />
          </button>
          <button
            onClick={() => setPage(p => Math.min(totalPages, p + 1))}
            disabled={page === totalPages}
            className="p-1.5 rounded-lg bg-slate-950 border border-slate-800 hover:bg-slate-800 text-slate-300 disabled:opacity-40 disabled:cursor-not-allowed"
          >
            <ChevronRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
};
