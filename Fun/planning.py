import pandas as pd

def add_activity(df, activity, start_time, end_time, day):
    """
    Ajoute une activité au DataFrame d'agenda.
    
    Args:
    df (DataFrame): Le DataFrame d'agenda actuel.
    activity (str): Nom de l'activité.
    start_time (str): Heure de début de l'activité au format HH:MM.
    end_time (str): Heure de fin de l'activité au format HH:MM.
    day (str): Jour de l'activité, ex. "Lundi".
    
    Returns:
    DataFrame: Le DataFrame d'agenda mis à jour.
    """
    df = df.append({
        "Jour": day,
        "Heure de début": start_time,
        "Heure de fin": end_time,
        "Activité": activity
    }, ignore_index=True)
    return df

def print_agenda(df):
    """
    Affiche le DataFrame d'agenda.
    
    Args:
    df (DataFrame): Le DataFrame d'agenda.
    """
    print(df)

if __name__ == "__main__":
    # Créez un DataFrame vide pour stocker les activités
    agenda = pd.DataFrame(columns=["Jour", "Heure de début", "Heure de fin", "Activité"])

    # Ajoutez une activité à l'agenda
    agenda = add_activity(agenda, "Cours de Python", "09:00", "10:00", "Lundi")

    # Affichez l'agenda
    print_agenda(agenda)