from modules.card import create_card
from modules.review import study_mode

def show_main_menu():
    while True:
        print("\nFlashcard Management System")
        print("1. Create Card")
        print("2. Study Mode")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            create_card(question, answer)
            print("Card created successfully!")
        elif choice == '2':
            study_mode()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

def navigate_options():
    """
    Facilitate option navigation in the menu.

    Returns:
    None
    """
    pass

def display_card(card):
    """
    Display a specific card.

    Parameters:
    card (dict): The card to display.

    Returns:
    None
    """
    pass

def display_all_cards():
    """
    Display all available cards.

    Returns:
    None
    """
    pass

def get_user_input():
    """
    Handle user input in a centralized manner.

    Returns:
    str: The user's input.
    """
    pass
