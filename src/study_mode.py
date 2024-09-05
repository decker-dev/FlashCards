from random import shuffle
from card_manager import cards

def study_mode(sequential=True):
    if not cards:
        print("No hay tarjetas disponibles para estudiar.")
        return

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
    rating = input("¿Cómo lo respondiste? (Perfecto/Bien/Mal/Nada): ").strip().lower()

    if rating in ["perfecto", "bien", "mal", "nada"]:
        return rating
    else:
        print("Respuesta no válida, se tomará como 'Nada'.")
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
