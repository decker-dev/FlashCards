import json
import os

FILE_NAME = 'data_store.json'

initial_data = {
    "default": [
        {"question": "¿Cuál es la capital de Francia?", "answer": "París"},
        {"question": "¿Cuál es el resultado de 2 + 2?", "answer": "4"},
        {"question": "¿Cuál es el idioma oficial de Brasil?", "answer": "Portugués"}
    ],
}

def save_data(data):
    """Guarda los datos en el archivo JSON."""
    try:
        file = open(FILE_NAME, 'w', encoding='utf-8')
        try:
            json.dump(data, file, ensure_ascii=False, indent=2)
        finally:
            file.close()
    except IOError as e:
        print(f"Error al guardar los datos en {FILE_NAME}: {e}")

def load_data():
    """Carga los datos desde el archivo JSON. Si no existe, lo crea con los datos iniciales."""
    try:
        if os.path.exists(FILE_NAME):
            file = open(FILE_NAME, 'r', encoding='utf-8')
            try:
                return json.load(file)
            finally:
                file.close()
        else:
            print(f"El archivo {FILE_NAME} no existe. Creando archivo con datos iniciales.")
            save_data(initial_data)
            return initial_data
    except IOError as e:
        print(f"Error al leer el archivo {FILE_NAME}: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON en el archivo {FILE_NAME}: {e}")
        return None