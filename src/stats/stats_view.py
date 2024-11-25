from utils.ui_utils import clear_screen

from graphics.graphics import print_bar


def show_ranking_view(scores):
    """
    Muestra el ranking global de usuarios basado en sus puntajes.

    Parameters:
        scores (dict): Puntajes y estadísticas de los usuarios.

    Returns:
        None
    """
    clear_screen()
    print_bar(is_upper=True)
    print("\t 🌈  🎉 🏆 Ranking de Usuarios 🏆 🎉 🌈 \n")
    if not scores:
        print("No hay puntajes registrados aún.")
        input("\nPresione Enter para continuar...")
        return
    # Convierte el diccionario 'scores' en una lista de tuplas (usuario, datos) para poder ordenarla
    # 'scores.items()' devuelve pares (clave, valor), es decir, (usuario, datos)
    sorted_users = sorted(scores.items(), key=lambda user_data: user_data[1]['points'], reverse=True)
    # Encuentra el máximo puntaje para escalar las barras gráficas
    max_points = max(user_stats['points'] for _, user_stats in sorted_users)
    graph_width = 30
    print(f"\t{'Usuario':<15} | {'Puntos':>7} | {'Precisión':>8} | Gráfico")
    print("-" * (30 + graph_width + 22))
    for position, (username, user_stats) in enumerate(sorted_users, 1):
        points = user_stats['points']
        total_correct = user_stats['total_correct']
        total_attempts = user_stats['total_attempts']
        # Calcula la precisión como porcentaje
        accuracy = (total_correct / total_attempts * 100) if total_attempts > 0 else 0
        # Calcula la longitud de la barra gráfica proporcional al puntaje
        bar_length = int((points / max_points) * graph_width) if max_points > 0 else 0
        bar = '█' * bar_length
        # Asigna medallas a los tres primeros lugares
        medal = {1: '🥇', 2: '🥈', 3: '🥉'}.get(position, '')
        print(f"\t{medal}{username:<15} | {points:>7} | {accuracy:>7.1f}% | {bar}")
    print_bar(is_upper=False)
    input("\nPresione Enter para continuar...")

def show_user_stats_view(scores, user):
    """
    Muestra las estadísticas individuales del usuario actual.

    Parameters:
        scores (dict): Puntajes y estadísticas de los usuarios.
        user (str): Nombre del usuario actual.

    Returns:
        None
    """
    clear_screen()
    print_bar(is_upper=True)
    if user not in scores:
        print(f"\nNo hay estadísticas disponibles para {user}")
        input("\nPresione Enter para continuar...")
        return
    user_data = scores[user]
    # Calcula la precisión como porcentaje
    accuracy = (user_data['total_correct'] / user_data['total_attempts'] * 100) if user_data['total_attempts'] > 0 else 0
    print(f"\n\t 📊 Estadísticas de ✨ {user} ✨ \n")
    print(f"\t🏆 Puntos totales: {user_data['points']}")
    print(f"\t📈 Precisión global: {accuracy:.1f}%")
    print(f"\t🎯 Correctas totales: {user_data['total_correct']}")
    print(f"\t🔄 Intentos totales: {user_data['total_attempts']}")
    print(f"\t🔥 Racha actual: {user_data['streak']}")
    print(f"\t⭐ Mejor racha: {user_data['best_streak']}")
    print_bar(is_upper=False)
    input("\nPresione Enter para continuar...")