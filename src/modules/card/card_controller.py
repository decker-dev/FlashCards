import re
from src.modules.card.card import create_card
from src.modules.deck.deck import get_all_decks, save_all_decks

def add_card_to_deck(deck_name, question, answer):
    decks = get_all_decks()
    card = create_card(question, answer)
    if deck_name in decks:
        decks[deck_name].append(card)
        save_all_decks(decks)
    else:
        print(f"El deck '{deck_name}' no existe.")

def edit_card_in_deck(deck_name, index, question, answer):
    decks = get_all_decks()
    card = create_card(question, answer)
    if deck_name in decks and 0 <= index < len(decks[deck_name]):
        decks[deck_name][index] = card
        save_all_decks(decks)
    else:
        print(f"El deck '{deck_name}' no existe o el índice es inválido.")

def delete_card_from_deck(deck_name, index):
    decks = get_all_decks()
    if deck_name in decks and 0 <= index < len(decks[deck_name]):
        decks[deck_name].pop(index)
        save_all_decks(decks)
    else:
        print(f"El deck '{deck_name}' no existe o el índice es inválido.")

def move_card_between_decks(from_deck, to_deck, index):
    decks = get_all_decks()
    if from_deck in decks and to_deck in decks and 0 <= index < len(decks[from_deck]):
        card = decks[from_deck].pop(index)
        decks[to_deck].append(card)
        save_all_decks(decks)
    else:
        print(f"Uno de los decks no existe o el índice es inválido.")

def search_cards_in_decks(query):
    decks = get_all_decks()
    found_cards = []
    for deck_name in decks:
        cards = decks[deck_name]
        for i, card in enumerate(cards):
            if (re.search(query, card["question"], re.IGNORECASE) or
                re.search(query, card["answer"], re.IGNORECASE)):
                found_cards.append((deck_name, i, card))
    return found_cards

def list_cards(deck_name):
    decks = get_all_decks()
    return decks.get(deck_name, [])
