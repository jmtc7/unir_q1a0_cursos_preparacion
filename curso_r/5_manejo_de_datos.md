# Manejo de Datos
## 1. Introducción
Los objetivos de este tema son:
- Importar y exportar ficheros de datos en R desde ficheros TXT, CSV, Excel y para programas comerciales como SAS, SPSS o Stata.
- Usar las principales acciones de manipulación de data frames con *pipes* en `dplyr`.
- Comprender cómo combinar `group_by()` y `summarize()` para obtener resúmenes de datasets.

## [2. Importar Datos (pág. 4)](https://unir.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=158e7ec6-7537-4ad4-8450-af1d00d05914)
Podemos importar datos de **archivos TXT** utilizando `read.table()`, que espera un archivo formateado como una tabla y que generará un data frame con los datos contenidos en él. Los argumentos principales de esta función son:
- `file`: Ruta hasta el archivo a leer. Debe ser una cadena de texto. Podemos escribirla o solicitarla al usuario con `file.choose()`.
- `header`: Booleano para indicar si el archivo contiene los nombres de las variables en la primera línea o no. De no tener nombres para las columnas, se puede utilizar el argumento `col_names` para pasarle una lista con los **nombres para las columnas** que queramos utilizar.
- `sep`: Carácter que separa cada columna. Los más comunes son `,`, `;`, ` ` y `\t`.
- `dec`: Carácter para separar la parte entera de la parte decimal de los números. Casi siempre es `.`, pero a veces puede ser `,`.
- `stringsAsFactors`: Booleano para que las columnas con cadenas de texto se almacenen como factores.
- `comment.char`: Es común que los archivos de datos comiencen con un comentario explicativo de los datos. Estas líneas suelen comenzar por un carácter, que podemos especificar utilizando este argumento para que sean ignoradas. Normalemente se usa `#`.
  - Si el fichero no utiliza ningún carácter específico para indicar que una línea es un comentario, se puede utilizar el argumento `skip`, que permite ignorar la cantidad de línas que se especifique.

Cabe destacar que `read.table()` puede leer ficheros en **local** o desde una URL de un archivo **web**. También podemos descargar archivos utilizando `download.file()`. En el script [actividades/ejercicios_tema5_manejo_de_datos.R](actividades/ejercicios_tema5_manejo_de_datos.R) se muestra un ejemplo de código que usa [datos locales](actividades/datos/t5/medidas_cuerpo.txt) y [datos remotos](https://www.biostatisticien.eu/springeR/imcenfant.txt).

Para **archivos CSV** (Comma-Separated Values) se puede utilizar `read.table()`, pero existen versiones optimizadas como `read.csv()`. En el mismo script hay **ejemplos** que usan los datos [gapminder_es.csv](https://github.com/cienciadedatos/datos-de-miercoles/blob/c8983df96111941319d9e50975d8f514a7003293/datos/2019/2019-04-24/gapminder_es.csv) (también disponibles [aquí](actividades/datos/t5/gapminder_es.csv)). Sus **argumentos clave** son los mismos que `read.table()`, sólo cambian sus valores por defecto.

Para **hojas de Excel** (archivos `.xls` y `.xlsx`) se suele usar el paquete `{readxl}`, que contiene la función `read_excel()`. A diferencia de las funciones anteriores, esta generará un `tibble` de `tidyverse`. El paquete también cuenta con las funciones `read_xls()` y `read_xlsx()`, que son más específicas y pueden evitar errores si sabemos el tipo de fichero con más detalle. Todas estas funciones leerán la primera hoja del fichero Excel por defecto. Si queremos **cargar una hoja en específico**, se usa el **argumento** `sheet`. Podemos obtener los **nombres de todas las hojas del archivo** utilizando `excel_sheets()`. Usaremos [datos oficiales del Gobierno de España](https://www.mapa.gob.es/dam/mapa/contenido/alimentacion/temas/consumo-y-tendencias-en-alimentacion/panel-de-consumo-alimentario/series-anuales/anuales/2024-datos-anuales-panel-consumo-hogares-base2021_v2.xlsx) (también disponibles [aquí](actividades/datos/t5/2024-datos-anuales-panel-consumo-hogares-base2021_v2.xlsx)) para este ejemplo. Otros argumentos útiles de estas funciones son:
- `skip`: Ignorar un número de filas iniciales potencialmente vacías o con datos irrelevantes.
- `range`: Cadena de texto con las celdas a importar en formato Excel. Por ejemplo: `"A1:B10"`.
- `col_names`: Booleano para indicar si la hoja a leer tiene nombres de las variables en la primera línea. Es decir, es equivalente al argumento `header` de `read.table()`.

Otra opción para importar datos es desde el **menú de RStudio**. Desde la barra de herramientas, podemos acceder a `File/Import Dataset/` (también podemos hacer click derecho desde el explorador de archivos o utilizar la opción `Import Dataset` desde la ventana del entorno), lo que mostrará varios formatos, usando R base o los paquetes `{readr}`, `{readxl}` o `{heaven}` del conjunto `tidyverse`. Esto permite elegir el archivo a cargar y ciertas opciones (nombre de la estructura de datos, presencia de encabezados, separador entre columnas, etc.) de forma gráfica. Al configurar todo, **RStudio generará en la consola el comando equivalente**, por lo que podremos copiarlo y añadirlo a nuestro script. Otra ventaja de hacerlo de esta manera es que RStudio muestra una **previsualización de los datos**, por lo que veremos si nuestra configuración es correcta o no. También desde RStudio, desde la **ventana *Environment***, se pueden abrir los data frames generados y **ordenar** de manera ascendente o descendente según alguna de sus columnas, **filtrar** para ver únicamente las filas que tengan cierto valor (o rango de ellos), etc.

Si queremos cargar **datos generados por R** (archivos `.RData` o `.rda`) utilizamos la función `load()`. Esto es útil si hemos generado ciertas estructuras de datos durante una **sesión de trabajo** y queremos continuar trabajando con ellas más tarde u otro día. También permite **compartir datos** entre distintas personas.

Finalmente, también es posible leer datos de **programas estadísticos comerciales**. Estos programas son muy comunes en ciertos campos. Por ejemplo, en **psicología** se usa mucho **SPSS Statistics**, de IBM, que genera archivos con extensión `.sav`. **STATA** es muy utilizado en **economía** y genera archivos `.dta`. Para esta tarea, se usa el **paquete `{heaven}`**, que soporta:
- **SAS**:
  - `read_sas()` para los archivos `.sas7bdat` y `.sas7bcata` de **SAS**.
  - `read_xpt()` para archivos de transporte SAS (versión 5 y 8).
  - `write_sas()` para escribir archivos `.sas7bdat` y `.sas7bcata`, aunque se considera más experimental.
- **SPSS**: 
  - `read_spss()` utiliza:
    - `read_sav()` para leer archivos `.sav` y `.zsav`.
    - `read_por()` para leer archivos `.por`.
  - `write_sav()` para escribir archivos `.sav`.
- **Stata**:
  - `read_dta()` y `read_stata()` leen archivos `.dta` hasta la versión 15.
  - `wrtie_dta()` escribe archivos `.dta` entre las versiones 8 y 15.
  
Otras formas de importar datos son paquetes como `{DBI}` o `{dplyr}` para **bases de datos**.

Un **paquete clave para importar datos** es `{readr}`, que forma parte del `{tidyvese}` (incluye 8 paquetes). Para usarlo, podemos instalar cualquiera de ellos. Su principal función es convertir un fichero de datos en un data frame de R. Incluye funciones para leer ficheros TXT y CSV, todas llamadas `read_*()` y con los mismos argumentos disponibles, aunque con distintos valores por defecto, como las ya mencionadas anteriormente (`read.table()`, `read.csv()`, etc.).

## 3. Leer Datos desde un Paquete (pág. 24)
R ofrece datos contenidos en paquetes cuyo objetivo suele ser practicar con las funciones de dichos paquetes. Uno de estos paquetes es `{datasets}`, que viene instalado por defecto. Para ver todos sus datasets podemos ejecutar `data(package = "datasets")`. Si no especificásemos `package`, obtendríamos todos los datasets de todos los paquetes disponibles en la sesión actual. Para utilizar cualquiera de estos datasets, basta con llamarlos por su nombre como si fuesen una variable más.

## 4. Exportar Datos (pág. 25)
Para **guardar todo el espacio de trabajo**, se utiliza la función `save.image()`, que guardará todas las variables existentes en un archivo `.RData`. Si solo queremos guardar **algunos objetos** pero no todos, se usa `save()`, enumerando los objetos a guardar separados por comas. Si solo vamos a guardar **un único objeto** (como listas), se utiliza `saveRDS()` y un archivo con la extensión `.rds`. Todos estos archivos son binarios y pueden volver a abrirse desde RStudio.

Para escribir un **fichero TXT** se utiliza `write.table()`. Los argumentos más comunes son:
- `x`: El data frame a guardar.
- `file`: El nombre del fichero a crear (se recomienda extensión `.txt`).
- `sep`: El carácter que se utilizará para separar las columnas.
- `row.names`: Booleano que indica si se deben escribir o no los nombres de las filas. Se recomienda dejarlo a FALSE para faciliar la re-lectura.
- `col.names`: Booleano que indica si se deben escribir o no los nombres de las columnas. Se recomienda dejarlo a TRUE.

Similarmente, para exportar a un **fichero CSV**, se utiliza `write.csv()` (si se quiere utilizar `;` como separador en vez de `,`, se usa `write.csv2()`).

Finalmente, para **ficheros Excel** se utiliza `write_xlsx()`, del paquete `{writexl}`.

## 5. Introducción al Tidyverse (pág. 32)
Los principios del ***Tidyverse*** son ordenar los datos con **una columna por variable y una fila por observación**. Para representar datos con ese estándar en R, utilizamos data frames o tibbles. Esta es su [web oficial](https://tidyverse.org/).

Otra característica del tidyverse es el **operador *pipe*** (`%>%`), que sirve para concatenar llamadas a funciones. Se lee como *después* o *luego*. Este operador pasa el elemento que está a su izquierda como argumento de la función que está a su derecha. Es equivalente al operador `|>` de R base, pero forma parte del paquere `{magrittr}` y es más flexible, ya que es compatible con todas las versiones de R y se puede insertar en cualquier parte del código, aunque es un poco más lento porque está implementado en R y no en C. **Si se trabaja con R >= 4.1. se recomienda utilizar el operador nativo `|>`**. Un ejemplo de uso sería `x <- 1:10 |> log() |> mean() |> sqrt()`, que se traduce en *Crear un vector, **luego** aplicarle el logaritmo, **luego** calcular la media y **luego** sacar la raíz cuadrada*.

Otro paquete importante del tidyverse es `{dplyr}`, que se centra en la **manipulación de datos**. En el tema 3 vimos cómo manipular datos con `[]`, `subset()`, `cbind()`, `rbind()`, etc. `{dplyr}` propone alternativas que generan un código más legible con funciones (llamadas *verbos*) como `filter()`, `select()`, `arrange()`, `mutate()`, `summarise()`, etc. Más detalles sobre la transformación de datos con `{dplyr}` se puede encontrar [aquí](https://rstudio.github.io/cheatsheets/html/data-transformation.html). Un ejemplo de uso sería:
```r
library(tidyverse)
datos <- read.table("actividades/datos/t5/IMCenfant.txt", skip=13)

# Selección por nombres de columnas
datos %>% select(SEXE, poids)      # Seleccionar las columnas "SEXE" y "poids"
datos %>% select(-c(SEXE, poids))  # Seleccionar todas las columnas EXCEPTO "SEXE" y "poids"
datos %>% select(-SEXE, -poids)    # Equivalente a lo anterior

# Selección condicional
datos %>% select(where(is.numeric))  # Selecciona elementos numéricos
datos %>% select_if(is.numeric)      # Equivalente a lo anterior
datos %>% select(starts_with("mo"))  # Selecciona elementos que empiecen por "mo"
datos %>% select(ends_with("le"))    # Selecciona elementos que acaben por "le"
datos %>% select(contains("oi"))     # Selecciona elementos que contengan "oi"
datos %>% filter(SEXE=="F", poids>18)  # Selecciona elementos que cumplan condiciones

# Modificación 
datos %>% mutate(taille = taille/100)  # Convertir la altura de m a cm
datos %>% mutate(across(where(is.numeric), function(x){(x-mean(x))/sd(x)}))  # Normalizar columnas numéricas
datos %>% mutate(across(where(is.numeric), scale))  # Equivalente a lo anterior
datos %>% mutate(across(contains("oi"), scale))     # Normalización columnas que contengan "oi"
datos %>% mutate(SEXE = ifelse(SEXE=="F", "FEMALE", "MALE"))  # Renombrar niveles del factor SEXE
datos %>% mutate(sexo = ifelse(SEXE=="F", "FEMALE", "MALE"))  # Equivalente a lo anterior creando nueva columna

# Encadenamiento de operaciones
datos %>% mutate(taille = taille/100) %>% mutate(imc = poids/taille^2)  # Modificar altura, luego crear "imc"

# Unir conjuntos de datos con variables en común
# Comparten ID, pero datosA tiene variables categóricas y datosB tiene variables numéricas
datosA = imcenfant %>% select(SEXE, zep) %>% rownames_to_column("ID")
datosB = imcenfant %>% select(where(is.numeric)) %>% rownames_to_column("ID")
datos1 <- datosA %>% inner_joint(datosB, by = "ID")  # Guardar filas existentes en ambos
datos2 <- datosA %>% left_join(datosB, by = "ID")  # Ignorar filas en B que no estén en A
datos3 <- datosA %>% right_join(datosB, by = "ID")  # Ignorar filas en A que no estén en B
datos4 <- datosA %>% full_join(datosB, by = "ID")  # Guardar todas las filas

# Obtención de resúmenes
datos %>% summarize(media = mean(taille), desvio=sd(taille))                 # Aplicar media y std a "taille"
datos %>% summarize(across(where(is.numeric), list(media=mean, desvio=sd)))  # Aplicar columnas numéricas
datos %>% group_by(SEXE) %>% summarize(across(taille, mean))       # Agrupadar "taille"  por género y aplicar media
datos %>% group_by(SEXE) %>% summarize(media=mean(taille), n=n())  # Calcular media y contar cuántas "taille" hay por género
```
 
## [6. Ejercicios (pág. 43)](https://unir.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=84c346d9-e210-43f3-87a8-af1f008595f7)
En este tema, se proponen 5 ejercicios para asegurar la comprensión de los conceptos presentados. Estos están resueltos en el archivo [actividades/ejercicios_tema5_manejo_de_datos.R](actividades/ejercicios_tema5_manejo_de_datos.R) y en el vídeo cuyo enlace está en el título de esta subsección se presenta la soluciones oficial al ejercicio 4.
