import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// https://astro.build
export default defineConfig({
  site: 'https://fionngavin.dev',
  integrations: [mdx(), sitemap()],
  markdown: {
    shikiConfig: {
      // Dual theme: light by default, dark via prefers-color-scheme (see global.css).
      themes: { light: 'github-light', dark: 'github-dark' },
      defaultColor: false,
      wrap: false,
    },
  },
});
