from src.card.card_controller import add_card_controller, view_cards_controller, edit_card_controller, \
    delete_card_controller
from src.deck.deck_controller import create_deck_controller, edit_deck_controller, delete_deck_controller
from src.practice.practice_controller import practice_controller
from src.stats.stats_controller import show_ranking_controller, show_user_stats_controller
from src.user.user_controller import select_user_controller
from src.utils.data_manager import load_data, save_data
from src.utils.ui_utils import select_option, show_message


def main_menu_controller():
    """
    Maneja el flujo del programa y el menú principal.

    Parameters:
        None

    Returns:
        None
    """


    # Diseño ASCII del título "Flash Cards"
    flashcards_ascii = """
    ┌─────────────────────────────────────────────────────────────────────────────────────┐
    │                                                                                     │
    │                                                                                     │                                                                   
    │   ███████ ██       █████  ███████ ██   ██  ██████  █████  ██████  ██████  ███████   │ 
    │   ██      ██      ██   ██ ██      ██   ██ ██      ██   ██ ██   ██ ██   ██ ██        │
    │   █████   ██      ███████ ███████ ███████ ██      ███████ ██████  ██   ██ ███████   │
    │   ██      ██      ██   ██      ██ ██   ██ ██      ██   ██ ██   ██ ██   ██      ██   │
    │   ██      ███████ ██   ██ ███████ ██   ██  ██████ ██   ██ ██   ██ ██████  ███████   │
    │                                                                                     │
    │                                                                                     │
    │                               URBANO + ALE SAMANIEGO                                │
    │                                                                                     │
    │                   UADE 2C-2024 - Programación 1 - TPO GRUPO 12                      │
    │                                                                                     │
    │                                                                                     │
    └─────────────────────────────────────────────────────────────────────────────────────┘
    """
    # Imprime el título al inicio
    print(flashcards_ascii)
    input("Presiona Enter para comenzar...")
    def main_menu_controller():
        """
        Maneja el flujo del programa y el menú principal.

        Parameters:
            None

        Returns:
            None
        """

        # ╔══════════════════════════════════════════════════════════════════╗
        # ║ Carga los datos almacenados desde un archivo JSON               ║
        # ║                                                                 ║
        # ║ decks, users, card_history, scores = load_data()                ║
        # ║                                                                 ║
        # ║ Permite al usuario seleccionar o crear un usuario               ║
        # ║                                                                 ║
        # ║ current_user = select_user_controller(users)                    ║
        # ║                                                                 ║
        # ║ exit_program = False                                            ║
        # ╚══════════════════════════════════════════════════════════════════╝


    # Carga los datos almacenados desde un archivo JSON
    decks, users, card_history, scores = load_data()
    # Permite al usuario seleccionar o crear un usuario
    current_user = select_user_controller(users)
    exit_program = False
    while not exit_program:
        # Define las opciones del menú principal en un diccionario
        options = {
            '1': "📝   Añadir Tarjeta",
            '2': "🎯   Practicar",
            '3': "📊   Ver Tarjetas y Estado",
            '4': "📚   Crear Nuevo Mazo",
            '5': "✏️Editar Mazo",
            '6': "🗑️ Eliminar Mazo",
            '7': "👤 Cambiar de Usuario",
            '8': "✏️Editar Tarjeta",
            '9': "🗑️ Eliminar Tarjeta",
            '10': "🏆 Ver Ranking Global",
            '11': "📈 Ver mis Estadísticas",
            '0' : "🚪  Salir"
        }
        # Muestra el menú y obtiene la opción seleccionada por el usuario
        user_choice = select_option(f"\n=== 🎮 Juego de Flashcards - Usuario: {current_user} ===", options)
        # Ejecuta acciones basadas en la opción seleccionada
        if user_choice == '1':
            add_card_controller(decks)
        elif user_choice == '2':
            practice_controller(decks, current_user, card_history, scores)
        elif user_choice == '3':
            view_cards_controller(decks, current_user, card_history)
        elif user_choice == '4':
            create_deck_controller(decks)
        elif user_choice == '5':
            edit_deck_controller(decks)
        elif user_choice == '6':
            delete_deck_controller(decks)
        elif user_choice == '7':
            current_user = select_user_controller(users)
        elif user_choice == '8':
            edit_card_controller(decks)
        elif user_choice == '9':
            delete_card_controller(decks)
        elif user_choice == '10':
            show_ranking_controller(scores)
        elif user_choice == '11':
            show_user_stats_controller(scores, current_user)
        elif user_choice == '0':
            print("\n¡Adiós! 👋")
            # Guarda los datos antes de salir del programa
            save_data(decks, users, card_history, scores)
            exit_program = True
        else:
            show_message("Opción inválida.")
        # Guarda los datos después de cada acción
        save_data(decks, users, card_history, scores)

if __name__ == "__main__":
    main_menu_controller()