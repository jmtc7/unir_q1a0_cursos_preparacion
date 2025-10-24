# Estructuras de Datos
## 1. Introducción
En este tema se presentarán las estructuras de datos más comunes en R, como los vectores, las matrices, las listas y los data frames. Veremos cómo crearlos, recuperar valores almacenados en ellos, modificarlos, etc.

## [2. Tipos de Objetos](https://unir.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=16c19a6b-c601-490a-abbb-af190122c62a)
Todo en R son **objetos**. Los objetos pertenecen a una **clase** y están constituidos por objetos más básicos, hasta llegar a los **objetos atómicos** explicados en el [Tema 1](2_conceptos_básicos.md). El siguiente snippet repasa los conceptos esenciales:
```r
x <- 1
class(x) # Devolverá "numeric"
type(x) # Devolverá "double", el único tipo de R distinto a su clase

y <- 1L # Especificar que queremos que sea un entero (también podría con as.integer(1))
class(x) # Devolverá "integer"
type(x) # Devolverá "integer"
```

## [3. Estructuras de Datos](https://unir.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f23d04a9-661c-467f-b9f8-af1c00763dbf)
Las estructuras de datos en R se organizan según su **dimensión** (una, dos o más dimensiones) y según si son **homogéneas o heterogéneas** (si todos los datos que contienen son del mismo tipo y clase o si pueden cambiar, respectivamente):

| Dimensiones | Homogéneas | Heterogéneas |
| ----------- | ---------- | ------------ |
|      1      |  Vectores  |    Listas    |
|      2      |  Matrices  | Data frames  |
|      n      |   Arrays   |              |

En los próximos sub-capítulos de este documento se explicarán las estructuras unidimensionales (vectores y listas) seguidas de las bidimensionales (matrices y data frames) y se acabará con las multidimensionales (arrays).

### 3.1. Vectores (00:02:35, pág. 4)
Son estructuras **homogéneas unidimensionales** que **solo pueden contener objetos atómicos**. Podemos obtener su longitud con `length()` y se accede a sus elementos con `[]`. Podemos verificar si una variable es un vector utilizando `is.vector()`. En el siguiente *snippet* se muestra código simple para manejar vectores:
```r
# Creación de vectores de diferentes tipos
x <- c(1, -2, 3.5) # "C" viene de "combinar" o "concatenar"
y <- c(4, 5)
z <- c("Lunes","Martes","Miércoles","Jueves","Viernes")

s <- c(x, y)  # Podemos concatenar vectores (1, -2, 3.5, 4, 5)
s2 <- c(1, "2", 3)  # Se convertirán todos los elementos a la clase más general (character en este caso)
s3 <- c(1, 1>2, 3)  # Se convertirán los elementos a numeric (FALSE -> 0)

length(z)  # Devuelve la longitud del vector (5)
nchar(z)   # Devuelve la cantidad de caracteres en cada cadena del vector (5, 6, 9, 6, 7)

# Acceso a elementos
s[1]          # Primer elemento de s (1)
s[length(s)]  # Último elemento de s (5)
s[1:3]        # Desde el primer hasta el tercer elemento de s (1, -2, 3.5)
s[c(1, 3)]    # Primer y tercer elemento de s (1, 3.5)
s[seq(2, length(s), 2)]   # Índices pares de s (-2, 4)
s[-seq(2, length(s), 2)]  # Índices NO pares de s (1, 3.5, 5)
s[c(1, 1, 2, 2, 2, 3)]    # Mostrar el 1er elemento 1 vez, el 2o 3 veces y el 3o 1 vez

s[s>3]  # Mostrar los elementos mayores que 3 (3.5, 4, 5) - También se pueden usar condiciones con otro vector
```

Otras formas de crear vectores es mediante el operador `:`, las funciones `seq()` o `rep()` para crear secuencias o repeticiones, el constructor `vector()` o funciones para crear números aleatorios, como `rnorm()`, `runif()`, etc. Por ejemplo:
```r
# Secuencias incrementando de 1 en 1
1:4    # (1, 2, 3, 4)
4:1    # (4, 3, 2, 1)
1.2:4  # (1.2, 2.2, 3.2)
-1:4   # (-1, 0, 1, 2, 3, 4)

# Secuencias incrementando con otros pasos
seq(from = 1, to = 10, by = 2)          # (1, 3, 5,  7, 9) -> Avanza de 2 en 2
seq(from = 1, to = 10, length.out = 5)  # (1, 3.25, 5.5, 7.75, 10) -> Divide el rango en 5-1 tramos iguales

# Repeticiones de elementos
rep(1, times = 4)    # (1, 1, 1, 1) -> Repetir el 1 4 veces
rep(1:3, times = 2)  # (1, 2, 3, 1, 2, 3) -> Repetir (1, 2, 3) 2 veces
rep(1:3, each = 2)   # (1, 1, 2, 2, 3, 3) -> Repetir cada valor de (1, 2, 3) 2 veces
rep(1:3, each = 2, times = 2)       # (1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3) -> Repetir cada valor de (1, 2, 3) 2 veces y repetir el resultado 2 veces
rep(1:3, each = 2, length.out = 5)  # (1, 1, 2, 2, 3) -> Repetir cada valor de (1, 2, 3) 2 veces (parar al alcanzar 5 elementos)
rep(1:3, each = 2, length.out = 9)  # (1, 1, 2, 2, 3, 3, 1, 1, 2) -> Repetir cada valor de (1, 2, 3) 2 veces (continuar hasta alcanzar 5 elementos)
rep(1:3, times = c(2, 3, 1))        # (1, 1, 2, 2, 2, 3) -> Repetir el 1 2 veces, el 2 3 veces y el 3 1 vez.

# Utilizlar constructores y wrappers
v2 <- vector(mode = "numeric", length = 3)    # Crear vector con 3 elementos de tipo "numeric" (por defecto a 0) - equivale a numeric(3)
v1 <- vector(mode = "logical", length = 3)    # Crear vector con 3 elementos de tipo "logical" (por defecto a FALSE) - equivale a logical(3)
v3 <- vector(mode = "character", length = 3)  # Crear vector con 3 elementos de tipo "character" (por defecto a "") - equivale a character(3)

# Equivalentes a las instrucciones anteriores
v11 <- logical(3)
v22 <- numerical(3)
v33 <- character(3)

# Generación de 10 números aleatorios (sólo algunos ejemplos)
rnorm(n = 10, mean = 1, sd = 1.2)   # Distribución normal (centrada en 1, desviación estándar 1.2)
runif(n = 10, min = 1, max = 3)     # Distribución uniforme (números entre 1 y 3 CON DECIMALES)
rbinom(n = 10, size = 10, p = 0.3)  # Distribución binomial (números enteros)
rpois(n = 10, lambda = 2)           # Distribución de Poisson (números enteros)

# Muestrear 10 veces los valores de "x" con las probabilidades "prob "pudiendo muestrear varias veces el mismo valor
sample(x = c(0, 1), size = 10, replace = TRUE, prob = c(0.5, 0.5))
```

Otra funcionalidad de los vectores es poder **nombrar sus elementos** con `setNames()` (creando un nuevo vector) o con `names()` (modificando el vector existente):
```r
precioskg <- c(2.3, 3.5, 8.9, 5.6)
frutas <- c('naranja', 'manzana', 'fresa','')

# Nombrar elementos: ('naranja' = 2.3, 'manzana' = 3.5, 'fresa' = 8.9,'' = 5.6)
precioskg_nom <- setNames(precioskg,frutas) 
names(precioskg) <- frutas

# Acceso a elementos usando nombres
precioskg[c('naranja','fresa')]  # ('naranja' = 2.3, 'fresa' = 8.9)
```

En R es posible realizar **operaciones vectorizadas**. Es decir, que al realizar una operación con dos vectores, se realiza dicha operación entre cada elemento de ambos vectores. Si se realiza una operación entre un vector y un escalar, dicha operación se le aplicará a cada elemento del vector.

Existe un tipo especial de vectores llamados **factores**. Estos representan internamente una serie de *strings* categóricos como números (aunque por consola se nos muestren los *strings*). Podemos generarlos con el constructor `factor()`. La diferencia clave entre los factores y los vectores es que los factores almacenan los ***niveles*** (*levels* en inglés), es decir, los valores diferentes del conjunto. Los datos se organizan como repeticiones de una serie de valores posibles. Esto permite, por ejemplo, definir un factor con una serie de niveles conocidos para que cualquier valor que se intente añadir que no corresponda a ninguno de los niveles (por errores tipográficos, por ejemplo), de un error y se convierta en `NA`. Se pueden definir los niveles de un factor utilizando el argumento `levels` del constructor `factor()`.

Como nota adicional, R tiene algunos vectores predefinidos, como `letters`, que contiene las letras del alfabeto en minúscula, o `LETTERS`, que las contiene en mayúscula.

### 3.2. Listas (00:41:10, pág. 63)
Al igual que los vectores, las listas son **unidimensionales**,, pero **pueden contener objetos NO atómicos** (e.g., listas, data frames, vectores, etc.) y son estructuras **heterogéneas**. Para crear listas podemos utilizar el constructor `list()` o la función de coerción `as.list()`. Al igual que con los vectores, también podemos asignarles nombres a los elementos:
```r
# Crear elementos a meter en las listas
v <- runif(10, 2, 10)  # Vector de 10 números aleatorios entre 2 y 10
m <- matrix(1:4, ncol = 2)  # Matriz
df <- data.frame("Nombres" = c("Lucía", "Bianca"), "Edades" = c(19, 20))  # Data frame

# Creación de listas
lista1 <- list(v, m, df)  # Lista sin nombres
lista2 <- list("Un_vector" = v, "Una_matriz" = m, "Un_df" = df)  # Lista con nombres (creanr una nueva lista)
names(lista2) <- c("Un_vector", "Una_matriz", "Un_df")  # Lista con nombres (modificar lista existente)
```

Al igual que los vectores, podemos obtener el **tamaño** de una lista utilizando `length()` y utilizamos `[]` para **acceder a sus elementos** (R devolverá una lista con los elementos seleccionados). Sin embargo, también podemos utilizar `[[]]`, lo que devolverá los elementos tal cual, sin estar contenidos en una lista. Si la lista contiene estructuras de datos, podemos acceder a dichas estructuras con vectores o con múltiples `[]`:
```r
# Clase y tipo de listas
class(lista1[1])    # list
class(lista1[[1]])  # numeric

# Acceso a elementos por índice
lista1[[c(1, 2)]]  # 2o elemento del primer elemento de la lista (2)
lista1[[1]][[2]]   # Equivalente a la línea anterior
lista1[c(1, 2)]    # 1er y 2o elementos de la lista (vector y matriz)

# Acceso a elementos por nombre
lista2[["Un_vector"]]
lista2$Un_vector  # Más frecuente

# Concatenación de listas
lista4 <- list(list(1, 2), c(3, 4)) # Crea una lista de 2 elementos (lista y vector)
lista5 <- c(list(1, 2), c(3, 4))    # Coerce el vector en lista y crea una lista de 4 elementos
```

### 3.3. Matrices (00:55:30, pág. 23)
Son estructuras rectangulares (**bidimensionales**) de **objetos atómicos** del **mismo tipo**. Se dividen en filas y columnas y se puede acceder a ellas con `[i,]` o `[, j]`, respectivamente. Para crearlas, se usa el constructor `matrix()`:
```r
# Opción 1: Utilizar el constructor
# Si faltan o sobran filas/columnas, se ignorarán o repetirán los elementos del principio, como con los vectores
m1 <- matrix(data=1:15, nrow=3, ncol=5, byrow = TRUE)  # Rellenar por filas
##     [,1] [,2] [,3] [,4] [,5]
## [1,]   1    2    3    4    5
## [2,]   6    7    8    9   10
## [3,]  11   12   13   14   15

m2 <- matrix(data=1:15, nrow=3, ncol=5, byrow=FALSE)  # Rellenar por columnas
##     [,1] [,2] [,3] [,4] [,5]
## [1,]   1    4    7   10   13
## [2,]   2    5    8   11   14
## [3,]   3    6    9   12   15

# Opción 2: Apilar vectores
x <- 1:5
y <- 6:10
z <- 11:15
m11 <- rbind(x, y, z)  # Usar vectores como filas
m22 <- cbind(x, y, z)  # Usar vectores como columnas

m11 <- rbind(m11, 16:20)  # Añadir filas
m22 <- cbind(m11, 16:20)  # Añadir columnas

# Opción 3: Añadir dimensiones a un vector
v <- 1:15
dim(v) <- c(3, 5)  # Rellenará por columnas y NO se puede cambiar...
```

Podemos utilizar el argumento o función `dimnames` para darle **nombres a las filas y a las columnas** o `unname()` para quitárselos. También se pueden utilizar `rownames()` y `colnames()` para configurar los nombres de las filas y las columnas independientemente:
```r
# Asignación de nombres en matrices
dimnames(m) <- list(LETTERS[1:3], letters[1:5])  # (A, B, C) como nombres de filas y (a, b, c, d, e) como nombres de columnas
colnames(m) <- letters[1:5]                      # (a, b, c, d, e) como nombres de columnas
rownames(m) <- LETTERS[1:3]                      # (A, B, C) como nombres de filas

# Borrado de nombres en matrices
unname(m)            # Borrar los nombres de las filas y de las columnas
colnames(m) <- NULL  # Borrar los nombres de las columnas
rownames(m) <- NULL  # Borrar los nombres de las filas
```

Algunos ejemplos de cómo acceder a los elementos de las matrices son:
```r
# Acceso a elementos de matrices
m[2, 1]      # Elemento en la 2a fila y 1a columna
m[2,]        # 2a fila
m[,1]        # 1a columna
m[,2:4]      # Columnas desde la 2 a la 4
m[c(1, 3),]  # Filas 1 y 3
m["Tienda", c("Melon", "Manzana")]  # Elementos de la fila "Tienda" en las columnas "Melon" y "Manzana"
m[,-4]       # Toda la matriz EXCEPTO la 4a columna
```

Podemos utilizar las funciones `dim()`, `ncol()`, `nrow()` y `length()` para obtener sus **dimensiones** (filas, columnas), número de **columnas**, número de **filas** y **cantidad de elementos** (equivalente a ncol*nrow). Para verificar si un objeto es una matriz, se usa `is.matrix()`. Otras operaciones disponibles para matrices son:
- **Sumas y restas** elemento a elemento con `+` y `-`.
- **Producto** celemento a elemento con `*`.
- **Producto matricial** con el operador `%*%`. La cantidad de filas de la primera matriz debe ser igual a la cantidad de columnas de la segunda.
  - Similarmente, `^` eleva todos los elementos de la matriz, mientras que `%^%` realiza la versión matricial de dicha operación. Estas operaciones están implementadas en el paquete `{expm}`. Otra opción es utilizar la función `matrix.power()` del paquete `{matrixcalc}`.
- **Transposición** de filas por columnas y viceversa con la función `t()`.
- **Determinante** de una matriz cuadrada con la función `det()`.
- **Inversa** de una matriz cuadrada invertible con la función `solve()`.
- **Diagonal principal** con la función `diag()`. Si la matriz no es cuadrada, cogerá la matriz más grande posible empezando desde el primer elemento.
  - **ATENCIÓN**: También se puede utilizar para construir matrices diagonales. Con `diag(1, nrow = 3)` (equivalente a `diag(3)`) se genera una matriz identidad 3x3, pero se le puede especificar otro número de columnas o un vector a meter en la diagonal en lugar de unos. 
- **Traza de una matriz** combinando funciones, con `sum(diag(m))`.

Como nota adicional, con la función `solve()` también se pueden resolver sistemas de ecuaciones como el siguiente:
```r
# Definir ecuaciones
# 3x − 2y = 6
# −x + 5y = −2
A <- matrix(c(3, -2, -1, 5), ncol = 2, byrow = TRUE)
b <- c(6, -2)
solve(A, b)  # Resuldao: 2 0
```

### 3.4. Data frames (01:19:35, pág. 40)
Son estructuras **bidimensionales heterogéneas**. Generalmente, las columnas representan variables (e.g., altura, peso y edad) y las filas representan observaciones (e.g., individuos). Su clase es `data.frame` pero su tipo es `lista`. A continuación se muestra un uso básico:
```r
# Creación de un data frame
altura <- c(167, 192, 173, 174, 172, 167, 171, 185, 163, 170)  # cm
peso <- c(86, 74, 83, 50, 78, 66, 66, 51, 50, 55)  # Kg
fuma <- c("No", "Si", "No", "Si", "No", "No", "Si", "Si", "Si", "No")
sexo <- c("M", "M", "F", "M", "M", "M", "F", "M", "F", "F")
df <- data.frame(altura, peso, fumador = fuma, sexo)  # Renombrar "fuma" a "fumador"

# Acceso a elementos por índices
df["peso"]  # Recupera todas las filas de la columna "peso"
df[1:3]     # 3 primeros elementos de la "lista" de columnas (todas las filas de "altura", "peso" y "fumador")
df[1, 3]    # 1er elemento de la 3a columna ("No")
df[1:3,]    # Todas las columnas de las 3 primeras filas
subset(df, select = c(2, 3))   # Equivalente a df[c(2, 3)], coge todas las filas de las columnas 2 y 3 ("peso" y "fumador"))
subset(df, select = -c(2, 3))  # Equivalente a df[-c(2, 3)], coge todas las filas de todas las columnas EXCEPTO la 2 y la 3

# Acceso a elementos como variables
df$peso     # Devuelve la columna "peso" en un vector (puedo aplicar min(), max(), etc.). df["peso"] devuelve un data frame.
attach(df)  # Permite acceder a las columnas del data frame como si fuesen variables (altura, peso, fumador, sexo) - PELIGRO!
detach(df)  # Elimina de la memoria las columnas del data frame (debe hacerse siempre cuando no se necesite más)

# Acceso lógico a elementos
df[df$sexo == "M", ]  # Devuelve las filas donde el sexo sea masculino (todas las columnas)
subset(df, subset = sexo == "M", select = peso)  # Devuelve los elementos de la columna "peso" donde el sexo sea masculino
subset(df, sexo == "M" & peso < mean(peso))      # Devuelve los elementos masculinos con peso menor a la media total

# Funciones para obtener información simple
# NOTA: Pueden usarse para cambiar los nombres de las columnas y filas
names(df)     # Devuelve los nombres de las columnas del data frame (al igual que colnames())
colnames(df)  # Devuelve los nombres de las columnas del data frame (al igual que names())
rownames(df)  # Devuelve los nombres de las filas del data frame
summary(df)   # Resume cada columna (dependiendo de su tipo)

# Funciones con data frames
head(df, n = 5)         # Muestra las 5 primeras filas del data frame
tail(df, n = 3)         # Muestra las 3 últimas filas del data frame
table(df$sexo)          # Contar cuántos sujetos hay de cada género
table(fumador, sexo)    # Ver las combinaciones de sujetos por género y hábito de fumar
df[order(df$altura), ]  # Ordenar las filas del data frame por altura
aggregate(altura ~ sexo, data = df, FUN = mean)              # Altura media separada por "sexo" (hombres y mujeres)
aggregate(altura ~ sexo + fumador, data = df, FUN = mean)    # Altura media separada por cada combinación de "sexo" y "fumador"

# Transformar data frames
cbind(df, edad = c(36, 19, 25, 42, 17, 49, 61, 18, 21, 58))  # Añadir una columna al data frame
fila <- data.frame(altura = 178, peso = 72, fumador = "Si", sexo = "F", edad = 25)  # Preparar la fila a añadir
rbind(df, fila)  # Añadir fila al data frame
df <- transform(df, altura.m = 0.01*altura, peso = peso*1000)  # Crear altura.m (en m) y transformar los pesos de Kg a g
df$sexo <- factor(df$sexo)  # Transformar la columna sexo a factor (summary() dirá cuántos M y cuántos F hay)
```

R ofrece una serie de **conjuntos de datos nativos** que pueden verse ejecutando `data()`. Están en forma de data frames y uno de los más populares es el `iris data set`, que contiene información sobre flores. Para ver sus primera filas podemos ejecutar `head(iris, 4)` y, para más detalles, `?iris`.

Actualmente, existen **variantes más modernas** de los data frames, como los ***data tables*** del paquete `{data.table}` o los ***tibbles*** del `tibble` (forma parte de la colección `tidyverse`). Los **data tables** ocupan menos espacio que los data frames, mejoran el tiempo de ejecución al trabajar con CSVs y añaden funciones como `group_by()` para ordenar las tablas, entre otras. Son compatibles con las funciones para los data frames *normales*. Respecto a los **tibbles**, se verán en más profundidad en el [tema 5](5_manejo_de_datos.md).

### 3.5. Arrays Multidimensionales (pág. 37)
Los arrays son como bloques de varias matrices. Son **multidimensionales y homogéneos**, ya que solo pueden contener **objetos atómicos**. Su uso se asemeja mucho al de las matrices:
```r
# Creación
a1 <- array(data=letters[1:24], dim=c(3, 4, 2))  # Grupo de dos matrices con 3 filas y 4 columnas cada una
a2 <- array(data=1:16, dim = c(2, 3, 3, 2))      # "Matriz" de 3x2 donde cada elemento es una matriz con 2x3

# Acceso a elementos
a1[1, 3, 2]  # 1a fila de la 3a columna de la 2a matriz
a1[, 1, 1]   # Toda la columna 1 de la primera matriz
a1[1, , 1]   # Toda la fila 1 de la primera matriz
a1[, 1, ]    # 1a columna de cada matriz
a1[, , 2]    # 2a matriz

# Funciones
length(a1)  # Cantidad de elementos en un array (24)
dim(a1)     # Dimensión del array (3, 4, 2)
```
