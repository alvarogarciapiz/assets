---
title: "Necesitas conocer MCP..."
date: "12 de Enero de 2026"
edition: 15
source: "https://www.blog.lvrpiz.com/p/model-context-protocol-guia"
---

# Necesitas conocer MCP...

Te cuento qué es el Model Context Protocol (MCP) y por qué si no lo conoces lo acabarás usando

Hace unas semanas os hablaba por aquí de las [Claude Skills](https://www.blog.lvrpiz.com/p/introduccion-claude-skills-guia-espanol-diferencia-mcp) y de cómo podíamos **mejorar nuestros asistentes de IA** para que hicieran cosas que van mucho más allá del chat. En ese post comentaba de refilón qué es MCP pero visto la adopción que está teniendo creo que merece su propio post.

Leyendo este post quiero que entiendas **qué es MCP** y por qué cada vez va a tener más protagonismo, **cómo funciona**, **cómo usarlo** e incluso cómo desarrollar tus propios servidores MCP para tus necesidades.

Hace unos meses estuve en la universidad compartiendo cómo funciona este protocolo. Al acabar el taller compartí estas **3 reflexiones**:

3 reflexiones sobre MCP y su futuro

Entre estas reflexiones, comentaba que los **agentes no dejan de ser LLMs a los que les damos accesos a herramientas** (tools) a través de protocolos como MCP para aumentar sus capacidades. Esto lo hemos visto durante todo este año 2025 con modelos que durante la fase de RL y RLHF mejoran las capacidades de function calling y por tanto sus ‘capacidades agénticas’. El futuro de los agentes, por lo menos en el corto y medio plazo pasa por MCP y Skills.

Por si todavía no te he convencido de la importancia de MCP, la segunda reflexión y apuesta personal es que ChatGPT lanzaría su propio **“App Store” de MCPs**. Esto lo vimos hecho realidad hace unas semanas.

ChatGPT Apps

Adivinad qué usan estas apps bajo el capó para funcionar… Si queréis un post explicando cómo crear apps para ChatGPT usando MCP hacédmelo saber :)

Por último, MCP está directamente integrado en prácticamente todos los IDEs

Integraciones MCP en VSCode

Conocer cómo funcionan los MCPs es clave para aprovechar las herramientas que tenemos en nuestras manos al máximo como desarrolladores. Dicho esto, vamos al lio.

## Qué es el Model Context Protocol (MCP) y por qué revoluciona la IA

El Model Context Protocol (MCP) es un **estándar abierto que permite conectar modelos de inteligencia artificial con fuentes de datos y herramientas locales o remotas** de forma universal, eliminando la necesidad de crear integraciones específicas para cada modelo.

Para que nos entendamos, imaginad por un momento el lío que teníamos antes con los cargadores de móviles. Tenías uno para Nokia, otro para la play, otro para el MP3... un desastre. Luego llegó el USB y, más tarde, el USB-C. De repente, un solo cable valía para todo. Pues bien, **MCP es básicamente el puerto USB-C para las aplicaciones de Inteligencia Artificial**. Es un símil que no me acaba de gustar pero que la gente parece entender cuando lo comento a si que ahí queda.

Hasta ahora, si querías que ChatGPT leyera tu base de datos, tenías que usar sus herramientas específicas. Si querías que Claude hiciera lo mismo, te tocaba reescribir la integración para las herramientas de Claude. Y si mañana salía un modelo nuevo de Google o de Meta que te gustaba más, pues vuelta a empezar.

**El problema que resuelve MCP es** el de la fragmentación del contexto. Los LLMs (Large Language Models) son muy listos, pero viven aislados en sus servidores. No saben qué archivos tienes en tu ordenador, no pueden ver el estado de tu repositorio de Git local ni pueden consultar los logs de tu servidor de producción a menos que tú les pegues el texto. MCP crea una vía estandarizada para que cualquier "Host" (como Claude Desktop, IDEs como Cursor o Zed, y ahora GitHub Copilot) pueda conectarse a cualquier "Server" (tu base de datos, tu sistema de ficheros, tu Slack) sin que tengan que conocerse íntimamente entre ellos.

Pensad en un segundo en la **evolución que hemos visto con los LLMs**:

1. Cuando salió ChatGPT ‘sólo’ podíamos **conversar** con el sistema, no era capaz de crear imágenes, ni ejecutar scripts… sólo inferencia
2. Con el éxito de ChatGPT llegaron las primeras necesidades y mejoras. Creación de imágenes, ejecución de scripts, generación de documentos… **Tools** internas desarrolladas por OpenAI para hacer su producto más completo y cubrir más casos de uso.

   ¿El problema? Que OpenAI NO puede desarrollar absolutamente todas las soluciones habidas y por haber.
3. **MCP** viene a solucionar esto, permitiendo que cualquiera desarrolle tools que cualquier LLM sea capaz de utilizar y explotar.

Evolución de LLM a LLM con Tools a LLM con MCP

Es una capa de abstracción brutal. Tú construyes un servidor MCP que exponga, por ejemplo, los datos de tus clientes, y ese mismo servidor te vale para que Claude te haga resúmenes, para que Copilot te ayude a refactorizar código relacionado con esos datos, o para cualquier otra herramienta que decida soportar el protocolo mañana.

## ¿Cómo funciona MCP? Arquitectura y comunicaciones

MCP funciona mediante una **arquitectura cliente-servidor** basada en JSON-RPC, donde un host (la aplicación de IA como Claude o ChatGPT) se conecta a uno o varios servidores (las fuentes de datos) para descubrir y ejecutar tres tipos de capacidades principales: recursos, herramientas y prompts.

Arquitectura simplificada de MCP

La tecnología que hay debajo de MCP es sorprendentemente sencilla y robusta. Y eso es bueno. La arquitectura se divide en tres piezas fundamentales que tenéis que tener claras:

- El **Host** (o **Cliente MCP**): Es la aplicación donde tú interactúas con la IA. Ahora mismo el ejemplo más claro es la app de escritorio de Claude, pero también lo son el editor Zed, Replit o, como decíamos, GitHub Copilot. El Host es el que lleva la voz cantante; es el que tiene la interfaz de usuario y el que decide cuándo llamar a una herramienta.
- El **Servidor MCP**: Es un programa ligero que tú ejecutas (o que ejecuta alguien por ti) y que sabe cómo hablar con una fuente de datos específica. Puede ser un servidor que sabe leer archivos de tu disco duro, uno que sabe hacer consultas a Google Drive, o uno que sabe ejecutar comandos de terminal.
- El **Protocolo**: Es el idioma en el que hablan el Host y el Servidor.

Aquí viene lo técnico pero interesante. La comunicación se basa en JSON-RPC 2.0. No se han inventado un formato nuevo, es texto plano, legible y estándar. Para mover esos mensajes JSON, **MCP define lo que llaman "Transportes"**. Ahora mismo hay dos principales:

- **Stdio**: Es decir, entrada y salida estándar. El Host arranca el Servidor como un subproceso y se hablan escribiendo y leyendo de la consola. Esto es la leche para herramientas locales porque es rapidísimo y muy seguro (los datos no salen de tu máquina).
- **SSE (Server-Sent Events)**: Para cuando el servidor está en remoto. Esto permite conectar tu Claude Desktop local con un agente que esté corriendo en un servidor en la nube.

Al inicio de la comunicación se realiza un handshake similar al que conocemos en TLS

Handshake MCP

Dentro de esta conversación, el **servidor le ofrece al host tres cosas**. Quedaros con esto porque es la base de todo:

- **Resources** (Recursos): Son datos pasivos. Imagina que quieres que la IA pueda leer logs o ficheros. El servidor le dice: "Oye, tengo estos archivos disponibles en estas rutas". El modelo puede leerlos, pero no cambiarlos. Es como darle permisos de lectura.
- **Prompts**: Son plantillas reutilizables. Si tienes una forma muy concreta de pedirle a la IA que revise un bug, puedes guardar ese "prompt" en el servidor. Así, el usuario solo selecciona "Revisar Bug" en el menú, y el servidor le inyecta todo el contexto necesario al modelo.
- **Tools** (Herramientas): Aquí es donde está lo importante. Son funciones ejecutables. El servidor dice: "Yo sé cómo ejecutar una consulta SQL" o "Yo sé cómo crear una incidencia en Jira". El modelo (el LLM) es lo suficientemente inteligente para decidir cuándo llamar a estas herramientas y con qué parámetros conociendo las firmas de estas funciones.

### ¿Por qué debería aprender y utilizar MCP como desarrollador?

Si te da pereza aprender MCP, Claude Skills, LSP… sólo lee este tweet de **Andrej Karpathy** y quédate con esta frase: “*I have a sense that I could be 10X more powerful if I just properly string together what has become available over the last*”.

> [— # (#)](https://twitter.com/karpathy/status/2004607146781278521?s=20)

Y es que aprender esto no va solo de trastear con una tecnología nueva, va de darte la portabilidad necesaria para que tu trabajo no muera si mañana decides cambiar de modelo, pero sobre todo te permite inyectar contexto real: tus bases de datos, tu código local, tus logs… Es la diferencia entre tener un chatbot que escribe poemas y tener un **sistema conectado que puede cruzar datos entre tus logs de AWS y tus commits de Git para decirte exactamente por qué ha fallado un deploy**, todo bajo tu control y en tu propia máquina si así lo quieres.

## ¿Cómo puedo empezar a usar MCP hoy mismo? Tutorial

Puedes empezar a usar MCP inmediatamente instalando **Claude Desktop** y configurando servidores existentes mediante su archivo de configuración JSON, lo que te permitirá conectar la IA con tus archivos locales, bases de datos o repositorios de GitHub en cuestión de minutos.

Vale, vamos a bajar al barro. La teoría está muy bien, pero aquí hemos venido a jugar. La forma más sencilla de probar esto ahora mismo es con la aplicación de escritorio de Claude ([Claude Desktop](https://claude.com/download)). Ojo, necesitas la app instalada, no vale la versión web del navegador, porque la web no puede ejecutar procesos en tu máquina local por seguridad.

Si no te gusta Claude te dejo una [lista extensa](https://github.com/punkpeye/awesome-mcp-clients/?tab=readme-ov-file#clients) y actualizada de clientes que soportan MCP.

El corazón de todo esto reside en un fichero de configuración. Dependiendo de si usas macOS o Windows, estará en una ruta u otra:

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

Este fichero, si no lo has tocado nunca, probablemente ni exista. Lo creas y listo. Su estructura es un JSON muy simple donde defines qué servidores quieres levantar.

Mira, te pongo un ejemplo de cómo se ve este fichero para conectar dos cosas: un servidor que inspecciona tu sistema de ficheros y otro que conecta con una base de datos SQLite local.

```
{"mcpServers":{"filesystem":{"command":"npx","args":["-y","@modelcontextprotocol/server-filesystem","/Users/alvaro/proyectos","/Users/alvaro/documentos"]},"sqlite":{"command":"uvx","args":["mcp-server-sqlite","--db-path","/Users/alvaro/proyectos/mi_app/data.db"]}}}
```

¿Qué está pasando aquí? Dos ejemplos valen más que uno:

- **filesystem**: Le estamos diciendo a Claude que arranque un servidor usando npx (Node.js). Este servidor es oficial (@modelcontextprotocol/server-filesystem) y le pasamos como argumentos las carpetas que queremos que sean accesibles. Ojo aquí: Claude solo podrá ver lo que haya en esas rutas. Es una medida de seguridad. En este caso estamos corriendo un MCP en nuestro equipo usando Node (JS o TS).

- **sqlite**: Aquí usamos uvx (una herramienta de Python muy rápida, si no la tienes, instálala o usa pip) para ejecutar un servidor de SQLite apuntando a un fichero .db concreto.

Una vez guardas este fichero y reinicias Claude Desktop, verás un icono nuevo de un enchufe o similar en la interfaz. Si le das, verás las herramientas disponibles.

Servidores MCP disponibles en Claude Desktop

De repente, puedes decirle a Claude: "Oye, busca en la carpeta de proyectos el archivo [main.py](https://main.py) y dime qué hace". Y Claude usará la herramienta read\_file del servidor filesystem para leerlo. O le puedes decir: "Dame los últimos 5 usuarios registrados en la base de datos". Y él solito construirá la query SQL, se la mandará al servidor sqlite, y te mostrará los resultados. Sin que tú hayas escrito ni una línea de SQL.

La leche, ¿verdad? Y esto es solo usando servidores que ya existen. Lo divertido empieza cuando creas los tuyos.

Lo bueno es que estos mismos MCPs que estás configurando para Claude también los tienes disponibles en VSCode:

Servidores MCP disponibles en VSCode

### Casos de uso de MCP y donde encontrar nuevos MCPs disponibles

Actualmente existe una [web](https://mcp.so) que recopila a modo de App Store todos los MCPs construidos disponibles para poder descubrir casos de uso y reaprovecharlos. Aún con ello te comparto varios casos de uso que me encantan:

El primero es el de filesystem, un MCP sencillo pero muy potente. Este pequeño MCP permite al LLM acceder a los ficheros de nuestro equipo y hacer operaciones con estos archivos como leerlos, copiarlos, moverlos…

MCP Filesystem

Uno de los MCPs más utilizados es el de GitHub, este MCP permite a los LLMs crear PRs, Issues, clonarse repositorios, comitear… pensad en las implicaciones que tiene esto con los agentes de programación sumado al MCP anterior de filesystem.

MCP GitHub

Existen miles de MCPs ya desarrollados y el poder no está en usarlos de forma aislada, sino dar la utilidad a los LLMs para hacerlos más potentes y poder automatizar muchas más tareas, se me ocurren infinidad de posibilidades con esto…

## ¿Cómo crear un servidor MCP desde cero en Python, TS o JS?

Para **crear tu propio servidor MCP**, puedes utilizar los SDKs oficiales de TypeScript o Python, definiendo las herramientas y recursos mediante decoradores simples que exponen tus funciones locales al protocolo MCP de forma automática.

Aquí es donde la cosa se pone interesante de verdad. Usar lo que otros han hecho está bien, pero **queremos que la IA se conecte a nuestra API interna, a nuestro CRM legacy o a ese script de Python** que tenemos para controlar las luces de casa.

He creado un repositorio con unos primeros pasos para MCP, con varios MCP de ejemplo y con una lista de MCPs de terceros para que probéis. El repo es accesible desde [aquí](https://github.com/alvarogarciapiz/assets/tree/main/1_IA_para_desarrolladores/mcp).

Crear un servidor MCP es mucho más fácil de lo que parece. No tienes que pegarte con el JSON-RPC a mano ni gestionar sockets. Los SDKs te lo dan todo hecho.

Vamos a ver **un ejemplo en Python**, que suele ser el lenguaje franco para estas cosas de IA. Existe una librería llamada mcp y una forma rápida de hacerlo con FastMCP (que se parece mucho a FastAPI, si lo has usado te sentirás como en casa).

Primero, instalas la librería: `pip install mcp`

Ahora, imagina que queremos crear una herramienta sencilla que le permita a Claude descargar videos de YouTube en nuestro equipo simplemente pasándole un enlace:

```
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
```

¡Ya lo tienes! Fíjate que aquí somos un poco **más explícitos que en otros frameworks**, lo cual te da un control total. La clave está en estos **dos manejadores** que hemos definido:

- **ListToolsRequestSchema**: Aquí es donde le presentas tus capacidades del MCP a Claude. Le dices: "Oye, tengo una herramienta llamada download que necesita una url".
- **CallToolRequestSchema**: Aquí es donde está la acción. Cuando Claude decide usar la herramienta, el servidor recibe la petición, extrae la URL y ejecuta el comando de sistema yt-dlp.

Lo bueno de esto es el transporte. Fíjate en la línea new *StdioServerTransport().* Estamos usando la entrada y salida estándar del sistema. Esto significa **que la IA no necesita internet para hablar con tu script, todo ocurre dentro de tu máquina**, pasando mensajes JSON de un proceso a otro.

### ¿Qué es y cómo usar MCP Inspector? Debug de tus MCPs

Para probar que todo esto funciona sin volverte loco abriendo y cerrando Claude, puedes usar el **MCP Inspector**. Es una herramienta web oficial que te permite depurar tu servidor visualmente. Si tienes el archivo compilado o ejecutable, lo lanzarías así:

```
npx @modelcontextprotocol/inspector node dist/index.js
```

Esto te abrirá un panel en el navegador donde verás tu herramienta download, podrás pegarle una URL de YouTube manual y ver cómo responde tu servidor en tiempo real.

MCP Inspector

La clave aquí es entender que tú solo escribes código normal y corriente (en este caso TypeScript y comandos de sistema). MCP se encarga de convertir esas funciones en tools estandarizados que cualquier IA compatible puede entender y ejecutar.

## La evolución de los IDEs y asistentes de código con MCP integrado

No tengo una bola de cristal, pero viendo cómo Anthropic, GitHub, Replit y compañía se han tirado a la piscina, está claro que **MCP va a ser el estándar de facto**.

Imaginad un futuro muy cercano donde te descargas una librería de NPM o de PyPI y ya viene con su servidor MCP incluido. De modo que, al instalarla, tu IDE y tu asistente ya saben automáticamente cómo usarla, cómo configurarla y cómo depurarla. O imagina que tu **empresa tiene un servidor MCP interno** que expone de forma segura la documentación técnica y el estado de la infraestructura. Cualquier desarrollador nuevo que entre al equipo podría abrir su Copilot o su Claude y preguntar: "¿Cómo despliego el microservicio de pagos?", y la IA tendría acceso a la documentación real y actualizada de la empresa para responder.

Estamos **pasando de chatear con un bot a colaborar con un sistema integrado**. Y la pieza que une todo ese sistema es este protocolo. Así que sí, os recomiendo encarecidamente que le dediquéis una tarde a trastear con ello. Configurad vuestro Claude Desktop, probad el servidor de filesystem, y si os animáis, escribid vuestro primer Hola Mundo en MCP. Merece la pena.