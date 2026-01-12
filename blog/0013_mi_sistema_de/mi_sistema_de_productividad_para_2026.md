---
title: "Mi sistema de productividad para 2026: Vuelta al papel"
date: "12 de Enero de 2026"
edition: 13
source: "https://www.blog.lvrpiz.com/p/mejores-apps-productividad-mac-programadores-2026"
---

# Mi sistema de productividad para 2026: Vuelta al papel

Aplicaciones, Herramientas y Sistemas que utilizo para aprovechar el tiempo y organizarme

A este año 2025 le queda apenas una semana y dos ediciones de esta newsletter. En este **primer post** he querido hacer una recopilación de todas las herramientas que uso para organizarme y ser **más productivo**. La semana que viene, para despedir el año, estoy redactando un post que llevo preparando desde hace unos meses con todo lo que se viene en materia de inteligencia artificial para 2026.

Hoy te quiero contar qué herramientas uso para trabajar, estudiar y crear proyectos así como sistemas y formas de organizar todo.

La mayoría al otro lado de la pantalla me conocéis pero para los que no, trabajo como ingeniero informático, estudio un máster, me encanta desarrollar aplicaciones, jugar con la IA y contar todo lo que aprendo por aquí.

Trabajo con un ordenador más de la mitad del día por lo que contar con buenas herramientas y sistemas me ayuda a ser más productivo y ahorrar tiempo y es justo lo que quería compartir hoy.

Venga, vamos al lío.

## Organización: ¿Por qué un ingeniero informático vuelve al papel?

He probado cantidad de cosas y hay algo que tiene el **papel físico** que no lo consigues con nada más. ¿notas en el iPad con el Apple pencil? Mal, mucha fricción, no es rápido, puro desorden. ¿notas digitales? Un poco más de lo mismo, lo he probado varias veces y nunca he conseguido adaptarme. Al final lo que me funciona muy es un cuaderno, blanco básico.

Nada de libretas con espacio para cada día ni espacio dedicado a cada cosa. No sabes lo que vas a escribir cada día ni el espacio que necesitas. Una agenda que te da un espacio limitado está condenada al fracaso.

Uso el cuaderno el 90% del tiempo para temas de trabajo, máster e ideas y proyectos. La diferencia de tenerlo o no tenerlo es grande para mi. Aun así no lo uso para todo.

Uso un **calendario digital**. He probado varias apps y al final menos es más. Uso la app de calendario nativa que viene por defecto pero para uso más personal: cumpleaños, eventos, comidas… no suelo usarlo para recordar cosas ni para nada de trabajo.

Para acordarme de todo con el cuaderno me vale el 80% del tiempo pero también uso la app de **recordatorios** (aquí igual, he probado varias apps y al final he vuelto a lo nativo y que mejor me funciona). Aprovecho esta app para cosas puntuales que tengo que recordar dentro de semanas y meses. Un uso que he empezado a usar es hacer que me recuerde unos días antes de la fecha de caducidad de ciertas cosas para anticiparme a renovarlas como documentos de identidad, tarjetas bancarias, sanitarias…

Por último, uso mucho la app de notas. Al final el cuaderno lo uso para ideas y cosas que tengo que hacer el corto plazo o como “memoria ram” antes de pasarlo a otro medio si merece quedarse 😅.

Para las notas durante mucho tiempo estuve usando Notion. Funcionaba muy bien pero desde que Apple metió soporte para markdown en su app de Notas nativa me llevé todo aquí y lo tengo todo sincronizado en iCloud de forma nativa y sin aplicaciones de terceros.

Para organizar las notas uso el [método PARA](https://amzn.to/4iI5A6Y) de Tiago Forte: **P** de *projects* donde guardo ideas, recursos y demás información relevante de los proyectos personales que desarrollo. **A** para las áreas, el cajón más abandonado pero actualmente lo uso para estudiar la certificación de Kubernetes, son cosas en vuelo. Aquí también tengo una carpeta de *mini essays* con intereses sobre los que voy anotando consejos o recursos como de oratoria. **R** de Recursos y **A** de Archivo donde va todo lo que no necesito ya y generalmente no consulto.

## Aplicaciones de desarrollo: Vercel, Cloudflare y Xcode

Este año he desarrollado varios proyectos entre aplicaciones, webs y demás. Una de las tecnologías que quería aprender este año es **swift**, el lenguaje de programación para la plataforma de Apple en el que he creado varias aplicaciones que te cuento luego. Xcode aquí lo uso porque no te queda otra aunque tiene una curva de aprendizaje ligera.

Todo lo demás lo hago en **VSCode**, tampoco me quiero parar aquí porque cada uno tiene su IDE de confianza y este es el mio. Tampoco tengo muchas extensiones ni nada en especial.

Ahora, cosas que te pueden servir si estás pensando en alojar una web personal o de algún proyecto que estés construyendo. Lo primero **Cloudflare**. Es una pasada todo lo que tiene. Aquí tengo mi dominio, correo, registros DNS de subdominios y muchas reglas WAF y configuración para evitar ataques y bots en las páginas que gestiono.

Todas las webs salvo esta del blog las creo en React + [Vite](https://vite.dev/guide/), las subo a **GitHub** y las despliego en **Vercel**. Vercel también es una pasada porque monitorea tus repositorios y en el momento que detecta un push construye la página y la despliega en cuestión de segundos.

Vercel está muy bien pero hay que tener cuidado, tiene una capa gratuita generosa pero si te pasas de cierto tráfico te cobran (como es lógico). ¿Por qué te lo digo entonces? Se dan casos de gente que pone su web con Vercel y sufre un ataque en el que consumen sus recursos.

Este tipo de ataques no tienen mayor objetivo que j\*derte. Van a tu web, abren los devTools, cogen el **recurso más pesado de tu web** y empiezan a hacerle **consultas** de forma masiva. Si no estás preparado al día siguiente te despiertas con una factura como la del tweet que pongo aquí arriba.

¿Tiene solución? Si. El propio Vercel te da herramientas para configurar un firewall y minimizarlo. Yo personalmente lo tengo configurado en Cloudflare y si te pasas de cierto límite verás este mensaje:

Para toda la lógica de servidor, en el caso de las aplicaciones para iOS y Apple Watch utilizo los propios servicios de Apple de **CloudKit** como CloudKit DataBase que te vienen incluidos. Para los demás, estoy empezando ahora un proyecto que necesitaré una nube y seguramente me decante por **AWS** a pesar de que usaré muchos servicios de Gemini (Google) para el proyecto.

Sobre este proyecto te contaré más en enero. Es un proyecto que me hace mucha ilusión empezar y me molaría hacer un poco de “build in public” enseñando todo el proceso de principio a fin.

## IAs: GitHub Copilot, Gemini, ChatGPT y Perplexity

No te miento si te digo que todas las semanas uso Gemini, ChatGPT, Copilot, Grok y Perplexity. ¿Por qué? Bueno. Grok y Perplexity son las que menos uso.

De hecho creo que **Perplexity** acabará muriendo con el tiempo si no evolucionan su modelo de negocio. Lo uso principalmente para trabajos del máster para recopilar fuentes. En lugar de buscarlas yo manualmente le explico el tema y le pido fuentes académicas para el tema y ya parto yo de una base de donde filtrar.

**Grok**. Similar a Perplexity pero para documentar mis curiosidades, me permite buscar con lenguaje natural entre todos los tweets. Que tenga todo Twitter de contexto es una pasada si lo sabes usar a tu favor.

**GitHub Copilot**. Sin duda la que más uso últimamente. Es la IA de GitHub que agrupa modelos de OpenAI, Google, Anthropic… para desarrollar. Ya sólo por el autocompletado y los mensajes de commit generados automáticamente merece la pena. Aquí si que tengo una configuración extensa entre ajustes de los modelos, MCPs, ficheros de instrucciones.

Un pequeño tip. Si quieres que copilot genere mensajes de commit automáticamente por ti, en español, con el formato que tú quieras edita el settings.json de VScode y añade algo como esto, edítalo a tu gusto:

```
"github.copilot.chat.commitMessageGeneration.instructions": [

        {
            "text": "Generate commit messages in Spainsh following the Conventional Commits specification (e.g., feat(api): description). Use imperative mood for the description. Infer the type (feat, fix, refactor, test, docs) and optional scope from the changes. Write them in  Spanish and in friendly tone. If no changes are detected, return 'No changes detected'.",
        }
    ],
```

**Gemini y ChatGPT**. El día que Gemini integre proyectos en su aplicación diré adiós a ChatGPT. He pasado de ser hater de Gemini cuando se llamaba Bard y ser fan la verdad jajaja. Por modelo, ventana d contexto, edición de imagen y video Gemini es una pasada. Sólo uso ChatGPT para dos cosas: proyectos por el contexto y hablar con él.

El **modo voz de ChatGPT** me parece todavía mucho mejor al de Gemini y lo uso a diario. Actualmente con temas del máster me apunto en el cuaderno cosas que no entiendo como conceptos o explicaciones y por la tarde cuando salgo de paseo o voy en el coche al gimnasio pongo el modo voz y voy repasando con Chat todo esto. Para mi es un salto loco para entender conceptos complejos, bajarlos a tierra, poder explicarlos y que me corrijan. Si estáis estudiando probadlo un par de veces porque merece la pena.

## Otras Aplicaciones

Quizás la sección más importante si lo que quieres es descubrir aplicaciones nuevas que te hagan la vida más fácil.

Como navegador uso Safari el 95% del tiempo, es rápido, no me ha fallado nunca, buena gestión de memoria… ¿el 5% restante? **Brave Browser** por YouTube sin anuncios.

Atajo para abrir YouTube en iPhone o iPad

Os dejo este atajo para abrir YouTube directamente en Brave en el iPhone. Lo añadís a la pantalla de inicio, le ponéis el icono de YouTube y a correr.

Una cosa que me revienta de macOS es la gestión de ventanas. No existe la posibilidad de configurar atajos de teclado para redimensionarlas como en Windows. Existe una aplicación buenísima que se llama Magnet que lo soluciona aunque también hay una versión Open Source igual de buena que es [Rectangle](https://rectangleapp.com) que es la que llevo usando varios años y es un 10/10.

Si trabajáis con monitores externos tenéis que tener [Better Display](https://github.com/waydabber/BetterDisplay) para poder gestionar el brillo y sonido del monitor directamente con los controles nativos del mac.

Si tenéis un macbook entonces también necesitas [battery](https://github.com/actuallymentor/battery), una app para gestionar los límites de carga de la batería y que alargará la vida útil de tu batería si la usas conectada a la corriente casi siempre.

Para diseños sólo uso **Figma**, es una pasada lo bien que funciona. Uno de los primeros posts que escribí fue explicando como uso Figma para los diseños de una app. Te lo dejo por [aquí](https://www.blog.lvrpiz.com/p/como-disenar-app-figma-ai) si te interesa.

Por último te quería hablar de dos aplicaciones creadas por un servidor. La primera es de la que ya te he hablado en varias ocasiones: [Stress Tracker](https://stressapp.lvrpiz.com), una app para Apple Watch que consume datos de HealthKit para estimar tus niveles de estrés en base a la variabilidad de la frecuencia cardiaca (HRV), HR, descanso, edad y sexo. Es una app que disfruté mucho construir y que me ha sorprendido la cantidad de usuarios que la usan semanalmente.

Finalmente te hablo de [Lapis](https://lapis.lvrpiz.com), una app que te permite correr modelos de IA en local en tu móvil o iPad sin conexión a internet, de forma privada. Le doy un uso muy esporádico pero me permite probar modelos Open Source que van saliendo como Qwen, Gemma, Phi… y testearlos. Quizás esta app requiera unos ciertos conocimientos previos sobre LLMs como saber ajustar temperatura, TopP, TopK, ventanas de contexto… pero si te gusta trastear está muy bien.

Hasta aquí las aplicaciones que uso y mi sistema de productividad. Sólo decirte que si usas una app que crees que me gustaría responde a este mail con el nombre o el enlace. La idea es reescribir este mismo post el año que viene y ver qué ha cambiado (si ha cambiado algo).