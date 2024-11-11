import json

def load_data(file_path="flashcards_data.json"):
    """
    Carga los datos desde un archivo JSON.

    Parameters:
        file_path (str): Ruta del archivo JSON a cargar.

    Returns:
        tuple: Contiene decks (dict), users (dict), card_history (dict), scores (dict).
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Obtiene los datos del archivo o valores predeterminados si no existen
            decks = data.get('decks', {'General': []})
            users = data.get('users', {})
            card_history = data.get('card_history', {})
            scores = data.get('scores', {})
            return decks, users, card_history, scores
    except FileNotFoundError:
        # Si el archivo no existe, retorna valores iniciales
        return {'General': []}, {}, {}, {}

def save_data(decks, users, card_history, scores, file_path="flashcards_data.json"):
    """
    Guarda los datos en un archivo JSON.

    Parameters:
        decks (dict): Diccionario con los mazos y sus tarjetas.
        users (dict): Diccionario con la información de los usuarios.
        card_history (dict): Historial de revisión de tarjetas por usuario.
        scores (dict): Puntajes y estadísticas de los usuarios.
        file_path (str): Ruta del archivo JSON donde se guardarán los datos.

    Returns:
        None
    """
    data = {
        'decks': decks,
        'users': users,
        'card_history': card_history,
        'scores': scores
    }
    with open(file_path, 'w', encoding='utf-8') as file:
        # Guarda los datos en formato JSON con una indentación para mayor legibilidad
        json.dump(data, file, indent=2)