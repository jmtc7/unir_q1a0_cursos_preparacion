# Funciones Lambda y Logging

La sección 4 incluye información básica sobre la creación y uso de funciones, parámetros y documentación, así como el uso de librerías estándar como `os`, `sys`, `pathlib` y `logging`. Sin embargo, en estas notas sólo se incluyen los aspectos más avanzados de esta sección: las funciones lambda y el uso del módulo `logging`.

También incluí algunas notas sobre qué son, cómo funcionan y para qué se usan los **decoradores**, aunque no forma parte del contenido de esta sección en el curso.

## 1. Funciones Lambda
Las funciones lambda son funciones simples que se necesitan de forma temporal y se pueden implementar en una sola línea. Su uso principal es ser pasadas como **argumentos a funciones *normales***, como funciones de ordenación o de filtrado, o aplicar una operación a todos los elementos de alguna estrucutra de datos. Algunos ejemplos son:

```python
# Ejemplos de funciones lambda
cuadrado = lambda x: x ** 2  # 1 parámetro (x) y retorno de un número
es_par = lambda x: x % 2 == 0  # 1 parámetro (x) y retorno de un booleano
suma = lambda x, y: x + y  # 2 parámetros (x, y)

# Elevar todos los elementos de una lista al cuadrado
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(cuadrado, numeros))

# Filtrar los elementos de una lista
pares = list(filter(es_par, numeros))

# Ordenado de una lista por números absolutos (también se pueden ordenar strings por longitud, etc.)
numbers = [1, 10, -1, 3, -10, 5]
sorted_stuff = sorted(numbers)  # [-10, -1, 1, 3, 5, 10]
sorted_numbers_absolute = sorted(numbers, key=lambda x: abs(x))  # [1, -1, 3, 5, 10, -10]
```


## 2. Uso del Módulo *Logging*
Existen varios **niveles de *logging***, según la importancia o cuán crítica sea la información a transmitir:
- **DEBUG (10)**: Información para diagnóstico de problemas (normalmente sólo para desarrolladores).
- **INFO (20)**: Confirmación de que las cosas funcionan según lo esperado.
- **WARNING (30)**: Indicación de que algo inesperado ocurrió o podría ocurrir, pero el programa puede seguir funcionando.
- **ERROR (40)**: Error que impidió que una función específica funcionara.
- **CRITICAL (50)**: Error grave que impide que el programa termine.

La **configuración básica** es elegir el **nivel** de logging a utilizar (todos los mensajes por debajo de dicho nivel no se reportarán). El **formato** en el que queremos mostrar los mensajes (`%(asctime)s` para fecha y hora, `%(levelname)s` el nivel, `%(message)s` el mensaje, `%(filename)s` el fichero, `%(lineno)d` la línea donde se generó el registro y `%(name)s` el nombre del *logger*).

```python
import logging

# Configurar el nivel básico de logging a INFO
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Este es un mensaje de debug")  # No se mostrará
logging.info("Aplicación iniciada")  # Se mostrará "2025-10-12 12:53:45,123 - INFO - Aplicación iniciada"
logging.warning("Archivo de configuración no encontrado, usando valores predeterminados")  # Se mostrará
logging.error("No se pudo procesar el archivo de datos")  # Se mostrará
logging.critical("Error crítico: base de datos no disponible")  # Se mostrará
```

Es común querer mostrar los registros tanto en la consola como en el archivo de log. Para hacer eso, podemos:

```python
import logging

# Crear un logger
logger = logging.getLogger('mi_aplicacion')
logger.setLevel(logging.DEBUG)

# Crear manejador para archivo
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)  # Mostrar todos los mensajes

# Crear manejador para consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # En consola solo mostramos INFO o superior (ignorar debug)

# Definir formato
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Añadir los manejadores al logger y utilizarlo
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.debug("Este mensaje solo aparece en el archivo")
logger.info("Este mensaje aparece en archivo y consola")
```

Para aplicaciones que se ejecutan durante mucho tiempo, es importante utilizar **rotación en los archivos de log**, para evitar que ocupen demasiado. Es posible limitar el uso de cada archivo de log por su tamaño o por el tiempo de ejecución. Este es un ejemplo:

```python
import logging
from logging.handlers import RotatingFileHandler

# Configurar logger
logger = logging.getLogger('mi_aplicacion')
logger.setLevel(logging.DEBUG)

# Crear manejador con rotación
# ROTACIÓN POR TAMAÑO: Máximo 5 archivos de backup, cada uno de máximo 2MB
handler = RotatingFileHandler(
    'app.log', 
    maxBytes = 2*1024*1024,  # 2 MB
    backupCount=5
)

# ROTACIÓN POR TIEMPO: Cambiar de archivo cada medianoche, conservando 30 días
handler = TimedRotatingFileHandler(
    'app.log',
    when='midnight',
    interval=1,
    backupCount=30
)

handler.setLevel(logging.DEBUG)

# Configurar formato
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Añadir manejador al logger y utilizarlo
logger.addHandler(handler)
logger.debug("Mensaje de depuración")
```

## 3. Decoradores
Otro aspecto avanzado de Python son los **decoradores**. Son una forma de cambiar el comportamiento de funciones o métodos sin cambiar el código. En Python, todo son objetos, incluyendo las funciones, por lo que podemos pasarlas como argumentos a otras funciones o constructores y devolverlas como valor de retorno. Los decoradores permiten automatizar este tipo de funcionamiento. En el siguiente código, cada vez que llamemos a la función `f()`, Python va a llamara `f1()` usando `f` como argumento:
```python
def f1(f):
  def wrapper(*args, **kwargs):  # Necesitamos *args y **kwargs por si acaso `f()` toma argumentos
    print('Comienzo')
    ret_val = f(*args, **kwargs)
    print('Final')
    return ret_val  # Necesitamos manejar el return explícitamente por si acaso `f()` devuelve algo

  return wrapper

@f1
def f():
  print('Hola')

@f1  # El mismo decorador se puede usar para varias funciones
def sum(a, b=9):
  return a+b

f()  # Imprimirá 'Comienzo\nHola\nFinal'!
print(sum(1, b=9))  # Imprimirá 'Comienzo\nFinal\n10'!
```

Uno de los usos más comunes de los decoradores es **medir el tiempo de ejecución** de una función:
```python
import time

def timer(func)
  def wrapper(*args, **kwargs):
    comienzo = time.time()
    ret_val = f(*args, **kwargs)
    final = time.time()
    print(f'Tiempo de ejecución: {final-comienzo} segundos')
    return ret_val

  return wrapper

@timer
def run():
  print('Pausando...')
  time.sleep(2)
  print('Despertado!')

run()  # Imprimirá 'Pausando...\nDespertado!\nTiempo de ejecución: 2.001 segundos' (aproximadamente)
```

Otras aplicaciones incluyen *loggear* las llamadas a cada función y los argumentos utilizados, 
