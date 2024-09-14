from src.utils.file_manager import save_data, load_data
from src.modules.deck.deck import create_deck

decks = load_data()


def create_deck_controller(deck_name):
    if create_deck(decks, deck_name):
        save_data(decks)
        return True
    else:
        return False


def list_decks_controller():
    return list(decks.keys())
