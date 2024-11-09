from datetime import datetime, timedelta

from src.utils.ui_utils import get_input, select_option, clear_screen, format_time


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

def display_cards_view(cards, deck_name, user, card_history):
    """
    Muestra las tarjetas de un mazo y su estado de disponibilidad.

    Parameters:
        cards (list): Lista de tarjetas.
        deck_name (str): Nombre del mazo.
        user (str): Nombre del usuario actual.
        card_history (dict): Historial de revisión de tarjetas por usuario.

    Returns:
        None
    """
    clear_screen()
    print(f"\n=== Tarjetas del Mazo '{deck_name}' ===\n")
    now = datetime.now()
    for index, card in enumerate(cards, 1):
        print(f"Tarjeta {index}:")
        print(f"Pregunta: {card['question']}")
        print(f"Respuesta: {card['answer']}")
        history_key = f"{user}_{card['id']}"
        if history_key in card_history:
            last_review = datetime.strptime(card_history[history_key]['last_review'], "%Y-%m-%d %H:%M:%S")
            interval_seconds = card_history[history_key]['interval']
            interval = timedelta(seconds=interval_seconds)
            next_review = last_review + interval
            if now < next_review:
                remaining_time = next_review - now
                print(f"Estado: Bloqueado - Disponible en: {format_time(remaining_time)}")
            else:
                print("Estado: Disponible para revisar")
        else:
            print("Estado: Nuevo - Aún no estudiado")
        print()
    input("\nPresione Enter para continuar...")