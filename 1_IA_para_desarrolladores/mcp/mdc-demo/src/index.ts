#!/usr/bin/env node
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
    CallToolRequestSchema,
    ErrorCode,
    ListToolsRequestSchema,
    McpError,
} from '@modelcontextprotocol/sdk/types.js';

class SimpleGreetingServer {
    private server: Server;

    constructor() {
        console.error('[Setup] Inicializando servidor...');
        this.server = new Server(
            {
                name: 'hola-mcp-server',
                version: '0.1.0',
            },
            {
                capabilities: {
                    tools: {},
                },
            }
        );

        this.setupToolHandler();

        this.server.onerror = (error) => console.error('[Error]', error);
        process.on('SIGINT', async () => {
            await this.server.close();
            process.exit(0);
        });
    }

    private setupToolHandler() {
        this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
            tools: [
                {
                    name: 'greet',
                    description: 'Saluda al usuario, devuelve "Buenos días <nombre>"',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            name: {
                                type: 'string',
                                description: 'Nombre de la persona a saludar',
                            },
                        },
                        required: ['name'],
                    },
                },
            ],
        }));

        this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
            if (request.params.name !== 'greet') {
                throw new McpError(
                    ErrorCode.MethodNotFound,
                    `Herramienta desconocida: ${request.params.name}`
                );
            }

            const args = request.params.arguments as { name: string };
            if (!args.name) {
                throw new McpError(
                    ErrorCode.InvalidParams,
                    'Falta el parámetro requerido: name'
                );
            }

            const greeting = `Buenos días ${args.name}`;
            return {
                content: [
                    {
                        type: 'text',
                        text: greeting,
                    },
                ],
            };
        });
    }

    async run() {
        const transport = new StdioServerTransport();
        await this.server.connect(transport);
        console.error('Simple Greeting MCP server corriendo sobre stdio');
    }
}

const server = new SimpleGreetingServer();
server.run().catch(console.error);