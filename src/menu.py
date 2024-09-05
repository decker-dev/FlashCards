from card_manager import create_card, edit_card, delete_card, list_cards, move_card, search_cards
from deck_manager import create_deck, list_decks
from study_mode import study_mode


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
    while True:
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
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def show_study_menu():
    while True:
        print("\n--- Empezar Estudio ---")
        print("1. Modo Secuencial")
        print("2. Modo Aleatorio")
        print("3. Volver al Menú Principal")

        option = input("Seleccione una opción: ")

        if option == "1":
            study_mode(sequential=True)
        elif option == "2":
            study_mode(sequential=False)
        elif option == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def show_card_management_menu():
    while True:
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
            create_card()
        elif option == "2":
            edit_card()
        elif option == "3":
            delete_card()
        elif option == "4":
            list_cards()
        elif option == "5":
            move_card()
        elif option == "6":
            search_cards()
        elif option == "7":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def show_deck_management_menu():
    while True:
        print("\n--- Gestionar Mazos ---")
        print("1. Crear Mazo")
        print("2. Listar Mazos")
        print("3. Volver al Menú Principal")

        option = input("Seleccione una opción: ")

        if option == "1":
            create_deck()
        elif option == "2":
            list_decks()
        elif option == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
