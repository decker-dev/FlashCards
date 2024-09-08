from src.modules.card.card_ui import create_card_ui, edit_card_ui, delete_card_ui, list_cards_ui, move_card_ui, \
    search_cards_ui
from src.modules.deck.deck_ui import create_deck_ui, list_decks_ui
from src.study_mode import study_mode


def show_welcome_menu():
    flashcards_ascii = """
███████ ██       █████  ███████ ██   ██  ██████  █████  ██████  ██████  ███████ 
██      ██      ██   ██ ██      ██   ██ ██      ██   ██ ██   ██ ██   ██ ██      
█████   ██      ███████ ███████ ███████ ██      ███████ ██████  ██   ██ ███████ 
██      ██      ██   ██      ██ ██   ██ ██      ██   ██ ██   ██ ██   ██      ██ 
██      ███████ ██   ██ ███████ ██   ██  ██████ ██   ██ ██   ██ ██████  ███████ 
"""
    print(flashcards_ascii)
    input("Para comenzar, presione Enter...")
    show_main_menu()


def show_main_menu():
    menu_active = True
    while menu_active:
        print("\n--- Menú Principal ---")
        print("1. Empezar Estudio")
        print("2. Gestionar Tarjetas")
        print("3. Gestionar Mazos")
        print("4. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            show_study_menu()
        elif option == "2":
            show_card_management_menu()
        elif option == "3":
            show_deck_management_menu()
        elif option == "4":
            print("Saliendo...")
            menu_active = False
        else:
            print("Opción no válida. Intente de nuevo.")


def show_study_menu():
    menu_active = True
    while menu_active:
        print("\n--- Empezar Estudio ---")
        print("1. Modo Flashcards")
        print("2. Modo Aleatorio")
        print("3. Volver al Menú Principal")

        option = input("Seleccione una opción: ")

        if option == "1":
            study_mode(True)
        elif option == "2":
            study_mode(False)
        elif option == "3":
            menu_active = False
        else:
            print("Opción no válida. Intente de nuevo.")


def show_card_management_menu():
    menu_active = True
    while menu_active:
        print("\n--- Gestionar Tarjetas ---")
        print("1. Crear Tarjeta")
        print("2. Editar Tarjeta")
        print("3. Eliminar Tarjeta")
        print("4. Listar Tarjetas")
        print("5. Mover Tarjeta a Mazo")
        print("6. Buscar Tarjetas")
        print("7. Volver al Menú Principal")

        option = input("Seleccione una opción: ")

        if option == "1":
            create_card_ui()
        elif option == "2":
            edit_card_ui()
        elif option == "3":
            delete_card_ui()
        elif option == "4":
            list_cards_ui()
        elif option == "5":
            move_card_ui()
        elif option == "6":
            search_cards_ui()
        elif option == "7":
            menu_active = False
        else:
            print("Opción no válida. Intente de nuevo.")


def show_deck_management_menu():
    menu_active = True
    while menu_active:
        print("\n--- Gestionar Mazos ---")
        print("1. Crear Mazo")
        print("2. Listar Mazos")
        print("3. Volver al Menú Principal")

        option = input("Seleccione una opción: ")

        if option == "1":
            create_deck_ui()
        elif option == "2":
            list_decks_ui()
        elif option == "3":
            menu_active = False
        else:
            print("Opción no válida. Intente de nuevo.")
