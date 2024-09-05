from random import shuffle
from card_manager import cards


def study_mode():
    if not cards:
        print("No hay tarjetas disponibles para estudiar.")
        return

    print("\n--- Modo Estudio ---")
    print("1. Secuencial")
    print("2. Aleatorio")

    option = input("Seleccione el modo de estudio: ")

    if option == "1":
        for card in cards:
            study_card(card)
    elif option == "2":
        shuffled_cards = cards[:]
        shuffle(shuffled_cards)
        for card in shuffled_cards:
            study_card(card)
    else:
        print("Opción no válida.")


def study_card(card):
    print(f"Pregunta: {card['question']}")
    input("Presione Enter para ver la respuesta...")
    print(f"Respuesta: {card['answer']}")
    input("Presione Enter para continuar...")
