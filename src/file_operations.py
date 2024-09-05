def save_decks(decks):
    # Simulación de guardar en archivo, por ahora solo devuelve los mazos
    return decks

def load_decks():
    # Simulación de cargar desde archivo, por ahora devuelve un mazo por defecto con algunas tarjetas precargadas
    return {
        "default": [
            {"question": "¿Cuál es la capital de Francia?", "answer": "París"},
            {"question": "¿Cuál es el resultado de 2 + 2?", "answer": "4"},
            {"question": "¿Cuál es el idioma oficial de Brasil?", "answer": "Portugués"}
        ]
    }
