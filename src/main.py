from src.card.card_controller import add_card, view_cards, edit_card, delete_card
from src.deck.deck_controller import create_deck, edit_deck, delete_deck
from src.practice.practice_controller import practice
from src.stats.stats_controller import show_ranking, show_user_stats
from src.user.user_controller import select_user
from src.utils.data_manager import load_data, save_data
from src.utils.ui_utils import select_option, show_message


def main_menu():
    """
    Función principal que maneja el flujo del programa y el menú principal.
    """
    decks, users, card_history, scores = load_data()
    current_user = select_user(users)
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
            add_card(decks)
        elif user_choice == '2':
            practice(decks, current_user, card_history, scores)
        elif user_choice == '3':
            view_cards(decks, current_user, card_history)
        elif user_choice == '4':
            create_deck(decks)
        elif user_choice == '5':
            edit_deck(decks)
        elif user_choice == '6':
            delete_deck(decks)
        elif user_choice == '7':
            current_user = select_user(users)
        elif user_choice == '8':
            edit_card(decks)
        elif user_choice == '9':
            delete_card(decks)
        elif user_choice == '10':
            show_ranking(scores)
        elif user_choice == '11':
            show_user_stats(scores, current_user)
        elif user_choice == '0':
            print("\n¡Adiós! 👋")
            save_data(decks, users, card_history, scores)
            exit_program = True
        else:
            show_message("Opción inválida.")
        save_data(decks, users, card_history, scores)


if __name__ == "__main__":
    main_menu()