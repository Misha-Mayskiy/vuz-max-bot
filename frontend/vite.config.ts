import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
const env =
  (globalThis as { process?: { env?: Record<string, string | undefined> } }).process?.env ?? {}

// https://vitejs.dev/config/
const hmrHost = env.VITE_HMR_HOST
const hmrProtocol = env.VITE_HMR_PROTOCOL ?? 'wss'
const hmrClientPort = env.VITE_HMR_CLIENT_PORT ? Number(env.VITE_HMR_CLIENT_PORT) : undefined
const hmrServerPort = env.VITE_HMR_SERVER_PORT ? Number(env.VITE_HMR_SERVER_PORT) : undefined

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    host: true,
    hmr: hmrHost
      ? {
          host: hmrHost,
          protocol: hmrProtocol,
          clientPort: hmrClientPort,
          port: hmrServerPort
        }
      : undefined
  },
  preview: {
    host: true,
    port: 4173
  }
})

