def create_deck_model(decks, deck_name):
    """
    Crea un nuevo mazo.

    Parameters:
        decks (dict): Diccionario de mazos existentes.
        deck_name (str): Nombre del mazo a crear.

    Returns:
        str: Nombre del mazo creado.
    """
    # Añade una nueva entrada al diccionario 'decks' con el nombre del mazo y una lista vacía de tarjetas
    decks[deck_name] = []
    return deck_name

def rename_deck_model(decks, old_name, new_name):
    """
    Renombra un mazo existente.

    Parameters:
        decks (dict): Diccionario de mazos existentes.
        old_name (str): Nombre actual del mazo.
        new_name (str): Nuevo nombre para el mazo.

    Returns:
        None
    """
    # Cambia la clave del mazo en el diccionario 'decks' del nombre antiguo al nuevo
    decks[new_name] = decks.pop(old_name)

def delete_deck_model(decks, deck_name):
    """
    Elimina un mazo existente.

    Parameters:
        decks (dict): Diccionario de mazos existentes.
        deck_name (str): Nombre del mazo a eliminar.

    Returns:
        None
    """
    # Elimina la entrada correspondiente al mazo en el diccionario 'decks'
    del decks[deck_name]