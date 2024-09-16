from random import shuffle


def shuffle_copy(original_list):
    """
    Creates a shuffled copy of the original list.

    Args:
        original_list (list): The list to copy and shuffle.

    Returns:
        list: A new list that is a shuffled copy of the original list.
    """
    copied_list = original_list[:]

    shuffle(copied_list)

    return copied_list
