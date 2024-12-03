from card.card_model import create_card_model, edit_card_model, delete_card_model
from stats.stats_model import update_score_model
from user.user_model import create_user_model


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


def test_create_user_model():
    users = {}
    username = 'nuevo_usuario'

    creado = create_user_model(users, username)

    assert creado == username
    assert username in users
    assert 'registration_date' in users[username]


def test_create_card_model():
    decks = {'Mazo1': []}
    deck_name = 'Mazo1'
    question = '¿Cuál es la capital de Francia?'
    answer = 'París'

    nueva_tarjeta = create_card_model(decks, deck_name, question, answer)

    assert nueva_tarjeta['id'] == f"{deck_name}_1"
    assert nueva_tarjeta['question'] == question
    assert nueva_tarjeta['answer'] == answer
    assert nueva_tarjeta['deck'] == deck_name
    assert nueva_tarjeta in decks[deck_name]

def test_edit_card_model():
    card = {
        "id": "Mazo1_1",
        "question": "Pregunta original",
        "answer": "Respuesta original",
        "deck": "Mazo1"
    }
    nueva_pregunta = "Pregunta editada"
    nueva_respuesta = "Respuesta editada"

    edit_card_model(card, nueva_pregunta, nueva_respuesta)

    assert card['question'] == nueva_pregunta
    assert card['answer'] == nueva_respuesta

def test_delete_card_model():
    card = {
        "id": "Mazo1_1",
        "question": "Pregunta de prueba",
        "answer": "Respuesta de prueba",
        "deck": "Mazo1"
    }
    decks = {'Mazo1': [card]}
    deck_name = 'Mazo1'
    card_index = 0

    delete_card_model(decks, deck_name, card_index)

    assert len(decks[deck_name]) == 0