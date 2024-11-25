from utils.ui_utils import select_option, get_input


def select_user_view(users):
    """
    Muestra el menú para seleccionar o crear un usuario.

    Parameters:
        users (dict): Diccionario de usuarios existentes.

    Returns:
        str: Opción seleccionada por el usuario.
    """
    # Creamos un diccionario 'options' para el menú de selección de usuario
    # 'enumerate(users.keys())' crea pares de índice y nombre de usuario
    # Por ejemplo, si users.keys() es ['Alice', 'Bob'], enumerate(users.keys()) genera (0, 'Alice'), (1, 'Bob')
    # Usamos 'index + 1' para que el índice empiece desde 1 en lugar de 0
    # Convertimos 'index + 1' a string usando 'str()' para que las claves sean cadenas
    options = {str(index + 1): username for index, username in enumerate(users.keys())}
    # Añadimos una opción adicional para crear un nuevo usuario
    # 'len(users) + 1' nos da el siguiente número disponible para la nueva opción
    options[str(len(users) + 1)] = "Crear Nuevo Usuario"
    # Mostramos el menú de opciones y obtenemos la elección del usuario
    user_choice = select_option("", options)
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