import json
import random
from datetime import datetime, timedelta


def clear_screen():
    print('\n' * 100)


def load_data():
    try:
        with open("flashcards_data.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            return (data.get('decks', {'General': []}),
                    data.get('users', {}),
                    data.get('card_history', {}),
                    data.get('scores', {}))
    except FileNotFoundError:
        return {'General': []}, {}, {}, {}


def save_data(decks, users, card_history, scores):
    data = {
        'decks': decks,
        'users': users,
        'card_history': card_history,
        'scores': scores
    }
    with open("flashcards_data.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def show_error(message):
    print(f"\n{message}")
    input("Presione Enter para continuar...")


def select_user(users):
    while True:
        clear_screen()
        print("\n=== Selección de Usuario ===")

        if users:
            print("\nUsuarios Existentes:")
            for i, name in enumerate(users.keys(), 1):
                print(f"{i}. {name}")
            print(f"{len(users) + 1}. Crear Nuevo Usuario")

            option = input("\nElegir una Opción: ")
            if option.isdigit():
                option = int(option)
                if 1 <= option <= len(users):
                    return list(users.keys())[option - 1]
                elif option == len(users) + 1:
                    return create_user(users)
        else:
            print("\nUsuario No registrado.")
            return create_user(users)

        show_error("Opción Inválida.")


def update_score(scores, user, results):
    if user not in scores:
        scores[user] = {
            'points': 0,
            'total_correct': 0,
            'total_attempts': 0,
            'streak': 0,
            'best_streak': 0
        }

    points_per_answer = {
        'Perfecto': 10,
        'Bien': 7,
        'Mal': 3,
        'Terriblemente_Nada': 1
    }

    session_points = sum(points_per_answer[response] * quantity
                         for response, quantity in results.items())

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


def create_user(users):
    while True:
        clear_screen()
        print("\n=== Crear Nuevo Usuario ===")
        name = input("\nIngrese el Nombre de Usuario: ").strip()

        if name and name not in users:
            users[name] = {
                'registration_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            return name

        show_error("Inválido o Usuario Existente. Intente con Otro Nombre.")


def select_deck(decks, mode="practice"):
    while True:
        clear_screen()
        print(f"\n=== Selección de Mazo para {mode} ===")

        print("\nMazos Disponibles:")
        for i, name in enumerate(decks.keys(), 1):
            count = len(decks[name])
            print(f"{i}. {name} ({count} Tarjetas)")
        print("0.Salir")

        if mode == "create":
            print(f"{len(decks) + 1}. Crear Nuevo Mazo")

        option = input("\nElegir una Opción: ")
        if option.isdigit():
            option = int(option)
            if option == 0:
                return 0
            if 1 <= option <= len(decks):
                return list(decks.keys())[option - 1]
            elif mode == "create" and option == len(decks) + 1:
                return create_deck(decks)

        show_error("Opción Inválida.")


def create_deck(decks):
    while True:
        clear_screen()
        print("\n=== Crear Nuevo Mazo ===")
        name = input("\nIngrese el Nombre del Mazo: ").strip()

        if name and name not in decks:
            decks[name] = []
            return name

        show_error("Inválido o Nombre ya Existente. Intente con Otro Nombre.")


def add_card(decks):
    deck_name = select_deck(decks, "create")
    if deck_name == 0:
        return
    clear_screen()
    print(f"\n=== Añadir Nueva Tarjeta al Mazo '{deck_name}' ===")
    question = input("\nIngresar Pregunta: ")
    answer = input("Ingresar Respuesta: ")

    new_card = {
        "id": f"{deck_name}_{len(decks[deck_name]) + 1}",
        "question": question,
        "answer": answer,
        "deck": deck_name
    }
    decks[deck_name].append(new_card)
    print("\nTarjeta Añadida Exitosamente!")
    input("Presione Enter para continuar...")
    return decks


def get_rating():
    while True:
        print("\n¿Cómo te fue con esta tarjeta?")
        print("1. Perfecto - Respuesta inmediata y correcta")
        print("2. Bien - Dudó pero recordó")
        print("3. Mal - Le costó recordar")
        print("4. Terriblemente_Nada - No recordó en absoluto")

        result = input("\nElija una opción (1-4): ")
        if result in ['1', '2', '3', '4']:
            intervals = {
                '1': ('Perfecto', timedelta(days=7).total_seconds()),
                '2': ('Bien', timedelta(days=1).total_seconds()),
                '3': ('Mal', timedelta(minutes=10).total_seconds()),
                '4': ('Terriblemente_Nada', 0.0)
            }
            return intervals[result]
        print("Por favor, ingrese un número del 1 al 4")


def calculate_available_cards(cards, card_history, user):
    now = datetime.now()
    available_cards = []

    for card in cards:
        card_id = card['id']
        history_key = f"{user}_{card_id}"

        if history_key not in card_history:
            available_cards.append(card)
        else:
            last_review = datetime.strptime(
                card_history[history_key]['last_review'],
                "%Y-%m-%d %H:%M:%S"
            )
            interval = timedelta(seconds=card_history[history_key]['interval'])
            next_review = last_review + interval

            if now >= next_review:
                available_cards.append(card)

    return available_cards


def show_ranking(scores):
    clear_screen()
    print("\n=== 🏆 Ranking de Usuarios ===\n")

    if not scores:
        print("No hay puntajes registrados aún.")
        input("\nPresione Enter para continuar...")
        return

    sorted_users = sorted(scores.items(),
                          key=lambda x: x[1]['points'],
                          reverse=True)

    max_points = max(data[1]['points'] for data in sorted_users)
    max_name_length = max(len(user) for user, _ in sorted_users)
    graph_width = 30

    print(f"{'Usuario':<{max_name_length}} | {'Puntos':>7} | {'Precisión':>8} | Gráfico")
    print("-" * (max_name_length + graph_width + 22))

    for pos, (user, data) in enumerate(sorted_users, 1):
        points = data['points']
        total_correct = data['total_correct']
        total_attempts = data['total_attempts']
        accuracy = (total_correct / total_attempts * 100) if total_attempts > 0 else 0

        bar_length = int((points / max_points) * graph_width) if max_points > 0 else 0
        bar = '█' * bar_length

        medal = ''
        if pos == 1:
            medal = '🥇 '
        elif pos == 2:
            medal = '🥈 '
        elif pos == 3:
            medal = '🥉 '

        print(f"{medal}{user:<{max_name_length}} | {points:>7} | {accuracy:>7.1f}% | {bar}")

    print("\nLeyenda:")
    print("• Puntos: Perfecto = 10pts, Bien = 7pts, Mal = 3pts, Terriblemente_Nada = 1pt")
    print("• Precisión: Porcentaje de respuestas correctas (Perfecto + Bien)")
    input("\nPresione Enter para continuar...")


def show_user_stats(scores, user):
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

    if data['total_attempts'] > 0:
        print("\nProgreso:")
        level = "Principiante"
        if data['points'] >= 1000:
            level = "Maestro"
        elif data['points'] >= 500:
            level = "Experto"
        elif data['points'] >= 200:
            level = "Avanzado"
        elif data['points'] >= 100:
            level = "Intermedio"

        print(f"📚 Nivel actual: {level}")

        if level != "Maestro":
            next_level = {
                "Principiante": ("Intermedio", 100),
                "Intermedio": ("Avanzado", 200),
                "Avanzado": ("Experto", 500),
                "Experto": ("Maestro", 1000)
            }
            next_level_name, points_needed = next_level[level]
            points_remaining = max(0, points_needed - data['points'])
            print(f"🎯 Puntos para {next_level_name}: {points_remaining}")

    input("\nPresione Enter para continuar...")


def practice(decks, user, card_history, scores):
    deck_name = select_deck(decks)
    cards = decks[deck_name]

    if not cards:
        show_error(f"No hay tarjetas en el mazo '{deck_name}'. Agregue algunas primero.")
        return

    available_cards = calculate_available_cards(cards, card_history, user)

    if not available_cards:
        show_error(f"No hay tarjetas disponibles para revisar en el mazo '{deck_name}'.\n" +
                   "Vuelva más tarde cuando los intervalos de revisión hayan terminado.")
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


def show_results(results, total_cards):
    clear_screen()
    print("\n=== Resultados de la Jugada ===")
    print("\nClasificación según el rating:")
    for rating, count in results.items():
        percentage = (count / total_cards) * 100 if total_cards > 0 else 0
        print(f"{rating}: {count} Tarjetas ({percentage:.1f}%)")

        if rating == 'Perfecto':
            print("  → Próxima Revisión en 1 semana")
        elif rating == 'Bien':
            print("  → Próxima Revisión en 1 día")
        elif rating == 'Mal':
            print("  → Próxima Revisión en 10 minutos")
        else:
            print("  → Aparecerá en la Próxima sesión")

    input("\nPresione Enter para continuar...")


def view_cards(decks, user, card_history):
    deck_name = select_deck(decks)
    cards = decks[deck_name]

    clear_screen()
    if not cards:
        show_error(f"No existen tarjetas en este mazo '{deck_name}'.")
    else:
        print(f"\n=== Tarjetas del Mazo '{deck_name}' ===\n")
        for i, card in enumerate(cards, 1):
            print(f"Tarjeta {i}:")
            print(f"Pregunta: {card['question']}")
            print(f"Respuesta: {card['answer']}")

            history_key = f"{user}_{card['id']}"
            if history_key in card_history:
                last_review = datetime.strptime(
                    card_history[history_key]['last_review'],
                    "%Y-%m-%d %H:%M:%S"
                )
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


def format_time(td):
    days = td.days
    hours = td.seconds // 3600
    minutes = (td.seconds % 3600) // 60

    if days > 0:
        return f"{days} días, {hours} horas"
    elif hours > 0:
        return f"{hours} horas, {minutes} minutos"
    else:
        return f"{minutes} minutos"


def edit_card(decks):
    deck_name = select_deck(decks)
    cards = decks[deck_name]
    if not cards:
        show_error(f"No existen tarjetas en este mazo '{deck_name}'.")
        return

    while True:
        clear_screen()
        print(f"\n=== Editar Tarjetas en el Mazo '{deck_name}' ===")
        for i, card in enumerate(cards, 1):
            print(f"{i}. {card['question']}")

        option = input("\nElegir una Tarjeta para Editar (0 para cancelar): ")
        if option == '0':
            return
        if option.isdigit() and 1 <= int(option) <= len(cards):
            card = cards[int(option) - 1]
            card['question'] = input(
                f"Pregunta Actual: {card['question']} \nNueva Pregunta (dejar en Blanco para conservar): ") or card['question']
            card['answer'] = input(
                f"Respuesta Actual: {card['answer']} \nNueva Respuesta (dejar en Blanco para conservar): ") or card['answer']
            print("\nTarjeta editada correctamente!")
            input("Presione Enter para continuar...")
            return
        show_error("Opción Inválida.")


def delete_card(decks):
    deck_name = select_deck(decks)
    cards = decks[deck_name]
    if not cards:
        show_error(f"No hay tarjetas en el mazo '{deck_name}'.")
        return

    while True:
        clear_screen()
        print(f"\n=== Eliminar Tarjetas en el Mazo '{deck_name}' ===")
        for i, card in enumerate(cards, 1):
            print(f"{i}. {card['question']}")

        option = input("\nElegir la Tarjeta que desea Eliminar (0 para cancelar): ")
        if option == '0':
            return
        if option.isdigit() and 1 <= int(option) <= len(cards):
            cards.pop(int(option) - 1)
            print("\nTarjeta eliminada correctamente!")
            input("Presione Enter para continuar...")
            return
        show_error("Opción Inválida.")


def edit_deck(decks):
    deck_name = select_deck(decks, mode="edit")
    new_name = input(f"\nIngresar el nuevo Nombre del Mazo '{deck_name}' (Enter para cancelar): ").strip()
    if not new_name:
        return
    if new_name and new_name not in decks:
        decks[new_name] = decks.pop(deck_name)
        print("\nMazo renombrado correctamente!")
        input("Presione Enter para continuar...")
    else:
        show_error("Nombre inválido o ya existente.")


def delete_deck(decks):
    deck_name = select_deck(decks)
    confirmation = input(f"\n¿Está seguro que desea eliminar el mazo '{deck_name}' y todas sus tarjetas? (y/n): ").lower()
    if confirmation == 'y':
        del decks[deck_name]
        print("\nMazo eliminado correctamente!")
    else:
        show_error("Eliminación cancelada.")


def main_menu():
    decks, users, card_history, scores = load_data()
    current_user = select_user(users)
    exit_program = True
    while exit_program:
        clear_screen()
        print(f"\n=== 🎮 Juego de Flashcards - Usuario: {current_user} ===")
        print("\n1. 📝 Añadir Tarjeta")
        print("2. 🎯 Practicar")
        print("3. 📊 Ver Tarjetas y Estado")
        print("4. 📚 Crear Nuevo Mazo")
        print("5. 👤 Cambiar de Usuario")
        print("6. ✏️ Editar Tarjeta")
        print("7. 🗑️ Eliminar Tarjeta")
        print("8. 📋 Editar Mazo")
        print("9. ❌ Eliminar Mazo")
        print("10. 🏆 Ver Ranking Global")
        print("11. 📈 Ver mis Estadísticas")
        print("12. 🚪 Salir")

        option = input("\nElegir una opción del 1 al 12: ")

        if option == '1':
            decks = add_card(decks)
        elif option == '2':
            practice(decks, current_user, card_history, scores)
        elif option == '3':
            view_cards(decks, current_user, card_history)
        elif option == '4':
            create_deck(decks)
        elif option == '5':
            current_user = select_user(users)
        elif option == '6':
            edit_card(decks)
        elif option == '7':
            delete_card(decks)
        elif option == '8':
            edit_deck(decks)
        elif option == '9':
            delete_deck(decks)
        elif option == '10':
            show_ranking(scores)
        elif option == '11':
            show_user_stats(scores, current_user)
        elif option == '12':
            print("\n¡Adiós! 👋")
            exit_program = False
        else:
            show_error("Opción Inválida. Por favor, elija una opción del 1 al 12")

        save_data(decks, users, card_history, scores)


if __name__ == "__main__":
    main_menu()