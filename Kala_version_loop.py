
import os
from groq import Groq

# Asignación directa de la clave
client = Groq(api_key="")

def consulta_rapida(texto):
    # Ejecuta una sola vez y termina
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": texto}],
        model="llama-3.3-70b-versatile"
    )
    print(f"Respuesta única: {completion.choices[0].message.content}")
