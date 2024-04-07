def generate_structure (names, goals, goals_avoided, assists):
    """
    Genera una estructura que reune nombre, goles, goles evitados y asistencias de jugadores.
    -Argumentos: String con nombre separados por coma, listas de goles, goles evitados y asistencias.
    -Retorna: Lista de tuplas con la informacion reunida.
    """
    special_characters = (' ', "'", '\n')
    for character in special_characters:
        if (character in names):
            names = names.replace (character, '') 

    names = names.split(',')
    
    info_players = []
    for i in range(len(names)):
        info_players.append((names[i].lower(), goals[i], goals_avoided[i], assists[i]))

    print ('Estructura creada correctamente.')
    return info_players


    


