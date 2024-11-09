def create_card(decks, deck_name, question, answer):
    """
    Añade una nueva tarjeta a un mazo.
    """
    new_card = {
        "id": f"{deck_name}_{len(decks[deck_name]) + 1}",
        "question": question,
        "answer": answer,
        "deck": deck_name
    }
    decks[deck_name].append(new_card)
    return new_card

def edit_card(card, question, answer):
    """
    Edita una tarjeta existente.
    """
    if question:
        card['question'] = question
    if answer:
        card['answer'] = answer

def delete_card(decks, deck_name, card_index):
    """
    Elimina una tarjeta de un mazo.
    """
    decks[deck_name].pop(card_index)