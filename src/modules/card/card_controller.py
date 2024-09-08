from src.modules.file_manager import save_data, load_data
from src.modules.card.card import create_card

decks = load_data()

def add_card_to_deck(deck_name, question, answer):
    card = create_card(question, answer)
    decks[deck_name].append(card)
    save_data(decks)

def edit_card_in_deck(deck_name, index, question, answer):
    card = create_card(question, answer)
    decks[deck_name][index] = card
    save_data(decks)

def delete_card_from_deck(deck_name, index):
    decks[deck_name].pop(index)
    save_data(decks)

def move_card_between_decks(from_deck, to_deck, index):
    card = decks[from_deck].pop(index)
    decks[to_deck].append(card)
    save_data(decks)

def search_cards_in_decks(query):
    found_cards = []
    for deck_name, cards in decks.items():
        for i, card in enumerate(cards):
            if query.lower() in card["question"].lower() or query.lower() in card["answer"].lower():
                found_cards.append((deck_name, i, card))
    return found_cards

def list_cards(deck_name):
    return decks.get(deck_name, [])
