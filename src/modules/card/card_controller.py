import re
from src.modules.card.card import create_card
from src.modules.deck.deck import get_all_decks, save_all_decks


def add_card_to_deck(deck_name, question, answer):
    decks = get_all_decks()
    card = create_card(question, answer)
    decks[deck_name].append(card)
    save_all_decks(decks)


def edit_card_in_deck(deck_name, index, question, answer):
    decks = get_all_decks()
    card = create_card(question, answer)
    decks[deck_name][index] = card
    save_all_decks(decks)


def delete_card_from_deck(deck_name, index):
    decks = get_all_decks()
    decks[deck_name].pop(index)
    save_all_decks(decks)


def move_card_between_decks(from_deck, to_deck, index):
    decks = get_all_decks()
    card = decks[from_deck].pop(index)
    decks[to_deck].append(card)
    save_all_decks(decks)


def search_cards_in_decks(query):
    decks = get_all_decks()
    found_cards = []
    for deck_name in decks:
        cards = decks[deck_name]
        i = 0
        for card in cards:
            if (re.search(query, card["question"], re.IGNORECASE) or
                    re.search(query, card["answer"], re.IGNORECASE)):
                found_cards.append((deck_name, i, card))
            i += 1
    return found_cards


def list_cards(deck_name):
    decks = get_all_decks()
    return decks.get(deck_name, [])
