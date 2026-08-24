import React, { useState } from 'react';
import { SaleRecord } from '@/types/sales';
import { SalesTable } from '@/components/dashboard/SalesTable';
import { SalesDetailModal } from '@/components/dashboard/SalesDetailModal';

interface TransactionsViewProps {
  data: SaleRecord[];
  onExportCSV: () => void;
}

export const TransactionsView: React.FC<TransactionsViewProps> = ({ data, onExportCSV }) => {
  const [selectedRecord, setSelectedRecord] = useState<SaleRecord | null>(null);

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-lg font-bold text-white">All Sales Transactions</h2>
        <p className="text-xs text-slate-400">Complete historical transactional ledger</p>
      </div>

      <SalesTable
        data={data}
        onSelectRecord={setSelectedRecord}
        onExport={onExportCSV}
      />

      <SalesDetailModal
        record={selectedRecord}
        onClose={() => setSelectedRecord(null)}
      />
    </div>
  );
};
