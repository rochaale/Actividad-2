def inicializar_estadisticas(rondas):
    # Creo el diccionario donde voy a guardar las estadísticas de cada participante
    estadisticas = {}

    # Recorro todas las rondas
    for ronda in rondas:
        # Recorro los participantes de cada ronda
        for participante in ronda['scores']:
            # Si el participante todavía no está en el diccionario, lo agrego
            if participante not in estadisticas:
                estadisticas[participante] = {
                    'total': 0,           # Puntaje total acumulado
                    'rondas_ganadas': 0,  # Cantidad de rondas ganadas
                    'mejor_ronda': 0,     # Mejor puntaje en una ronda
                    'puntajes': []        # Lista con los puntajes de cada ronda
                }
    return estadisticas


def procesar_ronda(ronda, estadisticas):
    # Esta función procesa una ronda completa
    puntajes_ronda = {}

    # Recorro cada participante y los puntajes de los jueces
    for participante, jueces in ronda['scores'].items():
        # Sumo los puntajes de los jueces
        puntaje = sum(jueces.values())
        puntajes_ronda[participante] = puntaje

        # Actualizo estadísticas
        estadisticas[participante]['total'] += puntaje
        estadisticas[participante]['puntajes'].append(puntaje)

        # Veo si es su mejor ronda
        if puntaje > estadisticas[participante]['mejor_ronda']:
            estadisticas[participante]['mejor_ronda'] = puntaje

    # Busco el ganador de la ronda
    ganador = max(puntajes_ronda, key=puntajes_ronda.get)

    # Le sumo una ronda ganada
    estadisticas[ganador]['rondas_ganadas'] += 1

    return ganador, puntajes_ronda


def ranking_actual(estadisticas):
    # Ordeno los participantes por puntaje total de mayor a menor
    return sorted(estadisticas.items(), key=lambda x: x[1]['total'], reverse=True)


def imprimir_ranking(ranking):
    # Imprime la tabla de posiciones
    print("Tabla de posiciones:")
    for nombre, datos in ranking:
        print(f"{nombre}: {datos['total']} pts")


def tabla_final(estadisticas):
    # Ordeno el ranking final
    ranking = sorted(estadisticas.items(), key=lambda x: x[1]['total'], reverse=True)

    print("\nTabla de posiciones final:")
    print("Cocinero       Puntaje   Rondas ganadas   Mejor ronda   Promedio")
    print("--------------------------------------------------------------")

    # Recorro el ranking
    for nombre, datos in ranking:
        # Calculo el promedio
        promedio = datos['total'] / len(datos['puntajes'])

        # Imprimo todo formateado
        print(f"{nombre:12} {datos['total']:8} {datos['rondas_ganadas']:15} {datos['mejor_ronda']:12} {round(promedio,1):10}")