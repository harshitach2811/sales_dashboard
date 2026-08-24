import { createClient, SupabaseClient } from '@supabase/supabase-js';

const STORAGE_URL_KEY = 'SALESPULSE_CUSTOM_SUPABASE_URL';
const STORAGE_ANON_KEY = 'SALESPULSE_CUSTOM_ANON_KEY';

export const DEFAULT_SUPABASE_URL = 
  import.meta.env.VITE_SUPABASE_URL || 'https://kbtfrzwcwmiijwgqynbr.supabase.co';

export const DEFAULT_SUPABASE_ANON_KEY = 
  import.meta.env.VITE_SUPABASE_ANON_KEY || 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh5dHliYXV6eXVlcm9qeG5yaGJiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODU0MDE4NjQsImV4cCI6MjEwMDk3Nzg2NH0.i6EYfRC0XTr1T-W4jcSXFJuxjfMxglvtVKP_1uNnwbQ';

export function getActiveConfig(): { url: string; anonKey: string; isCustom: boolean } {
  try {
    const customUrl = localStorage.getItem(STORAGE_URL_KEY);
    const customKey = localStorage.getItem(STORAGE_ANON_KEY);
    if (customUrl && customKey) {
      return { url: customUrl.trim(), anonKey: customKey.trim(), isCustom: true };
    }
  } catch {
    // localStorage may be unavailable
  }
  return { url: DEFAULT_SUPABASE_URL, anonKey: DEFAULT_SUPABASE_ANON_KEY, isCustom: false };
}

export function saveCustomConfig(url: string, anonKey: string): void {
  try {
    localStorage.setItem(STORAGE_URL_KEY, url.trim());
    localStorage.setItem(STORAGE_ANON_KEY, anonKey.trim());
    cachedClient = null;
  } catch (e) {
    console.error('Failed to save custom Supabase configuration', e);
  }
}

export function clearCustomConfig(): void {
  try {
    localStorage.removeItem(STORAGE_URL_KEY);
    localStorage.removeItem(STORAGE_ANON_KEY);
    cachedClient = null;
  } catch (e) {
    console.error('Failed to clear custom Supabase configuration', e);
  }
}

let cachedClient: SupabaseClient | null = null;
let currentClientUrl = '';
let currentClientKey = '';

export function getSupabaseClient(): SupabaseClient {
  const { url, anonKey } = getActiveConfig();
  if (!cachedClient || currentClientUrl !== url || currentClientKey !== anonKey) {
    cachedClient = createClient(url, anonKey, {
      auth: {
        persistSession: false,
        autoRefreshToken: false,
      },
    });
    currentClientUrl = url;
    currentClientKey = anonKey;
  }
  return cachedClient;
}

export async function testConnection(customUrl?: string, customKey?: string): Promise<{ success: boolean; message: string; details?: unknown }> {
  const targetUrl = customUrl?.trim() || getActiveConfig().url;
  const targetKey = customKey?.trim() || getActiveConfig().anonKey;
  
  const client = createClient(targetUrl, targetKey, {
    auth: { persistSession: false },
  });

  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 6000);

    const { data, error } = await client.rpc('get_sale_dashboard');
    clearTimeout(timeoutId);

    if (error) {
      return {
        success: false,
        message: `RPC error: ${error.message || 'Unknown Supabase error'} (${error.code || 'NO_CODE'})`,
        details: error,
      };
    }

    return {
      success: true,
      message: `Connection successful! Returned ${Array.isArray(data) ? data.length + ' records' : 'data object'}.`,
      details: data,
    };
  } catch (err: unknown) {
    const error = err as Error;
    return {
      success: false,
      message: error.name === 'AbortError' 
        ? 'Connection timed out after 6 seconds.' 
        : `Network / DNS failure: ${error.message}`,
      details: err,
    };
  }
}
