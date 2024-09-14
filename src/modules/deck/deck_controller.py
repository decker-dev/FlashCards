from src.modules.deck.deck import create_deck, list_decks

def create_deck_controller(deck_name):
    return create_deck(deck_name)

def list_decks_controller():
    return list_decks()
