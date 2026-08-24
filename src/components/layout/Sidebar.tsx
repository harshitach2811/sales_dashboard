import React from 'react';
import {
  BarChart3,
  ShoppingBag,
  Package,
  Users,
  FileText,
  Settings,
  ChevronLeft,
  ChevronRight,
  TrendingUp,
  Database,
  X
} from 'lucide-react';
import { ApiStatus } from '@/types/sales';

export type TabType = 'dashboard' | 'sales' | 'products' | 'customers' | 'reports' | 'settings';

interface SidebarProps {
  activeTab: TabType;
  setActiveTab: (tab: TabType) => void;
  collapsed: boolean;
  setCollapsed: (collapsed: boolean) => void;
  mobileOpen: boolean;
  setMobileOpen: (open: boolean) => void;
  apiStatus: ApiStatus | null;
  hasCustomers: boolean;
}

export const Sidebar: React.FC<SidebarProps> = ({
  activeTab,
  setActiveTab,
  collapsed,
  setCollapsed,
  mobileOpen,
  setMobileOpen,
  apiStatus,
  hasCustomers,
}) => {
  const navItems = [
    { id: 'dashboard' as TabType, label: 'Dashboard', icon: BarChart3 },
    { id: 'sales' as TabType, label: 'Sales Transactions', icon: ShoppingBag },
    { id: 'products' as TabType, label: 'Products', icon: Package },
    ...(hasCustomers ? [{ id: 'customers' as TabType, label: 'Customers & Team', icon: Users }] : []),
    { id: 'reports' as TabType, label: 'Reports', icon: FileText },
    { id: 'settings' as TabType, label: 'API & Settings', icon: Settings },
  ];

  const sidebarContent = (
    <div className="flex flex-col h-full bg-slate-950 border-r border-slate-800/80 text-slate-300 select-none">
      {/* Brand Header */}
      <div className="flex items-center justify-between p-4 border-b border-slate-800/80 h-16">
        <div className="flex items-center gap-3 overflow-hidden">
          <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-indigo-600 to-violet-500 flex items-center justify-center text-white shadow-lg shadow-indigo-600/30 shrink-0">
            <TrendingUp className="w-5 h-5" />
          </div>
          {!collapsed && (
            <div className="truncate">
              <span className="font-bold text-base tracking-tight text-white block leading-none">SalesPulse</span>
              <span className="text-[11px] font-medium text-indigo-400 uppercase tracking-wider block mt-1">Analytics BI</span>
            </div>
          )}
        </div>

        {/* Mobile close */}
        <button
          onClick={() => setMobileOpen(false)}
          className="lg:hidden p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Desktop Collapse Toggle */}
        <button
          onClick={() => setCollapsed(!collapsed)}
          className="hidden lg:flex p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800/80 transition-colors"
          title={collapsed ? 'Expand Sidebar' : 'Collapse Sidebar'}
        >
          {collapsed ? <ChevronRight className="w-4 h-4" /> : <ChevronLeft className="w-4 h-4" />}
        </button>
      </div>

      {/* Navigation Links */}
      <nav className="flex-1 p-3 space-y-1.5 overflow-y-auto">
        <div className={`text-[11px] font-semibold tracking-wider text-slate-500 uppercase px-3 py-1.5 ${collapsed ? 'text-center' : ''}`}>
          {collapsed ? '•••' : 'Main Navigation'}
        </div>
        {navItems.map(item => {
          const Icon = item.icon;
          const isActive = activeTab === item.id;
          return (
            <button
              key={item.id}
              onClick={() => {
                setActiveTab(item.id);
                setMobileOpen(false);
              }}
              className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl font-medium text-sm transition-all ${
                isActive
                  ? 'bg-indigo-600/15 text-indigo-400 border border-indigo-500/20 shadow-sm shadow-indigo-500/10'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900 border border-transparent'
              } ${collapsed ? 'justify-center px-0' : ''}`}
              title={collapsed ? item.label : undefined}
            >
              <Icon className={`w-5 h-5 shrink-0 ${isActive ? 'text-indigo-400' : 'text-slate-400'}`} />
              {!collapsed && <span className="truncate">{item.label}</span>}
              {!collapsed && isActive && (
                <div className="w-1.5 h-1.5 rounded-full bg-indigo-400 ml-auto" />
              )}
            </button>
          );
        })}
      </nav>

      {/* Connection Pill Status */}
      <div className="p-3 border-t border-slate-800/80 bg-slate-950/80">
        <div className={`p-3 rounded-xl border ${
          apiStatus?.source === 'live'
            ? 'bg-emerald-500/5 border-emerald-500/20 text-emerald-400'
            : 'bg-indigo-500/5 border-indigo-500/20 text-indigo-300'
        } flex items-center gap-2.5`}>
          <div className="relative shrink-0">
            <Database className="w-4 h-4" />
            <span className={`absolute -top-0.5 -right-0.5 w-2 h-2 rounded-full ${
              apiStatus?.source === 'live' ? 'bg-emerald-400 ring-2 ring-emerald-950 animate-pulse' : 'bg-indigo-400 ring-2 ring-indigo-950'
            }`} />
          </div>
          {!collapsed && (
            <div className="overflow-hidden">
              <div className="text-xs font-semibold truncate">
                {apiStatus?.source === 'live' ? 'Live Supabase RPC' : 'Active Demo Mode'}
              </div>
              <div className="text-[10px] text-slate-400 truncate">
                {apiStatus?.source === 'live' ? 'Connected & Verified' : 'Free tier paused (demo active)'}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );

  return (
    <>
      {/* Desktop Sidebar */}
      <aside className={`hidden lg:block h-screen sticky top-0 transition-all duration-300 z-30 ${
        collapsed ? 'w-20' : 'w-64'
      }`}>
        {sidebarContent}
      </aside>

      {/* Mobile Drawer Overlay */}
      {mobileOpen && (
        <div className="lg:hidden fixed inset-0 z-50 flex">
          <div
            className="fixed inset-0 bg-slate-950/80 backdrop-blur-sm transition-opacity"
            onClick={() => setMobileOpen(false)}
          />
          <div className="relative w-72 max-w-[80vw] h-full shadow-2xl z-10 animate-in slide-in-from-left duration-200">
            {sidebarContent}
          </div>
        </div>
      )}
    </>
  );
};
