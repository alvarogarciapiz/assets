# Modelos Locales de Inteligencia Artificial

Los **modelos locales** son modelos de inteligencia artificial que se ejecutan directamente en tu propio dispositivo, sin depender de servicios en la nube. Esto permite mayor privacidad, control sobre los datos y la posibilidad de usar IA incluso sin conexión a internet.

## ¿Cómo correr modelos locales?

Existen varias opciones para ejecutar modelos de IA localmente:

- **Docker Model Runner:** Permite ejecutar modelos de IA en contenedores Docker de forma sencilla. Puedes encontrar modelos listos para usar en el [Docker Hub](https://hub.docker.com/u/ai). Más información en la [documentación oficial](https://docs.docker.com/desktop/features/model-runner/).
- **Ollama:** Una herramienta para descargar y ejecutar modelos de lenguaje en tu equipo con un solo comando. Puedes explorar modelos disponibles en [Ollama Search](https://ollama.com/search). Más detalles en [ollama.com](https://ollama.com).
- **LM Studio:** Una aplicación con interfaz gráfica (UI) que facilita la descarga, gestión y ejecución de modelos de lenguaje locales. Más información en [lmstudio.ai](https://lmstudio.ai).

## ¿Para qué usar modelos locales?

- Procesamiento de datos sensibles sin exponerlos a la nube.
- Uso de IA en entornos sin conexión.
- Personalización y control total sobre el modelo y su funcionamiento.
- Reducción de costes asociados a servicios cloud.

## Ejemplo de uso: IntelliTweet

Un ejemplo práctico de modelos locales es el proyecto [IntelliTweet](https://github.com/alvarogarciapiz/IntelliTweet):

> Comparte fácilmente la noticia que prefieras desde tu dispositivo a tu cuenta de Twitter/X en segundos, gracias a la transformación automática de la información en un formato listo para publicar mediante inteligencia artificial avanzada.
>
> Comparte una noticia desde tu iPhone, iPad o Mac usando un atajo, e IntelliTweet leerá automáticamente la web por ti, extraerá la información importante y la publicará en tu cuenta de Twitter/X en cuestión de segundos.

IntelliTweet utiliza modelos locales para analizar y resumir noticias, permitiendo compartirlas en Twitter/X de forma automática y privada, directamente desde tus dispositivos Apple.

