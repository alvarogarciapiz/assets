import os
import json
from google import genai
from pydantic import BaseModel
import enum

# Configura el cliente (asegúrate de que GEMINI_API_KEY esté configurada en tu entorno de macOS)
cliente = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Definir esquema de enrutamiento
class Categoria(enum.Enum):
    CLIMA = "clima"
    CIENCIA = "ciencia"
    DESCONOCIDO = "desconocido"

class DecisionEnrutamiento(BaseModel):
    categoria: Categoria
    razonamiento: str

# Paso 1: Enrutar la consulta
consulta_usuario = "¿Cómo está el tiempo en París?"
# consulta_usuario = "Explica la física cuántica de forma sencilla."
# consulta_usuario = "¿Cuál es la capital de Francia?"

instruccion_enrutador = f"""
Analiza la consulta del usuario a continuación y determina su categoría.
Categorías:
- clima: Para preguntas sobre condiciones meteorológicas.
- ciencia: Para preguntas sobre ciencia.
- desconocido: Si la categoría no está clara.

Consulta: {consulta_usuario}
"""

# Uso de cliente.models.generate_content con configuración para salida estructurada
respuesta_enrutador = cliente.models.generate_content(
    model='gemini-2.0-flash-lite',
    contents=instruccion_enrutador,
    config={
        'response_mime_type': 'application/json',
        'response_schema': DecisionEnrutamiento,
    },
)
print(f"Decisión de enrutamiento: Categoría={respuesta_enrutador.parsed.categoria}, Razonamiento={respuesta_enrutador.parsed.razonamiento}")

# Paso 2: Entrega basada en el enrutamiento
respuesta_final = ""
if respuesta_enrutador.parsed.categoria == Categoria.CLIMA:
    instruccion_clima = f"Proporciona un breve pronóstico del tiempo para la ubicación mencionada en: '{consulta_usuario}'"
    respuesta_clima = cliente.models.generate_content(
        model='gemini-2.0-flash',
        contents=instruccion_clima
    )
    respuesta_final = respuesta_clima.text
elif respuesta_enrutador.parsed.categoria == Categoria.CIENCIA:
    respuesta_ciencia = cliente.models.generate_content(
        model="gemini-2.5-flash-preview-04-17",
        contents=consulta_usuario
    )
    respuesta_final = respuesta_ciencia.text
else:
    respuesta_desconocida = cliente.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=f"La consulta del usuario es: {instruccion_enrutador}, pero no pudo ser respondida. Aquí está el razonamiento: {respuesta_enrutador.parsed.razonamiento}. Escribe una respuesta útil para que el usuario intente de nuevo."
    )
    respuesta_final = respuesta_desconocida.text
print(f"\nRespuesta final: {respuesta_final}")