const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');

/** 產生含 base path 的站內連結，確保 GitHub Pages 子路徑下也正確。 */
export function u(path: string): string {
  if (!path.startsWith('/')) return path;
  return `${BASE}${path}` || '/';
}

/** 台灣市話轉成 tel: 可撥的國際格式。 */
export function telHref(tel: string): string {
  return `tel:+886${tel.replace(/[^0-9]/g, '').replace(/^0/, '')}`;
}
