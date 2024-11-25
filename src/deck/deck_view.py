from utils.ui_utils import select_option, get_input

from src.graphics.graphics import print_bar


def select_deck_view(decks, include_create=False):
    """
    Muestra el menú para seleccionar un mazo.

    Parameters:
        decks (dict): Diccionario de mazos existentes.
        include_create (bool): Si es True, incluye la opción de crear un nuevo mazo.

    Returns:
        str: Opción seleccionada por el usuario.
    """
    # Creamos un diccionario 'options' para el menú de selección de mazo
    # 'enumerate(decks.keys())' crea pares de índice y nombre de mazo
    # Por ejemplo, si decks.keys() es ['Matemáticas', 'Historia'], enumerate(decks.keys()) genera (0, 'Matemáticas'), (1, 'Historia')
    options = {str(index + 1): deck_name for index, deck_name in enumerate(decks.keys())}
    if include_create:
        # Añadimos una opción adicional para crear un nuevo mazo
        options[str(len(decks) + 1)] = "Crear Nuevo Mazo"
    # Añadimos la opción de 'Salir' con la clave '0'
    options['0'] = "Salir"
    # Mostramos el menú de opciones y obtenemos la elección del usuario
    user_choice = select_option("\n === 🕹️ 🎯 Selección de Mazo 🎯 🕹️ ===", options)
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