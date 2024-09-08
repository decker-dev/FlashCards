from src.modules.file_manager import load_decks, save_decks

def add_card_to_deck(decks, deck_name, card):
    decks[deck_name].append(card)
    save_decks(decks)

def edit_card_in_deck(decks, deck_name, index, card):
    decks[deck_name][index] = card
    save_decks(decks)

def delete_card_from_deck(decks, deck_name, index):
    decks[deck_name].pop(index)
    save_decks(decks)