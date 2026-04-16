
import os
from groq import Groq

key = ""

client = Groq(api_key=key)

def consultar_llama(prompt_usuario):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Eres un asistente servicial y conciso."},
                {"role": "user", "content": prompt_usuario}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7, # Ajustado a un valor más estable
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error en la consulta: {e}"

def ejecutar_interfaz():
    print("--- Interfaz de Kala 70B (Modo Loop) ---")
    while True:
        entrada = input("\nUsuario: ").strip()
        
        if entrada.lower() in ["salir", "exit", "quit"]:
            print("Cerrando sesión...")
            break
            
        if not entrada:
            continue

        respuesta = consultar_llama(entrada)
        print(f"\nKala: {respuesta}")

if __name__ == "__main__":
    ejecutar_interfaz()