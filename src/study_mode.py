from modules.deck.deck_ui import list_decks_ui
from modules.graphics import print_boxed_code
from modules.utils.file_manager import load_data
from modules.utils.list import shuffle_copy

decks = load_data()


def study_mode(is_flashcard_mode):
    list_decks_ui()
    deck_name = input("\nSeleccione el mazo para estudiar: ")
    if deck_name not in decks or not decks[deck_name]:
        print("El mazo no existe o está vacío.")
        return

    cards = decks[deck_name]

    if is_flashcard_mode:
        flashcard_mode(cards)
    else:
        random_mode(cards)


def flashcard_mode(cards):
    results = []
    for card in cards:
        result = study_card(card)
        if result == "abandonar":
            return
        results.append(result)

    show_results(results)


def random_mode(cards):
    shuffled_cards = shuffle_copy(cards)
    for card in shuffled_cards:
        print(f"\nPregunta: {card['question']}")
        input("Presione Enter para ver la respuesta...")
        print(f"\nRespuesta: {card['answer']}")
        input("Presione Enter para continuar...")


def study_card(card):
    print(f"\nPregunta: {card['question']}")
    input("Presione Enter para ver la respuesta...")
    print(f"'\nRespuesta: {card['answer']}")
    print("¿Cómo lo respondiste?")
    print("1. Perfecto")
    print("2. Bien")
    print("3. Mal")
    print("4. Nada")
    print("5. Abandonar partida")
    rating = input("Seleccione una opción: ").strip()

    if rating == "1":
        return "perfecto"
    elif rating == "2":
        return "bien"
    elif rating == "3":
        return "mal"
    elif rating == "4":
        return "nada"
    elif rating == "5":
        return "abandonar"
    else:
        print("Opción no válida, se tomará como 'Nada'.")
        return "nada"


def show_results(results):
    total = len(results)
    perfect = results.count("perfecto")
    good = results.count("bien")
    bad = results.count("mal")
    none = results.count("nada")

    print("\n--- RESULTADOS DEL ESTUDIO ---")
    print(f"Total de tarjetas: {total}")
    print(f"Perfecto: {perfect} ({(perfect / total) * 100:.2f}%)")
    print(f"Bien: {good} ({(good / total) * 100:.2f}%)")
    print(f"Mal: {bad} ({(bad / total) * 100:.2f}%)")
    print(f"Nada: {none} ({(none / total) * 100:.2f}%)")

    score = (perfect * 10 + good * 6 + bad * 4 + none * 1) / total
    print_boxed_code(f"Puntaje final: {score:.2f} / 10")