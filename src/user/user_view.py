from src.utils.ui_utils import select_option, get_input


def select_user_view(users):
    """
    Muestra el menú para seleccionar o crear un usuario.

    Parameters:
        users (dict): Diccionario de usuarios existentes.

    Returns:
        str: Opción seleccionada por el usuario.
    """
    options = {str(index+1): username for index, username in enumerate(users.keys())}
    options[str(len(users)+1)] = "Crear Nuevo Usuario"
    user_choice = select_option("\n=== Selección de Usuario ===", options)
    return user_choice

def get_username_view():
    """
    Solicita al usuario que ingrese un nombre de usuario.

    Parameters:
        None

    Returns:
        str: Nombre de usuario ingresado.
    """
    return get_input("\nIngrese el Nombre de Usuario")