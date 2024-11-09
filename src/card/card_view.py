from src.utils.ui_utils import get_input, select_option, clear_screen


def get_card_input_view():
    """
    Solicita al usuario que ingrese la pregunta y respuesta de la tarjeta.

    Parameters:
        None

    Returns:
        tuple: (question, answer)
    """
    question = get_input("\nIngresar Pregunta")
    answer = get_input("Ingresar Respuesta")
    return question, answer

def select_card_view(cards, action):
    """
    Muestra el menú para seleccionar una tarjeta.

    Parameters:
        cards (list): Lista de tarjetas.
        action (str): Acción a realizar (Editar/Eliminar).

    Returns:
        str: Opción seleccionada por el usuario.
    """
    options = {str(index+1): card['question'] for index, card in enumerate(cards)}
    options['0'] = "Cancelar"
    user_choice = select_option(f"\n=== Seleccione una Tarjeta para {action} ===", options)
    return user_choice

def display_cards_view(cards, deck_name):
    """
    Muestra las tarjetas de un mazo.

    Parameters:
        cards (list): Lista de tarjetas.
        deck_name (str): Nombre del mazo.

    Returns:
        None
    """
    clear_screen()
    print(f"\n=== Tarjetas del Mazo '{deck_name}' ===\n")
    for index, card in enumerate(cards, 1):
        print(f"Tarjeta {index}:")
        print(f"Pregunta: {card['question']}")
        print(f"Respuesta: {card['answer']}\n")
    input("\nPresione Enter para continuar...")