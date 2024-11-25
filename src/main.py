from card.card_controller import add_card_controller, view_cards_controller, edit_card_controller, \
    delete_card_controller
from deck.deck_controller import create_deck_controller, edit_deck_controller, delete_deck_controller
from practice.practice_controller import practice_controller, random_practice_controller
from graphics.graphics import print_flashcards, print_welcome, print_bar
from stats.stats_controller import show_ranking_controller, show_user_stats_controller
from user.user_controller import select_user_controller
from utils.data_manager import load_data, save_data
from utils.ui_utils import select_option, show_message



def main_menu_controller():
    """
    Maneja el flujo del programa y el menú principal.

    Parameters:
        None

    Returns:
        None
    """





    # Imprime el título al inicio
    print_flashcards()
    input("Presiona Enter para comenzar...")

    # Carga los datos almacenados desde un archivo JSON
    print_welcome()
    decks, users, card_history, scores = load_data()
    # Permite al usuario seleccionar o crear un usuario
    current_user = select_user_controller(users)
    exit_program = False
    while not exit_program:
        # Define las opciones del menú principal en un diccionario
        screen_title = 'Menú de opciones'
        options = {
            '1': "📝 Añadir Tarjeta",
            '2': "🎯 Practicar",
            '3': "🎲 Practica Libre",
            '4': "📊 Ver Tarjetas y Estado",
            '5': "📚 Crear Nuevo Mazo",
            '6': "✏️ Editar Mazo",
            '7': "🗑️ Eliminar Mazo",
            '8': "👤 Cambiar de Usuario",
            '9': "✏️ Editar Tarjeta",
            '10': "🗑️ Eliminar Tarjeta",
            '11': "🏆 Ver Ranking Global",
            '12': "📈 Ver mis Estadísticas",
            '0': "🚪 Salir"
        }
        # Muestra el menú y obtiene la opción seleccionada por el usuario
        print_bar(current_user=current_user)
        user_choice = select_option(f" 🎮 🕹️ Opciones del Juego 🕹️ 🎮\n", options)
        #print_screen(screen_title, options, current_user)
        #user_choice = select_option(options=options)
        # Ejecuta acciones basadas en la opción seleccionada

        if user_choice == '1':
            add_card_controller(decks)
        elif user_choice == '2':
            practice_controller(decks, current_user, card_history, scores)
        elif user_choice == '3':
            random_practice_controller(decks)
        elif user_choice == '4':
            view_cards_controller(decks, current_user, card_history)
        elif user_choice == '5':
            create_deck_controller(decks)
        elif user_choice == '6':
            edit_deck_controller(decks)
        elif user_choice == '7':
            delete_deck_controller(decks)
        elif user_choice == '8':
            current_user = select_user_controller(users)
        elif user_choice == '9':
            edit_card_controller(decks)
        elif user_choice == '10':
            delete_card_controller(decks)
        elif user_choice == '11':
            show_ranking_controller(scores)
        elif user_choice == '12':
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