import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import rehypeSlug from 'rehype-slug';

// https://astro.build
export default defineConfig({
  site: 'https://fionngavin.dev',
  integrations: [mdx(), sitemap()],
  markdown: {
    rehypePlugins: [rehypeSlug],
    shikiConfig: {
      theme: 'github-light',
      wrap: false,
    },
  },
});
