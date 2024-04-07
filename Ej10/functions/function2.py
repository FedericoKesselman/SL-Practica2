def most_scorer (info_players):
    """
    Busca el jugador con mas goles.
    -Argumentos: Lista de tuplas con info de los jugadores.
    -Retorna: Tupla del mas goleador (nombre_jugador, cantidad_goles).
    """
    player = max(info_players, key=lambda elem:elem[1])
    scorer = (player[0], player[1])

    return scorer
    

