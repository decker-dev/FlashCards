data_store = {
    "default": [
        {"question": "¿Cuál es la capital de Francia?", "answer": "París"},
        {"question": "¿Cuál es el resultado de 2 + 2?", "answer": "4"},
        {"question": "¿Cuál es el idioma oficial de Brasil?", "answer": "Portugués"}
    ]
}

def save_data(data):
    global data_store
    data_store = data

def load_data():
    global data_store
    return data_store
