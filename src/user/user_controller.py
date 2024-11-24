from user.user_model import create_user_model
from user.user_view import select_user_view, get_username_view
from utils.ui_utils import show_message


def select_user_controller(users):


    """
    Permite al usuario seleccionar o crear un usuario.

    Parameters:
        users (dict): Diccionario de usuarios existentes.

    Returns:
        str: Nombre del usuario seleccionado o creado.
    """

    user_choice = select_user_view(users)
    # Verificamos si el usuario eligió la opción de crear un nuevo usuario
    if user_choice == str(len(users) + 1):
        return handle_create_user_controller(users)
    else:
        # Reconstruimos el diccionario 'options' para mapear las opciones a los nombres de usuario
        # Esto es necesario para obtener el nombre de usuario correspondiente a la opción seleccionada
        options = {str(index + 1): username for index, username in enumerate(users.keys())}
        # Retornamos el nombre del usuario seleccionado
        return options[user_choice]

def handle_create_user_controller(users):
    """
    Maneja la creación de un nuevo usuario.

    Parameters:
        users (dict): Diccionario de usuarios existentes.

    Returns:
        str: Nombre del nuevo usuario creado.
    """
    username = get_username_view()
    while not username or username in users:
        # Verifica que el nombre no esté vacío y que no exista ya en el diccionario 'users'
        show_message("Nombre inválido o ya existente.")
        username = get_username_view()
    return create_user_model(users, username)