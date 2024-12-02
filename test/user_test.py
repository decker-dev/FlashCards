from src.stats.stats_model import update_score_model


def test_update_score_model():
    # Datos iniciales
    scores = {}
    user = 'usuario_test'
    results = {'Perfecto': 1, 'Bien': 0, 'Mal': 0, 'Terriblemente': 0}

    # Llamamos a la función a probar
    update_score_model(scores, user, results)

    # Valores esperados después de la actualización
    puntos_esperados = 10  # 1 'Perfecto' * 10 puntos
    total_correctas_esperado = 1  # Solo una respuesta correcta
    total_intentos_esperado = 1  # Un intento en total
    racha_esperada = 1  # La racha debería ser 1
    mejor_racha_esperada = 1  # Mejor racha actualizada a 1

    # Verificamos que los resultados sean los esperados
    assert scores[user]['points'] == puntos_esperados
    assert scores[user]['total_correct'] == total_correctas_esperado
    assert scores[user]['total_attempts'] == total_intentos_esperado
    assert scores[user]['streak'] == racha_esperada
    assert scores[user]['best_streak'] == mejor_racha_esperada