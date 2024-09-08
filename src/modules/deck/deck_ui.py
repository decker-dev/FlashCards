from src.modules.deck.deck_controller import create_deck_controller, list_decks_controller


def create_deck_ui():
    deck_name = input("Ingrese el nombre del nuevo mazo: ")
    if create_deck_controller(deck_name):
        print(f"Mazo '{deck_name}' creado exitosamente.")
    else:
        print("El mazo ya existe.")


def list_decks_ui():
    print("Mazos disponibles:")
    for deck_name in list_decks_controller():
        print(f"- {deck_name}")
