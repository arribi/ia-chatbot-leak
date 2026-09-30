import os
import openai

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def preguntar_ia(prompt):
    print(f"Enviando consulta a OpenAI: {prompt}")

if __name__ == "__main__":
    preguntar_ia("¿Cómo configurar Caddy como proxy inverso?")