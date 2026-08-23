from collections import deque


class Grafo:

    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia

    def obtener_vecinos(self, v):
        return self.lista_adyacencia[v]

    # funcion heuristica
    def h(self, n):
        #inserte su codigo aqui
        return H[n] # puede retornar una lista con el calculo de la heuristica para cada estado

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
       #inserte si codigo aqui
        return None
