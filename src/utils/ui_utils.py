def clear_screen():
    """
    Limpia la pantalla simulando saltos de línea.
    """
    print('\n' * 100)

def show_message(message):
    """
    Muestra un mensaje y espera a que el usuario presione Enter.
    """
    print(f"\n{message}")
    input("Presione Enter para continuar...")

def format_time(time_difference):
    """
    Formatea un objeto timedelta en una cadena legible.
    """
    days = time_difference.days
    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds % 3600) // 60
    if days > 0:
        return f"{days} días, {hours} horas"
    elif hours > 0:
        return f"{hours} horas, {minutes} minutos"
    else:
        return f"{minutes} minutos"

def select_option(prompt_message, options):
    """
    Muestra un menú de opciones y devuelve la elección del usuario.
    """
    user_choice = None
    while user_choice not in options:
        clear_screen()
        print(prompt_message)
        for option_key, option_value in options.items():
            print(f"{option_key}. {option_value}")
        user_choice = input("\nElegir una opción: ")
        if user_choice not in options:
            show_message("Opción inválida. Intente nuevamente.")
    return user_choice

def get_input(prompt_message):
    """
    Solicita una entrada al usuario.
    """
    return input(f"{prompt_message}: ").strip()