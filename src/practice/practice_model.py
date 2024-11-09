from datetime import datetime, timedelta

def calculate_available_cards_model(cards, card_history, user):
    """
    Calcula las tarjetas disponibles para practicar.

    Parameters:
        cards (list): Lista de tarjetas en el mazo.
        card_history (dict): Historial de revisión de tarjetas por usuario.
        user (str): Nombre del usuario actual.

    Returns:
        list: Lista de tarjetas disponibles para practicar.
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

def update_card_history_model(card_history, user, card_id, rating, interval):
    """
    Actualiza el historial de revisión de una tarjeta.

    Parameters:
        card_history (dict): Historial de revisión de tarjetas por usuario.
        user (str): Nombre del usuario actual.
        card_id (str): ID de la tarjeta.
        rating (str): Calificación del usuario.
        interval (float): Intervalo hasta la próxima revisión en segundos.

    Returns:
        None
    """
    history_key = f"{user}_{card_id}"
    card_history[history_key] = {
        'last_review': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'rating': rating,
        'interval': interval
    }