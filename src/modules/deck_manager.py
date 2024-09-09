

from modules.file_manager import load_decks, save_decks


decks: dict[str, list[dict[str, str]]] = load_decks()

def create_deck():
    deck_name = input("\nIngrese el nombre del nuevo mazo: ")
    if deck_name not in decks:
        decks[deck_name] = []
        save_decks(decks)
        print(f"Mazo '{deck_name}' creado exitosamente.")
    else:
        print("El mazo ya existe.")

def list_decks():
    print("Mazos disponibles:")
    for deck_name in decks:
        print(f"- {deck_name}")
