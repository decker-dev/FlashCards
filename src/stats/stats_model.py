def update_score(scores, user, results):
    """
    Actualiza las estadísticas y puntajes del usuario.
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