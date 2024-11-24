from datetime import timedelta

from utils.ui_utils import select_option, clear_screen


def get_rating_view():
    """
    Solicita al usuario que califique su desempeño en una tarjeta.

    Parameters:
        None

    Returns:
        tuple: (rating, interval)
    """
    options = {
        '1': "Perfecto - Respuesta inmediata y correcta",
        '2': "Bien - Dudó pero recordó",
        '3': "Mal - Le costó recordar",
        '4': "Terriblemente_Nada - No recordó en absoluto"
    }
    # Muestra las opciones de calificación y obtiene la elección del usuario
    user_choice = select_option("\n¿Cómo te fue con esta tarjeta?", options)
    # Define los intervalos hasta la próxima revisión según la calificación
    intervals = {
        '1': ('Perfecto', timedelta(days=7).total_seconds()),
        '2': ('Bien', timedelta(days=1).total_seconds()),
        '3': ('Mal', timedelta(minutes=10).total_seconds()),
        '4': ('Terriblemente_Nada', 0.0)
    }
    return intervals[user_choice]

def show_results_view(results, total_cards, is_random=False):
    """
    Muestra los resultados de la práctica al usuario.

    Parameters:
        is_random: (bool): Indica si la práctica fue aleatoria.
        results (dict): Resultados de la práctica actual.
        total_cards (int): Número total de tarjetas practicadas.

    Returns:
        None
    """
    clear_screen()
    print("\n=== Resultados de la Práctica ===")
    print("\nClasificación según el rating:")
    for rating, count in results.items():
        # Calcula el porcentaje de tarjetas por rating
        percentage = (count / total_cards) * 100 if total_cards > 0 else 0
        print(f"{rating}: {count} Tarjetas ({percentage:.1f}%)")
        # Muestra el tiempo hasta la próxima revisión según el rating
        next_review = {
            'Perfecto': "1 semana",
            'Bien': "1 día",
            'Mal': "10 minutos",
            'Terriblemente_Nada': "Inmediato"
        }
        if not is_random:
            print(f"  → Próxima Revisión en: {next_review[rating]}")
    input("\nPresione Enter para continuar...")