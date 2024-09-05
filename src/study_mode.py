from random import shuffle
from card_manager import cards

def study_mode(sequential=True):
    if not cards:
        print("No hay tarjetas disponibles para estudiar.")
        return

    if sequential:
        for card in cards:
            study_card(card)
    else:
        shuffled_cards = cards[:]
        shuffle(shuffled_cards)
        for card in shuffled_cards:
            study_card(card)

def study_card(card):
    print(f"Pregunta: {card['question']}")
    input("Presione Enter para ver la respuesta...")
    print(f"Respuesta: {card['answer']}")
    input("Presione Enter para continuar...")
