from src.modules.card.card_controller import add_card_to_deck, list_cards, edit_card_in_deck, delete_card_from_deck, \
    move_card_between_decks, search_cards_in_decks
from src.modules.deck.deck_controller import list_decks_controller
from src.modules.deck.deck_ui import list_decks_ui


def create_card_ui():
    question = input("Ingrese la pregunta: ")
    answer = input("Ingrese la respuesta: ")
    add_card_to_deck("default", question, answer)
    print("Tarjeta creada exitosamente.")


def edit_card_ui():
    list_cards_ui()
    index = int(input("Seleccione el número de la tarjeta a editar: "))
    if 0 <= index < len(list_cards("default")):
        question = input("Ingrese la nueva pregunta: ")
        answer = input("Ingrese la nueva respuesta: ")
        edit_card_in_deck("default", index, question, answer)
        print("\nTarjeta editada exitosamente.")
    else:
        print("\nÍndice no válido.")


def delete_card_ui():
    list_cards_ui()
    index = int(input("\nSeleccione el número de la tarjeta a eliminar: "))
    if 0 <= index < len(list_cards("default")):
        delete_card_from_deck("default", index)
        print("Tarjeta eliminada exitosamente.")
    else:
        print("Índice no válido.")


def list_cards_ui():
    decks = list_decks_controller()
    for deck_name in decks:
        print(f"\nMazo: {deck_name}")
        cards = list_cards(deck_name)
        if cards:
            cards = sorted(cards, key = lambda card: card['question'])
            for card in cards:
                print(f"Pregunta: {card['question']}, Respuesta: {card['answer']}")
        else:
            print("\n No hay tarjetas disponibles.")


def move_card_ui():
    list_cards_ui()
    index = int(input("\nSeleccione el número de la tarjeta a mover: "))
    if 0 <= index < len(list_cards("default")):
        list_decks_ui()
        deck_name = input("Ingrese el nombre del mazo destino: ")
        if deck_name in list_decks_controller():
            move_card_between_decks("default", deck_name, index)
            print("Tarjeta movida exitosamente.")
        else:
            print("\nEl mazo no existe.")
    else:
        print("\nÍndice no válido.")


def search_cards_ui():
    query = input("Ingrese parte del contenido a buscar (pregunta o respuesta): ")
    found_cards = search_cards_in_decks(query)
    if found_cards:
        print("Tarjetas encontradas:")
        for deck_name, i, card in found_cards:
            print(f"Mazo: {deck_name}, Tarjeta {i}: Pregunta: {card['question']}, Respuesta: {card['answer']}")
    else:
        print("No se encontraron tarjetas que coincidan con la búsqueda.")
