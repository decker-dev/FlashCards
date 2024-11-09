def create_card_model(decks, deck_name, question, answer):
    """
    Añade una nueva tarjeta a un mazo.

    Parameters:
        decks (dict): Diccionario de mazos existentes.
        deck_name (str): Nombre del mazo.
        question (str): Pregunta de la tarjeta.
        answer (str): Respuesta de la tarjeta.

    Returns:
        dict: La tarjeta creada.
    """
    new_card = {
        # Genera un ID único para la tarjeta combinando el nombre del mazo y el número total de tarjetas más uno
        "id": f"{deck_name}_{len(decks[deck_name]) + 1}",
        "question": question,
        "answer": answer,
        "deck": deck_name
    }
    # Añade la nueva tarjeta a la lista de tarjetas del mazo correspondiente
    decks[deck_name].append(new_card)
    return new_card

def edit_card_model(card, question, answer):
    """
    Edita una tarjeta existente.

    Parameters:
        card (dict): Tarjeta a editar.
        question (str): Nueva pregunta (opcional).
        answer (str): Nueva respuesta (opcional).

    Returns:
        None
    """
    if question:
        card['question'] = question
    if answer:
        card['answer'] = answer

def delete_card_model(decks, deck_name, card_index):
    """
    Elimina una tarjeta de un mazo.

    Parameters:
        decks (dict): Diccionario de mazos existentes.
        deck_name (str): Nombre del mazo.
        card_index (int): Índice de la tarjeta a eliminar.

    Returns:
        None
    """
    # Elimina la tarjeta en la posición 'card_index' de la lista de tarjetas del mazo
    decks[deck_name].pop(card_index)