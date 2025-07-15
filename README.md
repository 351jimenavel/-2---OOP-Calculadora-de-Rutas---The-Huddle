# Refactorización de "Calculadora de Rutas"
Este proyecto es una **refactorización** del desafío anterior titulado *Calculadora de Rutas*.  
El objetivo principal fue **reestructurar el código aplicando principios de la Programación Orientada a Objetos (POO)** para lograr una solución más clara, modular y mantenible.


## División de Responsabilidades

Dividí el proyecto en dos clases principales para aplicar el principio de **responsabilidad única (SRP)**:

### 1. Mapa
Encargada únicamente de construir y mostrar el tablero.

**Métodos principales:**
- Crear el tablero.
- Colocar entrada.
- Colocar salida.
- Colocar obstáculos.
- Mostrar el tablero.
- Validar coordenadas.

También encapsula la lógica visual:
- Limpieza de consola.
- Representación visual de cada símbolo.

### 2. CalculadoraDeRutas
Encargada exclusivamente de la lógica del algoritmo BFS.

**Métodos principales:**
- Buscar el camino más corto entre Entrada y Salida.
- Reconstruir y mostrar la ruta final encontrada.


## Qué aprendí del proceso de refactorización

- Cómo **dividir el código** en responsabilidades claras.  
  Antes todo estaba en funciones sueltas; ahora, al separarlo en clases, el código quedó más organizado y fácil de mantener.

- Cómo **encapsular la lógica**: escondí detalles internos (validaciones, limpieza de consola) dentro de métodos, para que el usuario solo tenga que usar los objetos sin preocuparse por la implementación.

- La diferencia entre usar funciones sueltas vs. trabajar con **objetos y métodos**: entendí cómo esto mejora la escalabilidad y el mantenimiento del código.


## Decisiones tomadas y por qué

- **Usar POO** (Programación Orientada a Objetos):  
  Para que el proyecto sea más escalable, reutilizable y sencillo de probar o extender.

- **No aplicar herencia ni polimorfismo**:  
  Porque el problema no lo requería. No había jerarquías ni comportamientos comunes entre clases que justificaran su uso. Incluirlos habría sido innecesariamente complejo.

- **Acceso a atributos**:  
  Dejé ciertos atributos como matriz públicos, ya que los uso directamente desde otros módulos.  
  Sin embargo, si el proyecto crece, podría encapsularlos con getters/setters para mejorar la seguridad y control.


## Diferencias con respecto al proyecto anterior

#### - Uso correcto de la POO
- Se introdujo una estructura clara de clases con atributos, métodos y aplicación de **abstracción** y **encapsulamiento**.

#### - Visualización del camino resuelto
- Antes, el backtracking mostraba el camino desde la **Salida hacia la Entrada**, dificultando entender el recorrido.
- Ahora, el camino se muestra correctamente desde la **Entrada (E) hasta la Salida (S)** gracias a la inversión del recorrido con reverse.

#### - Estructura modular y clara
- Antes, todo estaba en funciones desordenadas.
- Ahora se divide en clases bien organizadas (Mapa, CalculadoraDeRutas), siguiendo SRP, con métodos agrupados por funcionalidad.

#### - Separación del flujo principal (main.py)
- Antes, el script mezclaba lógica, entradas y ejecución.
- Ahora, main.py se encarga solo del flujo general: entradas del usuario, creación de objetos y ejecución de métodos.

#### - Mejor manejo de errores y validaciones
- Se agregaron validaciones dentro de los métodos para evitar errores por coordenadas fuera del tablero o celdas ocupadas, aplicando el principio de **encapsulamiento**.

