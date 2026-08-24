import React from 'react';
import { AlertCircle, RefreshCw, Settings, ShieldAlert } from 'lucide-react';

interface ErrorStateProps {
  message: string;
  endpoint?: string;
  onRetry: () => void;
  onOpenSettings?: () => void;
}

export const ErrorState: React.FC<ErrorStateProps> = ({
  message,
  endpoint,
  onRetry,
  onOpenSettings,
}) => {
  return (
    <div className="p-6">
      <div className="bg-rose-950/20 border border-rose-800/30 rounded-2xl p-6 md:p-8 max-w-3xl mx-auto shadow-xl">
        <div className="flex items-start gap-4">
          <div className="p-3 bg-rose-500/10 rounded-xl border border-rose-500/20 text-rose-400 shrink-0">
            <ShieldAlert className="w-7 h-7" />
          </div>
          <div className="space-y-3 flex-1">
            <div>
              <h3 className="text-lg font-semibold text-rose-200">Supabase RPC Connection Alert</h3>
              <p className="text-sm text-rose-300/80 mt-1">
                Unable to establish a direct connection to the Supabase RPC endpoint.
              </p>
            </div>

            <div className="p-3.5 bg-slate-900/80 border border-slate-800 rounded-xl font-mono text-xs text-slate-300 break-all space-y-1">
              {endpoint && <div className="text-slate-400"><span className="text-slate-500">Target:</span> {endpoint}</div>}
              <div><span className="text-slate-500">Details:</span> {message}</div>
            </div>

            <div className="text-xs text-slate-400 space-y-1 bg-slate-900/40 p-3 rounded-lg border border-slate-800/50">
              <p className="font-semibold text-slate-300">Potential Causes:</p>
              <ul className="list-disc list-inside space-y-0.5 text-slate-400">
                <li>The Supabase free-tier project is currently paused due to inactivity.</li>
                <li>Custom network/firewall policies blocking direct DNS resolution.</li>
                <li>The RPC function name or schema signature differs on the target project.</li>
              </ul>
            </div>

            <div className="flex flex-wrap items-center gap-3 pt-2">
              <button
                onClick={onRetry}
                className="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-500 rounded-xl shadow-lg shadow-indigo-600/20 transition-all"
              >
                <RefreshCw className="w-4 h-4" />
                Retry Connection
              </button>

              {onOpenSettings && (
                <button
                  onClick={onOpenSettings}
                  className="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-slate-200 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded-xl transition-all"
                >
                  <Settings className="w-4 h-4" />
                  Configure Supabase Endpoint
                </button>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
