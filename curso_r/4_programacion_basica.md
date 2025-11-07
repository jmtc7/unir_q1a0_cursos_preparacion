# Programación Básica

## 1. Introducción
El objetivo de este tema es ser capaces de:
- Controlar la ejecución de código con la ayuda de las estructuras condicionales if() y else().
- Ejecutar bloques de código repetidamente mediante estructuras iterativas (bucles for()).
- Definir funciones sencillas que utilicen argumentos


## 2. Operadores (pág. 4)
Los operadores se pueden clasificar en los siguientes tipos:
- **Aritméticos**: `+`, `-`, `*`, `/`, `^` (potencia), `%/%` (división entera) y `%%` (módulo o resto).
- **Lógicos**: `|` (disyunción u *or* en inglés), `&` (conjunción o *and* en inglés), `!` (negación) y `xor()` (disyunción exclusiva).
- **Relacionales**: `<`, `<=`, `>`, `>=`, `==` y `!=`.
- **Asignación**: `<-` (asignación izquierda), `=` (asignación de argumentos) y `->` (asignación derecha).
- **Otros**: `$` (acceso a variables de data frames), `:` (generar sucesiones de números), `::` (acceso a funciones de paquetes), `%in%` (verificar si un elemento se encuentra en un vector) y `~` (formulación de modelos).

Ciertas operaciones matemáticas no tienen un operador asignado, pero están implementadas como una función. Por ejemplo: `sqrt()`, `exp()`, `log()`, `log10()`, `log(,a)`, `factorial()`, `choose()`, `sin()`, `cos()`, `tan()`, `asin()`, `acos()`, `atan()` y `abs()`, 


## 3. Estructuras de Control (pág. 14)
Permiten controlar la manera en la que se ejecuta el código. Se dividen en:
- **Estructuras condicionales**: Ejecutan una serie de instrucciones sólo si se cumplen ciertas condiciones. En R, se usan con la estructura `if - else if - else`.
- **Estructuras iterativas**: Repiten una parte del código un número determinado de veces o hasta que se cumpla una condición. R ofrece varios tipos de bucles: `for`, `while` y `repeat`. También disponemos de las cláusulas `break` y `next`.

### 3.1. Estructuras condicionales (pág. 15)
Un ejemplo de una estructura condicional en R sería:
```r
a <- 2
b <- 3

if (a > b) {         # Si 'a' es mayor que 'b'
  print("a gana!")
} else if (a < b) {  # Si 'b' es mayor que 'a'
  print("b gana!")
} else {             # En cualquier otro caso (i.e., son iguales)
  print("Esto es un empate :(")
}
```

Si estamos tratando con vectores, R ofrece la función `ifelse()`, lo que permite evitar hacer bucles o escribir condiciones para cada elemento de un vector. Un ejemplo de uso sería:
```r
x <- c(5, 3, 2, 8, -4, 1)
resultados <- ifelse(x %% 2 == 0, 'Es par', 'Es impar')  # c("Es impar", "Es impar", "Es par", "Es par", "Es par", "Es impar")

# Anidación de funciones ifelse()
ifelse(x %% 2 == 0,  # 1a condición: Ver si el número es par
        ifelse(x %% 4 == 0, "múltiplo de 4", "múltiplo de 2 pero no de 4"),  # Si es par, se fija si también es múltiplo de 4
        "impar")  # Resultado si NO es par
```

### 3.1. Estructuras iterativas (pág. 22)
A continuación se muestran ejemplos de los distintos bucles en R:
```r
# Bucle for - Itera a través de ciertos elementos 
for(i in 1:3) {
  print(2 * i)
}

# Bucle while - Se repite hasta que se cumpla una condición
while (dado != 6) {  # Repetir hasta que 'dado' tenga el valor 6
  dado <- sample(1:6, 1)  # Simular que tiro un dado
}

# Bucle repeat - Bucle infinito hasta que se interrumpa (con break, por ejemplo)
repeat{
   valor <- valor / 2
  if(valor < 0.5) {  # Si 'valor' es suficientemente pequeño
    break          # Salir del bucle
  }
}
```

En el código anterior se mostró cómo utilizar `break` para interrumpir la iteración actual de un bucle y salir de él. Sin embargo, existe otra cláusula muy útil cuando se trabaja con bucles: `next`. `next` permite interrumpir la iteración actual y pasar a la siguiente (por lo que no se sale del bucle, simplemente se ignoran las líneas contenidas en él que aún no hayan sido ejecutadas).

Los bucles `for` suelen no ser la opción más simple de operar con estructuras de datos. La familia de funciones `apply` suele ser una mejor alternativa. Estas sirven para aplicar una función a cada elemento de una estructura de datos, como `matrices`, `data frames`, `arrays` y `listas`. **Estas funciones no son necesariamente más rápidas, pero su uso resulta en un código más limpio y claro**. Algunas de ellas son `apply()`, `eapply()`, `sapply()`, `lapply()`, `mapply()`, `rapply()`, `tapply()` y `vapply()`. A continuación se muestra un ejemplo de cómo usar las más comunes:
- `apply()`: Aplica una función con todos los elementos de las filas o columnas de una estructura. Por ejemplo, generar un vector con la suma de los elementos de cada columna de una matriz.
- `tapply()`: Aplica una función a un subvector definida por otro subvector. Por ejemplo, calcular la media de las longitudes de pétalos del dataset *iris* diferenciando entre las especies de flores.
- `apply()`: Versión de `apply()` que aplicará una función sobre todos los elementos de una estructura. Los resultados se almacenan en otra lista. Es necesario destacar que al utilizar `lapply()` con data frames, la función se aplicará sobre cada columna, no cada elemento.
```r
a1 <- array(data=1:24, dim = c(3, 4, 2))
# MARGIN = 1 para aplicar sobre filas, 2 para aplicar sobre columnas
# apply() tiene argumentos extra, como 'na.rm' para eliminar valores 'NA'
apply(a1, MARGIN = 2, FUN = sum)  # Sumar las columnas de todas las matrices del array 'a1'
apply(a1[,,2], 2, sum)            # Sumar las columnas de la matriz 2 del array 'a1'

tapply(iris$Petal.Length, iris$Species, mean)  # Media de longitudes de pétalo diferenciando por especies

lapply(x, log)     # Generar el logaritmo de todos los elementos en la lista 'x'
lapply(m, mean)    # Obtener la media de cada ELEMENTO de la matriz 'm'
lapply(df, class)  # Obtener la clase de cada COLUMNA del data frame 'df'
```

## 4. Funciones (pág. 43)
Para crear funciones en R se utiliza la instrucción `function` y se hace de la siguiente manera:
```r
# Función 'mi_funcion' y argumentos 'x' y 'potencia' ('potencia' tiene valor predeterminado)
mi_función <- function(x, potencia = 2) {
  resultado <- x * potencia
  return(resultado)
}

mi_funcion(2)  # Llamada a 'mi_funcion' (no necesito especificar el valor de 'potencia')
```

Por defecto, las funciones devuelven el último objeto evaluado dentro de ellas, pero también podemos utilizar la función `return()` para devolver el objeto que nosotros queramos y terminar la ejecución de la función. Dado que sólo podemos **devolver un objeto por función**, si queremos devolver varios, neceistaremos meterlos en una lista. Otra particularidad es que, si queremos capturar potenciales **argumentos adicionales** no definidos, podemos indicarlo añadiendo `...` a la lista de argumentos.

R ofrece varias formas de conocer **información sobre las funciones**, como `formals()` para conocer la lista de argumentos (también llamados *parámetros formales*) o `body()` para obtener el código que contiene. Otra opción es escribir el nombre de una función directamente, lo que devolverá toda su definición.

En R hay un tipo especial de funciones llamadas **funciones anónimas**, que son funciones simples que no tienen nombre y que sólo se usan una vez. Normalmente se suelen usar como argumento en las funciones de la familia `apply`, como por ejemplo `sapply(vector, function(x) (x+5))`, donde `function(x) (x+5)` es una función anónima con un argumento.

Aunque R no está estríctamente estandarizado, es conveniente seguir alguna **guía de estilo** de manera consistente. Una muy popular y extendida es la ***Tidyverse style guide***, que indica:
- Utilizar espacios y no tabuladores para indentar bloques de código.
- Utilizar 2 espacios (4 sólo se usaban en proyectos antiguos) para indentar.
- Al declarar condiciones, bucles o funciones, abrir la llave (`{`) en la misma línea de la declaración y cerrarla (`}`) en una nueva línea vacía.


## [5. Ejercicios (pág. 58)](https://unir.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=62e9b786-74c1-450f-8173-af1c011e97a5)
En este tema, se proponen 6 ejercicios para asegurar la comprensión de los conceptos presentados. Estos están resueltos en el archivo [actividades/ejercicios_tema4_programacion_basica.R](actividades/ejercicios_tema4_programacion_basica.R) y en el vídeo cuyo enlace está en el título de esta subsección se presentan las soluciones oficiales a los ejercicios 4 y 5.

Mis **conclusiones** tras comparar mis soluciones a las soluciones propuestas por la profesora son:
- Los conocimientos básicos están adquiridos, pude crear funciones y utilizar estructuras de control y de datos sin problema.
- Debo intentar utilizar más operaciones vectorizadas y menos bucles.
