from modules.utils.file_manager import save_data, load_data
from modules.deck.deck import create_deck

def create_deck_controller(deck_name):
    return create_deck(deck_name)

def list_decks_controller():
    return list_decks()
