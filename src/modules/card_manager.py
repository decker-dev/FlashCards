import re

from modules.deck_manager import list_decks
from modules.file_manager import load_decks, save_decks

decks = load_decks()

def create_card():
    question = input("Ingrese la pregunta: ")
    answer = input("Ingrese la respuesta: ")
    card = {"question": question, "answer": answer}
    decks["default"].append(card)
    save_decks(decks)
    print("Tarjeta creada exitosamente.")

def edit_card():
    list_cards()
    index = int(input("Seleccione el número de la tarjeta a editar: "))
    if 0 <= index < len(decks["default"]):
        question = input("Ingrese la nueva pregunta: ")
        answer = input("Ingrese la nueva respuesta: ")
        decks["default"][index] = {"question": question, "answer": answer}
        save_decks(decks)
        print("Tarjeta editada exitosamente.")
    else:
        print("Índice no válido.")

def delete_card():
    list_cards()
    index = int(input("Seleccione el número de la tarjeta a eliminar: "))
    if 0 <= index < len(decks["default"]):
        decks["default"].pop(index)
        save_decks(decks)
        print("Tarjeta eliminada exitosamente.")
    else:
        print("Índice no válido.")

def list_cards(deck_name="default"):
    if decks[deck_name]:
        for i, card in enumerate(decks[deck_name]):
            print(f"{i}. Pregunta: {card['question']}, Respuesta: {card['answer']}")
    else:
        print("No hay tarjetas disponibles.")

def move_card():
    list_cards()
    index = int(input("Seleccione el número de la tarjeta a mover: "))
    if 0 <= index < len(decks["default"]):
        list_decks()
        deck_name = input("Ingrese el nombre del mazo destino: ")
        if deck_name in decks:
            card = decks["default"].pop(index)
            decks[deck_name].append(card)
            save_decks(decks)
            print("Tarjeta movida exitosamente.")
        else:
            print("El mazo no existe.")
    else:
        print("Índice no válido.")

def search_cards():
    query = input("Ingrese parte del contenido a buscar (pregunta o respuesta): ")
    found_cards = []

    for deck_name, cards in decks.items():
        for i in range(len(cards)):
            card = cards[i]
            if re.search(query, card["question"], re.IGNORECASE) or re.search(query, card["answer"], re.IGNORECASE):
                found_cards.append((deck_name, i, card))

    if found_cards:
        print("Tarjetas encontradas:")
        for deck_name, i, card in found_cards:
            print(f"Mazo: {deck_name}, Tarjeta {i}: Pregunta: {card['question']}, Respuesta: {card['answer']}")
    else:
        print("No se encontraron tarjetas que coincidan con la búsqueda.")
