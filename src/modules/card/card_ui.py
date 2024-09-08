from src.modules.card.card_controller import add_card_to_deck, edit_card_in_deck, delete_card_from_deck, move_card_between_decks, search_cards_in_decks, list_cards
from src.modules.deck_manager import list_decks


def create_card_ui():
    question = input("Ingrese la pregunta: ")
    answer = input("Ingrese la respuesta: ")
    card = {"question": question, "answer": answer}
    add_card_to_deck("default", card)
    print("Tarjeta creada exitosamente.")

def edit_card_ui():
    list_cards_ui()
    index = int(input("Seleccione el número de la tarjeta a editar: "))
    if 0 <= index < len(list_cards("default")):
        question = input("Ingrese la nueva pregunta: ")
        answer = input("Ingrese la nueva respuesta: ")
        edit_card_in_deck("default", index, {"question": question, "answer": answer})
        print("Tarjeta editada exitosamente.")
    else:
        print("Índice no válido.")

def delete_card_ui():
    list_cards_ui()
    index = int(input("Seleccione el número de la tarjeta a eliminar: "))
    if 0 <= index < len(list_cards("default")):
        delete_card_from_deck("default", index)
        print("Tarjeta eliminada exitosamente.")
    else:
        print("Índice no válido.")

def list_cards_ui(deck_name="default"):
    cards = list_cards(deck_name)
    if cards:
        for i, card in enumerate(cards):
            print(f"{i}. Pregunta: {card['question']}, Respuesta: {card['answer']}")
    else:
        print("No hay tarjetas disponibles.")

def move_card_ui():
    list_cards_ui()
    index = int(input("Seleccione el número de la tarjeta a mover: "))
    if 0 <= index < len(list_cards("default")):
        list_decks()
        deck_name = input("Ingrese el nombre del mazo destino: ")
        if deck_name in list_cards():
            move_card_between_decks("default", deck_name, index)
            print("Tarjeta movida exitosamente.")
        else:
            print("El mazo no existe.")
    else:
        print("Índice no válido.")

def search_cards_ui():
    query = input("Ingrese parte del contenido a buscar (pregunta o respuesta): ")
    found_cards = search_cards_in_decks(query)
    if found_cards:
        print("Tarjetas encontradas:")
        for deck_name, i, card in found_cards:
            print(f"Mazo: {deck_name}, Tarjeta {i}: Pregunta: {card['question']}, Respuesta: {card['answer']}")
    else:
        print("No se encontraron tarjetas que coincidan con la búsqueda.")