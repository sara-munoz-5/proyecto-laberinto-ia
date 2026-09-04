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


def identificar_nodos_decision(lista_adyacencia, inicio, meta):
    """Devuelve las celdas que delimitan corredores del laberinto."""
    return {
        nodo
        for nodo, vecinos in lista_adyacencia.items()
        if len(vecinos) != 2 or nodo in (inicio, meta)
    }


def construir_macro_grafo(lista_adyacencia, inicio, meta):
    """Construye aristas que representan corredores completos.

    Cada arista conserva el corredor recorrido para poder reconstruir luego
    la ruta celda por celda. Su formato es (destino, costo, corredor).
    """
    nodos_decision = identificar_nodos_decision(lista_adyacencia, inicio, meta)
    macro_grafo = {nodo: [] for nodo in nodos_decision}

    for nodo_origen in nodos_decision:
        for vecino_inicial, peso in lista_adyacencia[nodo_origen]:
            corredor = [nodo_origen, vecino_inicial]
            nodo_anterior = nodo_origen
            nodo_actual = vecino_inicial
            costo = peso

            while nodo_actual not in nodos_decision:
                siguientes = [
                    (vecino, peso_vecino)
                    for vecino, peso_vecino in lista_adyacencia[nodo_actual]
                    if vecino != nodo_anterior
                ]
                nodo_anterior, nodo_actual = nodo_actual, siguientes[0][0]
                costo += siguientes[0][1]
                corredor.append(nodo_actual)

            macro_grafo[nodo_origen].append(
                (nodo_actual, costo, corredor)
            )

    return macro_grafo


def expandir_ruta_macro(ruta_macro, macro_grafo):
    """Expande una ruta de nodos de decisión a todas sus celdas."""
    if not ruta_macro:
        return None

    ruta_completa = [ruta_macro[0]]
    for origen, destino in zip(ruta_macro, ruta_macro[1:]):
        arista = next(
            (arista for arista in macro_grafo[origen] if arista[0] == destino),
            None,
        )
        if arista is None:
            raise ValueError("La ruta macro contiene una conexión inexistente.")
        ruta_completa.extend(arista[2][1:])

    return ruta_completa