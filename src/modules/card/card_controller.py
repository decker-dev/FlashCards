import re
from src.modules.file_manager import load_decks, save_decks

decks = load_decks()

def add_card_to_deck(deck_name, card):
    decks[deck_name].append(card)
    save_decks(decks)

def edit_card_in_deck(deck_name, index, card):
    decks[deck_name][index] = card
    save_decks(decks)

def delete_card_from_deck(deck_name, index):
    decks[deck_name].pop(index)
    save_decks(decks)

def move_card_between_decks(from_deck, to_deck, index):
    card = decks[from_deck].pop(index)
    decks[to_deck].append(card)
    save_decks(decks)

def search_cards_in_decks(query):
    found_cards = []
    for deck_name, cards in decks.items():
        for i, card in enumerate(cards):
            if re.search(query, card["question"], re.IGNORECASE) or re.search(query, card["answer"], re.IGNORECASE):
                found_cards.append((deck_name, i, card))
    return found_cards

def list_cards(deck_name="default"):
    return decks.get(deck_name, [])
