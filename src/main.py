# Importa el módulo estándar utilizado para medir tiempos de ejecución.
import time

# Importa las funciones que leen, validan y localizan los puntos del laberinto.
from lector_laberinto import leer_laberinto, encontrar_inicio_y_meta, validar_laberinto
# Importa la función que convierte la matriz en una lista de adyacencia.
from transformacion_grafo import matriz_a_grafo
# Importa la clase que implementa los algoritmos DFS, BFS y A*.
from grafo import Grafo


# Define el archivo de laberinto que utilizará el programa.
RUTA_LABERINTO = "data/laberinto.txt"


def ejecutar_algoritmo(nombre, funcion, inicio, meta):
    """Ejecuta un algoritmo, mide su tiempo y organiza sus resultados."""
    # Guarda el instante justo antes de iniciar la búsqueda.
    tiempo_inicial = time.perf_counter()
    # Ejecuta el algoritmo y recibe la ruta y el número de nodos visitados.
    camino, nodos_visitados = funcion(inicio, meta)
    # Guarda el instante en el que termina la búsqueda.
    tiempo_final = time.perf_counter()

    # Calcula el tiempo transcurrido y lo convierte a milisegundos.
    tiempo_ms = (tiempo_final - tiempo_inicial) * 1000
    # Calcula la cantidad de nodos de la ruta, o cero si no existe una ruta.
    longitud = len(camino) if camino else 0

    # Muestra en pantalla los resultados individuales del algoritmo.
    print(f"\n--- {nombre} ---")
    print(f"Camino encontrado: {'SÍ' if camino else 'NO'}")
    print(f"Longitud del camino: {longitud} nodos")
    print(f"Nodos visitados: {nodos_visitados}")
    print(f"Tiempo de ejecución: {tiempo_ms:.3f} ms")

    # Agrupa los datos para poder compararlos con los otros algoritmos.
    return {
        "nombre": nombre,
        "encontrado": camino is not None,
        "longitud": longitud,
        "visitados": nodos_visitados,
        "tiempo_ms": tiempo_ms,
        "camino": camino,
    }


def imprimir_tabla_comparativa(resultados):
    """Imprime una tabla con los resultados de todos los algoritmos."""
    # Imprime el título y los encabezados de la tabla.
    print("\n" + "=" * 73)
    print("TABLA COMPARATIVA DE ALGORITMOS")
    print("=" * 73)
    print(
        f"{'Algoritmo':<15}{'Encontró':<12}{'Longitud':<12}"
        f"{'Visitados':<14}{'Tiempo (ms)':<15}"
    )
    print("-" * 73)

    # Recorre los resultados e imprime una fila para cada algoritmo.
    for resultado in resultados:
        # Convierte el valor booleano en una respuesta legible.
        encontrado = "Sí" if resultado["encontrado"] else "No"
        # Alinea los datos en las columnas correspondientes.
        print(
            f"{resultado['nombre']:<15}{encontrado:<12}"
            f"{resultado['longitud']:<12}{resultado['visitados']:<14}"
            f"{resultado['tiempo_ms']:<15.3f}"
        )

    # Cierra visualmente la tabla comparativa.
    print("=" * 73)


def probar_casos_limite(grafo):
    """Comprueba cómo responden DFS y BFS ante situaciones especiales."""
    # Imprime el encabezado de las pruebas manuales.
    print("\n" + "=" * 55)
    print("PRUEBAS DE CASOS LÍMITE")
    print("=" * 55)

    # Relaciona el nombre de cada algoritmo con su función de búsqueda.
    algoritmos = {
        "DFS": grafo.primero_profundidad,
        "BFS": grafo.primero_anchura,
    }

    # Selecciona un nodo válido del grafo para usarlo en las pruebas.
    nodo_cualquiera = next(iter(grafo.lista_adyacencia))

    # Ejecuta las mismas pruebas para DFS y BFS.
    for nombre, funcion in algoritmos.items():
        # Caso 1: el nodo de inicio también es la meta.
        camino, _ = funcion(nodo_cualquiera, nodo_cualquiera)
        # La respuesta correcta debe contener solamente el nodo inicial.
        correcto = camino == [nodo_cualquiera]
        print(
            f"[{nombre}] inicio == meta -> "
            f"{'OK' if correcto else 'FALLÓ'} (resultado: {camino})"
        )

        # Caso 2: se utiliza como meta una coordenada inexistente.
        camino, _ = funcion(nodo_cualquiera, (-1, -1))
        # El resultado correcto es no encontrar ningún camino.
        correcto = camino is None
        print(
            f"[{nombre}] meta inexistente -> "
            f"{'OK (no se encontró camino)' if correcto else 'FALLÓ'}"
        )


def main():
    """Coordina la carga, búsqueda y presentación de los resultados."""
    # 1. Lee del archivo la meta declarada y la matriz del laberinto.
    meta_declarada, laberinto = leer_laberinto(RUTA_LABERINTO)
    # 2. Valida la forma de la matriz y obtiene sus dimensiones.
    filas, columnas = validar_laberinto(laberinto)
    # 3. Localiza las celdas marcadas con 2 (inicio) y 3 (meta).
    inicio, meta = encontrar_inicio_y_meta(laberinto)

    # Muestra la información general del laberinto cargado.
    print(f"Laberinto cargado: {filas}x{columnas}")
    print(f"Meta declarada en el archivo: {meta_declarada}")
    print(f"Inicio: {inicio} | Meta: {meta}")

    # 4. Convierte las celdas transitables de la matriz en un grafo.
    lista_adyacencia = matriz_a_grafo(laberinto)
    # 5. Crea el objeto que permite ejecutar los algoritmos de búsqueda.
    grafo = Grafo(lista_adyacencia)
    # Informa cuántas celdas pueden ser recorridas.
    print(f"Nodos transitables: {len(lista_adyacencia)}")

    # 6. Ejecuta los tres algoritmos con el mismo inicio y la misma meta.
    resultados = [
        ejecutar_algoritmo("DFS", grafo.primero_profundidad, inicio, meta),
        ejecutar_algoritmo("BFS", grafo.primero_anchura, inicio, meta),
        ejecutar_algoritmo("A*", grafo.a_estrella, inicio, meta),
    ]

    # 7. Presenta en una sola tabla los resultados obtenidos.
    imprimir_tabla_comparativa(resultados)

    # 8. Busca el resultado de BFS dentro de la lista de resultados.
    resultado_bfs = next(r for r in resultados if r["nombre"] == "BFS")
    # Muestra la ruta completa solamente si BFS encontró una solución.
    if resultado_bfs["encontrado"]:
        print(f"\nRuta completa encontrada por BFS:\n{resultado_bfs['camino']}")

    # 9. Ejecuta al final las comprobaciones de casos especiales.
    probar_casos_limite(grafo)


# Evita que el programa se ejecute automáticamente al importar este módulo.
if __name__ == "__main__":
    # Inicia el programa cuando main.py se ejecuta directamente.
    main()
