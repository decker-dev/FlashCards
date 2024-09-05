from random import shuffle
from deck_manager import decks, list_decks


def study_mode(sequential=True):
    list_decks()
    deck_name = input("Seleccione el mazo para estudiar: ")
    if deck_name not in decks or not decks[deck_name]:
        print("El mazo no existe o está vacío.")
        return

    cards = decks[deck_name]
    if sequential:
        results = [study_card(card) for card in cards]
    else:
        shuffled_cards = cards[:]
        shuffle(shuffled_cards)
        results = [study_card(card) for card in shuffled_cards]

    show_results(results)

def study_card(card):
    print(f"Pregunta: {card['question']}")
    input("Presione Enter para ver la respuesta...")
    print(f"Respuesta: {card['answer']}")
    print("¿Cómo lo respondiste?")
    print("1. Perfecto")
    print("2. Bien")
    print("3. Mal")
    print("4. Nada")
    rating = input("Seleccione una opción: ").strip()

    if rating == "1":
        return "perfecto"
    elif rating == "2":
        return "bien"
    elif rating == "3":
        return "mal"
    elif rating == "4":
        return "nada"
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
