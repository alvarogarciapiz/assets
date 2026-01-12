---
title: "Tendencias IA 2026: Antes de planificar tu año, lee este análisis"
date: "12 de Enero de 2026"
edition: 14
source: "https://www.blog.lvrpiz.com/p/tendencias-ia-2026-analisis"
---

# Tendencias IA 2026: Antes de planificar tu año, lee este análisis

Guía completa sobre las tendencias IA 2026. Futuro de los agentes, qué esperar de los world models y por qué el contenido humano será más valioso que nunca.

Hola,

Bueno, pues ya estamos aquí. Último día del año. Llevo medio año con este proyecto de la newsletter y el recibimiento ha sido muy bueno. De verdad, gracias a todos los que estáis al otro lado leyendo cada semana, respondiendo y compartiendo esto.

En la edición anterior os dije que si solo podíais leer un post de todos los que publique este año, que fuera este. Y no lo decía por decir. Hoy **no** quiero traeros el típico resumen de *lo mejor de 2025*, porque eso ya lo habéis visto en mil sitios. Hoy quiero mirar hacia delante.

El tema es el futuro de la inteligencia artificial, pero poniendo el foco en **2026**. En este post os voy a soltar bastantes ideas, algunas quizás un poco polémicas, otras más técnicas, pero todas fruto de lo que he estado observando, probando y sufriendo este último año.

Aquí van mis apuestas y reflexiones para el futuro de la IA para el año 2026:

### **El mito de los agentes autónomos (y por qué 2026 tampoco será su año)**

El año pasado nos vendieron que 2025 sería el *año de los agentes*. Y, ojo, a pesar de que mucha gente insista en que lo ha sido, la realidad es que ni de lejos. Una cosa es que se presente la tecnología en una demo muy bonita y otra muy distinta es que sea productiva en el mundo real.

Vimos la presentación del navegador de OpenAI, **Atlas**, que no deja de ser un *wrapper* de Google Chrome con ChatGPT siempre accesible. Nada más. Sí, tiene una parte agéntica, pero todavía no es funcional del todo.

El problema de fondo es la confianza. La tecnología no está lo suficientemente madura como para dejarla trabajar por su cuenta sin supervisión. Tanto es así que las demos más impresionantes que nos enseñaron, esas que supuestamente tienen que dejarnos con la boca abierta, no dejaban de ser tareas simples como "hazme la compra". Y, para colmo, para agregar cuatro productos al carrito tardaba mucho más de lo que hubiéramos tardado tú o yo en hacerlo.

Y siempre te queda esa incertidumbre de: "Oye, ¿lo ha hecho bien? ¿Ha mirado mi marca favorita? ¿Ha cogido la mejor oferta?". Esa fricción cognitiva mata la utilidad del agente. Mientras tengas que revisar con lupa lo que hace, no es un agente, es un becario muy rápido pero poco fiable.

### **La trampa de los Agentes de Programación y los IDEs**

Aquí hemos visto un salto que parece cualitativo, pero tiene truco. Vimos *Antigravity* de Google, hemos visto *Codex*, y prácticamente cada empresa de IA (más un montón de startups que son meros *wrappers*) ha sacado su propio IDE que etiquetan como agéntico.

La realidad es que de agénticos tienen poco. Lo que hacen muy bien es aprovechar modelos con capacidades brutales de *Function Calling* (llamadas a herramientas), que es vital, se aprovechan de los MCPs (Model Context Protocol) y otras tecnologías, pero lo que tenemos hoy son **workflows agénticos**, no agentes reales.

Os cuento esto porque me picó la curiosidad y hace un mes me propuse un reto: crear desde cero una aplicación sencilla sin escribir yo ni una sola línea de código, usando solo *Antigravity* y los mejores modelos del momento. He aprendido una barbaridad, pero **mi conclusión es que estos modelos siguen siendo orquestadores de funciones**.

Es como un modo edición supervitaminado donde tú pides algo y el modelo es capaz de listar ficheros, eliminar cosas o editar directorios porque le hemos dado permisos, pero no tiene la autonomía real para tomar decisiones complejas de arquitectura o corregir el rumbo si se equivoca profundamente. **No tienen todavía capacidad de ver un proyecto como un todo** por mucho que haya gente que te diga que con varios ficheros de instrucciones y contexto lo tienes solucionado. Solucionan errores provocando otros en otras partes del código a pesar de usar ficheros de contexto especiales y buen prompting.

2026 mejorará la llamada a funciones y los modelos podrán razonar durante más tiempo antes de actuar, pero seguirán fallando estrepitosamente en tareas de largo recorrido sin intervención humana.

### **La gran deuda técnica: Memoria y Contexto**

Si hay algo que tiene que mejorar sí o sí, es la memoria. Actualmente, es uno de los puntos más débiles. Las memorias que usamos ahora mismo son, básicamente, parches que ocupan contexto del modelo.

Cuando empiezas un chat nuevo, tienes el *System Prompt*, y a eso se le añaden ciertas memorias que el modelo ha guardado de conversaciones anteriores. El problema es que **esas memorias consumen tokens de entrada**. Cuantas más cosas recuerde de ti, menos espacio le queda para procesar la tarea actual, y a veces eso hace que las respuestas sean más personalizadas pero menos precisas técnicamente.

Lo ideal, y lo que creo que veremos madurar en 2026, es un sistema donde el modelo sepa inyectar en tiempo real esas memorias sin necesidad de ocupar todo el contexto de golpe. Ya hay bastantes *papers* académicos de finales de este año apuntando a arquitecturas de memoria dinámica. **2026 será el año donde la memoria mejore cuantitativamente**, permitiendo que la IA mantenga el hilo de proyectos largos sin alucinar o olvidar lo que le dijiste hace tres días. Aquí Antrhopic lleva ventaja y tiene un modelo de memoria superior a la de otras empresas, os dejo este [post](https://simonwillison.net/2025/Sep/12/claude-memory/) de Simon Willison donde lo explica.

### **Vídeo, Imagen y el rechazo social**

En imagen y vídeo, 2025 ha sido una locura. No es el campo que sigo con más especialidad, pero hay que reconocer que modelos como *Flux* o lo que está haciendo *Sora* o *Veo 3* son impresionantes. Para 2026, veremos modelos de vídeo que entiendan mucho mejor las físicas y que obedezcan mejor nuestras instrucciones

Y aquí viene mi *hot take*: creo que **en 2026 veremos la primera serie o película un poco** ***mainstream*** **hecha íntegramente con IA**, seguramente en alguna plataforma de streaming. Pero, y aquí está la clave, creo que tendrá un rechazo enorme.

Ya está pasando. Fijaos en los anuncios de esta [Navidad de Coca-Cola](https://www.youtube.com/watch?v=Yy6fByUmPuE) o [McDonald's](https://www.youtube.com/watch?v=E-YwjXEVGo8) hechos con IA. La gente los ha puesto a parir. Y es normal. Todavía somos capaces de identificar esos fallos, esa falta de alma, y nos produce rechazo. Pero estamos llegando a ese punto peligroso donde dejará de ser distinguible. El problema no será técnico, será social: **nos vamos a cansar de la perfección sintética**. 2026 será definitivamente el año del vídeo técnico, pero también el año de la fatiga visual por IA.

### **World Models: El texto NO es suficiente**

Hay una barrera que los LLMs no van a poder cruzar con facilidad y es poder interactuar con el mundo físico. Las máquinas, a corto y medio plazo, no van a ser tan precisas moviéndose por el mundo real como nosotros. Un LLM sabe predecir la siguiente palabra, **pero no entiende la gravedad o que si suelta un vaso, se rompe, a menos que lo haya leído**.

Por eso, a partir de 2026, gran parte de los esfuerzos de investigación (y de la pasta) se irán a los [**World Models**](https://www.nvidia.com/en-us/glossary/world-models/). De hecho, varios investigadores top ya están dejando de lado los LLMs puros, diciendo que el trabajo ahí ya es residual o de optimización, y se están [pasando a modelos que simulan entornos físicos](https://techcrunch.com/2025/12/19/yann-lecun-confirms-his-new-world-model-startup-reportedly-seeks-5b-valuation/). Estos modelos ayudarán a los robots a entender el entorno.

Pero hasta que eso llegue, va a pasar un tiempo largo. Y entre medias, va a ocurrir algo curioso que ya estamos viendo: estamos delegando la carga cognitiva a las máquinas, y las máquinas nos están ordenando el trabajo manual a nosotros. **Somos la interfaz de los LLMs en el mundo físico**.

Pensadlo con *Glovo* o *Uber*. Hay una IA (no un LLM, pero un algoritmo complejo) que decide quién recoge qué, dónde y cuándo. Optimiza la ruta. Y los humanos somos los que ejecutamos la tarea física de mover el paquete. **Somos la interfaz de la máquina con el mundo real**. Seguiremos siendo el middleware físico hasta que la robótica, impulsada por estos World Models, esté lista. Y para eso queda más que para 2026.

### **La teoría del Internet Muerto y el valor de lo humano**

Este año, en el evento del *VallTechSummit*, comenté una noticia que me dio que pensar: la [teoría del Internet Muerto](https://www.galaxy.com/insights/perspectives/dead-internet-theory-collapse-online-truth) cada vez tiene más sentido. Esta teoría dice que, en el futuro, la mayoría del tráfico y contenido en internet será generado por bots interactuando con otros bots, y los humanos seremos una minoría.

En 2025 ya cruzamos una frontera histórica: [la cantidad de contenido generado por IA superó al contenido generado por humanos](https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans). Esto nos lleva a dos vertientes para 2026.

La primera es la identificación. **Necesitamos saber qué es humano y qué no**. En otro post os hablé de [*SynthID*](https://www.blog.lvrpiz.com/p/guia-synthid-watermarking-texto-imagen-video) [de Google](https://www.blog.lvrpiz.com/p/guia-synthid-watermarking-texto-imagen-video), una solución técnica muy buena para marcar (watermarking) texto, imagen y vídeo. A las propias empresas de IA les interesa esto porque si entrenan a sus futuros modelos con datos generados por sus modelos anteriores, se produce un colapso de la información, se vuelven repetitivos. Necesitan filtrar para entrenar solo con datos humanos frescos. Veremos marcas de *Generado por IA* en Instagram, Facebook, WhatsApp y LinkedIn (donde ya está). Twitter... bueno, Twitter es otro mundo, aunque **la UE seguramente meta mano ahí con regulaciones** a no tardar.

En cuanto al contenido, circula una teoría sobre el [protocolo x402](https://www.x402.org) que vendría a proteger el contenido humano en internet haciendo pagar una tasa a los bots que leen webs para entrenar modelos. Este protocolo exigiría a los agentes de IA pagar por el acceso a la API en tiempo real. No creo que esto se convierta en un estándar ni de lejos pero es curioso como hay esfuerzos en seguir protegiendo el contenido humano.

La segunda vertiente es justo esto mismo. **El contenido humano tendrá cada vez más valor (o precio)**. Las experiencias presenciales, los encuentros físicos, la opinión real de una persona con cara y ojos... eso va a cotizar al alza. La gente se va a cansar del contenido infinito y perfecto pero vacío.

### **Apple Intelligence y la falsa necesidad de un Chatbot**

Aquí quiero hacer un inciso importante con Apple. Se les ha criticado muchísimo este año por no tener su propio ChatGPT, como si eso fuera el único estándar de IA válido. Pero ojo, que la gente se olvida de que Apple lleva años integrando *machine learning* en todo su sistema operativo y, de hecho, sus chips son los que mejor preparados están ahora mismo, con diferencia, para correr cargas de IA en local y creo que aunque lleguen tarde la idea que proponen es realmente buena.

Y aquí lanzo la pregunta: ¿Realmente necesitan su propio ChatGPT? Mi opinión es que no. Su *approach* es completamente diferente y mucho más ambicioso. Piensa que a ChatGPT le tienes que dar tú el contexto, tienes que explicarle las cosas, Apple no quiere ir por esa vía. Apple quiere (y puede) usar modelos fundacionales diseñados para entender tu contexto personal al máximo. **Ellos ya tienen la pieza que les falta a los demás: saben tus citas, tus eventos, tus correos y tus hábitos.**

No creo que Apple vaya a sacar una *app* para competir con ChatGPT ni a corto ni a medio plazo: para las preguntas genéricas ya tienen el acuerdo con OpenAI y uno futuro con Google. Su apuesta real es crear un asistente proactivo que funcione solo, que se anticipe y que entienda al usuario profundamente sin que le tengas que escribir un *prompt*. Esa es la verdadera IA personal.

### **Hardware y Wearables: ¿Realmente necesitamos llevar un collar inteligente?**

Hay rumores fuertes de que OpenAI está trabajando con Jony Ive en un [dispositivo](https://www.bloodinthemachine.com/p/an-always-on-openai-device-is-a-massive) [*hardware*](https://www.bloodinthemachine.com/p/an-always-on-openai-device-is-a-massive). Se habla de algo tipo collar, con micrófono y altavoz, para ir hablando con la IA todo el día.

Concepto del posible dispositivo de OpenAI

Mira, yo aquí soy muy escéptico. El **teléfono móvil es una tecnología demasiado madura y perfecta como para que un** ***wearable*** **sin pantalla lo reemplace**. Además, hay un factor social que se nos olvida: hablar con una máquina en público es raro (por ahora).

La mayoría de nosotros pasamos el día en oficinas, transporte público o espacios compartidos. No vas a ponerte a dictarle a tu collar un correo o a preguntarle dudas existenciales delante de tu compañero de mesa. La voz como interfaz principal está destinada al fracaso en entornos sociales, al menos a corto plazo.

Para mí, **todo esto debería ser una** ***app*****, no un dispositivo**. Si Apple o Google integran bien sus asistentes en el móvil, el dispositivo dedicado pierde todo el sentido.

### **El hardware como foso defensivo y software como commodity**

Pensadlo un momento: en un mundo donde cualquiera puede generar código y crear "software" casi al instante, **tener una app deja de ser una ventaja competitiva. El software se está convirtiendo en una commodity**.

Entonces, ¿dónde está el valor real? **En atar ese software a algo físico**. El hardware se convierte en el nuevo foso defensivo para las empresas. Las compañías que realmente van a destacar en 2026 no son las que te den otro chatbot, sino las que integren verticalmente de forma que sea imposible de copiarlas.

Mirad el éxito de [Oura](https://ouraring.com/es?srsltid=AfmBOooYheRn4QTBXMCKSuckgU9AULFsMXwvhVQP3EThVkBE7AvNvuX-) o [Whoop](https://www.whoop.com/es/es/?srsltid=AfmBOoqyFvSeH27rCD5hgIRnErHboOAjiYJ8_v3UBlmE9Gl5-z9f3MhX). La IA ahí es brutal, sí, pero está casada a fuego con el anillo o la pulsera. O casos más de nicho como [Board](https://board.fun) para juegos físicos conectados o [Meter](https://www.meter.com) en redes empresariales. No te venden solo el panel de control con IA, te venden el equipo industrial necesario para que eso funcione. Esa combinación es mucho más difícil de replicar para un competidor que simplemente clonar un repo de GitHub.

Además aquí hay un cambio importante, cada vez es más fácil fabricar. Están surgiendo un montón de empresas que simplifican el diseño de chips, los prototipos y la gestión de la cadena de suministro. Montar una startup de hardware solía ser una locura financiera, ahora empieza a ser viable. Así que preparaos **para ver mucha más variedad de productos físicos específicos**, y menos SaaS genéricos que no aportan nada nuevo.

### **La burbuja económica: ¿Dónde está el dinero real?**

Para cerrar, una reflexión económica. ¿Estamos en una burbuja de IA? Depende de dónde mires. En el *hardware* no hay burbuja: Nvidia y los fabricantes de chips están haciendo caja real. Es dinero físico circulando ahí hay negocio tangible.

Donde sí veo una **burbuja es en la capa de aplicación**. Hay miles de empresas que por el simple hecho de ponerse un *AI* en el nombre y ser un *wrapper* básico de ChatGPT se han valorado por múltiplos absurdos. Esas empresas, que no tienen barrera de entrada tecnológica, van a desaparecer. En Estados Unidos están saliendo como setas y caerán igual de rápido. Solo sobrevivirán las que aporten valor real sobre el modelo, no las que solo lo revenden.

Dicho esto, el año que viene por estas fechas nos pasamos de nuevo por aquí y repasamos juntos si me he equivocado mucho, que seguro que alguna patinada hay.

Gracias por estar ahí este 2025. Buena entrada de año 2026 🥂

Abrazo, Álvaro