from random import shuffle

from modules import menu
from modules.deck_manager import list_decks, decks




def study_mode(is_flashcard_mode):
    list_decks()
    deck_name = input("Seleccione el mazo para estudiar: ")
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
        results.append(result)

    show_results(results)


def random_mode(cards):
    shuffled_cards = cards[:]
    shuffle(shuffled_cards)
    for card in shuffled_cards:
        print(f"\nPregunta: {card['question']}")
        input("Presione Enter para ver la respuesta...")
        print(f"Respuesta: {card['answer']}")
        input("Presione Enter para continuar...")


def study_card(card):
    print(f"\nPregunta: {card['question']}")
    input("Presione Enter para ver la respuesta...")
    print(f"Respuesta: {card['answer']}")
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
        menu.show_main_menu()
    else:
        print("Opción no válida, se tomará como 'Nada'.")
        return "nada"


def show_results(results):
    total = len(results)
    perfect = results.count("perfecto")
    good = results.count("bien")
    bad = results.count("mal")
    none = results.count("nada")

    print("\n--- Resultados del Estudio ---")
    print(f"Total de tarjetas: {total}")
    print(f"Perfecto: {perfect} ({(perfect / total) * 100:.2f}%)")
    print(f"Bien: {good} ({(good / total) * 100:.2f}%)")
    print(f"Mal: {bad} ({(bad / total) * 100:.2f}%)")
    print(f"Nada: {none} ({(none / total) * 100:.2f}%)")

    score = (perfect * 10 + good * 6 + bad * 4 + none * 1) / total
    print(f"\nPuntaje final: {score:.2f} / 10")
