def most_influential (info_players):
    """
    Busca el jugador mas influyente del equipo. Promedio ponderado. 
        Valores: 1.5 para goles, 1.25 para goles evitados, 1 para aistencias.
    -Argumentos: Lista de tuplas con info de los jugadores.
    -Retorna: Tupla del mas influyente (nombre_jugador, valor).
    """
    max_points = -1

    for player in info_players:
        points = (player[1]*1.5) + (player[2]*1.25) + (player[3]*1)

        if (points > max_points):
            max_points = points
            influential = (player[0], points)

    return influential
