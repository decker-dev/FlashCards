from card_manager import create_card, edit_card, delete_card, list_cards
from study_mode import study_mode


def show_main_menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear Tarjeta")
        print("2. Editar Tarjeta")
        print("3. Eliminar Tarjeta")
        print("4. Listar Tarjetas")
        print("5. Modo Estudio")
        print("6. Salir")

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
            study_mode()
        elif option == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
