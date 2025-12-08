# ¿Qué es MCP (Model Context Protocol)?

MCP (Model Context Protocol) es un estándar abierto que define cómo los modelos de inteligencia artificial pueden interactuar con diferentes fuentes de datos, servicios y herramientas externas de forma segura y estructurada. Permite a los modelos acceder a información y funcionalidades externas a través de "servidores MCP", facilitando la integración y ampliando las capacidades de los modelos. MCP está siendo adoptado globalmente como protocolo de referencia para conectar modelos con el mundo real.

## ¿Para qué se puede usar MCP?

MCP se puede utilizar para:
- Acceder a bases de datos, servicios web, sistemas de archivos, APIs y más desde un modelo de IA.
- Automatizar tareas complejas que requieren interacción con múltiples fuentes externas.
- Estandarizar la forma en que los modelos interactúan con el entorno, facilitando la interoperabilidad y la seguridad.

## Ejemplos de MCP disponibles en esta carpeta

En esta carpeta encontrarás varios servidores MCP listos para usar:
- **mcp-hosting:** Para gestionar el hosting y almacenamiento de ficheros.
- **mcp-youtube:** Para descargar vídeos de YouTube.

Otros MCP útiles:
- [Postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres): Acceso a bases de datos PostgreSQL.
- [Google Maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps): Consultas y operaciones sobre Google Maps.
- [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/github): Interacción con repositorios y datos de GitHub.
- [Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem): Manejo del sistema de archivos local.
- [Brave Search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search): Búsqueda en internet usando Brave Search.

## ¿Cómo ejecutar MCPs en Claude o VSCode?

Para que un modelo (por ejemplo, Claude) pueda usar estos MCP, debes añadirlos a la configuración correspondiente.  
En Claude Desktop, edita el archivo (en mac):

```
/Users/<usuario>/Library/Application Support/Claude/claude_desktop_config.json
```

y añade los MCPs a la lista de servidores.

En VSCode, puedes configurarlos en el archivo de configuración, por ejemplo:

```json
{
  "mcpServers": {
    "okx": {
      "command": "node",
      "args": ["/Users/<usuario>/Documents/Coding/others/okx-mcp/build/index.js"],
      "disabled": false,
      "autoApprove": []
    },
    "youtube": {
      "command": "node",
      "args": ["/Users/<usuario>/Documents/Coding/others/mcp-youtube/build/index.js"],
      "disabled": false,
      "autoApprove": []
    }
    // ...otros MCPs...
  }
}
```

Esto es así porque cada MCP se ejecuta como un proceso independiente (normalmente con Node.js) y el modelo se comunica con ellos a través del protocolo MCP, permitiendo modularidad y seguridad en el acceso a recursos externos.

