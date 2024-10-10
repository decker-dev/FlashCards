import json
import os

# Nombre del archivo donde se guardarán los datos
FILE_NAME = 'data_store.json'

initial_data = {
    "default": [
        {"question": "¿Cuál es la capital de Francia?", "answer": "París"},
        {"question": "¿Cuál es el resultado de 2 + 2?", "answer": "4"},
        {"question": "¿Cuál es el idioma oficial de Brasil?", "answer": "Portugués"}
    ],
    "ciencia": [
        {"question": "¿Cuál es la fórmula química del agua?", "answer": "H2O"},
        {"question": "¿Qué planeta es conocido como el Planeta Rojo?", "answer": "Marte"},
        {"question": "¿Qué gas es esencial para la respiración humana?", "answer": "Oxígeno"}
    ],
    "historia": [
        {"question": "¿En qué año se descubrió América?", "answer": "1492"},
        {"question": "¿Quién fue el primer presidente de Estados Unidos?", "answer": "George Washington"},
        {"question": "¿Cuál fue la primera civilización en usar escritura?", "answer": "Los sumerios"}
    ],
    "geografia": [
        {"question": "¿Cuál es el río más largo del mundo?", "answer": "Río Amazonas"},
        {"question": "¿Cuál es el desierto más grande del mundo?", "answer": "Desierto del Sahara"},
        {"question": "¿Cuál es la montaña más alta del mundo?", "answer": "Monte Everest"}
    ],
    "literatura": [
        {"question": "¿Quién escribió 'Don Quijote de la Mancha'?", "answer": "Miguel de Cervantes"},
        {"question": "¿Cuál es la obra más famosa de William Shakespeare?", "answer": "Hamlet"},
        {"question": "¿Quién escribió 'Cien años de soledad'?", "answer": "Gabriel García Márquez"}
    ]
}


def save_data(data):
    """Guarda los datos en el archivo JSON."""
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_data():
    """Carga los datos desde el archivo JSON. Si no existe, lo crea con los datos iniciales."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        print(f"El archivo {FILE_NAME} no existe. Creando archivo con datos iniciales.")
        save_data(initial_data)
        return initial_data
