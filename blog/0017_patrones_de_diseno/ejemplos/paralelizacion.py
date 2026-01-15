import os
import asyncio
import time
from google import genai

# Configura el cliente (asegúrate de que GEMINI_API_KEY esté en tu entorno de macOS)
cliente = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

async def generar_contenido(instruccion: str) -> str:
    respuesta = await cliente.aio.models.generate_content(
        model="gemini-2.0-flash",
        contents=instruccion
    )
    return respuesta.text.strip()

async def tareas_paralelas():
    # Definir tareas en paralelo
    tema = "un robot amigable explorando una selva"
    instrucciones = [
        f"Escribe una idea corta y aventurera sobre {tema}.",
        f"Escribe una idea corta y divertida sobre {tema}.",
        f"Escribe una idea corta y misteriosa sobre {tema}."
    ]
    
    # Ejecutar tareas de forma concurrente y reunir resultados
    tiempo_inicio = time.time()
    tareas = [generar_contenido(instruccion) for instruccion in instrucciones]
    resultados = await asyncio.gather(*tareas)
    tiempo_fin = time.time()
    print(f"Tiempo transcurrido: {tiempo_fin - tiempo_inicio} segundos")

    print("\n--- Resultados individuales ---")
    for i, resultado in enumerate(resultados):
        print(f"Resultado {i+1}: {resultado}\n")

    # Agregar resultados y generar historia final
    ideas_historias = '\n'.join([f"Idea {i+1}: {resultado}" for i, resultado in enumerate(resultados)])
    instruccion_agregacion = f"Combina las siguientes tres ideas en un único párrafo de resumen cohesivo: {ideas_historias}"
    
    respuesta_agregacion = await cliente.aio.models.generate_content(
        model="gemini-2.5-flash-preview-04-17",
        contents=instruccion_agregacion
    )
    return respuesta_agregacion.text

# Ejecución del bucle de eventos
resultado_final = await tareas_paralelas()
print(f"\n--- Resumen agregado ---\n{resultado_final}")