import logging
from strands import Agent
from strands.multiagent import Swarm

# Habilitar registros de depuración y enviarlos a la salida de error estándar
logging.getLogger("strands.multiagent").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

# Crear agentes especializados
investigador = Agent(name="investigador", system_prompt="Eres un especialista en investigación...")
programador = Agent(name="programador", system_prompt="Eres un especialista en programación...")
revisor = Agent(name="revisor", system_prompt="Eres un especialista en revisión de código...")
arquitecto = Agent(name="arquitecto", system_prompt="Eres un especialista en arquitectura de sistemas...")

# Crear un enjambre (Swarm) con estos agentes, comenzando por el investigador
enjambre = Swarm(
    [programador, investigador, revisor, arquitecto],
    entry_point=investigador,  # Iniciar con el investigador
    max_handoffs=20,
    max_iterations=20,
    execution_timeout=900.0,  # 15 minutos
    node_timeout=300.0,       # 5 minutos por agente
    repetitive_handoff_detection_window=8,  # Debe haber >= 3 agentes únicos en los últimos 8 traspasos
    repetitive_handoff_min_unique_agents=3
)

# Ejecutar el enjambre en una tarea
resultado = enjambre("Diseña e implementa una API REST simple para una aplicación de tareas (todo app)")

# Acceder al resultado final
print(f"Estado: {resultado.status}")
print(f"Historial de nodos: {[nodo.node_id for nodo in resultado.node_history]}")