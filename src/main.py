from lector_laberinto import (
    leer_laberinto,
    encontrar_inicio_y_meta,
    validar_laberinto
)

from transformacion_grafo import matriz_a_grafo


RUTA_LABERINTO = "data/laberinto.txt"

meta_declarada, laberinto = leer_laberinto(RUTA_LABERINTO)

filas, columnas = validar_laberinto(laberinto)
inicio, meta = encontrar_inicio_y_meta(laberinto)

grafo = matriz_a_grafo(laberinto)

print("Cantidad de nodos transitables:", len(grafo))
print("Vecinos de la salida:", grafo[inicio])
print("Meta declarada en el archivo:", meta_declarada)
print("Dimensiones reales:", filas, "x", columnas)
print("Salida:", inicio)
print("Meta:", meta)