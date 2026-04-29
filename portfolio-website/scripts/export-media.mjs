import { writeFileSync } from 'fs';
import { fileURLToPath, pathToFileURL } from 'url';
import { resolve, dirname } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Import media data — dates are serialized to ISO strings for JSON
const mediaPath = resolve(__dirname, '../src/components/media.js');
const { media } = await import(pathToFileURL(mediaPath).href);

const serialized = media.map(({ slug, title, publication, date, description, tags, links }) => ({
  slug,
  title,
  publication,
  date: date.toISOString().slice(0, 10),
  description,
  tags,
  links,
}));

const outPath = resolve(__dirname, '../media.json');
writeFileSync(outPath, JSON.stringify(serialized, null, 2));
console.log(`Exported ${serialized.length} media entries to media.json`);
