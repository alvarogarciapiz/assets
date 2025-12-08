#!/usr/bin/env node
import { exec } from 'child_process';
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
    CallToolRequestSchema,
    ErrorCode,
    ListToolsRequestSchema,
    McpError,
} from '@modelcontextprotocol/sdk/types.js';

class YouTubeDownloaderServer {
    private server: Server;

    constructor() {
        console.error('[Setup] Inicializando YouTube Downloader MCP server...');
        this.server = new Server(
            {
                name: 'youtube-downloader-mcp-server',
                version: '0.1.0',
            },
            {
                capabilities: {
                    tools: {},
                },
            }
        );

        this.setupToolHandlers();

        this.server.onerror = (error) => console.error('[Error]', error);
        process.on('SIGINT', async () => {
            await this.server.close();
            process.exit(0);
        });
    }

    private setupToolHandlers() {
        // Registrar la herramienta que descarga videos de YouTube.
        this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
            tools: [
                {
                    name: 'download',
                    description: 'Descarga un video de YouTube usando yt-dlp',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            url: {
                                type: 'string',
                                description: 'URL del video de YouTube a descargar',
                            },
                        },
                        required: ['url'],
                    },
                },
            ],
        }));

        this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
            if (request.params.name !== 'download') {
                throw new McpError(
                    ErrorCode.MethodNotFound,
                    `Herramienta desconocida: ${request.params.name}`
                );
            }

            const args = request.params.arguments as { url: string };
            if (!args.url) {
                throw new McpError(
                    ErrorCode.InvalidParams,
                    'Falta el parámetro requerido: url'
                );
            }

            const downloadsDir = '/Users/alvaro/Downloads';
            // Construir el comando para descargar el video con yt-dlp
            const command = `yt-dlp "${args.url}" -o "${downloadsDir}/%(title)s.%(ext)s"`;
            console.error(`[API] Ejecutando comando: ${command}`);

            return new Promise((resolve, reject) => {
                exec(command, (error, stdout, stderr) => {
                    if (error) {
                        console.error('[API] Error al descargar el video:', error);
                        return reject(
                            new McpError(ErrorCode.MethodNotFound, error.message)
                        );
                    }
                    console.error('[API] Video descargado exitosamente');
                    resolve({
                        content: [
                            {
                                type: 'text',
                                text: `Video descargado con éxito en ${downloadsDir}`,
                            },
                        ],
                    });
                });
            });
        });
    }

    async run() {
        const transport = new StdioServerTransport();
        await this.server.connect(transport);
        console.error('YouTube Downloader MCP server corriendo sobre stdio');
    }
}

const server = new YouTubeDownloaderServer();
server.run().catch(console.error);