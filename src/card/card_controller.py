from src.card.card_model import create_card
from src.card.card_view import get_card_input, select_card_view, display_cards
from src.deck.deck_controller import select_deck
from src.utils.ui_utils import show_message, get_input


def add_card(decks):
    """
    Añade una nueva tarjeta a un mazo seleccionado.
    """
    deck_name = select_deck(decks, include_create=True)
    if not deck_name:
        return
    question, answer = get_card_input()
    create_card(decks, deck_name, question, answer)
    show_message("Tarjeta añadida exitosamente.")

def edit_card(decks):
    """
    Permite al usuario editar una tarjeta existente en un mazo.
    """
    deck_name = select_deck(decks)
    if not deck_name or not decks[deck_name]:
        show_message("No hay tarjetas para editar en este mazo.")
        return
    cards = decks[deck_name]
    user_choice = select_card_view(cards, "Editar")
    if user_choice == '0':
        return
    card_index = int(user_choice) - 1
    selected_card = cards[card_index]
    question = get_input(f"Pregunta Actual: {selected_card['question']} \nNueva Pregunta (dejar en blanco para conservar)")
    answer = get_input(f"Respuesta Actual: {selected_card['answer']} \nNueva Respuesta (dejar en blanco para conservar)")
    edit_card(selected_card, question, answer)
    show_message("Tarjeta editada correctamente.")

def delete_card(decks):
    """
    Permite al usuario eliminar una tarjeta existente en un mazo.
    """
    deck_name = select_deck(decks)
    if not deck_name or not decks[deck_name]:
        show_message("No hay tarjetas para eliminar en este mazo.")
        return
    cards = decks[deck_name]
    user_choice = select_card_view(cards, "Eliminar")
    if user_choice == '0':
        return
    card_index = int(user_choice) - 1
    delete_card(decks, deck_name, card_index)
    show_message("Tarjeta eliminada correctamente.")

def view_cards(decks, user, card_history):
    """
    Muestra las tarjetas de un mazo y su estado de disponibilidad.
    """
    deck_name = select_deck(decks)
    if not deck_name or not decks[deck_name]:
        show_message("No hay tarjetas en este mazo.")
        return
    cards = decks[deck_name]
    display_cards(cards, deck_name)