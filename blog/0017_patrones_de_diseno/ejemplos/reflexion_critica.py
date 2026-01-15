import os
import json
from google import genai
from pydantic import BaseModel
import enum

# Configura el cliente (asegúrate de que GEMINI_API_KEY esté en tu entorno de macOS)
cliente = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

class EstadoEvaluacion(enum.Enum):
    APROBADO = "APROBADO"
    RECHAZADO = "RECHAZADO"

class Evaluacion(BaseModel):
    evaluacion: EstadoEvaluacion
    comentarios: str
    razonamiento: str

# --- Función de generación inicial ---
def generar_poema(tema: str, comentarios: str = None) -> str:
    instruccion = f"Escribe un poema corto de cuatro líneas sobre {tema}."
    if comentarios:
        instruccion += f"\nIncorpora estos comentarios: {comentarios}"
    
    respuesta = cliente.models.generate_content(
        model='gemini-2.0-flash',
        contents=instruccion
    )
    poema = respuesta.text.strip()
    print(f"Poema generado:\n{poema}")
    return poema

# --- Función de evaluación ---
def evaluar(poema: str) -> Evaluacion:
    print("\n--- Evaluando poema ---")
    instruccion_critica = f"""Critica el siguiente poema. ¿Rima bien? ¿Tiene exactamente cuatro líneas? 
¿Es creativo? Responde con APROBADO o RECHAZADO y proporciona comentarios.

Poema:
{poema}
"""
    respuesta_critica = cliente.models.generate_content(
        model='gemini-2.0-flash',
        contents=instruccion_critica,
        config={
            'response_mime_type': 'application/json',
            'response_schema': Evaluacion,
        },
    )
    critica = respuesta_critica.parsed
    print(f"Estado de la evaluación: {critica.evaluacion}")
    print(f"Comentarios de la evaluación: {critica.comentarios}")
    return critica

# Bucle de reflexión
max_iteraciones = 3
iteracion_actual = 0
tema = "un robot aprendiendo a pintar"

# Poema simulado que no pasará la evaluación (solo dos líneas)
poema_actual = "Con circuitos zumbando, fríos y brillantes,\nuna mano de metal sostiene ahora un pincel"

while iteracion_actual < max_iteraciones:
    iteracion_actual += 1
    print(f"\n--- Iteración {iteracion_actual} ---")
    resultado_evaluacion = evaluar(poema_actual)

    if resultado_evaluacion.evaluacion == EstadoEvaluacion.APROBADO:
        print("\nPoema final:")
        print(poema_actual)
        break
    else:
        poema_actual = generar_poema(tema, comentarios=resultado_evaluacion.comentarios)
        if iteracion_actual == max_iteraciones:
            print("\nMáximo de iteraciones alcanzado. Último intento:")
            print(poema_actual)