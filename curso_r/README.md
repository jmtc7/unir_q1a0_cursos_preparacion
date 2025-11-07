# Curso de Iniciación a R
Este curso está dividido en las siguientes secciones:
1. [**Introducción**](1_introducción.md)
   1. Instalación
   2. Utilización Básica
2. [**Conceptos Básicos**](2_conceptos_básicos.md)
   1. RStudio
   2. Scripts y Proyectos
   3. Biblioteca de R y Paquetes
3. [**Estructuras de Datos**](3_estructuras_de_datos.md)
   1. Vectores y Factores
   2. Listas
   3. Matrices
   4. Data frames
   5. Arrays
4. [**Programación Básica**](4_programación_básica.md)
   1. Operadores y Funciones Matemáticas
   1. Estructuras Condicionales
   2. Estructuras Iterativas
   3. Funciones y Argumentos
5. [**Manejo de Datos**](5_manejo_de_datos.md)
   1. Importar Datos R, TXT, CSV, Excel, SAS, SPSS y Stata
   2. Exportar Datos R, TXT, CSV y Excel
   3. Introducción al Tidyverse
6. [**Visualización de Datos**](6_visualización_de_datos.md)
   1. Gráficos Básicos con plot() y Superposición de Elementos
   2. Otros Gráficos con hist(), boxplot() y barplot()
   3. Gŕaficos con {GGPlot2}
7. [**Introducción al R Markdown**](7_r_markdown.md)
   1. Bases del R Markdown
   2. Formatos de Salida
   3. Bloques de Código y Código en Línea
   4. Expresiones Matemáticas con LaTeX
8. [**R y Bases de Datos**](8_bases_de_datos.md)
   1. Conexión con MySQL, SQLite y MongoDB
   2. Manipulación y Análisis de Datos
   3. Visualización de Datos y Reporting

Cada sección tiene un fichero Markdown `*.md` asociado que contiene las notas relativas a ella. Algunos títulos en dichos ficheros tienen links asociados a los vídeos donde se profundiza en los detalles de las secciones correspondientes

También existen la **carpeta** `actividades/`, que contiene los **ejercicios prácticos** realizados para este curso. Dentro de ella encontramos múltiples archivos con los ejercicios de cada tema. Algunos temas tienen una subcarpeta dedicada, ya que requieren de múltiples archivos.

## Actividad Final
La actividad final consiste en un ejemplo detallado de las tareas típicas a realizar en un proyecto de datos. Todo está implementado en el fichero R Markdown [Enunciado Actividad Final.Rmd](actividades/actividad_final/Enunciado%20Actividad%20Final.Rmd). El objetivo es comprender todo el código y por qué se hace cada parte del mismo. El **ejemplo** incluye:
- **Carga, resumen, limpieza y transformación** de datos
  - Cargar un CSV en un dataframe
  - Resumir los datos visualizando las primeras muestras y algunas métricas estadísticas y valores de cada variable
  - Identificar cuántos valores faltantes hay en cada columna
  - Eliminación de filas con valores faltantes
  - Imputación de valores faltantes (usando el valor medio de la variable)
    - Se añade una nueva variable para indicar en qué filas se han imputado valores
  - Normalización de una variable (edad)
  - Convertir una variable categórica a partir de una numérica (clasificar edades en joven, adulto, etc.)
  - Convertir una variable numérica en una categórica (tratar ocupaciones como un factor numérico)
  - Agrupar valores categóricos poco comunes en un nuevo valor ("otros")
- **Visualización** de datos
  - Histogramas de variables numéricas (edad y versión numérica de la ocupación)
  - Diagrama de barras de variables categóricas (educación y versión categórica de la edad) y numéricas (versión numérica de la ocupación e ingresos)
  - Diagrama de cajas para visualizar la distribución de la edad dividida por género
  - Número medio de coches de los clientes agrupados por su estado civil
  - Diagrama de barras de bicis compradas por cada nivel educativo
  - Gráfico de dispersión que relaciona edad e ingresos de los compradores (distinguiendo entre géneros)
- **Análisis explorativo** de los datos (EDA) para comprender las variables
  - Ingreso medio de los compradores
  - Ingreso medio de cada nivel educativo
  - Buscar correlación entre número de coches y número de hijos

Además, se proponen una serie de **retos**:
- Edad media entre los que compraron bicicletas y los que no
- Número medio de hijos de los compradores agrupados por región
- Diferencia entre los ingresos medios de cada género (mujeres respecto a hombres y hombres respecto a mujeres)
- Contar cuántas personas con más de $ 50.000 de ingresos compraron o no compraron bicicletas
- Crear una variable categórica dividiendo la edad en 3 grupos y crear un gráfico de barras que compare cuántos en cada grupo compraron o no compraron.
- Calcular la correlación entre el número de coches y el ingreso de todas las personas. Repetir sólo para los que compraron y sólo para los que no compraron.
- 