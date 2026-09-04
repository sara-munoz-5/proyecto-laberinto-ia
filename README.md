# Proyecto Laberinto IA

Un proyecto de Introducción a la Inteligencia Artificial que implementa algoritmos para la resolución de laberintos, incluyendo la transformación de matrices de laberintos en grafos para el análisis y búsqueda de caminos.

## Descripción del Proyecto

Este proyecto implementa herramientas para:
- **Leer y validar laberintos** representados como matrices desde archivos de texto
- **Identificar inicio y meta** dentro del laberinto
- **Transformar laberintos a grafos** para análisis de rutas
- **Comparar algoritmos de búsqueda**: DFS (Profundidad), BFS (Anchura) y A* (Heurístico)
- **Medir y comparar rendimiento** de los diferentes algoritmos
- **Validar casos límite** y comportamiento en escenarios especiales

### Representación del Laberinto
- `0`: Celda transitable (camino)
- `1`: Celda no transitable (pared)
- `2`: Posición de inicio (salida)
- `3`: Posición de meta (objetivo)

## Requisitos

- Python 3.7 o superior
- No hay dependencias externas (el proyecto solo utiliza la librería estándar de Python)

## Estructura del Proyecto

```
proyecto-laberinto-ia/
├── README.md                    # Este archivo
├── data/
│   └── laberinto.txt           # Archivo con la definición del laberinto
├── src/
│   ├── main.py                 # Script principal
│   ├── lector_laberinto.py     # Módulo para leer y validar laberintos
│   ├── grafo.py                # Estructura de datos del grafo
│   └── transformacion_grafo.py # Conversión de matriz a grafo
└── tests/
    └── test_algoritmos.py      # Pruebas unitarias
```

### Descripción de los módulos

- **main.py**: Punto de entrada del programa. Carga el laberinto, lo valida, lo convierte en grafo y ejecuta tres algoritmos de búsqueda (DFS, BFS, A*), midiendo su rendimiento y mostrando una tabla comparativa.

- **lector_laberinto.py**: Contiene funciones para:
  - `leer_laberinto()`: Lee el archivo del laberinto
  - `validar_laberinto()`: Valida que el laberinto sea una matriz válida
  - `encontrar_inicio_y_meta()`: Localiza las posiciones de inicio (2) y meta (3)

- **transformacion_grafo.py**: Convierte la matriz del laberinto en una estructura de grafo (diccionario de adyacencias).

- **grafo.py**: Define la clase `Grafo` con tres métodos de búsqueda:
  - `primero_profundidad(inicio, meta)`: Búsqueda por profundidad (DFS)
  - `primero_anchura(inicio, meta)`: Búsqueda por anchura (BFS)
  - `a_estrella(inicio, meta)`: Búsqueda con heurística A*
  - `h(nodo)`: Función heurística basada en distancia Manhattan

- **test_algoritmos.py**: Suite de pruebas para validar la funcionalidad del proyecto.

## Cómo Ejecutar el Proyecto

### 1. Requisitos Previos

Asegúrate de tener Python 3.7+ instalado:

```bash
python --version
```

### 2. Navegar al directorio del proyecto

```bash
cd "ruta/a/proyecto-laberinto-ia"
```

### 3. Ejecutar el programa principal

Desde el directorio raíz del proyecto:

```bash
python src/main.py
```

El programa mostrará:
- Información del laberinto cargado (dimensiones, inicio y meta)
- Resultados de tres algoritmos de búsqueda (DFS, BFS, A*)
- Tiempo de ejecución de cada algoritmo en milisegundos
- Tabla comparativa de rendimiento
- La ruta completa encontrada por BFS
- Pruebas de casos límite (mismo inicio y meta, meta inexistente, etc.)

**Ejemplo de salida:**
```
Laberinto cargado: 17x34
Meta declarada en encabezado: (17, 17)
Inicio: (0, 0) | Meta: (17, 17)
Nodos transitables: 450

--- DFS ---
Camino encontrado: SI
Longitud del camino: 67 nodos
Tiempo de ejecución: 12.345 ms

--- BFS ---
Camino encontrado: SI
Longitud del camino: 35 nodos
Tiempo de ejecución: 8.567 ms

--- A* ---
Camino encontrado: SI
Longitud del camino: 35 nodos
Tiempo de ejecución: 5.234 ms

=======================================================
TABLA COMPARATIVA DE ALGORITMOS
=======================================================
Algoritmo           Encontró     Longitud     Tiempo (ms)
-------------------------------------------------------
DFS                 Sí           67           12.345
BFS                 Sí           35           8.567
A*                  Sí           35           5.234
=======================================================

Ruta completa encontrada por BFS:
[(0, 0), (1, 0), (2, 0), (3, 1), (4, 1), ..., (17, 17)]

=======================================================
PRUEBAS DE CASOS LÍMITE
=======================================================
[DFS] inicio == meta -> OK (resultado: [(0, 0)])
[BFS] inicio == meta -> OK (resultado: [(0, 0)])
...
```

### 4. Ejecutar las pruebas

Para verificar que todo funciona correctamente:

```bash
python -m pytest tests/
```

O sin pytest (si lo prefieres):

```bash
python tests/test_algoritmos.py
```

## Algoritmos de Búsqueda Implementados

### 1. **DFS (Depth-First Search / Búsqueda por Profundidad)**
- Explora el laberinto siguiendo un camino hasta llegar a un callejón sin salida
- Utiliza una **pila** (stack) para almacenar nodos por explorar
- Encuentra **una solución**, pero no garantiza que sea la más corta
- Generalmente más rápido pero con rutas más largas

### 2. **BFS (Breadth-First Search / Búsqueda por Anchura)**
- Explora el laberinto nivel por nivel desde el inicio
- Utiliza una **cola** (queue) para explorar nodos uniformemente
- **Garantiza encontrar la solución más corta** (óptima)
- Más consumidor de memoria pero con rutas óptimas

### 3. **A* (A-Star Search)**
- Combina lo mejor de DFS y BFS usando una **función heurística**
- La heurística utilizada es la **distancia Manhattan**: `|x₁-x₂| + |y₁-y₂|`
- **Más eficiente que BFS** mientras mantiene optimalidad (bajo ciertas condiciones)
- Ideal para búsquedas en espacios grandes

## Comparación de Algoritmos

El programa ejecuta automáticamente los tres algoritmos y presenta una tabla comparativa mostrando:

| Métrica | DFS | BFS | A* |
|---------|-----|-----|-----|
| **Optimalidad** | No garantiza ruta corta | ✅ Óptima | ✅ Óptima |
| **Complejidad Espacio** | O(n) - mejor | O(n) | O(n) |
| **Complejidad Tiempo** | O(n+e) | O(n+e) | O(n log n) |
| **Uso en práctica** | Exploración general | Camino más corto | Búsqueda eficiente |

La tabla comparativa al final de la ejecución te permitirá evaluar qué algoritmo es más eficiente para tu laberinto.

## Modificación: A* sobre un Macro-Grafo

La modificación implementa una versión optimizada de A* para que el algoritmo no
explore cada celda del corredor como si fuera una decisión independiente. Se
mantiene el A* original para comparar ambos comportamientos.

### Cómo funciona

1. `identificar_nodos_decision()` considera nodos de decisión las celdas cuyo
  grado es diferente de 2. Por esto incluye bifurcaciones, callejones sin salida
  y, explícitamente, el inicio y la meta.
2. `construir_macro_grafo()` recorre cada corredor desde un nodo de decisión
  hasta el siguiente. Cada macro-arista guarda el nodo destino, el costo del
  corredor en pasos y la secuencia completa de celdas que lo forman.
3. `Grafo.astar_macro()` ejecuta A* sobre esos macro-vecinos. El costo acumulado
  `g(n)` suma la longitud de cada corredor recorrido, por lo que conserva los
  costos reales del laberinto.
4. `expandir_ruta_macro()` convierte la secuencia compacta de nodos de decisión
  en la ruta celda por celda. Así se puede visualizar el camino completo sin
  perder los pasos intermedios.

### Ejecución y comparación

Desde la carpeta raíz del proyecto, ejecuta:

```bash
python src/main.py
```

La salida incluye `A*`, que trabaja celda por celda, y `A* macro`, que trabaja
con corredores. Para cada algoritmo se muestran la longitud de la ruta, los
nodos visitados y el tiempo de ejecución. En el caso de `A* macro`, la longitud
corresponde a la ruta expandida, mientras que los nodos visitados corresponden
únicamente a nodos de decisión. Una reducción en esta última métrica evidencia
la optimización en laberintos con corredores largos.

Las pruebas específicas de la modificación se ejecutan junto con la suite:

```bash
python -m pytest tests/
```

Estas pruebas verifican que la ruta macro se expande desde el inicio hasta la
meta y que conserva la longitud óptima encontrada por BFS.

## Modificar el Laberinto

El archivo `data/laberinto.txt` contiene el laberinto a resolver. Para modificarlo:

1. **Primera línea**: Tupla con las coordenadas de la meta declarada: `(fila, columna)`
2. **Líneas siguientes**: Cada fila de la matriz del laberinto como lista de números

Ejemplo de estructura:
```
(17, 17)
[2, 1, 0, 0, ...]
[0, 0, 1, 0, ...]
...
```

## Ejemplo de Ejecución Paso a Paso

1. **Colócate en el directorio del proyecto:**
   ```bash
   cd "C:\Users\thoma\Desktop\Universidad\7. Septimo Semestre\Introduccion_a_la_IA\Proyectos\Proyecto1\proyecto-laberinto-ia"
   ```

2. **Ejecuta el programa:**
   ```bash
   python src/main.py
   ```

3. **Visualiza los resultados** que se imprimirán en la consola.

## Troubleshooting

### Error: `ModuleNotFoundError: No module named 'lector_laberinto'`
- Asegúrate de ejecutar el comando desde el directorio raíz del proyecto
- Verifica que el archivo `src/main.py` existe

### Error: `FileNotFoundError: [Errno 2] No such file or directory: 'data/laberinto.txt'`
- Verifica que el archivo `data/laberinto.txt` existe
- Asegúrate de ejecutar desde el directorio raíz del proyecto

### Problemas con la ruta en Windows
Si tienes problemas con la ruta, usa comillas alrededor de la ruta completa:
```bash
cd "C:\Users\thoma\Desktop\...\proyecto-laberinto-ia"
```

## Autores

- Thomas Arévalo Rodríguez 
- Laura Sofía Aponte Sánchez 
- Alexander Aponte Largacha 
- Sara Sofia Muñoz 

## Licencia

Este proyecto es parte de un curso académico de la universidad.
