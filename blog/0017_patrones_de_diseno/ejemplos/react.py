import os
from google import genai
from pydantic import BaseModel, Field
from typing import List

# Configura el cliente (asegúrate de que GEMINI_API_KEY esté configurada en tu entorno de macOS)
cliente = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Definición del esquema del plan
class Tarea(BaseModel):
    id_tarea: int
    descripcion: str
    asignado_a: str = Field(description="¿Qué tipo de trabajador debe manejar esto? Ej: Investigador, Escritor, Programador")

class Plan(BaseModel):
    objetivo: str
    pasos: List[Tarea]

# Paso 1: Generar el plan (LLM Planificador)
objetivo_usuario = "Escribe una entrada de blog corta sobre los beneficios de los agentes de IA."

instruccion_planificador = f"""
Crea un plan paso a paso para alcanzar el siguiente objetivo. 
Asigna cada paso a un tipo de trabajador hipotético (Investigador, Escritor).

Objetivo: {objetivo_usuario}
"""

print(f"Objetivo: {objetivo_usuario}")
print("Generando plan...")

# Uso de un modelo con capacidad de planificación y salida estructurada
# Se utiliza la versión 2.5 Pro para razonamiento complejo
respuesta_plan = cliente.models.generate_content(
    model='gemini-2.5-pro-preview-03-25',
    contents=instruccion_planificador,
    config={
        'response_mime_type': 'application/json',
        'response_schema': Plan,
    },
)

# Paso 2: Ejecutar el plan (Orquestador/Trabajadores)
# Iteramos sobre los pasos parseados automáticamente por el SDK
for paso in respuesta_plan.parsed.pasos:
    print(f"Paso {paso.id_tarea}: {paso.descripcion} (Asignado a: {paso.asignado_a})")