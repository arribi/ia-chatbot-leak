import openai

# Configuración del modelo de IA
OPENAI_API_KEY = "sk-0123456789abcdefghijT3BlbkFJ0123456789abcdefghij"

def preguntar_ia(prompt):
    print(f"Enviando consulta a OpenAI: {prompt}")

if __name__ == "__main__":
    preguntar_ia("¿Cómo configurar Caddy como proxy inverso?")