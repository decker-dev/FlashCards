def create_deck(decks, deck_name):
    if deck_name not in decks:
        decks[deck_name] = []
        return True
    else:
        return False
