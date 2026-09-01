# Proyecto Laberinto IA

Un proyecto de Introducción a la Inteligencia Artificial que implementa algoritmos para la resolución de laberintos, incluyendo la transformación de matrices de laberintos en grafos para el análisis y búsqueda de caminos.

## Descripción del Proyecto

Este proyecto implementa herramientas para:
- **Leer y validar laberintos** representados como matrices desde archivos de texto
- **Identificar inicio y meta** dentro del laberinto
- **Transformar laberintos a grafos** para análisis de rutas
- **Aplicar algoritmos de búsqueda** para encontrar el camino más corto

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

- **main.py**: Punto de entrada del programa. Lee el laberinto, lo valida y lo convierte en grafo, mostrando información sobre la estructura.

- **lector_laberinto.py**: Contiene funciones para:
  - `leer_laberinto()`: Lee el archivo del laberinto
  - `validar_laberinto()`: Valida que el laberinto sea una matriz válida
  - `encontrar_inicio_y_meta()`: Localiza las posiciones de inicio (2) y meta (3)

- **transformacion_grafo.py**: Convierte la matriz del laberinto en una estructura de grafo (diccionario de adyacencias).

- **grafo.py**: Define la estructura y operaciones del grafo.

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
- Cantidad de nodos transitables en el laberinto
- Los vecinos de la posición de salida
- La meta declarada en el archivo
- Las dimensiones del laberinto
- Las coordenadas de inicio y meta

**Ejemplo de salida:**
```
Cantidad de nodos transitables: 450
Vecinos de la salida: [(0, 1), (1, 0)]
Meta declarada en el archivo: (17, 17)
Dimensiones reales: 17 x 34
Salida: (0, 0)
Meta: (17, 17)
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
