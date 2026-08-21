def es_transitable(valor):
    return valor in (0, 2, 3)


def matriz_a_grafo(laberinto):
    grafo = {}

    filas = len(laberinto)
    columnas = len(laberinto[0])

    movimientos = [
        (-1, 0),  # arriba
        (1, 0),   # abajo
        (0, -1),  # izquierda
        (0, 1)    # derecha
    ]

    for fila in range(filas):
        for columna in range(columnas):

            if es_transitable(laberinto[fila][columna]):
                nodo_actual = (fila, columna)
                grafo[nodo_actual] = []

                for cambio_fila, cambio_columna in movimientos:
                    vecino_fila = fila + cambio_fila
                    vecino_columna = columna + cambio_columna

                    dentro_del_laberinto = (
                        0 <= vecino_fila < filas
                        and 0 <= vecino_columna < columnas
                    )

                    if dentro_del_laberinto:
                        valor_vecino = laberinto[vecino_fila][vecino_columna]

                        if es_transitable(valor_vecino):
                            vecino = (vecino_fila, vecino_columna)
                            grafo[nodo_actual].append((vecino, 1))

    return grafo