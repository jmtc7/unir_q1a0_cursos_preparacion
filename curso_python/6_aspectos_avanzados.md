# Aspectos Avanzados

## 1. Introducción
En esta sección se verán conceptos avanzados de la programación con Python como son:
- Expresiones regulares (RegEx) para buscar y modificar patrones en texto
- Gestión de errores
- Compresión para crear estructuras de datos

## 2. Expresiones Regulares (RegEx)
Las expresiones regulares son una secuencia de caracteres con otros caracteres especiales que nos permiten definir y buscar patrones de texto. Para usarlas, se necesita importar el módulo `re`. Algunas de las funciones más útiles son:
- `re.search()`: Busca un patrón y permite saber dónde se encuentra el comiezo y el final de dicho patrón en el texto. Si el patrón no se encuentra, devuelve `None`.
- `re.match()`: Busca un patrón al principio de un texto. Si no se encuentra, devuelve `None`.
- `re.split()`: Divide un texto utilizando un patrón.
- `re.sub()`: Sustituye un patrón del texto por otro.
- `re.findall()`: Busca todas las apariciones de un patrón en un texto.

```python
import re
mensaje = 'Esto es un mensaje de prueba para el curso de Python'
match = re.search('curso', mensaje)  # match.start() es 37 y match.end() es 42
match = re.match('Esto', mensaje)  # match.start() es 0 y match.end() es 4
msg_dividido = re.split(' ', mensaje)  # Lista cuyos elementos son las palabras del mensaje
mensaje2 = re.sub('Python', 'Java', mensaje)  # Devuelve 'Esto es un mensaje de prueba para el curso de Java'
apariciones = re.findall('de', mensaje)  # Devuelve ['de', 'de']
```

Estas son las funciones básicas, pero necesitamos conocer los componentes que pueden aparecer en los textos:
- **Literales**: Caracteres básicos, como letras, símbolos o números.
- **Caracteres de escape**: Tienen funciones *especiales*, como salto de línea (\n), tabulador (\t), barra diagonal inversa (\\\\), dígito (\d), carácter alfanumérico (\w), espacio en blanco (\s), carácter que NO sea un dígito (\D), o carácter que NO sea alfanumérico (\W).

Esta información nos permite construir **grupos de caracteres** más complejos. Por ejemplo, podemos buscar las palabras que empiecen por `se-` y que tengan otra palabra a continuación con el siguiente patrón `re.findall('se\w+\s\w+', texto)`, lo que debería devolver `['sentido para', 'ser descifrado', 'sentido en']`.

Si quisiésemos recopilar únicamente la palabra que empieza por `se-` y usar lo demás sólo para la búsqueda, haríamos `re.findall('(se\w+)\s\w+', texto)`, lo que nos daría `['sentido', 'ser', 'sentido']`.

También existen los **metacaracteres**, que son caracteres que tienen un significado especial dentro de las expresiones regulares. Los más comunes son:
- `|`: Permite separar distintas alternativas dentro de un texto.
- `?`: El elemento que le precede aparece una vez o ninguna.
- `+`: El elemento que le precede aparece una o más veces.
- `*`: El elemento que le precede aparece ninguna o más veces.
- `{n}`: El elemento que le precede aparece n veces.
- `{n,m}`: El elemento anterior aparece entre `n` y `m`. Si `n` está vacío significará que el elemento aparece de 0 a `m` veces. Si, por el contrario, `m` está vacío significará que el elemento aparece `n` o más veces.
- `[]`: Representa clases de caracteres, es decir, buscará cadenas que tengan algunos de los caracteres definidos dentro de los corchetes.
- `-`: Define un rango de caracteres. 

```python
import re
re.sub('es|ser', '**AQUI**', texto)  # Cambiar todas las apariciones de 'es' y 'ser' por '**AQUI**'

ejemplo = '1 22 333 4444'
re.findall('\d?\s', ejemplo)  # Buscar números con 1 o ningún dígito seguido de un espacio. Devuelve ['1', '2', '3']
re.findall('3+', ejemplo)  # Buscar dónde aparece el número 3 1 o más veces. Devuelve ['333']
re.findall('(1*2)', ejemplo)  # Buscar dónde aparece el número 1 ninguna o más veces seguido del número 2. Devuelve ['12', '2']
re.findall('\d{3}', ejemplo)  # Buscar dónde aparece cualquier número repetido 3 veces. Devuelve ['333', '444']
re.findall('\d{2,3}', ejemplo)  # Buscar dónde aparece cualquier número 2 o 3 veces seguidas. Devuelve ['22', '333', '444']
re.findall('[2,3]{2,3}', ejemplo)  # Buscar dónde aparece el 2 o el 3 repetidos 2 o 3 veces seguidas. Devuelve ['22', '333']
re.findall('[1-3]{2,3}', ejemplo)  # Buscar dónde aparecen números entre el 1 y el 3 repetidos 2 o 3 veces seguidas. Devuelve ['22', '333']
```

Más información sobre las expresiones regulares puede encontrarse [aquí](https://www.w3schools.com/python/python_regex.asp).


## 3. Gestión de Errores

Al ser un lenguaje interpretado, es relativamente normal que aparezcan errores en tiempo de ejecución. Los **tipos de errores** más comunes son:
- **Errores de tipo** (`TypeError`): Cuando no podemos realizar una operación porque el tipo de datos de alguno de los elementos no es válido. Por ejemplo, si intentamos sumar un número con un texto.
- **Errores de sintaxis** (`SyntaxError`): Cuando una sentencia o instrucción no está bien escrita. Por ejemplo, si falta cerrar un paréntesis.
- **Errores de nombre** (`NameError`): Cuando llamamos a un identificador desconocido para Python. Por ejemplo, si intentamos utilizar una variable o función que no existe (o con algún error tipográfico en su nombre).
- **Errores de índice** (`IndexError`): Cuando intentamos acceder a una posición que no existe dentro de una secuencia (lista, diccionario, conjunto, etc.).

En ocasiones, errores de este tipo son críticos y deben terminar la ejecución del programa. Sin embargo, a veces es posible detectarlos y gestionarlos a través de una **excepción**, permitiendo continuar la ejecución. Para hacer esto, utilizamos los bloques `try-except`. Se puede usar sin especificar el tipo de error a capturar o especificando uno o varios tipos de error:

```python
lista = [1, 2, 3]
try:
  idx = 5  # El índice 5 no existe en la lista
  print(lista[idx])
except IndexError:
  print('No existe la posición solicitada')
except TypeError:
  print('El tipo de la operación es erróneo')
except:  # Capturar cualquier otro tipo de error
  print('Ha ocurrido un error')
```

También es posible añadir un bloque `else` que se ejecutará sólo **si no ha habido ningún error** y/o un bloque `finally` que **se ejecutará siempre**, haya habido error o no:

```python
lista = [1, 2, 3]
try:
  idx = 2
  print(lista[idx])
except: 
  print('No existe la posición solicitada')
else:
  print('No ha habido ningún error')
finally:
  print('Fin del bloque try-except')
```

### 3.1. Lanzamiento de errores
En ocasiones es interesante **lanzar errores nosotros mismos** para enviar mensajes personalizados. Para hacerlo, utilizamos la sentencia `rise`:

```python
lista = [1, 2, 3]
try:
  idx = 5
  if idx > len(lista):
    raise IndexError('Mensaje personalizado de error de índice')
  else:
    print(lista[idx])
except: 
  print('Se ha detectado un error')
```

Puedes encontrar **más información** sobre los errores y las excepciones en la [documentación oficial de Python](https://docs.python.org/3/tutorial/errors.html).


## 4. Compresión de Estructuras de Datos
Es una forma de crear listas, diccionarios o conjuntos donde cada elemento es el resultado de una operación. Por ejemplo, para crear una `lista` que almacene los cuadrados de los números del 1 al 10 podemos hacer `resultado = [i**2 for i in range(1, 11)]` y obtendremos lo mismo que haciendo:

```python
resultado = []
for i in range(1, 11):
  resultado.append(i**2)
```

Esto permite producir un código más compacto pero, sobretodo, **más rápido**. Esto se debe a que este mecanismo está implementado (y optimizado) en C, mientras que con el bucle se utiliza la interpretación de código y se genera una pila de llamadas a funciones (`append()`). Otra funcionalidad de este mecanismo es poder **añadir condiciones**, como en `resultado = [i**2 for i in range(1, 11) if i%3 = 0`, donde sólo se almacenarán (y se le aplicará la operación) a los números múltiplos de 3.

También se puede aplicar el mismo mecanismo **a diccionarios y a conjuntos** utilizando `{}` en lugar de `[]`. Si damos una clave y un valor generaremos un diccionario y si damos sólo valores generaremos un conjunto:

```python
mi_diccionario = {i: i**2 for i in range(1, 11) if i%2 = 0}
mi_conjunto = {i**2 for i in range(1, 11) if i%2 = 0}
```
