# Aspectos Avanzados

## 1. Introducción
En esta sección se verán conceptos avanzados de la programación con Python como son:
- Funciones para buscar y modificar texto.
- Sintaxis de expresiones regulares (RegEx) para definir patrones de texto.
- Gestión de errores.
- Usar la técnica de la compresión para crear estructuras de datos.

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
re.findall('\d?\s', ejemplo) # Buscar números con 1 o ningún dígito seguido de un espacio. Devuelve ['1', '2', '3']
re.findall('3+', ejemplo) # Buscar dónde aparece el número 3 1 o más veces. Devuelve ['333']
re.findall('(1*2)', ejemplo) # Buscar dónde aparece el número 1 ninguna o más veces seguido del número 2. Devuelve ['12', '2']
re.findall('\d{3}', ejemplo) # Buscar dónde aparece cualquier número repetido 3 veces. Devuelve ['333', '444']
re.findall('\d{2,3}', ejemplo) # Buscar dónde aparece cualquier número 2 o 3 veces seguidas. Devuelve ['22', '333', '444']
re.findall('[2,3]{2,3}', ejemplo) # Buscar dónde aparece el 2 o el 3 repetidos 2 o 3 veces seguidas. Devuelve ['22', '333']
re.findall('[1-3]{2,3}', ejemplo) # Buscar dónde aparecen números entre el 1 y el 3 repetidos 2 o 3 veces seguidas. Devuelve ['22', '333']
```

Más información sobre las expresiones regulares puede encontrarse [aquí](https://www.w3schools.com/python/python_regex.asp).
