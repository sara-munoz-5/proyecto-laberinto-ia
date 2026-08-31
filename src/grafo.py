from collections import deque
import heapq


class Grafo:

    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia
        self.meta = None

    def obtener_vecinos(self, v):
        return self.lista_adyacencia[v]

    # funcion heuristica
    def h(self, n):
        return abs(n[0] - self.meta[0]) + abs(n[1] - self.meta[1]) # puede retornar una lista con el calculo de la heuristica para cada estado

    def primero_profundidad(self, nodo_inicio, nodo_final):
        pila = [(nodo_inicio, [nodo_inicio])]
        visitados = set()

        while pila:
            nodo_actual, camino = pila.pop()

            if nodo_actual in visitados:
                continue

            visitados.add(nodo_actual)

            if nodo_actual == nodo_final:
                return camino

            vecinos = self.obtener_vecinos(nodo_actual)
            for vecino, _ in reversed(vecinos):
                if vecino not in visitados:
                    pila.append((vecino, camino + [vecino]))

        return None

    def primero_anchura(self, nodo_inicio, nodo_final):
        cola = deque([(nodo_inicio, [nodo_inicio])])
        visitados = {nodo_inicio}

        while cola:
            nodo_actual, camino = cola.popleft()

            if nodo_actual == nodo_final:
                return camino

            for vecino, _ in self.obtener_vecinos(nodo_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, camino + [vecino]))

        return None

    def a_estrella(self, nodo_inicio, nodo_final):
        self.meta = nodo_final

        contador = 0
        cola_prioridad = [(self.h(nodo_inicio), contador, nodo_inicio, [nodo_inicio], 0)]
        visitados = set()

        while cola_prioridad:
            f_actual, _, nodo_actual, camino, g_actual = heapq.heappop(cola_prioridad)

            if nodo_actual == nodo_final:
                return camino

            if nodo_actual in visitados:
                continue
            visitados.add(nodo_actual)

            for vecino, peso in self.obtener_vecinos(nodo_actual):
                if vecino not in visitados:
                    g_nuevo = g_actual + peso
                    f_nuevo = g_nuevo + self.h(vecino)
                    contador += 1
                    heapq.heappush(
                        cola_prioridad,
                        (f_nuevo, contador, vecino, camino + [vecino], g_nuevo)
                    )

        return None
