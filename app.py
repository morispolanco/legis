import streamlit as st
import requests
import json

# Título de la aplicación
st.title("Consultas sobre las leyes de Guatemala")

# Entrada de texto para la pregunta del usuario
pregunta = st.text_input("Haz una pregunta sobre las leyes de Guatemala:")

# Función para hacer la solicitud a la API
def obtener_respuesta(pregunta):
    url = "https://proxy.tune.app/chat/completions"
    headers = {
        "Authorization": f"Bearer {st.secrets['api_key']}",
        "Content-Type": "application/json"
    }
    payload = {
        "temperature": 0,
        "messages": [
            {
                "role": "system",
                "content": "Eres un abogado experto conocedor de la legislación guatemalteca"
            },
            {
                "role": "user",
                "content": pregunta
            }
        ],
        "model": "rohan/mistral-large-2",
        "stream": False,
        "frequency_penalty": 0,
        "max_tokens": 6058
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()["choices"][0]["message"]["content"]

# Botón para enviar la pregunta
if st.button("Enviar"):
    if pregunta:
        respuesta = obtener_respuesta(pregunta)
        st.write("**Respuesta:**")
        st.write(respuesta)
    else:
        st.write("Por favor, ingresa una pregunta.")
