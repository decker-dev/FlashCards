from deck.deck_model import create_deck_model, rename_deck_model, delete_deck_model
from deck.deck_view import select_deck_view, get_deck_name_view
from utils.ui_utils import show_message, get_input


def select_deck_controller(decks, include_create=False):
    """
    Permite al usuario seleccionar un mazo existente o crear uno nuevo.

    Parameters:
        decks (dict): Diccionario de mazos existentes.
        include_create (bool): Si es True, incluye la opción de crear un nuevo mazo.

    Returns:
        str or None: Nombre del mazo seleccionado o None si se cancela.
    """
    user_choice = select_deck_view(decks, include_create)
    if user_choice == '0':
        return None
    elif include_create and user_choice == str(len(decks) + 1):
        # El usuario eligió crear un nuevo mazo
        return handle_create_deck_controller(decks)
    else:
        # Reconstruimos el diccionario 'options' para mapear las opciones a los nombres de mazos
        options = {str(index + 1): deck_name for index, deck_name in enumerate(decks.keys())}
        # Retornamos el nombre del mazo seleccionado
        return options[user_choice]

def handle_create_deck_controller(decks):
    """
    Maneja la creación de un nuevo mazo.

    Parameters:
        decks (dict): Diccionario de mazos existentes.

    Returns:
        str: Nombre del nuevo mazo creado.
    """
    deck_name = get_deck_name_view("\nIngrese el Nombre del Mazo")
    while not deck_name or deck_name in decks:
        # Verifica que el nombre no esté vacío y que no exista ya en el diccionario 'decks'
        show_message("Nombre inválido o ya existente.")
        deck_name = get_deck_name_view("\nIngrese el Nombre del Mazo")
    create_deck_model(decks, deck_name)
    show_message("Mazo creado exitosamente.")
    return deck_name

def create_deck_controller(decks):
    """
    Crea un nuevo mazo.

    Parameters:
        decks (dict): Diccionario de mazos existentes.

    Returns:
        str: Nombre del nuevo mazo creado.
    """
    deck_name = get_deck_name_view("\nIngrese el Nombre del Mazo")
    while not deck_name or deck_name in decks:
        show_message("Nombre inválido o ya existente.")
        deck_name = get_deck_name_view("\nIngrese el Nombre del Mazo")
    create_deck_model(decks, deck_name)
    show_message("Mazo creado exitosamente.")
    return deck_name

def edit_deck_controller(decks):
    """
    Permite al usuario renombrar un mazo existente.

    Parameters:
        decks (dict): Diccionario de mazos existentes.

    Returns:
        None
    """
    deck_name = select_deck_controller(decks)
    if not deck_name:
        return
    new_deck_name = get_deck_name_view(f"\nIngrese el nuevo nombre para el mazo '{deck_name}' (dejar en blanco para cancelar)")
    if new_deck_name and new_deck_name not in decks:
        rename_deck_model(decks, deck_name, new_deck_name)
        show_message("Mazo renombrado correctamente.")
    else:
        show_message("Nombre inválido o ya existente.")

def delete_deck_controller(decks):
    """
    Permite al usuario eliminar un mazo existente.

    Parameters:
        decks (dict): Diccionario de mazos existentes.

    Returns:
        None
    """
    deck_name = select_deck_controller(decks)
    if not deck_name:
        return
    confirmation = get_input(f"¿Está seguro que desea eliminar el mazo '{deck_name}' y todas sus tarjetas? (s/n)").lower()
    if confirmation == 's':
        delete_deck_model(decks, deck_name)
        show_message("Mazo eliminado correctamente.")
    else:
        show_message("Eliminación cancelada.")