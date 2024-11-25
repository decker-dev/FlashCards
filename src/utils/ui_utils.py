from src.graphics.graphics import print_bar, print_welcome, print_screen_title


def clear_screen():
    """
    Limpia la pantalla simulando saltos de línea.

    Parameters:
        None

    Returns:
        None
    """
    print('\n' * 10)

def show_message(message):
    """
    Muestra un mensaje y espera a que el usuario presione Enter.

    Parameters:
        message (str): El mensaje a mostrar.

    Returns:
        None
    """
    print(f"{message}")
    input("Presione Enter para continuar...")

def format_time(time_difference):
    """
    Formatea un objeto timedelta en una cadena legible.

    Parameters:
        time_difference (timedelta): Diferencia de tiempo a formatear.

    Returns:
        str: Cadena con el tiempo formateado.
    """
    days = time_difference.days
    # Calcula las horas totales en el objeto timedelta
    hours = time_difference.seconds // 3600
    # Calcula los minutos restantes después de quitar las horas
    minutes = (time_difference.seconds % 3600) // 60
    if days > 0:
        return f"{days} días, {hours} horas"
    elif hours > 0:
        return f"{hours} horas, {minutes} minutos"
    else:
        return f"{minutes} minutos"

def select_option(prompt_message='', options={}):
    """
    Muestra un menú de opciones y devuelve la elección del usuario.

    Parameters:
        prompt_message (str): Mensaje a mostrar al usuario.
        options (dict): Diccionario de opciones disponibles.

    Returns:
        str: La clave de la opción seleccionada.
    """
    # print('--- ',prompt_message)
    # print('---',options)
    user_choice = None
    while user_choice not in options:
        # print(prompt_message)
        parts = prompt_message.split("===")
        if len(parts) > 1:
            screen_title = parts[1].strip()

            print_screen_title(screen_title)
        # Recorre el diccionario de opciones y muestra cada una
        # print_bar(current_user)
        for option_key, option_value in options.items():
            print(f"\t{option_key}. {option_value}")
        print_bar(is_upper=False)
        user_choice = input("Elegir una opción: ")
        if user_choice not in options:
            show_message("Opción inválida. Intente nuevamente.")
            print_welcome()
        # print('---', user_choice)
        return user_choice

def get_input(prompt_message):
    """
    Solicita una entrada al usuario.

    Parameters:
        prompt_message (str): Mensaje a mostrar al usuario.

    Returns:
        str: Entrada del usuario sin espacios en blanco al inicio y al final.
    """
    return input(f"{prompt_message}: ").strip()