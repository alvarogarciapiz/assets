import os
from google import genai

# Configura el cliente (asegúrate de que GEMINI_API_KEY esté configurada en tu entorno)
cliente = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# --- Paso 1: Resumir texto ---
texto_original = "Los modelos de lenguaje grandes son potentes sistemas de IA entrenados con vastas cantidades de datos de texto. Pueden generar texto similar al humano, traducir idiomas, escribir diferentes tipos de contenido creativo y responder a sus preguntas de forma informativa."
instruccion1 = f"Resume el siguiente texto en una sola frase: {texto_original}"

# Uso de cliente.models.generate_content
respuesta1 = cliente.models.generate_content(
    model='gemini-2.0-flash',
    contents=instruccion1
)
resumen = respuesta1.text.strip()
print(f"Resumen: {resumen}")

# --- Paso 2: Traducir el resumen ---
instruccion2 = f"Traduce el siguiente resumen al francés, solo devuelve la traducción, sin ningún otro texto: {resumen}"

# Uso de cliente.models.generate_content
respuesta2 = cliente.models.generate_content(
    model='gemini-2.0-flash',
    contents=instruccion2
)
traduccion = respuesta2.text.strip()
print(f"Traducción: {traduccion}")