from src.utils.ui_utils import clear_screen


def view_show_ranking(scores):
    """
    Muestra el ranking global de usuarios basado en sus puntajes.
    """
    clear_screen()
    print("\n=== 🏆 Ranking de Usuarios ===\n")
    if not scores:
        print("No hay puntajes registrados aún.")
        input("\nPresione Enter para continuar...")
        return
    sorted_users = sorted(scores.items(), key=lambda user_data: user_data[1]['points'], reverse=True)
    max_points = max(user_stats['points'] for _, user_stats in sorted_users)
    graph_width = 30
    print(f"{'Usuario':<15} | {'Puntos':>7} | {'Precisión':>8} | Gráfico")
    print("-" * (15 + graph_width + 22))
    for position, (username, user_stats) in enumerate(sorted_users, 1):
        points = user_stats['points']
        total_correct = user_stats['total_correct']
        total_attempts = user_stats['total_attempts']
        accuracy = (total_correct / total_attempts * 100) if total_attempts > 0 else 0
        bar_length = int((points / max_points) * graph_width) if max_points > 0 else 0
        bar = '█' * bar_length
        medal = {1: '🥇', 2: '🥈', 3: '🥉'}.get(position, '')
        print(f"{medal}{username:<15} | {points:>7} | {accuracy:>7.1f}% | {bar}")
    input("\nPresione Enter para continuar...")

def view_show_user_stats(scores, user):
    """
    Muestra las estadísticas individuales del usuario actual.
    """
    clear_screen()
    if user not in scores:
        print(f"\nNo hay estadísticas disponibles para {user}")
        input("\nPresione Enter para continuar...")
        return
    user_data = scores[user]
    accuracy = (user_data['total_correct'] / user_data['total_attempts'] * 100) if user_data['total_attempts'] > 0 else 0
    print(f"\n=== 📊 Estadísticas de {user} ===\n")
    print(f"🏆 Puntos totales: {user_data['points']}")
    print(f"📈 Precisión global: {accuracy:.1f}%")
    print(f"🎯 Correctas totales: {user_data['total_correct']}")
    print(f"🔄 Intentos totales: {user_data['total_attempts']}")
    print(f"🔥 Racha actual: {user_data['streak']}")
    print(f"⭐ Mejor racha: {user_data['best_streak']}")
    input("\nPresione Enter para continuar...")