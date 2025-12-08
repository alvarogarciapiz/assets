#!/usr/bin/env node
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { CallToolRequestSchema, ErrorCode, ListToolsRequestSchema, McpError, } from '@modelcontextprotocol/sdk/types.js';
import { execFile } from 'child_process';
import { promisify } from 'util';
import path from 'path';
class MCPHostingServer {
    server;
    constructor() {
        console.error('[Setup] Inicializando servidor...');
        this.server = new Server({
            name: 'mcphostingserver',
            version: '0.1.0',
        }, {
            capabilities: {
                tools: {},
            },
        });
        this.setupToolHandler();
        this.server.onerror = (error) => console.error('[Error]', error);
        process.on('SIGINT', async () => {
            await this.server.close();
            process.exit(0);
        });
    }
    setupToolHandler() {
        this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
            tools: [
                {
                    name: 'HostingFicheros',
                    description: 'Sube un fichero a un servidor de hosting y devuelve la URL',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            path: {
                                type: 'string',
                                description: 'Ruta absoluta del fichero a subir (ejemplo: /Users/alvaro/Desktop/a.txt)',
                            },
                        },
                        required: ['path'],
                    },
                },
            ],
        }));
        this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
            const args = request.params.arguments;
            if (!args.path) {
                throw new McpError(ErrorCode.InvalidParams, 'Falta el parámetro requerido: path del fichero a subir');
            }
            // Convertir la ruta a absoluta si es relativa
            const absolutePath = path.isAbsolute(args.path)
                ? args.path
                : path.resolve(process.cwd(), args.path);
            const execFileAsync = promisify(execFile);
            try {
                const { stdout } = await execFileAsync('curl', [
                    '-F',
                    `files[]=@${absolutePath}`,
                    'https://pomf2.lain.la/upload.php'
                ]);
                const json = JSON.parse(stdout);
                // Extraer la URL del archivo subido y devolverla como texto
                const url = json?.files?.[0]?.url;
                if (!url) {
                    throw new McpError(ErrorCode.InternalError, 'No se pudo obtener la URL del archivo subido');
                }
                return {
                    content: [
                        {
                            type: 'text',
                            text: url,
                        },
                    ],
                };
            }
            catch (error) {
                throw new McpError(ErrorCode.InternalError, `Error subiendo el fichero: ${error.message || error}`);
            }
        });
    }
    async run() {
        const transport = new StdioServerTransport();
        await this.server.connect(transport);
        console.error('Hosting MCP server running');
    }
}
const server = new MCPHostingServer();
server.run().catch(console.error);
