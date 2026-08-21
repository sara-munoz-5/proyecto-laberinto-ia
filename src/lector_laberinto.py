import ast


def leer_laberinto(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    meta_declarada = ast.literal_eval(lineas[0].strip())

    laberinto = []

    for linea in lineas[1:]:
        fila = ast.literal_eval(linea.strip())
        laberinto.append(fila)

    return  meta_declarada, laberinto
def encontrar_inicio_y_meta(laberinto):
    inicio = None
    meta = None

    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[fila])):

            if laberinto[fila][columna] == 2:
                inicio = (fila, columna)

            elif laberinto[fila][columna] == 3:
                meta = (fila, columna)

    return inicio, meta
def validar_laberinto(laberinto):
    if not laberinto:
        raise ValueError("El laberinto está vacío.")

    cantidad_columnas = len(laberinto[0])

    for fila in laberinto:
        if len(fila) != cantidad_columnas:
            raise ValueError(
                "Error: las filas del laberinto no tienen la misma cantidad de columnas."
            )

    return len(laberinto), cantidad_columnas
def encontrar_inicio_y_meta(laberinto):
    inicio = None
    meta = None

    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[fila])):

            if laberinto[fila][columna] == 2:
                if inicio is not None:
                    raise ValueError("El laberinto tiene más de una salida.")

                inicio = (fila, columna)

            elif laberinto[fila][columna] == 3:
                if meta is not None:
                    raise ValueError("El laberinto tiene más de una meta.")

                meta = (fila, columna)

    if inicio is None:
        raise ValueError("El laberinto no tiene salida, marcada con 2.")

    if meta is None:
        raise ValueError("El laberinto no tiene meta, marcada con 3.")

    return inicio, meta