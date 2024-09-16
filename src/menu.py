from modules.card.card_ui import create_card_ui, edit_card_ui, delete_card_ui, list_cards_ui, move_card_ui, \
    search_cards_ui
from modules.deck.deck_ui import create_deck_ui, list_decks_ui
from modules.graphics import print_boxed_code
from src.modules.study_mode.study_mode_ui import start_study_mode


def show_welcome_menu():

    flashcards_ascii = """
███████ ██       █████  ███████ ██   ██  ██████  █████  ██████  ██████  ███████ 
██      ██      ██   ██ ██      ██   ██ ██      ██   ██ ██   ██ ██   ██ ██      
█████   ██      ███████ ███████ ███████ ██      ███████ ██████  ██   ██ ███████ 
██      ██      ██   ██      ██ ██   ██ ██      ██   ██ ██   ██ ██   ██      ██ 
██      ███████ ██   ██ ███████ ██   ██  ██████ ██   ██ ██   ██ ██████  ███████ 
"""
    print_boxed_code(flashcards_ascii)
    input("Para comenzar, presione Enter...")
    show_main_menu()


def show_main_menu():
    menu_active = True
    while menu_active:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Empezar Estudio")
        print("2. Gestionar Tarjetas")
        print("3. Gestionar Mazos")
        print("S. Salir")

        option = input("\nSeleccione una opción: ")

        if option == "1":
            show_study_menu()
        elif option == "2":
            show_card_management_menu()
        elif option == "3":
            show_deck_management_menu()
        elif option == "S" or option =="s":
            print("\nSaliendo...\n")
            menu_active = False
        else:
            print("Opción no válida. Intente de nuevo.")


def show_study_menu():
    menu_active = True
    while menu_active:
        print("\n--- EMPEZAR ESTUDIO ---")
        print("1. Modo Flashcards")
        print("2. Modo Aleatorio")
        print("3. Volver al Menú Principal")
        print("S. Salir")

        option = input("\nSeleccione una opción: ")

        if option == "1":
            start_study_mode(True)
        elif option == "2":
            start_study_mode(False)
        elif option == "3":
            menu_active = False
        elif option == "s" or option == "S":
            exit("\nSaliendo...\n")

        else:
            print("Opción no válida. Intente de nuevo.")


def show_card_management_menu():
    menu_active = True
    while menu_active:
        print("\n--- GESTIONAR TARJETAS ---")
        print("1. Crear Tarjeta")
        print("2. Editar Tarjeta")
        print("3. Eliminar Tarjeta")
        print("4. Listar Tarjetas")
        print("5. Mover Tarjeta a Mazo")
        print("6. Buscar Tarjetas")
        print("7. Volver al Menú Principal")
        print("S. Salir")


        option = input("\nSeleccione una opción: ")

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
        elif option == "s" or option == "S":
            exit("\nSaliendo...\n")
        else:
            print("Opción no válida. Intente de nuevo.")


def show_deck_management_menu():
    menu_active = True
    while menu_active:
        print("\n--- GESTIONAR MAZOS ---")
        print("1. Crear Mazo")
        print("2. Listar Mazos")
        print("3. Volver al Menú Principal")
        print("S. Salir")

        option = input("\nSeleccione una opción: ")

        if option == "1":
            create_deck_ui()
        elif option == "2":
            list_decks_ui()
        elif option == "3":
            menu_active = False
        elif option == "s" or option == "S":
            exit("\nSaliendo...\n")
        else:
            print("Opción no válida. Intente de nuevo.")
