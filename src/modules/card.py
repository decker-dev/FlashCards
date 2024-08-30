def create_card(question, answer):
    """
    Create a new card with a question and answer.

    Parameters:
    question (str): The question for the flashcard.
    answer (str): The answer for the flashcard.

    Returns:
    dict: A dictionary representing the created card.
    """
    pass

def edit_card(card_id, new_question, new_answer):
    """
    Edit an existing card with a new question and answer.

    Parameters:
    card_id (int): The ID of the card to edit.
    new_question (str): The new question for the card.
    new_answer (str): The new answer for the card.

    Returns:
    bool: True if the card was successfully edited, False otherwise.
    """
    pass

def delete_card(card_id):
    """
    Delete a card by its ID.

    Parameters:
    card_id (int): The ID of the card to delete.

    Returns:
    bool: True if the card was successfully deleted, False otherwise.
    """
    pass

def get_card_by_id(card_id):
    """
    Get details of a specific card by its ID.

    Parameters:
    card_id (int): The ID of the card to retrieve.

    Returns:
    dict: A dictionary representing the card, or None if not found.
    """
    pass

def list_all_cards():
    """
    List all available cards.

    Returns:
    list: A list of dictionaries, each representing a card.
    """
    pass
