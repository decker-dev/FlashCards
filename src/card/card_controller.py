from card.card_model import create_card_model, edit_card_model, delete_card_model
from card.card_view import get_card_input_view, select_card_view, display_cards_view
from deck.deck_controller import select_deck_controller
from utils.ui_utils import show_message, get_input

from graphics.graphics import print_bar


def add_card_controller(decks):
    """
    Añade una nueva tarjeta a un mazo seleccionado.

    Parameters:
        decks (dict): Diccionario de mazos existentes.

    Returns:
        None
    """
    # Permite al usuario seleccionar un mazo existente o crear uno nuevo
    #print_bar(is_upper=True)
    deck_name = select_deck_controller(decks, include_create=True)
    if not deck_name:
        return
    # Obtiene la pregunta y respuesta de la tarjeta
    question, answer = get_card_input_view()
    # Crea y añade la nueva tarjeta al mazo seleccionado
    create_card_model(decks, deck_name, question, answer)
    show_message("Tarjeta añadida exitosamente.")
    #print_bar(is_upper=False)

def edit_card_controller(decks):
    """
    Permite al usuario editar una tarjeta existente en un mazo.

    Parameters:
        decks (dict): Diccionario de mazos existentes.

    Returns:
        None
    """
    # Permite al usuario seleccionar un mazo
    #print_bar(is_upper=True)
    deck_name = select_deck_controller(decks)
    if not deck_name or not decks[deck_name]:
        show_message("No hay tarjetas para editar en este mazo.")
        return
    cards = decks[deck_name]
    # Muestra las tarjetas del mazo y permite seleccionar una para editar
    user_choice = select_card_view(cards, "Editar")
    if user_choice == '0':
        return
    # Convierte la opción seleccionada a índice (restando 1 porque los índices empiezan en 0)
    card_index = int(user_choice) - 1
    selected_card = cards[card_index]
    # Solicita la nueva pregunta y respuesta (opcionalmente)
    question = get_input(f"Pregunta Actual: {selected_card['question']} \nNueva Pregunta (dejar en blanco para conservar)")
    answer = get_input(f"Respuesta Actual: {selected_card['answer']} \nNueva Respuesta (dejar en blanco para conservar)")
    # Actualiza la tarjeta con la nueva información
    edit_card_model(selected_card, question, answer)
    show_message("Tarjeta editada correctamente.")
    #print_bar(is_upper=False)

def delete_card_controller(decks):
    """
    Permite al usuario eliminar una tarjeta existente en un mazo.

    Parameters:
        decks (dict): Diccionario de mazos existentes.

    Returns:
        None
    """
    # Permite al usuario seleccionar un mazo
    print_bar(is_upper=True)
    deck_name = select_deck_controller(decks)
    if not deck_name or not decks[deck_name]:
        show_message("No hay tarjetas para eliminar en este mazo.")
        return
    cards = decks[deck_name]
    # Muestra las tarjetas del mazo y permite seleccionar una para eliminar
    user_choice = select_card_view(cards, "Eliminar")
    if user_choice == '0':
        return
    # Convierte la opción seleccionada a índice
    card_index = int(user_choice) - 1
    # Elimina la tarjeta seleccionada
    delete_card_model(decks, deck_name, card_index)
    show_message("Tarjeta eliminada correctamente.")
    print_bar(is_upper=False)

def view_cards_controller(decks, user, card_history):
    """
    Muestra las tarjetas de un mazo y su estado de disponibilidad.

    Parameters:
        decks (dict): Diccionario de mazos existentes.
        user (str): Nombre del usuario actual.
        card_history (dict): Historial de revisión de tarjetas por usuario.

    Returns:
        None
    """
    # Permite al usuario seleccionar un mazo
    deck_name = select_deck_controller(decks)
    if not deck_name or not decks[deck_name]:
        show_message("No hay tarjetas en este mazo.")
        return
    cards = decks[deck_name]
    # Muestra las tarjetas y su estado
    display_cards_view(cards, deck_name, user, card_history)
