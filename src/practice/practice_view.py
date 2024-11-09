from datetime import timedelta

from src.utils.ui_utils import select_option, clear_screen


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
    user_choice = select_option("\n¿Cómo te fue con esta tarjeta?", options)
    intervals = {
        '1': ('Perfecto', timedelta(days=7).total_seconds()),
        '2': ('Bien', timedelta(days=1).total_seconds()),
        '3': ('Mal', timedelta(minutes=10).total_seconds()),
        '4': ('Terriblemente_Nada', 0.0)
    }
    return intervals[user_choice]

def show_results_view(results, total_cards):
    """
    Muestra los resultados de la práctica al usuario.

    Parameters:
        results (dict): Resultados de la práctica actual.
        total_cards (int): Número total de tarjetas practicadas.

    Returns:
        None
    """
    clear_screen()
    print("\n=== Resultados de la Práctica ===")
    print("\nClasificación según el rating:")
    for rating, count in results.items():
        percentage = (count / total_cards) * 100 if total_cards > 0 else 0
        print(f"{rating}: {count} Tarjetas ({percentage:.1f}%)")
        next_review = {
            'Perfecto': "1 semana",
            'Bien': "1 día",
            'Mal': "10 minutos",
            'Terriblemente_Nada': "Inmediato"
        }
        print(f"  → Próxima Revisión en: {next_review[rating]}")
    input("\nPresione Enter para continuar...")