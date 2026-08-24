import React from 'react';
import { X, Database, CheckCircle2, ShieldCheck, Terminal, Copy } from 'lucide-react';
import { ApiStatus } from '@/types/sales';

interface ApiInspectorModalProps {
  isOpen: boolean;
  onClose: () => void;
  apiStatus: ApiStatus | null;
}

export const ApiInspectorModal: React.FC<ApiInspectorModalProps> = ({
  isOpen,
  onClose,
  apiStatus,
}) => {
  if (!isOpen) return null;

  const copyToClipboard = (text: string) => {
    navigator.clipboard.writeText(text);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      {/* Backdrop */}
      <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-sm transition-opacity" onClick={onClose} />

      {/* Dialog */}
      <div className="relative w-full max-w-2xl bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl p-6 overflow-hidden z-10 animate-in zoom-in-95 duration-150">
        <div className="flex items-center justify-between border-b border-slate-800 pb-4 mb-4">
          <div className="flex items-center gap-2.5">
            <div className="p-2 rounded-xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400">
              <Terminal className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base font-bold text-white">API Diagnostic Inspector</h3>
              <p className="text-xs text-slate-400">Telemetry & Supabase RPC response telemetry</p>
            </div>
          </div>
          <button onClick={onClose} className="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800">
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Telemetry info */}
        <div className="space-y-4 text-xs">
          <div className="grid grid-cols-2 gap-3">
            <div className="p-3 bg-slate-950 border border-slate-800 rounded-xl space-y-1">
              <span className="text-slate-500 block">Data Source</span>
              <span className="font-semibold text-slate-200 capitalize">{apiStatus?.source || 'Demo'}</span>
            </div>
            <div className="p-3 bg-slate-950 border border-slate-800 rounded-xl space-y-1">
              <span className="text-slate-500 block">Last Queried</span>
              <span className="font-semibold text-slate-200">
                {apiStatus?.lastFetched ? apiStatus.lastFetched.toLocaleTimeString() : 'Just now'}
              </span>
            </div>
          </div>

          <div className="p-3 bg-slate-950 border border-slate-800 rounded-xl space-y-1">
            <span className="text-slate-500 block">Endpoint Target</span>
            <span className="font-mono text-slate-300 break-all">{apiStatus?.endpoint}</span>
          </div>

          <div className="space-y-1.5">
            <div className="flex items-center justify-between text-slate-400">
              <span>Telemetry Sample Payload</span>
              <button
                onClick={() => copyToClipboard(JSON.stringify(apiStatus?.rawSample, null, 2))}
                className="inline-flex items-center gap-1 text-[11px] text-indigo-400 hover:text-indigo-300"
              >
                <Copy className="w-3 h-3" />
                Copy JSON
              </button>
            </div>
            <pre className="p-3 bg-slate-950 border border-slate-800 rounded-xl font-mono text-[11px] text-indigo-300 max-h-48 overflow-y-auto">
              {JSON.stringify(apiStatus?.rawSample, null, 2) || '// No raw response payload'}
            </pre>
          </div>
        </div>

        {/* Footer */}
        <div className="mt-6 pt-4 border-t border-slate-800 flex justify-end">
          <button
            onClick={onClose}
            className="px-4 py-2 text-xs font-semibold text-white bg-indigo-600 hover:bg-indigo-500 rounded-xl transition-all"
          >
            Done
          </button>
        </div>
      </div>
    </div>
  );
};
