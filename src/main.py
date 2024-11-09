from src.utils.data_manager import load_data, save_data


def main_menu_controller():
    """
    Maneja el flujo del programa y el menú principal.

    Parameters:
        None

    Returns:
        None
    """
    decks, users, card_history, scores = load_data()
    current_user = select_user_controller(users)
    exit_program = False
    while not exit_program:
        options = {
            '1': "📝 Añadir Tarjeta",
            '2': "🎯 Practicar",
            '3': "📊 Ver Tarjetas y Estado",
            '4': "📚 Crear Nuevo Mazo",
            '5': "✏️ Editar Mazo",
            '6': "🗑️ Eliminar Mazo",
            '7': "👤 Cambiar de Usuario",
            '8': "✏️ Editar Tarjeta",
            '9': "🗑️ Eliminar Tarjeta",
            '10': "🏆 Ver Ranking Global",
            '11': "📈 Ver mis Estadísticas",
            '0': "🚪 Salir"
        }
        user_choice = select_option(f"\n=== 🎮 Juego de Flashcards - Usuario: {current_user} ===", options)
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
            save_data(decks, users, card_history, scores)
            exit_program = True
        else:
            show_message("Opción inválida.")
        save_data(decks, users, card_history, scores)