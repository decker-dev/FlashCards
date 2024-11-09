from src.user.user_model import create_user
from src.user.user_view import select_user_view, get_username
from src.utils.ui_utils import show_message


def select_user(users):
    """
    Permite al usuario seleccionar o crear un usuario.
    """
    user_choice = select_user_view(users)
    if user_choice == str(len(users)+1):
        return handle_create_user(users)
    else:
        options = {str(index+1): username for index, username in enumerate(users.keys())}
        return options[user_choice]

def handle_create_user(users):
    """
    Maneja la creación de un nuevo usuario.
    """
    username = get_username()
    while not username or username in users:
        show_message("Nombre inválido o ya existente.")
        username = get_username()
    return create_user(users, username)