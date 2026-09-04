"""
pytest tests/test_algoritmos.py -v

"""
import sys
import os


sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from grafo import Grafo
from lector_laberinto import leer_laberinto, encontrar_inicio_y_meta, validar_laberinto
from transformacion_grafo import (
    matriz_a_grafo,
    construir_macro_grafo,
    expandir_ruta_macro,
)


# ---------- Fixtures / datos de prueba ----------

def grafo_con_ciclo():
    """
    Grafo pequeño con un ciclo, para verificar que los algoritmos
    no entren en bucle infinito:
    """
    lista_adyacencia = {
        "A": [("B", 1), ("C", 1)],
        "B": [("A", 1), ("D", 1)],
        "C": [("A", 1), ("D", 1)],
        "D": [("B", 1), ("C", 1), ("E", 1)],
        "E": [("D", 1)],
    }
    return Grafo(lista_adyacencia)


def grafo_desconectado():
    """Grafo donde la meta es inalcanzable desde el inicio."""
    lista_adyacencia = {
        "A": [("B", 1)],
        "B": [("A", 1)],
        "X": [("Y", 1)],
        "Y": [("X", 1)],
    }
    return Grafo(lista_adyacencia)


def cargar_grafo_real():
    """Carga el laberinto real del proyecto y lo convierte en grafo."""
    ruta = os.path.join(os.path.dirname(__file__), "..", "data", "laberinto.txt")
    _, laberinto = leer_laberinto(ruta)
    validar_laberinto(laberinto)
    inicio, meta = encontrar_inicio_y_meta(laberinto)
    grafo = Grafo(matriz_a_grafo(laberinto))
    return grafo, inicio, meta


# ---------- Pruebas: grafo con ciclo ----------

def test_dfs_encuentra_ruta_en_grafo_con_ciclo():
    g = grafo_con_ciclo()
    camino, _ = g.primero_profundidad("A", "E")
    assert camino is not None
    assert camino[0] == "A"
    assert camino[-1] == "E"


def test_bfs_encuentra_ruta_en_grafo_con_ciclo():
    g = grafo_con_ciclo()
    camino, _ = g.primero_anchura("A", "E")
    assert camino is not None
    assert camino[0] == "A"
    assert camino[-1] == "E"


def test_bfs_devuelve_la_ruta_minima():
    # En este grafo, la ruta mínima de A a E es A-B-D-E o A-C-D-E (3 aristas, 4 nodos)
    g = grafo_con_ciclo()
    camino, _ = g.primero_anchura("A", "E")
    assert len(camino) == 4


def test_a_estrella_encuentra_ruta_en_grafo_con_ciclo():
    """
    La heurística h(n) del proyecto asume nodos tipo (fila, columna),
    ya que se diseñó específicamente para el laberinto (usa n[0], n[1]).
    Por eso esta prueba usa un grafo con nodos-coordenada, no letras,
    a diferencia de las pruebas de DFS/BFS que sí funcionan con cualquier
    tipo de nodo hashable.

    """
    lista_adyacencia = {
        (0, 0): [((0, 1), 1), ((1, 0), 1)],
        (0, 1): [((0, 0), 1), ((1, 1), 1)],
        (1, 0): [((0, 0), 1), ((1, 1), 1)],
        (1, 1): [((0, 1), 1), ((1, 0), 1), ((1, 2), 1)],
        (1, 2): [((1, 1), 1)],
    }
    g = Grafo(lista_adyacencia)
    camino, _ = g.a_estrella((0, 0), (1, 2))
    assert camino is not None
    assert camino[0] == (0, 0)
    assert camino[-1] == (1, 2)


# ---------- Pruebas: casos límite ----------

def test_inicio_igual_a_meta_dfs():
    g = grafo_con_ciclo()
    camino, _ = g.primero_profundidad("A", "A")
    assert camino == ["A"]


def test_inicio_igual_a_meta_bfs():
    g = grafo_con_ciclo()
    camino, _ = g.primero_anchura("A", "A")
    assert camino == ["A"]


def test_meta_inalcanzable_dfs():
    g = grafo_desconectado()
    camino, _ = g.primero_profundidad("A", "X")
    assert camino is None


def test_meta_inalcanzable_bfs():
    g = grafo_desconectado()
    camino, _ = g.primero_anchura("A", "X")
    assert camino is None


# ---------- Pruebas: laberinto real del proyecto ----------

def test_dfs_en_laberinto_real_llega_de_salida_a_meta():
    grafo, inicio, meta = cargar_grafo_real()
    camino, _ = grafo.primero_profundidad(inicio, meta)
    assert camino is not None
    assert camino[0] == inicio
    assert camino[-1] == meta


def test_bfs_en_laberinto_real_llega_de_salida_a_meta():
    grafo, inicio, meta = cargar_grafo_real()
    camino, _ = grafo.primero_anchura(inicio, meta)
    assert camino is not None
    assert camino[0] == inicio
    assert camino[-1] == meta


def test_a_estrella_en_laberinto_real_llega_de_salida_a_meta():
    grafo, inicio, meta = cargar_grafo_real()
    camino, _ = grafo.a_estrella(inicio, meta)
    assert camino is not None
    assert camino[0] == inicio
    assert camino[-1] == meta


def test_a_estrella_encuentra_ruta_igual_de_corta_que_bfs():
    """
    Con costos unitarios y una heurística admisible (Manhattan),
    A* debe encontrar una ruta de la misma longitud óptima que BFS.
    """
    grafo, inicio, meta = cargar_grafo_real()
    camino_bfs, _ = grafo.primero_anchura(inicio, meta)
    camino_a_estrella, _ = grafo.a_estrella(inicio, meta)
    assert len(camino_bfs) == len(camino_a_estrella)


def test_dfs_no_garantiza_ruta_minima_en_laberinto_real():
    """
    Verificación de la propiedad teórica: DFS puede (y en este laberinto,
    de hecho lo hace) encontrar una ruta más larga que la óptima.
    """
    grafo, inicio, meta = cargar_grafo_real()
    camino_dfs, _ = grafo.primero_profundidad(inicio, meta)
    camino_bfs, _ = grafo.primero_anchura(inicio, meta)
    assert len(camino_dfs) >= len(camino_bfs)


def test_macro_grafo_expande_la_ruta_completa():
    grafo, inicio, meta = cargar_grafo_real()
    macro_grafo = construir_macro_grafo(grafo.lista_adyacencia, inicio, meta)

    ruta_macro, _ = grafo.astar_macro(inicio, meta, macro_grafo)
    ruta_completa = expandir_ruta_macro(ruta_macro, macro_grafo)

    assert ruta_macro is not None
    assert ruta_completa[0] == inicio
    assert ruta_completa[-1] == meta
    assert len(ruta_completa) >= len(ruta_macro)


def test_astar_macro_conserva_la_longitud_optima_de_bfs():
    grafo, inicio, meta = cargar_grafo_real()
    macro_grafo = construir_macro_grafo(grafo.lista_adyacencia, inicio, meta)

    ruta_bfs, _ = grafo.primero_anchura(inicio, meta)
    ruta_macro, _ = grafo.astar_macro(inicio, meta, macro_grafo)
    ruta_completa = expandir_ruta_macro(ruta_macro, macro_grafo)

    assert len(ruta_completa) == len(ruta_bfs)