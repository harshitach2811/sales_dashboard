// Currency, number, percentage, and date formatters

export function formatCurrency(
  amount: number | undefined | null,
  currency: 'INR' | 'USD' | 'EUR' = 'INR',
  compact: boolean = false
): string {
  if (amount === undefined || amount === null || isNaN(amount)) return '₹0';
  
  if (currency === 'INR') {
    if (compact) {
      if (Math.abs(amount) >= 10000000) {
        return `₹${(amount / 10000000).toFixed(2)} Cr`;
      }
      if (Math.abs(amount) >= 100000) {
        return `₹${(amount / 100000).toFixed(2)} L`;
      }
      if (Math.abs(amount) >= 1000) {
        return `₹${(amount / 1000).toFixed(1)}k`;
      }
    }
    return new Intl.NumberFormat('en-IN', {
      style: 'currency',
      currency: 'INR',
      maximumFractionDigits: 0,
    }).format(amount);
  }

  if (compact) {
    if (Math.abs(amount) >= 1000000) {
      return `$${(amount / 1000000).toFixed(2)}M`;
    }
    if (Math.abs(amount) >= 1000) {
      return `$${(amount / 1000).toFixed(1)}k`;
    }
  }

  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: currency,
    maximumFractionDigits: 0,
  }).format(amount);
}

export function formatNumber(num: number | undefined | null, compact: boolean = false): string {
  if (num === undefined || num === null || isNaN(num)) return '0';
  if (compact) {
    if (Math.abs(num) >= 1000000) return `${(num / 1000000).toFixed(1)}M`;
    if (Math.abs(num) >= 1000) return `${(num / 1000).toFixed(1)}k`;
  }
  return new Intl.NumberFormat('en-IN').format(num);
}

export function formatPercentage(val: number | undefined | null, includeSign: boolean = true): string {
  if (val === undefined || val === null || isNaN(val)) return '0.0%';
  const prefix = includeSign && val > 0 ? '+' : '';
  return `${prefix}${val.toFixed(1)}%`;
}

export function formatDate(dateStr: string | undefined | null, style: 'short' | 'medium' | 'long' | 'time' = 'medium'): string {
  if (!dateStr) return 'N/A';
  try {
    const d = new Date(dateStr);
    if (isNaN(d.getTime())) return String(dateStr);

    if (style === 'short') {
      return d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short' });
    }
    if (style === 'time') {
      return d.toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' });
    }
    if (style === 'long') {
      return d.toLocaleDateString('en-IN', {
        day: 'numeric',
        month: 'short',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
      });
    }
    return d.toLocaleDateString('en-IN', {
      day: 'numeric',
      month: 'short',
      year: 'numeric',
    });
  } catch {
    return String(dateStr);
  }
}
