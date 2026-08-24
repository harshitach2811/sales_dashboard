import React from 'react';
import { X, ShoppingBag, User, Calendar, CreditCard, Tag, DollarSign, MapPin } from 'lucide-react';
import { SaleRecord } from '@/types/sales';
import { StatusBadge } from '@/components/ui/StatusBadge';
import { formatCurrency, formatDate } from '@/utils/formatters';

interface SalesDetailModalProps {
  record: SaleRecord | null;
  onClose: () => void;
}

export const SalesDetailModal: React.FC<SalesDetailModalProps> = ({ record, onClose }) => {
  if (!record) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      {/* Backdrop */}
      <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-sm transition-opacity" onClick={onClose} />

      {/* Dialog */}
      <div className="relative w-full max-w-lg bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl p-6 overflow-hidden z-10 animate-in zoom-in-95 duration-150">
        {/* Header */}
        <div className="flex items-center justify-between border-b border-slate-800 pb-4 mb-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400">
              <ShoppingBag className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base font-bold text-white">{record.order_id}</h3>
              <p className="text-xs text-slate-400">{formatDate(record.date, 'long')}</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content Details */}
        <div className="space-y-4 text-sm">
          {/* Status & Amount Highlight */}
          <div className="flex items-center justify-between p-4 bg-slate-950/70 border border-slate-800 rounded-xl">
            <div>
              <span className="text-xs text-slate-400 block mb-1">Status</span>
              <StatusBadge status={record.status} />
            </div>
            <div className="text-right">
              <span className="text-xs text-slate-400 block mb-1">Total Transaction</span>
              <span className="text-xl font-extrabold text-emerald-400">
                {formatCurrency(record.amount, 'INR')}
              </span>
            </div>
          </div>

          {/* Product & Quantity */}
          <div className="space-y-2">
            <h4 className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Product Info</h4>
            <div className="p-3 bg-slate-950/50 border border-slate-800/80 rounded-xl space-y-1.5">
              <div className="flex justify-between">
                <span className="text-slate-400">Product Name:</span>
                <span className="font-semibold text-slate-200">{record.product_name || 'Standard Catalog Item'}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-400">Category:</span>
                <span className="text-indigo-400 font-medium">{record.category || 'General'}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-400">Quantity:</span>
                <span className="text-slate-200">{record.quantity || 1} units</span>
              </div>
              {record.discount ? (
                <div className="flex justify-between text-amber-400">
                  <span>Discount Applied:</span>
                  <span>- {formatCurrency(record.discount, 'INR')}</span>
                </div>
              ) : null}
            </div>
          </div>

          {/* Customer & Rep */}
          <div className="space-y-2">
            <h4 className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Customer & Sales Team</h4>
            <div className="p-3 bg-slate-950/50 border border-slate-800/80 rounded-xl space-y-1.5">
              {record.customer_name && (
                <div className="flex justify-between">
                  <span className="text-slate-400">Customer:</span>
                  <span className="font-semibold text-slate-200">{record.customer_name}</span>
                </div>
              )}
              {record.customer_email && (
                <div className="flex justify-between">
                  <span className="text-slate-400">Email:</span>
                  <span className="text-slate-300 font-mono text-xs">{record.customer_email}</span>
                </div>
              )}
              {record.customer_city && (
                <div className="flex justify-between">
                  <span className="text-slate-400">Location:</span>
                  <span className="text-slate-300">{record.customer_city} ({record.region || 'HQ'})</span>
                </div>
              )}
              {record.salesperson && (
                <div className="flex justify-between">
                  <span className="text-slate-400">Account Executive:</span>
                  <span className="text-indigo-400 font-medium">{record.salesperson}</span>
                </div>
              )}
              {record.payment_method && (
                <div className="flex justify-between">
                  <span className="text-slate-400">Payment Channel:</span>
                  <span className="text-slate-200">{record.payment_method}</span>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="mt-6 pt-4 border-t border-slate-800 flex justify-end">
          <button
            onClick={onClose}
            className="px-4 py-2 text-sm font-medium text-slate-200 bg-slate-800 hover:bg-slate-700 rounded-xl transition-colors"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
};
