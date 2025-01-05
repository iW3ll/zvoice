import gradio as gr
import requests
import tempfile
import os

def text_to_speech(text, voice_id, api_key):
    api_key ="" # Put api key here from eleven labs
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,  
        "Content-Type": "application/json",
        "accept": "audio/mpeg"
    }
    data = {
    "text": text,
    "voice_settings": {
        "stability": 0.5,  # Let voice more statable
        "similarity_boost": 0.75  # Let the voice better more human
    }
}
    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return f"Erro: {response.text}" 

    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
        f.write(response.content)
        filepath = f.name
    return filepath

def delete_temp_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)

inputs = [
    gr.Textbox(label="Text"),
    gr.Textbox(label="Voice ID  "),
    gr.Textbox(label="API Key")
]

output = gr.Audio()

title = "IA Project - Text To Voice"
description = "Convert Text To Voice"
examples = [
    ["Esse é um projeto da disciplina de IA. Ele cria uma GUI que o usuário possa interagir e transforma o texto em audio em diferentes idiomas dependendo do texto", "XB0fDUnXU5powFXDhCwa", "api_key"],
    ["Olá, como você está?", "2EiwWnXFnvU5JabPnv8n", "api_key"],
    ["Pode tocar alguma música?", "ThT5KcBeYPX3keUQqHPh", "api_key"]
]

# Inicializa a interface Gradio
gr.Interface(fn=text_to_speech, inputs=inputs, outputs=output, title=title, description=description, examples=examples).launch()