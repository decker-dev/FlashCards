from src.modules.deck.deck_ui import list_decks_ui
from src.modules.study_mode.study_mode_controller import study_mode, show_results


def start_study_mode(is_flashcard_mode):
    list_decks_ui()
    deck_name = input("Seleccione el mazo para estudiar: ")

    results, error = study_mode(deck_name, is_flashcard_mode)

    if error:
        print(error)
        return

    if is_flashcard_mode:
        show_results(results)
    else:
        for card in results:
            print(f"\nPregunta: {card['question']}")
            input("Presione Enter para ver la respuesta...")
            print(f"Respuesta: {card['answer']}")
            input("Presione Enter para continuar...")
