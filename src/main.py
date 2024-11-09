import json
import random
from datetime import datetime, timedelta

# ===================== Gestión de Datos =====================

def load_data(file_path="flashcards_data.json"):
    """
    Carga los datos desde un archivo JSON.

    Parámetros:
    - file_path (str): Ruta del archivo JSON a cargar.

    Retorna:
    - decks (dict): Diccionario con los mazos y sus tarjetas.
    - users (dict): Diccionario con la información de los usuarios.
    - card_history (dict): Historial de revisión de tarjetas por usuario.
    - scores (dict): Puntajes y estadísticas de los usuarios.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            decks = data.get('decks', {'General': []})
            users = data.get('users', {})
            card_history = data.get('card_history', {})
            scores = data.get('scores', {})
            return decks, users, card_history, scores
    except FileNotFoundError:
        # Si el archivo no existe, inicializa los datos por defecto
        return {'General': []}, {}, {}, {}

def save_data(decks, users, card_history, scores, file_path="flashcards_data.json"):
    """
    Guarda los datos en un archivo JSON.

    Parámetros:
    - decks (dict): Diccionario con los mazos y sus tarjetas.
    - users (dict): Diccionario con la información de los usuarios.
    - card_history (dict): Historial de revisión de tarjetas por usuario.
    - scores (dict): Puntajes y estadísticas de los usuarios.
    - file_path (str): Ruta del archivo JSON donde se guardarán los datos.
    """
    data = {
        'decks': decks,
        'users': users,
        'card_history': card_history,
        'scores': scores
    }
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

# ===================== Utilidades =====================

def clear_screen():
    """
    Limpia la pantalla simulando saltos de línea.
    """
    print('\n' * 100)

def show_message(message):
    """
    Muestra un mensaje y espera a que el usuario presione Enter.

    Parámetros:
    - message (str): El mensaje a mostrar.
    """
    print(f"\n{message}")
    input("Presione Enter para continuar...")

def format_time(time_difference):
    """
    Formatea un objeto timedelta en una cadena legible.

    Parámetros:
    - time_difference (timedelta): Diferencia de tiempo a formatear.

    Retorna:
    - str: Cadena con el tiempo formateado.
    """
    days = time_difference.days
    hours = time_difference.seconds // 3600  # Calcula las horas totales en los segundos
    minutes = (time_difference.seconds % 3600) // 60  # Calcula los minutos restantes
    if days > 0:
        return f"{days} días, {hours} horas"
    elif hours > 0:
        return f"{hours} horas, {minutes} minutos"
    else:
        return f"{minutes} minutos"

# Nota: La función `format_time` es una **función pura** porque:
# - Su salida depende únicamente de sus entradas.
# - No modifica variables externas ni tiene efectos secundarios.

# ===================== Interfaz de Usuario =====================

def select_option(prompt_message, options):
    """
    Muestra un menú de opciones y devuelve la elección del usuario.

    Parámetros:
    - prompt_message (str): Mensaje a mostrar al usuario.
    - options (dict): Diccionario de opciones disponibles.

    Retorna:
    - str: La clave de la opción seleccionada.
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

    Parámetros:
    - prompt_message (str): Mensaje a mostrar al usuario.

    Retorna:
    - str: Entrada del usuario sin espacios en blanco al inicio y al final.
    """
    return input(f"{prompt_message}: ").strip()

# ===================== Funciones de Usuario =====================

def select_user(users):
    """
    Permite al usuario seleccionar o crear un usuario.

    Parámetros:
    - users (dict): Diccionario de usuarios existentes.

    Retorna:
    - str: Nombre del usuario seleccionado o creado.
    """
    # Crea un diccionario de opciones con índices numéricos como claves
    options = {str(index+1): username for index, username in enumerate(users.keys())}
    options[str(len(users)+1)] = "Crear Nuevo Usuario"
    user_choice = select_option("\n=== Selección de Usuario ===", options)
    if user_choice == str(len(users)+1):
        return create_user(users)
    return options[user_choice]

def create_user(users):
    """
    Crea un nuevo usuario y lo agrega al diccionario de usuarios.

    Parámetros:
    - users (dict): Diccionario de usuarios existentes.

    Retorna:
    - str: Nombre del nuevo usuario creado.
    """
    username = get_input("\nIngrese el Nombre de Usuario")
    while not username or username in users:
        show_message("Nombre inválido o ya existente.")
        username = get_input("\nIngrese el Nombre de Usuario")
    users[username] = {'registration_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    return username

# ===================== Funciones de Mazo =====================

def select_deck(decks, include_create=False):
    """
    Permite al usuario seleccionar un mazo existente o crear uno nuevo.

    Parámetros:
    - decks (dict): Diccionario de mazos existentes.
    - include_create (bool): Si es True, incluye la opción de crear un nuevo mazo.

    Retorna:
    - str o None: Nombre del mazo seleccionado o None si se cancela.
    """
    options = {str(index+1): deck_name for index, deck_name in enumerate(decks.keys())}
    if include_create:
        options[str(len(decks)+1)] = "Crear Nuevo Mazo"
    options['0'] = "Salir"
    user_choice = select_option("\n=== Selección de Mazo ===", options)
    if user_choice == '0':
        return None
    elif include_create and user_choice == str(len(decks)+1):
        return create_deck(decks)
    return options[user_choice]

def create_deck(decks):
    """
    Crea un nuevo mazo y lo agrega al diccionario de mazos.

    Parámetros:
    - decks (dict): Diccionario de mazos existentes.

    Retorna:
    - str: Nombre del nuevo mazo creado.
    """
    deck_name = get_input("\nIngrese el Nombre del Mazo")
    while not deck_name or deck_name in decks:
        show_message("Nombre inválido o ya existente.")
        deck_name = get_input("\nIngrese el Nombre del Mazo")
    decks[deck_name] = []
    return deck_name

def edit_deck(decks):
    """
    Permite al usuario renombrar un mazo existente.

    Parámetros:
    - decks (dict): Diccionario de mazos existentes.
    """
    deck_name = select_deck(decks)
    if not deck_name:
        return
    new_deck_name = get_input(f"\nIngrese el nuevo nombre para el mazo '{deck_name}' (dejar en blanco para cancelar)")
    if new_deck_name and new_deck_name not in decks:
        decks[new_deck_name] = decks.pop(deck_name)
        show_message("Mazo renombrado correctamente.")
    else:
        show_message("Nombre inválido o ya existente.")

def delete_deck(decks):
    """
    Permite al usuario eliminar un mazo existente.

    Parámetros:
    - decks (dict): Diccionario de mazos existentes.
    """
    deck_name = select_deck(decks)
    if not deck_name:
        return
    confirmation = get_input(f"¿Está seguro que desea eliminar el mazo '{deck_name}' y todas sus tarjetas? (s/n)").lower()
    if confirmation == 's':
        del decks[deck_name]
        show_message("Mazo eliminado correctamente.")
    else:
        show_message("Eliminación cancelada.")

# ===================== Funciones de Tarjeta =====================

def add_card(decks):
    """
    Añade una nueva tarjeta a un mazo seleccionado.

    Parámetros:
    - decks (dict): Diccionario de mazos existentes.
    """
    deck_name = select_deck(decks, include_create=True)
    if not deck_name:
        return
    question = get_input("\nIngresar Pregunta")
    answer = get_input("Ingresar Respuesta")
    new_card = {
        "id": f"{deck_name}_{len(decks[deck_name]) + 1}",
        "question": question,
        "answer": answer,
        "deck": deck_name
    }
    decks[deck_name].append(new_card)
    show_message("Tarjeta añadida exitosamente.")

def edit_card(decks):
    """
    Permite al usuario editar una tarjeta existente en un mazo.

    Parámetros:
    - decks (dict): Diccionario de mazos existentes.
    """
    deck_name = select_deck(decks)
    if not deck_name or not decks[deck_name]:
        show_message("No hay tarjetas para editar en este mazo.")
        return
    cards = decks[deck_name]
    # Crea opciones para seleccionar la tarjeta a editar
    options = {str(index+1): card['question'] for index, card in enumerate(cards)}
    options['0'] = "Cancelar"
    user_choice = select_option("\n=== Seleccione una Tarjeta para Editar ===", options)
    if user_choice == '0':
        return
    selected_card = cards[int(user_choice)-1]
    # Solicita nueva pregunta y respuesta
    question = get_input(f"Pregunta Actual: {selected_card['question']} \nNueva Pregunta (dejar en blanco para conservar)")
    answer = get_input(f"Respuesta Actual: {selected_card['answer']} \nNueva Respuesta (dejar en blanco para conservar)")
    if question:
        selected_card['question'] = question
    if answer:
        selected_card['answer'] = answer
    show_message("Tarjeta editada correctamente.")

def delete_card(decks):
    """
    Permite al usuario eliminar una tarjeta existente en un mazo.

    Parámetros:
    - decks (dict): Diccionario de mazos existentes.
    """
    deck_name = select_deck(decks)
    if not deck_name or not decks[deck_name]:
        show_message("No hay tarjetas para eliminar en este mazo.")
        return
    cards = decks[deck_name]
    options = {str(index+1): card['question'] for index, card in enumerate(cards)}
    options['0'] = "Cancelar"
    user_choice = select_option("\n=== Seleccione una Tarjeta para Eliminar ===", options)
    if user_choice == '0':
        return
    cards.pop(int(user_choice)-1)
    show_message("Tarjeta eliminada correctamente.")

# ===================== Funciones de Práctica =====================

def get_rating():
    """
    Solicita al usuario que califique su desempeño en una tarjeta.

    Retorna:
    - tuple: Un par (rating, interval), donde rating es la calificación y interval es el tiempo hasta la próxima revisión.
    """
    options = {
        '1': "Perfecto - Respuesta inmediata y correcta",
        '2': "Bien - Dudó pero recordó",
        '3': "Mal - Le costó recordar",
        '4': "Terriblemente_Nada - No recordó en absoluto"
    }
    user_choice = select_option("\n¿Cómo te fue con esta tarjeta?", options)
    intervals = {
        '1': ('Perfecto', timedelta(days=7).total_seconds()),
        '2': ('Bien', timedelta(days=1).total_seconds()),
        '3': ('Mal', timedelta(minutes=10).total_seconds()),
        '4': ('Terriblemente_Nada', 0.0)
    }
    return intervals[user_choice]

def calculate_available_cards(cards, card_history, user):
    """
    Calcula las tarjetas disponibles para practicar según el historial y los intervalos.

    Parámetros:
    - cards (list): Lista de tarjetas en el mazo.
    - card_history (dict): Historial de revisión de tarjetas por usuario.
    - user (str): Nombre del usuario actual.

    Retorna:
    - list: Lista de tarjetas disponibles para practicar.
    """
    now = datetime.now()
    available_cards = []
    for card in cards:
        history_key = f"{user}_{card['id']}"  # Llave única por usuario y tarjeta
        if history_key not in card_history:
            # Si la tarjeta no ha sido revisada antes, está disponible
            available_cards.append(card)
        else:
            # Obtiene la última revisión y el intervalo para la tarjeta
            last_review = datetime.strptime(card_history[history_key]['last_review'], "%Y-%m-%d %H:%M:%S")
            interval = timedelta(seconds=card_history[history_key]['interval'])
            next_review = last_review + interval
            if now >= next_review:
                # Si es tiempo de revisar la tarjeta nuevamente
                available_cards.append(card)
    return available_cards

def practice(decks, user, card_history, scores):
    """
    Permite al usuario practicar las tarjetas disponibles en un mazo.

    Parámetros:
    - decks (dict): Diccionario de mazos existentes.
    - user (str): Nombre del usuario actual.
    - card_history (dict): Historial de revisión de tarjetas por usuario.
    - scores (dict): Puntajes y estadísticas de los usuarios.
    """
    deck_name = select_deck(decks)
    if not deck_name:
        return
    cards = decks[deck_name]
    if not cards:
        show_message(f"No hay tarjetas en el mazo '{deck_name}'.")
        return
    available_cards = calculate_available_cards(cards, card_history, user)
    if not available_cards:
        show_message("No hay tarjetas disponibles para revisar en este momento.")
        return
    random.shuffle(available_cards)  # Mezcla las tarjetas disponibles
    results = {'Perfecto': 0, 'Bien': 0, 'Mal': 0, 'Terriblemente_Nada': 0}
    for index, card in enumerate(available_cards, 1):
        clear_screen()
        print(f"\n=== Mazo: {deck_name} - Pregunta {index}/{len(available_cards)} ===")
        print(f"\nPregunta: {card['question']}")
        input("\nPresione Enter para ver la respuesta...")
        print(f"\nRespuesta: {card['answer']}")
        rating, interval = get_rating()  # Obtiene la calificación y el intervalo correspondiente
        results[rating] += 1  # Actualiza el contador de resultados
        history_key = f"{user}_{card['id']}"
        # Actualiza el historial con la nueva revisión
        card_history[history_key] = {
            'last_review': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'rating': rating,
            'interval': interval
        }
    update_score(scores, user, results)  # Actualiza el puntaje del usuario
    show_results(results, len(available_cards))

def update_score(scores, user, results):
    """
    Actualiza las estadísticas y puntajes del usuario basado en los resultados de la práctica.

    Parámetros:
    - scores (dict): Puntajes y estadísticas de los usuarios.
    - user (str): Nombre del usuario actual.
    - results (dict): Resultados de la práctica actual.
    """
    if user not in scores:
        # Inicializa las estadísticas si el usuario no existe en scores
        scores[user] = {'points': 0, 'total_correct': 0, 'total_attempts': 0, 'streak': 0, 'best_streak': 0}
    points_per_answer = {'Perfecto': 10, 'Bien': 7, 'Mal': 3, 'Terriblemente_Nada': 1}
    # Calcula los puntos obtenidos en la sesión
    session_points = sum(points_per_answer[response] * quantity for response, quantity in results.items())
    scores[user]['points'] += session_points
    # Actualiza las respuestas correctas y los intentos totales
    scores[user]['total_correct'] += results['Perfecto'] + results['Bien']
    scores[user]['total_attempts'] += sum(results.values())
    if sum(results.values()) > 0:
        # Actualiza la racha dependiendo del desempeño
        if results['Perfecto'] + results['Bien'] > results['Mal'] + results['Terriblemente_Nada']:
            scores[user]['streak'] += 1
        else:
            scores[user]['streak'] = 0
    # Actualiza la mejor racha si es necesario
    if scores[user]['streak'] > scores[user]['best_streak']:
        scores[user]['best_streak'] = scores[user]['streak']

def show_results(results, total_cards):
    """
    Muestra los resultados de la práctica al usuario.

    Parámetros:
    - results (dict): Resultados de la práctica actual.
    - total_cards (int): Número total de tarjetas practicadas.
    """
    clear_screen()
    print("\n=== Resultados de la Práctica ===")
    print("\nClasificación según el rating:")
    for rating, count in results.items():
        percentage = (count / total_cards) * 100 if total_cards > 0 else 0
        print(f"{rating}: {count} Tarjetas ({percentage:.1f}%)")
        next_review = {
            'Perfecto': "1 semana",
            'Bien': "1 día",
            'Mal': "10 minutos",
            'Terriblemente_Nada': "Inmediato"
        }
        print(f"  → Próxima Revisión en: {next_review[rating]}")
    input("\nPresione Enter para continuar...")

# ===================== Funciones de Estadísticas =====================

def show_ranking(scores):
    """
    Muestra el ranking global de usuarios basado en sus puntajes.

    Parámetros:
    - scores (dict): Puntajes y estadísticas de los usuarios.
    """
    clear_screen()
    print("\n=== 🏆 Ranking de Usuarios ===\n")
    if not scores:
        print("No hay puntajes registrados aún.")
        input("\nPresione Enter para continuar...")
        return
    # Ordena los usuarios por puntaje de mayor a menor
    sorted_users = sorted(scores.items(), key=lambda user_data: user_data[1]['points'], reverse=True)
    max_points = max(user_stats['points'] for _, user_stats in sorted_users)  # Puntaje máximo para normalizar la gráfica
    graph_width = 30  # Ancho máximo de la barra gráfica
    print(f"{'Usuario':<15} | {'Puntos':>7} | {'Precisión':>8} | Gráfico")
    print("-" * (15 + graph_width + 22))
    for position, (username, user_stats) in enumerate(sorted_users, 1):
        points = user_stats['points']
        total_correct = user_stats['total_correct']
        total_attempts = user_stats['total_attempts']
        accuracy = (total_correct / total_attempts * 100) if total_attempts > 0 else 0
        # Calcula la longitud de la barra proporcional al puntaje
        bar_length = int((points / max_points) * graph_width) if max_points > 0 else 0
        bar = '█' * bar_length
        medal = {1: '🥇', 2: '🥈', 3: '🥉'}.get(position, '')
        print(f"{medal}{username:<15} | {points:>7} | {accuracy:>7.1f}% | {bar}")
    input("\nPresione Enter para continuar...")

def show_user_stats(scores, user):
    """
    Muestra las estadísticas individuales del usuario actual.

    Parámetros:
    - scores (dict): Puntajes y estadísticas de los usuarios.
    - user (str): Nombre del usuario actual.
    """
    clear_screen()
    if user not in scores:
        print(f"\nNo hay estadísticas disponibles para {user}")
        input("\nPresione Enter para continuar...")
        return
    user_data = scores[user]
    print(f"\n=== 📊 Estadísticas de {user} ===\n")
    accuracy = (user_data['total_correct'] / user_data['total_attempts'] * 100) if user_data['total_attempts'] > 0 else 0
    print(f"🏆 Puntos totales: {user_data['points']}")
    print(f"📈 Precisión global: {accuracy:.1f}%")
    print(f"🎯 Correctas totales: {user_data['total_correct']}")
    print(f"🔄 Intentos totales: {user_data['total_attempts']}")
    print(f"🔥 Racha actual: {user_data['streak']}")
    print(f"⭐ Mejor racha: {user_data['best_streak']}")
    input("\nPresione Enter para continuar...")

# ===================== Menú Principal =====================

def main_menu():
    """
    Función principal que maneja el flujo del programa y el menú principal.
    """
    decks, users, card_history, scores = load_data()
    current_user = select_user(users)
    exit_program = False
    while not exit_program:
        options = {
            '1': "📝 Añadir Tarjeta",
            '2': "🎯 Practicar",
            '3': "📊 Ver Tarjetas y Estado",
            '4': "📚 Crear Nuevo Mazo",
            '5': "✏️ Editar Mazo",
            '6': "🗑️ Eliminar Mazo",
            '7': "👤 Cambiar de Usuario",
            '8': "✏️ Editar Tarjeta",
            '9': "🗑️ Eliminar Tarjeta",
            '10': "🏆 Ver Ranking Global",
            '11': "📈 Ver mis Estadísticas",
            '0': "🚪 Salir"
        }
        user_choice = select_option(f"\n=== 🎮 Juego de Flashcards - Usuario: {current_user} ===", options)
        if user_choice == '1':
            add_card(decks)
        elif user_choice == '2':
            practice(decks, current_user, card_history, scores)
        elif user_choice == '3':
            view_cards(decks, current_user, card_history)
        elif user_choice == '4':
            create_deck(decks)
        elif user_choice == '5':
            edit_deck(decks)
        elif user_choice == '6':
            delete_deck(decks)
        elif user_choice == '7':
            current_user = select_user(users)
        elif user_choice == '8':
            edit_card(decks)
        elif user_choice == '9':
            delete_card(decks)
        elif user_choice == '10':
            show_ranking(scores)
        elif user_choice == '11':
            show_user_stats(scores, current_user)
        elif user_choice == '0':
            print("\n¡Adiós! 👋")
            save_data(decks, users, card_history, scores)
            exit_program = True  # Cambiamos el estado para salir del bucle
        else:
            show_message("Opción inválida.")
        save_data(decks, users, card_history, scores)

def view_cards(decks, user, card_history):
    """
    Muestra las tarjetas de un mazo y su estado de disponibilidad.

    Parámetros:
    - decks (dict): Diccionario de mazos existentes.
    - user (str): Nombre del usuario actual.
    - card_history (dict): Historial de revisión de tarjetas por usuario.
    """
    deck_name = select_deck(decks)
    if not deck_name or not decks[deck_name]:
        show_message("No hay tarjetas en este mazo.")
        return
    cards = decks[deck_name]
    clear_screen()
    print(f"\n=== Tarjetas del Mazo '{deck_name}' ===\n")
    for index, card in enumerate(cards, 1):
        print(f"Tarjeta {index}:")
        print(f"Pregunta: {card['question']}")
        print(f"Respuesta: {card['answer']}")
        history_key = f"{user}_{card['id']}"
        if history_key in card_history:
            last_review = datetime.strptime(card_history[history_key]['last_review'], "%Y-%m-%d %H:%M:%S")
            interval = timedelta(seconds=card_history[history_key]['interval'])
            next_review = last_review + interval
            now = datetime.now()
            if now < next_review:
                # Calcula el tiempo restante hasta la próxima revisión
                remaining_time = next_review - now
                print(f"Estado: Bloqueado - Disponible en: {format_time(remaining_time)}")
            else:
                print("Estado: Disponible para revisar")
        else:
            print("Estado: Nuevo - Aún no estudiado")
        print()
    input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main_menu()