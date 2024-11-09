from src.utils.ui_utils import select_option, get_input


def select_deck_view(decks, include_create=False):
    """
    Muestra el menú para seleccionar un mazo.

    Parameters:
        decks (dict): Diccionario de mazos existentes.
        include_create (bool): Si es True, incluye la opción de crear un nuevo mazo.

    Returns:
        str: Opción seleccionada por el usuario.
    """
    options = {str(index+1): deck_name for index, deck_name in enumerate(decks.keys())}
    if include_create:
        options[str(len(decks)+1)] = "Crear Nuevo Mazo"
    options['0'] = "Salir"
    user_choice = select_option("\n=== Selección de Mazo ===", options)
    return user_choice

def get_deck_name_view(prompt):
    """
    Solicita al usuario que ingrese el nombre del mazo.

    Parameters:
        prompt (str): Mensaje a mostrar al usuario.

    Returns:
        str: Nombre del mazo ingresado.
    """
    return get_input(prompt)