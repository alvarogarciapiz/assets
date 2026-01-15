# Patrones de Diseño para Agentes de IA

Este repositorio contiene ejemplos prácticos de las arquitecturas fundamentales para el desarrollo de agentes autónomos. Los scripts están adaptados al castellano e incluyen explicaciones detalladas sobre su lógica y ejecución.

## Inspiracion y Referencias

El código y los conceptos implementados se basan en las siguientes fuentes técnicas:

- Agentic Patterns (Philipp Schmid): https://www.philschmid.de/agentic-pattern#multi-agent-pattern
- Strands Agents Documentation (Swarm): https://strandsagents.com/latest/documentation/docs/user-guide/concepts/multi-agent/swarm/

## Contexto del Proyecto

Este material es el complemento técnico de la edición número 17 de la newsletter **The Blueprint Circle** de Álvaro García Pizarro, publicada el 21 de enero de 2026.

Artículo de referencia: https://www.blog.lvrpiz.com/p/patrones-diseno-agentes-ia

## Catalogo de Patrones Implementados

- Encadenamiento de Prompts: Secuencias fijas donde la salida de un modelo es la entrada del siguiente.
- Enrutamiento: Clasificación de intenciones para dirigir la consulta hacia flujos especializados.
- Paralelización: Ejecución simultánea de tareas (Sectioning y Voting) para optimizar latencia.
- Orquestador y Trabajadores: Un planificador central que descompone tareas y delega en especialistas.
- Reflexión y Crítica (Evaluator-Optimizer): Bucles de revisión para el refinamiento iterativo de resultados.
- Razonamiento y Acción (ReAct): Ciclos de pensamiento y ejecución de herramientas con observación de resultados.
- Enjambre (Swarm): Colaboración descentralizada entre múltiples agentes mediante protocolos de traspaso (handoffs).