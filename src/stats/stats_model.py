def update_score_model(scores, user, results):
    """
    Actualiza las estadísticas y puntajes del usuario.

    Parameters:
        scores (dict): Puntajes y estadísticas de los usuarios.
        user (str): Nombre del usuario actual.
        results (dict): Resultados de la práctica actual.

    Returns:
        None
    """
    if user not in scores:
        # Inicializa las estadísticas del usuario si aún no existen
        scores[user] = {'points': 0, 'total_correct': 0, 'total_attempts': 0, 'streak': 0, 'best_streak': 0}
    # Define los puntos otorgados por cada tipo de respuesta
    points_per_answer = {'Perfecto': 10, 'Bien': 7, 'Mal': 3, 'Nada': 1}
    # Calcula los puntos obtenidos en la sesión actual
    session_points = sum(points_per_answer[response] * quantity for response, quantity in results.items())
    scores[user]['points'] += session_points
    # Actualiza el total de respuestas correctas y el total de intentos
    scores[user]['total_correct'] += results['Perfecto'] + results['Bien']
    scores[user]['total_attempts'] += sum(results.values())
    # Actualiza la racha actual y la mejor racha
    if sum(results.values()) > 0:
        if results['Perfecto'] + results['Bien'] > results['Mal'] + results['Nada']:
            scores[user]['streak'] += 1
        else:
            scores[user]['streak'] = 0
    if scores[user]['streak'] > scores[user]['best_streak']:
        scores[user]['best_streak'] = scores[user]['streak']