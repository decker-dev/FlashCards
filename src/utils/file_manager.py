data_store = {
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
    global data_store
    data_store = data


def load_data():
    global data_store
    return data_store
