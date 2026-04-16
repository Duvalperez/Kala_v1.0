import os
from groq import Groq

def consultar_con_validaciones(prompt):
    # Clave directa
    key = ""
    
    # Validaciones
    if not key or key == "TU_CLAVE_AQUI":
        return "Error: Falta la API Key."
    
    if not prompt.strip():
        return "Error: El mensaje está vacío."

    try:
        # Inicialización del cliente dentro de la función
        client = Groq(api_key=key)
        
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error de conexión o API: {str(e)}"

# --- BLOQUE PARA QUE EL CÓDIGO CORRA ---
if __name__ == "__main__":
    print("--- Probando conexión con Groq ---")
    pregunta = input("Escribe tu pregunta para Kala: ")
    resultado = consultar_con_validaciones(pregunta)
    print(f"Respuesta: {resultado}")