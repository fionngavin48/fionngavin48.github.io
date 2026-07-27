import { monthYearLong } from './date';

interface PostBylineData {
  author: string;
  publishedAt: Date;
  readingTime?: string;
}

/** Formats author, date, and reading time for article listings. */
export function postByline(data: PostBylineData): string {
  return [
    data.author,
    monthYearLong(data.publishedAt),
    data.readingTime,
  ].filter(Boolean).join(' · ');
}
