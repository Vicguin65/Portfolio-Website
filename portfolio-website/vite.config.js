import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  optimizeDeps: {
    // pdfjs-dist ships its own ESM; exclude it from Vite's pre-bundler
    exclude: ['pdfjs-dist'],
  },
})
