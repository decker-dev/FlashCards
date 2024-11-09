import json

def load_data(file_path="flashcards_data.json"):
    """
    Carga los datos desde un archivo JSON.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            decks = data.get('decks', {'General': []})
            users = data.get('users', {})
            card_history = data.get('card_history', {})
            scores = data.get('scores', {})
            return decks, users, card_history, scores
    except FileNotFoundError:
        return {'General': []}, {}, {}, {}

def save_data(decks, users, card_history, scores, file_path="flashcards_data.json"):
    """
    Guarda los datos en un archivo JSON.
    """
    data = {
        'decks': decks,
        'users': users,
        'card_history': card_history,
        'scores': scores
    }
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)