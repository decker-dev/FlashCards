import random

from src.deck.deck_controller import select_deck
from src.practice.practice_model import calculate_available_cards, update_card_history
from src.practice.practice_view import get_rating, show_results
from src.stats.stats_model import update_score
from src.utils.ui_utils import show_message, clear_screen


def practice(decks, user, card_history, scores):
    """
    Permite al usuario practicar las tarjetas disponibles en un mazo.
    """
    deck_name = select_deck(decks)
    if not deck_name:
        return
    cards = decks[deck_name]
    if not cards:
        show_message(f"No hay tarjetas en el mazo '{deck_name}'.")
        return
    available_cards = calculate_available_cards(cards, card_history, user)
    if not available_cards:
        show_message("No hay tarjetas disponibles para revisar en este momento.")
        return
    random.shuffle(available_cards)
    results = {'Perfecto': 0, 'Bien': 0, 'Mal': 0, 'Terriblemente_Nada': 0}
    for index, card in enumerate(available_cards, 1):
        clear_screen()
        print(f"\n=== Mazo: {deck_name} - Pregunta {index}/{len(available_cards)} ===")
        print(f"\nPregunta: {card['question']}")
        input("\nPresione Enter para ver la respuesta...")
        print(f"\nRespuesta: {card['answer']}")
        rating, interval = get_rating()
        results[rating] += 1
        update_card_history(card_history, user, card['id'], rating, interval)
    update_score(scores, user, results)
    show_results(results, len(available_cards))