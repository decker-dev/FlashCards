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
        # Construye una clave única para identificar el historial de esta tarjeta para el usuario actual
        history_key = f"{user}_{card['id']}"
        if history_key not in card_history:
            # Si la tarjeta no ha sido estudiada antes, está disponible
            available_cards.append(card)
        else:
            # Si la tarjeta tiene historial, verifica si ya es tiempo de volver a revisarla
            last_review = datetime.strptime(card_history[history_key]['last_review'], "%Y-%m-%d %H:%M:%S")
            interval = timedelta(seconds=card_history[history_key]['interval'])
            next_review = last_review + interval
            if now >= next_review:
                # Si la fecha actual es igual o posterior a la próxima revisión, la tarjeta está disponible
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
    # Construye una clave única para identificar el historial de esta tarjeta para el usuario actual
    history_key = f"{user}_{card_id}"
    # Actualiza el historial con la fecha actual, el rating y el nuevo intervalo
    card_history[history_key] = {
        'last_review': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'rating': rating,
        'interval': interval
    }