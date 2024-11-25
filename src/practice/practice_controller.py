import random

from deck.deck_controller import select_deck_controller
from practice.practice_model import calculate_available_cards_model, update_card_history_model
from practice.practice_view import get_rating_view, show_results_view
from stats.stats_model import update_score_model
from utils.ui_utils import show_message, clear_screen

from graphics.graphics import print_bar


def practice_controller(decks, user, card_history, scores):
    """
    Permite al usuario practicar las tarjetas disponibles en un mazo.

    Parameters:
        decks (dict): Diccionario de mazos existentes.
        user (str): Nombre del usuario actual.
        card_history (dict): Historial de revisión de tarjetas por usuario.
        scores (dict): Puntajes y estadísticas de los usuarios.

    Returns:
        None
    """
    # Permite al usuario seleccionar un mazo
    deck_name = select_deck_controller(decks)
    if not deck_name:
        return
    cards = decks[deck_name]
    if not cards:
        show_message(f"No hay tarjetas en el mazo '{deck_name}'.")
        return
    # Calcula las tarjetas disponibles para practicar
    available_cards = calculate_available_cards_model(cards, card_history, user)
    if not available_cards:
        show_message("No hay tarjetas disponibles para revisar en este momento.")
        return
    # Mezcla las tarjetas disponibles aleatoriamente
    random.shuffle(available_cards)
    results = {'Perfecto': 0, 'Bien': 0, 'Mal': 0, 'Nada': 0}
    for index, card in enumerate(available_cards, 1):
        clear_screen()
        print_bar(is_upper=True)
        print(f"\t=== 🧩 📚 Mazo: {deck_name} - Pregunta {index}/{len(available_cards)}  📚 🧩 ===")
        print(f"\n \t Pregunta: {card['question']}")
        input("\n \t Presione Enter para ver la respuesta...")
        print(f"\n \tRespuesta: {card['answer']}")
        input("\n \t Presione Enter para calificar la tarjeta...")
        # Obtiene el rating y el intervalo para la tarjeta actual
        rating, interval = get_rating_view()
        # Actualiza el conteo de resultados según el rating
        results[rating] += 1
        # Actualiza el historial de la tarjeta
        update_card_history_model(card_history, user, card['id'], rating, interval)
    # Actualiza las estadísticas del usuario
    update_score_model(scores, user, results)
    # Muestra los resultados de la práctica
    show_results_view(results, len(available_cards))

def random_practice_controller(decks):
    """
    Permite al usuario practicar con tarjetas aleatorias del mazo seleccionado.

    Parameters:
        decks (dict): Diccionario de mazos existentes.

    Returns:
        None
    """
    # Permite al usuario seleccionar un mazo
    deck_name = select_deck_controller(decks)
    if not deck_name:
        return
    cards = decks[deck_name]
    if not cards:
        show_message(f"No hay tarjetas en el mazo '{deck_name}'.")
        return
    # Mezcla las tarjetas del mazo aleatoriamente
    random.shuffle(cards)
    results = {'Perfecto': 0, 'Bien': 0, 'Mal': 0, 'Nada': 0}
    for index, card in enumerate(cards, 1):
        clear_screen()
        print_bar(is_upper=True)
        print(f"\t 📚 🧩 Mazo: {deck_name} - Pregunta {index}/{len(cards)} 🧩 📚 ")
        print(f"\n \tPregunta: {card['question']}")
        input("\n \tPresione Enter para ver la respuesta...")
        print(f"\n \tRespuesta: {card['answer']}")
        input("\n \tPresione Enter para calificar la tarjeta...")
        rating, interval = get_rating_view()
        results[rating] += 1

    show_results_view(results, len(cards), is_random=True)