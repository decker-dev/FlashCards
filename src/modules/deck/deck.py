from src.utils.file_manager import save_data, load_data

def get_all_decks():
    return load_data()

def create_deck(deck_name):
    decks = get_all_decks()
    if deck_name not in decks:
        decks[deck_name] = []
        save_data(decks)
        return True
    else:
        return False

def list_decks():
    decks = get_all_decks()
    return list(decks.keys())

