from functions import generate_structure
from functions.function2 import most_scorer
from functions.function3 import most_influential
from functions.function4 import average_team_goals

names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA,
CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia,
Francsica', FEDERICO, Fernanda, GONZALO, Nancy """

goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0, 11]
goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2, 3, 0, 0]
assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1, 0]

info_players = generate_structure (names, goals, goals_avoided, assists)

# function2
scorer = most_scorer(info_players)
print (f'Mas goleador/a: ', scorer[0], ' con ', scorer[1], ' goles.')

# function3
influential = most_influential(info_players)
print (f'Jugador/a mas influyente: ', influential[0], ' con ', influential[1], ' puntos.')

# function4
average_goals_team = average_team_goals(goals)
print (f'Promedio de goles por partido del equipo: ', average_goals_team)

# function5
average_goals_scorer = scorer[1] / 25
print (f'Promedio de goles por partido del mas goleador/a: ', average_goals_scorer)
