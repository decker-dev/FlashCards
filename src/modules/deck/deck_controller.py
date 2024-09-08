from src.modules.file_manager import save_decks, load_decks
from src.modules.deck.deck import create_deck

decks = load_decks()

def create_deck_controller(deck_name):
    if create_deck(decks, deck_name):
        save_decks(decks)
        return True
    else:
        return False

def list_decks_controller():
    return list(decks.keys())
