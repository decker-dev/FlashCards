from src.stats.stats_view import view_show_ranking, view_show_user_stats


def show_ranking(scores):
    """
    Controlador para mostrar el ranking global.
    """
    view_show_ranking(scores)

def show_user_stats(scores, user):
    """
    Controlador para mostrar las estadísticas del usuario.
    """
    view_show_user_stats(scores, user)