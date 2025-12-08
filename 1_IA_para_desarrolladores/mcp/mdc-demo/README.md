# MCP Server Demo con Claude

Este es un servidor MCP de demostración que simplemente responde "Buenos días + nombre". Es una plantilla base para trabajar en proyectos utilizando Model Context Protocol (MCP).

## 🚀 Cómo montar uno desde cero

### 1️⃣ Requisitos previos
- Tener **Node.js 16+** instalado en tu sistema.
- Tener **Claude Desktop**.

### 2️⃣ Configuración del proyecto
Ejecuta los siguientes comandos en la terminal:

```sh
mkdir <nombre-del-proyecto>
cd <nombre-del-proyecto>
npm init -y
npm install @modelcontextprotocol/sdk axios
npm install --save-dev typescript @types/node
```

### 3️⃣ Configuración de TypeScript
Crea un archivo `tsconfig.json` en la raíz del proyecto con el siguiente contenido:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./build",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

### 4️⃣ Creación del servidor MCP

Crea una carpeta `src/` y dentro de ella un archivo `index.ts` con el siguiente código mínimo:

En este repositorio pueded copiar el de `src/index.ts` coom ejemplo funcional.

```typescript
#!/usr/bin/env node
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ErrorCode,
  ListToolsRequestSchema,
  McpError,
} from '@modelcontextprotocol/sdk/types.js';
import axios from 'axios';

class OKXServer {
  private server: Server;
  
  constructor() {
    this.server = new Server();
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('OKX MCP server running on stdio');
  }
}

const server = new OKXServer();
server.run().catch(console.error);
```

### 5️⃣ Compilación del código TypeScript

```sh
npx tsc
```

### 6️⃣ Inspección del servidor MCP

Te habilitará en localhost:5173 una interfaz web para testear tu servidor MCP antes de desplegarlo.

```sh
npx @modelcontextprotocol/inspector build/index.js
```

Si da error de permisos, ejecuta:

```sh
chmod +x build/index.js
```

### 7️⃣ Ejecución del servidor

Para correr el servidor:

```sh
node build/index.js
```

### 🔍 Conexión con Claude

Para conectar el servidor MCP con Claude, es necesario editar el fichero `claude_desktop_config.json`. En mi caso, este archivo se encuentra en:

```
/Users/alvaro/Library/Application Support/Claude/claude_desktop_config.json
```

Añade la configuración del servidor MCP para que quede algo como esto:

> [!CAUTION]
> Recuerda ajustar la ruta.

```json
{
  "mcpServers": {
    "hola": {
      "command": "node",
      "args": ["/Users/alvaro/Documents/Coding/others/mcp-demo/build/index.js"],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

¡Listo! Ahora tienes un servidor MCP funcional que puedes probar desde Claude