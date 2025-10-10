# Análisis de Datos

## 1. Introducción
En este tema, describiremos las principales funcionalidades de los dos módulos más importantes para manejar datos en Python: `NumPy` y `Pandas`. Esto incluirá:
- Estructuras de datos básicas de `NumPy`: *arrays* y *matrices*.
- Fnciones universales y estadísticas en `NumPy`.
- Conocer las estructuras de datos básicas de `Pandas`: *series* y *dataframes*.
- Funciones de filtrado en las estructuras de `Pandas`.
- unciones estadísticas en `Pandas`.
- Modificar los valores almacenados en las estructuras de datos de `Pandas`. 


## 2. NumPy
Es un módulo de Python orientado a librerías científicas. Proporciona nuevas estructuras de datos y métodos para trabajar con ellas.

### 2.1. Arrays y Matrices
Los ***arrays*** almacenan una secuencia de valores del mismo tipo. Muy similares a las listas de Python, pero más rápidos si se utiliza el mismo tipo en sus elementos. Es posible utilizar tipos distintos, pero sus métodos pueden dar errores. Podemos crear un *array* haciendo `array = np.array([1, 2, 3, 4])`. Para acceder al segundo elemento, usamos índices (igual que con las listas de Python), como `array[2]`, que devolvería `3`.

Las ***matrices***  son *arrays* con más dimensiones, aunque lo más común es que tenga dos. Se inicializan (y se comportan) como si fuesen listas de listas: `matriz = np.array([[1, 2, 3], [4, 5, 6]])`. **IMPORTANTE**: Si todas las filas NO tienen la misma longitud, se creará un array de listas en vez de una matriz.

Si comparamos la memoria que ocupa una lista y un array de o el tiempo que se tarda en realizar operaciones con ellos, vemos la diferencia en eficiencia:

```python
import numpy as np
import sys

lista = range(1000)
array = np.array(range(1000))

# Espacio ocupado por la lista y por el array
print(sys.getsizeof(1) * len(lista))  # 28000
print(array.size * array.itemsize)  # 8000 -> Menos del 30% que la lista
```

```python
import time

n_elementos = 1000000  # 1 millón
lista1 = range(n_elementos)
lista2 = range(n_elementos)
array1 = np.array(range(n_elementos))
array2 = np.array(range(n_elementos))

# Tiempo de restar los elementos de dos listas
comienzo = time.time()
resultado = [x - y for x, y in zip(lista1, lista2)]
final = time.time()
print(final - comienzo)  # 0.080843

# Tiempo de restar los elementos de dos arrays
comienzo = time.time()
resultado = [x - y for x, y in zip(array1, array2)]
final = time.time()
print(final - comienzo)  # 0.005764 -> Menos del 10% que con listas
```

### 2.2. Funciones Universales
Son aquellas que se aplican a todos los elementos de un array. Si se hacen con dos arrays, se aplicará elemento por elemento entre ambos (es necesario que ambos tengan el mismo tamaño). Las más importantes son:

```python
import numpy as np

array1 = np.array([4, 89, 15])
array1 = np.array([6, 39, 10])

# Funciones aritḿeticas
np.substract(array1, array2)  # Resta: np.array([-2, 50, 5])
np.add(array1, array2)        # Suma: np.array([10, 128, 25])
np.multiply(array1, array2)   # Multiplica: np.array([24, 3471, 150])
np.divide(array1, array2)     # Divide: np.array([0.6666, 2.2821, 1.5])
np.power(array1, array2)      # Elementos del 1 elevados a los elementos del 2: np.array([4, 81, 9765625]
np.sqrt(array1)               # Raíz cuadrada de los elementos de un array: np.array([2, 9.43398, 3.87298])
np.square(array1)             # Elementos de un array elevados al cuadrado: np.array([16, 7921, 225])
np.gcd(array1, array2)        # Máximo común divisor: np.array([2, 1, 5])
np.lcm(array1, array2)        # Mínimo común múltiplo: np.array([2, 12, 10])

# Funciones de comparación
np.greater(array1, array2)  # Verifica si los elementos del array1 son MAYORES que los del 2: np.array([False, True, True])
np.greater_equal(array1, array2)  # Verifica si los elementos del array1 son MAYORES O IGUALES que los del 2
np.less(array1, array2)  # Verifica si los elementos del array1 son MENORES que los del 2: np.array([True, False, True])
np.less_equal(array1, array2)  # Verifica si los elementos del array1 son MENORES O IGUALES que los del 2
np.equal(array1, array2)  # Verifica si los elementos son iguales
np.not_equal(array1, array2)  # Verifica si los elementos son diferentes

# Funciones booleanas
array1 = np.array([True, False, True])
array1 = np.array([False, False, True])

np.logical_and(array1, array2)  # np.array(False, False, True])
np.logical_or(array1, array2)   # np.array([True, False, True])
np.logical_xor(array1, array2)  # np.array([True, False, False])
np.logical_not(array1, array2)  # np.array([False, True, False])

# Funciones estadísticas
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
np.amin(array)  # Valor mínimo del array: 1
np.amax(array)  # Valor máximo del array: 10
np.percentile(array, 25)  # Percentil 25: 3.25
np.median(array)  # Mediana (división del conjunto en dos mitades): 5.5
np.mean(array)  # Media (tendencia central del conjunto): 5.5
np.average(array, weights=pesos)  # Media ponderada usando una lista de pesos -> sum(val_n*peso_n) / n_valores
np.std(array)  # Desviación estándar: 2.87228
np.var(array)  # Varianza: 8.25
```


## 3. Pandas
Es una extensión de `NumPy` y se orienta a manipular y analizar datos.

### 3.1. Series y DataFrames
Las ***series*** son similares a las listas y a los arrays (datos en una dimensión). La diferencia es que los índices de los elementos pueden ser etiquetas elegidas por nosotros (aunque también se puede acceder usando la posición que ocupa cada elemento), como en los diccionarios. Podemos crear una serie con índices personalizados de varias formas (usando diccionarios, listas o incluso NumPy arrays).

```python
import pandas as pd

serie1 = pd.Series({'a': 1, 'b': 2, 'c': 3})                    # Usando un diccionario
serie2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])            # Usando listas
serie3 = pd.Series(np.array([1, 2, 3]), index=['a', 'b', 'c'])  # Usando un NumPy.Array

# Acceso a elementos
elemento = serie1['b']  # 2
elemento = serie1[1]    # 2
elementos = serie1[1:]  # pd.Series({'b': 2, 'c': 3})

# Atributos importantes
indices = serie1.index   # ['a', 'b', 'c']
valores = serie1.values  # [1, 2, 3]
```

Dado que las series están basadas en NumPy arrays, podemos hacer operaciones vectorizadas fácilmente (siempre y cuando ambas tengan los mismos índices), como `serie1 + serie2`, `serie1 * 10` o `np.sqrt(serie1)`.

Los ***dataframes*** son las estructuras más utilizadas en `Pandas`. Representan una tabla con etiquetas en cada fila y columna. Se pueden crear de varias maneras

```python
import pandas as pd

diccionario = {'columna1': pd.Series({'a': 10, 'b': 20, 'c': 3}),
                'columna2': pd.Series({'a': 4, 'b': 5, 'd': 6})}  # 'columna1' NO tiene índice 'd' y 'columna2' NO tiene 'c'. Se les dará valor NaN
dataframe = pd.DataFrame(diccionario)  # Cada serie será una columna del DF. Cada índice de las series será una fila

lista = [{'a': 10, 'b': 20, 'c': 3}, {'a': 4, 'b': 5, 'd': 6}]  # Lista de diccionarios
dataframe = pd.DataFrame(diccionario)  # Cada diccionario será una fila con números como índices. Las claves de los diccionarios serán las columnas

# Acceso a elementos (columnas y filas)
col1 = dataframe['columna1']  # Acceso a una columna por su etiqueta -> devuelve pd.Series({'a': 10, 'b': 20, 'c': 3})
fila_b = dataframe.loc['b']   # Acceso a una fila por su etiqueta/índice -> devuelve {'columna1': 20, 'columna2': 5}
fila_1 = dataframe.iloc[1]    # Acceso a una fila por su posición -> devuelve {'columna1': 20, 'columna2': 5}
fila_1 = dataframe.iloc[1:3]  # Acceso a VARIAS filas -> devuelve DF {'columna1': {'b': 20, 'c': 3, 'd': Nan}, 'columna2': {'b': 5, 'c': NaN, 'd': 6}}

# Añadir/eliminar elementos/columnas
dataframe['columna3'] = pd.Series({'a': 7, 'b': 8, 'c': 9, 'd': 10})
del dataframe['columna3']

# Acceso a filas por array booleano (filtrado/queries)
filtro = np.greater(dataframe['columna1'], dataframe['columna2'])  # Devuelve qué elementos de la col1 son más grandes que los de la col2
dataframe[filtro]  # Devuelve DF {'columna1': {'a': 10, 'b': 20}, 'columna2': {'a': 4, 'b': 5}}
```

Al igual que con los NumPy arrays y con las series, también podemos aplicar operaciones con los dataframes, como `dataframe * 2` para multiplicar por 2 todos los elementos del dataframe o `dataframe1 + dataframe2` para sumar todos los elementos de dos dataframes. Sin embargo, hay que asegurarse de que tengan las mismas dimensiones para no causar errores (se generarán valores `NaN` en los elementos donde no se pueda operar). Otra operación útil con los dataframes es la **transpuesta**, que hace que las columnas se transformen en filas y viceversa. Se aplica ejecutando `dataframe.T`.

### 3.2. Funciones de Gestión de Datos
Utilizaremos el siguiente dataframe para los ejemplos:

<img src="imgs/7_analisis_datos__dataframe_ejemplo.jpg" height="300">

Podemos **ordenar las filas** de un dataframe usando la función `dataframe.sort_values(by='edad)`. También podemos **ordenar basándonos en los índices** de cada fila con `dataframe.sort_index()`. Si añadimos el argumento `ascending=False`, invertimos el orden. 

Tambien es posible **agrupar filas** que tengan el mismo valor de algún índice utilizando `dataframe.groupby(by='estado_civil')`. Es muy común añadir alguna operación para contar los elementos u obtener la media de algún otro atributo. Se puede hacer añadiendo `.count()`, por ejemplo.

Otro recurso es aplicar **funciones anónimas/lambda/map** a todos los elementos y obtener una serie con los resultados, como `serie = dataframe.apply(lambda item: item['edad']<35 and item['estado_civil']=='Soltero', axis=1)`, lo que devolvería `pd.Series({'user1': False, 'user2': False, 'user3': True, 'user4': False})`.

Al igual que las series, los dataframes también ofrecen **operaciones estadísticas**, como `dataframe.describe()`, que da información de cuántos valores distintos hay para cada atributo, la media, la desviación estándar, varios percentiles, el valor máximo, etc. Los resultados dependen del tipo de datos almacenados en el dataframe. También podemos aplicar funciones más específicas, las cuales se aplicarán sólo a las columnas compatibles. Por ejemplo, si hacemos `dataframe.median()`, sólo se aplicará a la columna `'edad'`.

## 4. Lectura y Escritura de Ficheros CSV
