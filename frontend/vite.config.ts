import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    host: true,
    hmr: {
      host: 'vuzuslugi.ru',
      protocol: 'wss',
      clientPort: 443,
      port: 3000
    },
    cors: true
  },
  preview: {
    host: true,
    port: 4173
  }
})