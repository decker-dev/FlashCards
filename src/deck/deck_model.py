def create_deck(decks, deck_name):
    """
    Crea un nuevo mazo.
    """
    decks[deck_name] = []
    return deck_name

def rename_deck(decks, old_name, new_name):
    """
    Renombra un mazo existente.
    """
    decks[new_name] = decks.pop(old_name)

def delete_deck(decks, deck_name):
    """
    Elimina un mazo existente.
    """
    del decks[deck_name]