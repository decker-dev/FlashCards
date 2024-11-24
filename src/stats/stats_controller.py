from stats.stats_view import show_ranking_view, show_user_stats_view


def show_ranking_controller(scores):
    """
    Controlador para mostrar el ranking global.

    Parameters:
        scores (dict): Puntajes y estadísticas de los usuarios.

    Returns:
        None
    """
    show_ranking_view(scores)

def show_user_stats_controller(scores, user):
    """
    Controlador para mostrar las estadísticas del usuario.

    Parameters:
        scores (dict): Puntajes y estadísticas de los usuarios.
        user (str): Nombre del usuario actual.

    Returns:
        None
    """
    show_user_stats_view(scores, user)