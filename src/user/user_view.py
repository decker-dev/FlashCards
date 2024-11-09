from src.utils.ui_utils import select_option, get_input


def select_user_view(users):
    """
    Muestra el menú para seleccionar o crear un usuario.
    """
    options = {str(index+1): username for index, username in enumerate(users.keys())}
    options[str(len(users)+1)] = "Crear Nuevo Usuario"
    user_choice = select_option("\n=== Selección de Usuario ===", options)
    return user_choice

def get_username():
    """
    Solicita al usuario que ingrese un nombre de usuario.
    """
    return get_input("\nIngrese el Nombre de Usuario")