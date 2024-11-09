from datetime import datetime

def create_user_model(users, username):
    """
    Crea un nuevo usuario y lo agrega al diccionario de usuarios.

    Parameters:
        users (dict): Diccionario de usuarios existentes.
        username (str): Nombre del usuario a crear.

    Returns:
        str: Nombre del usuario creado.
    """
    # Añade el nuevo usuario al diccionario con la fecha de registro actual
    users[username] = {'registration_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    return username