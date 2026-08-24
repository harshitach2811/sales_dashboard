import React, { useState } from 'react';
import { useSalesDashboard } from '@/hooks/useSalesDashboard';
import { Sidebar, TabType } from '@/components/layout/Sidebar';
import { Header } from '@/components/layout/Header';
import { FilterToolbar } from '@/components/dashboard/FilterToolbar';
import { DashboardView } from '@/components/views/DashboardView';
import { TransactionsView } from '@/components/views/TransactionsView';
import { ProductsView } from '@/components/views/ProductsView';
import { CustomersView } from '@/components/views/CustomersView';
import { ReportsView } from '@/components/views/ReportsView';
import { LoadingSkeleton } from '@/components/ui/LoadingSkeleton';
import { EmptyState } from '@/components/ui/EmptyState';
import { ErrorState } from '@/components/ui/ErrorState';
import { SettingsModal } from '@/components/settings/SettingsModal';
import { ApiInspectorModal } from '@/components/settings/ApiInspectorModal';

export function App() {
  const [activeTab, setActiveTab] = useState<TabType>('dashboard');
  const [sidebarCollapsed, setSidebarCollapsed] = useState<boolean>(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState<boolean>(false);
  const [settingsOpen, setSettingsOpen] = useState<boolean>(false);
  const [apiInspectorOpen, setApiInspectorOpen] = useState<boolean>(false);

  const {
    rawData,
    filteredData,
    loading,
    isRefreshing,
    apiStatus,
    filters,
    filterOptions,
    dimensions,
    metrics,
    timeSeries,
    timeInterval,
    categoryBreakdown,
    topProducts,
    salespersons,
    statusDistribution,
    paymentDistribution,
    setTimeInterval,
    updateFilter,
    resetFilters,
    refetch,
    exportCSV,
  } = useSalesDashboard();

  const renderActiveView = () => {
    if (loading) {
      return <LoadingSkeleton />;
    }

    if (rawData.length === 0) {
      return (
        <EmptyState
          title="No Sales Records"
          description="Supabase RPC did not return any records. Check your database connection or refresh."
          onResetFilters={refetch}
        />
      );
    }

    switch (activeTab) {
      case 'sales':
        return (
          <TransactionsView
            data={filteredData}
            onExportCSV={exportCSV}
          />
        );
      case 'products':
        return <ProductsView products={topProducts} />;
      case 'customers':
        return (
          <CustomersView
            salespersons={salespersons}
            records={filteredData}
          />
        );
      case 'reports':
        return (
          <ReportsView
            metrics={metrics}
            categories={categoryBreakdown}
            timeSeries={timeSeries}
            onExportCSV={exportCSV}
          />
        );
      case 'settings':
        return (
          <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 max-w-2xl">
            <h2 className="text-base font-bold text-white mb-2">Endpoint Management</h2>
            <p className="text-xs text-slate-400 mb-6">
              Configure your Supabase endpoint and manage real-time RPC integration credentials.
            </p>
            <button
              onClick={() => setSettingsOpen(true)}
              className="px-4 py-2 text-sm font-semibold text-white bg-indigo-600 hover:bg-indigo-500 rounded-xl shadow-lg shadow-indigo-600/20 transition-all"
            >
              Open API Configuration
            </button>
          </div>
        );
      case 'dashboard':
      default:
        return (
          <DashboardView
            metrics={metrics}
            timeSeries={timeSeries}
            timeInterval={timeInterval}
            onTimeIntervalChange={setTimeInterval}
            categoryBreakdown={categoryBreakdown}
            topProducts={topProducts}
            salespersons={salespersons}
            statusDistribution={statusDistribution}
            paymentDistribution={paymentDistribution}
            filteredData={filteredData}
            dimensions={dimensions}
            onExportCSV={exportCSV}
          />
        );
    }
  };

  return (
    <div className="flex min-h-screen bg-slate-950 text-slate-100 antialiased font-sans">
      {/* Sidebar */}
      <Sidebar
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        collapsed={sidebarCollapsed}
        setCollapsed={setSidebarCollapsed}
        mobileOpen={mobileMenuOpen}
        setMobileOpen={setMobileMenuOpen}
        apiStatus={apiStatus}
        hasCustomers={dimensions.hasCustomers || dimensions.hasSalespersons}
      />

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col min-w-0">
        <Header
          title={
            activeTab === 'dashboard'
              ? 'Sales Dashboard'
              : activeTab === 'sales'
              ? 'Sales Transactions'
              : activeTab === 'products'
              ? 'Products'
              : activeTab === 'customers'
              ? 'Customers & Team'
              : activeTab === 'reports'
              ? 'Reports'
              : 'API Settings'
          }
          isRefreshing={isRefreshing}
          onRefresh={refetch}
          onExport={exportCSV}
          onOpenSettings={() => setSettingsOpen(true)}
          onOpenApiInspector={() => setApiInspectorOpen(true)}
          onOpenMobileMenu={() => setMobileMenuOpen(true)}
          apiStatus={apiStatus}
          filters={filters}
          totalFilteredCount={filteredData.length}
        />

        <main className="flex-1 p-4 lg:p-8 max-w-7xl mx-auto w-full space-y-6">
          {/* Universal Filter Toolbar */}
          <FilterToolbar
            filters={filters}
            onUpdateFilter={updateFilter}
            onResetFilters={resetFilters}
            filterOptions={filterOptions}
            dimensions={dimensions}
            totalResults={filteredData.length}
          />

          {/* Active View Container */}
          {renderActiveView()}
        </main>
      </div>

      {/* Settings Modal */}
      <SettingsModal
        isOpen={settingsOpen}
        onClose={() => setSettingsOpen(false)}
        onRefreshData={refetch}
      />

      {/* API Inspector Modal */}
      <ApiInspectorModal
        isOpen={apiInspectorOpen}
        onClose={() => setApiInspectorOpen(false)}
        apiStatus={apiStatus}
      />
    </div>
  );
}

export default App;
