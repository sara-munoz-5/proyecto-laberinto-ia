import time

from lector_laberinto import (
    leer_laberinto,
    encontrar_inicio_y_meta,
    validar_laberinto
)
from transformacion_grafo import matriz_a_grafo
from grafo import Grafo


RUTA_LABERINTO = "data/laberinto.txt"


def ejecutar_algoritmo(nombre, funcion, inicio, meta):
    """Ejecuta un algoritmo de búsqueda, mide su tiempo y reporta resultados."""
    t0 = time.perf_counter()
    camino = funcion(inicio, meta)
    t1 = time.perf_counter()

    tiempo_ms = (t1 - t0) * 1000
    longitud = len(camino) if camino else 0

    print(f"\n--- {nombre} ---")
    if camino:
        print("Camino encontrado: SI")
        print(f"Longitud del camino: {longitud} nodos")
    else:
        print("Camino encontrado: NO (o algoritmo aún no implementado)")
    print(f"Tiempo de ejecución: {tiempo_ms:.3f} ms")

    return {
        "nombre": nombre,
        "encontrado": camino is not None,
        "longitud": longitud,
        "tiempo_ms": tiempo_ms,
        "camino": camino,
    }


def imprimir_tabla_comparativa(resultados):
    print("\n" + "=" * 55)
    print("TABLA COMPARATIVA DE ALGORITMOS")
    print("=" * 55)
    print(f"{'Algoritmo':<20}{'Encontró':<12}{'Longitud':<12}{'Tiempo (ms)':<12}")
    print("-" * 55)
    for r in resultados:
        encontrado = "Sí" if r["encontrado"] else "No"
        print(f"{r['nombre']:<20}{encontrado:<12}{r['longitud']:<12}{r['tiempo_ms']:<12.3f}")
    print("=" * 55)


def probar_casos_limite(grafo):
    
    print("\n" + "=" * 55)
    print("PRUEBAS DE CASOS LÍMITE")
    print("=" * 55)

    algoritmos = {
        "DFS": grafo.primero_profundidad,
        "BFS": grafo.primero_anchura,
    }

    for nombre, funcion in algoritmos.items():
        nodo_cualquiera = next(iter(grafo.lista_adyacencia))

        # Caso 1: inicio == meta
        resultado = funcion(nodo_cualquiera, nodo_cualquiera)
        ok = resultado == [nodo_cualquiera]
        print(f"[{nombre}] inicio == meta -> {'OK' if ok else 'FALLÓ'} (resultado: {resultado})")

        # Caso 2: meta inexistente en el grafo (nodo fuera del laberinto)
        try:
            resultado = funcion(nodo_cualquiera, (-1, -1))
            print(f"[{nombre}] meta inexistente -> lanzó excepción esperada: NO (revisar manejo de errores)")
        except KeyError:
            print(f"[{nombre}] meta inexistente -> lanzó KeyError (revisar si se debe manejar más elegante)")


def main():
    # 1. Carga y validación (Integrante 1)
    meta_declarada, laberinto = leer_laberinto(RUTA_LABERINTO)
    filas, columnas = validar_laberinto(laberinto)
    inicio, meta = encontrar_inicio_y_meta(laberinto)

    print(f"Laberinto cargado: {filas}x{columnas}")
    print(f"Meta declarada en encabezado: {meta_declarada}")
    print(f"Inicio: {inicio} | Meta: {meta}")

    # 2. Transformación a grafo (Integrante 1)
    lista_adyacencia = matriz_a_grafo(laberinto)
    grafo = Grafo(lista_adyacencia)
    print(f"Nodos transitables: {len(grafo.lista_adyacencia)}")

    # 3. Ejecutar los tres algoritmos y recolectar resultados
    resultados = []
    resultados.append(ejecutar_algoritmo("DFS", grafo.primero_profundidad, inicio, meta))
    resultados.append(ejecutar_algoritmo("BFS", grafo.primero_anchura, inicio, meta))
    resultados.append(ejecutar_algoritmo("A*", grafo.a_estrella, inicio, meta))

    # 5. Tabla comparativa final
    imprimir_tabla_comparativa(resultados)

    # 6. Imprimir la ruta encontrada por BFS
    for r in resultados:
        if r["encontrado"] and r["nombre"] == "BFS":
            print(f"\nRuta completa encontrada por BFS:\n{r['camino']}")

    # 7. Pruebas de casos límite (tu aporte independiente como Integrante 4)
    probar_casos_limite(grafo)


if __name__ == "__main__":
    main()