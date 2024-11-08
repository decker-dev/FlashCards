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

def format_time(td):
    """
    Formatea un objeto timedelta en una cadena legible.

    Parámetros:
    - td (timedelta): Diferencia de tiempo a formatear.

    Retorna:
    - str: Cadena con el tiempo formateado.
    """
    days = td.days
    hours = td.seconds // 3600
    minutes = (td.seconds % 3600) // 60
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

def select_option(prompt, options):
    """
    Muestra un menú de opciones y devuelve la elección del usuario.

    Parámetros:
    - prompt (str): Mensaje a mostrar al usuario.
    - options (dict): Diccionario de opciones disponibles.

    Retorna:
    - str: La clave de la opción seleccionada.
    """
    while True:
        clear_screen()
        print(prompt)
        for key, value in options.items():
            print(f"{key}. {value}")
        choice = input("\nElegir una opción: ")
        if choice in options:
            return choice
        show_message("Opción inválida. Intente nuevamente.")

def get_input(prompt):
    """
    Solicita una entrada al usuario.

    Parámetros:
    - prompt (str): Mensaje a mostrar al usuario.

    Retorna:
    - str: Entrada del usuario sin espacios en blanco al inicio y al final.
    """
    return input(f"{prompt}: ").strip()

# ===================== Funciones de Usuario =====================

def select_user(users):
    """
    Permite al usuario seleccionar o crear un usuario.

    Parámetros:
    - users (dict): Diccionario de usuarios existentes.

    Retorna:
    - str: Nombre del usuario seleccionado o creado.
    """
    options = {str(i+1): name for i, name in enumerate(users.keys())}
    options[str(len(users)+1)] = "Crear Nuevo Usuario"
    choice = select_option("\n=== Selección de Usuario ===", options)
    if choice == str(len(users)+1):
        return create_user(users)
    return options[choice]

def create_user(users):
    """
    Crea un nuevo usuario y lo agrega al diccionario de usuarios.

    Parámetros:
    - users (dict): Diccionario de usuarios existentes.

    Retorna:
    - str: Nombre del nuevo usuario creado.
    """
    while True:
        name = get_input("\nIngrese el Nombre de Usuario")
        if name and name not in users:
            users[name] = {'registration_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            return name
        show_message("Nombre inválido o ya existente.")

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
    options = {str(i+1): name for i, name in enumerate(decks.keys())}
    if include_create:
        options[str(len(decks)+1)] = "Crear Nuevo Mazo"
    options['0'] = "Salir"
    choice = select_option("\n=== Selección de Mazo ===", options)
    if choice == '0':
        return None
    elif include_create and choice == str(len(decks)+1):
        return create_deck(decks)
    return options[choice]

def create_deck(decks):
    """
    Crea un nuevo mazo y lo agrega al diccionario de mazos.

    Parámetros:
    - decks (dict): Diccionario de mazos existentes.

    Retorna:
    - str: Nombre del nuevo mazo creado.
    """
    while True:
        name = get_input("\nIngrese el Nombre del Mazo")
        if name and name not in decks:
            decks[name] = []
            return name
        show_message("Nombre inválido o ya existente.")

def edit_deck(decks):
    """
    Permite al usuario renombrar un mazo existente.

    Parámetros:
    - decks (dict): Diccionario de mazos existentes.
    """
    deck_name = select_deck(decks)
    if not deck_name:
        return
    new_name = get_input(f"\nIngrese el nuevo nombre para el mazo '{deck_name}' (dejar en blanco para cancelar)")
    if new_name and new_name not in decks:
        decks[new_name] = decks.pop(deck_name)
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
    options = {str(i+1): card['question'] for i, card in enumerate(cards)}
    options['0'] = "Cancelar"
    choice = select_option("\n=== Seleccione una Tarjeta para Editar ===", options)
    if choice == '0':
        return
    card = cards[int(choice)-1]
    question = get_input(f"Pregunta Actual: {card['question']} \nNueva Pregunta (dejar en blanco para conservar)")
    answer = get_input(f"Respuesta Actual: {card['answer']} \nNueva Respuesta (dejar en blanco para conservar)")
    if question:
        card['question'] = question
    if answer:
        card['answer'] = answer
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
    options = {str(i+1): card['question'] for i, card in enumerate(cards)}
    options['0'] = "Cancelar"
    choice = select_option("\n=== Seleccione una Tarjeta para Eliminar ===", options)
    if choice == '0':
        return
    cards.pop(int(choice)-1)
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
    choice = select_option("\n¿Cómo te fue con esta tarjeta?", options)
    intervals = {
        '1': ('Perfecto', timedelta(days=7).total_seconds()),
        '2': ('Bien', timedelta(days=1).total_seconds()),
        '3': ('Mal', timedelta(minutes=10).total_seconds()),
        '4': ('Terriblemente_Nada', 0.0)
    }
    return intervals[choice]

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
        history_key = f"{user}_{card['id']}"
        if history_key not in card_history:
            available_cards.append(card)
        else:
            last_review = datetime.strptime(card_history[history_key]['last_review'], "%Y-%m-%d %H:%M:%S")
            interval = timedelta(seconds=card_history[history_key]['interval'])
            next_review = last_review + interval
            if now >= next_review:
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
    random.shuffle(available_cards)
    results = {'Perfecto': 0, 'Bien': 0, 'Mal': 0, 'Terriblemente_Nada': 0}
    for i, card in enumerate(available_cards, 1):
        clear_screen()
        print(f"\n=== Mazo: {deck_name} - Pregunta {i}/{len(available_cards)} ===")
        print(f"\nPregunta: {card['question']}")
        input("\nPresione Enter para ver la respuesta...")
        print(f"\nRespuesta: {card['answer']}")
        rating, interval = get_rating()
        results[rating] += 1
        history_key = f"{user}_{card['id']}"
        card_history[history_key] = {
            'last_review': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'rating': rating,
            'interval': interval
        }
    update_score(scores, user, results)
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
        scores[user] = {'points': 0, 'total_correct': 0, 'total_attempts': 0, 'streak': 0, 'best_streak': 0}
    points_per_answer = {'Perfecto': 10, 'Bien': 7, 'Mal': 3, 'Terriblemente_Nada': 1}
    session_points = sum(points_per_answer[response] * quantity for response, quantity in results.items())
    scores[user]['points'] += session_points
    scores[user]['total_correct'] += results['Perfecto'] + results['Bien']
    scores[user]['total_attempts'] += sum(results.values())
    if sum(results.values()) > 0:
        if results['Perfecto'] + results['Bien'] > results['Mal'] + results['Terriblemente_Nada']:
            scores[user]['streak'] += 1
        else:
            scores[user]['streak'] = 0
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
    sorted_users = sorted(scores.items(), key=lambda x: x[1]['points'], reverse=True)
    max_points = max(data['points'] for _, data in sorted_users)
    graph_width = 30
    print(f"{'Usuario':<15} | {'Puntos':>7} | {'Precisión':>8} | Gráfico")
    print("-" * (15 + graph_width + 22))
    for pos, (user, data) in enumerate(sorted_users, 1):
        points = data['points']
        total_correct = data['total_correct']
        total_attempts = data['total_attempts']
        accuracy = (total_correct / total_attempts * 100) if total_attempts > 0 else 0
        bar_length = int((points / max_points) * graph_width) if max_points > 0 else 0
        bar = '█' * bar_length
        medal = {1: '🥇', 2: '🥈', 3: '🥉'}.get(pos, '')
        print(f"{medal}{user:<15} | {points:>7} | {accuracy:>7.1f}% | {bar}")
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
    data = scores[user]
    print(f"\n=== 📊 Estadísticas de {user} ===\n")
    accuracy = (data['total_correct'] / data['total_attempts'] * 100) if data['total_attempts'] > 0 else 0
    print(f"🏆 Puntos totales: {data['points']}")
    print(f"📈 Precisión global: {accuracy:.1f}%")
    print(f"🎯 Correctas totales: {data['total_correct']}")
    print(f"🔄 Intentos totales: {data['total_attempts']}")
    print(f"🔥 Racha actual: {data['streak']}")
    print(f"⭐ Mejor racha: {data['best_streak']}")
    input("\nPresione Enter para continuar...")

# ===================== Menú Principal =====================

def main_menu():
    """
    Función principal que maneja el flujo del programa y el menú principal.
    """
    decks, users, card_history, scores = load_data()
    current_user = select_user(users)
    while True:
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
        choice = select_option(f"\n=== 🎮 Juego de Flashcards - Usuario: {current_user} ===", options)
        if choice == '1':
            add_card(decks)
        elif choice == '2':
            practice(decks, current_user, card_history, scores)
        elif choice == '3':
            view_cards(decks, current_user, card_history)
        elif choice == '4':
            create_deck(decks)
        elif choice == '5':
            edit_deck(decks)
        elif choice == '6':
            delete_deck(decks)
        elif choice == '7':
            current_user = select_user(users)
        elif choice == '8':
            edit_card(decks)
        elif choice == '9':
            delete_card(decks)
        elif choice == '10':
            show_ranking(scores)
        elif choice == '11':
            show_user_stats(scores, current_user)
        elif choice == '0':
            print("\n¡Adiós! 👋")
            save_data(decks, users, card_history, scores)
            break
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
    for i, card in enumerate(cards, 1):
        print(f"Tarjeta {i}:")
        print(f"Pregunta: {card['question']}")
        print(f"Respuesta: {card['answer']}")
        history_key = f"{user}_{card['id']}"
        if history_key in card_history:
            last_review = datetime.strptime(card_history[history_key]['last_review'], "%Y-%m-%d %H:%M:%S")
            interval = timedelta(seconds=card_history[history_key]['interval'])
            next_review = last_review + interval
            now = datetime.now()
            if now < next_review:
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