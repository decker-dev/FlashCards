from datetime import datetime

def create_user(users, username):
    """
    Crea un nuevo usuario y lo agrega al diccionario de usuarios.
    """
    users[username] = {'registration_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    return username