# Curso de Iniciación a Python Orientado a Datos
Este curso está dividido en las siguientes secciones:
  1. [**Introducción**](1_introduccion.md)
  2. **Primeros Conceptos***
     1. Identificadores, palabras reservadas, comentarios y sangría/indentación
     2. Variables, constantes, tipos de datos y operadores
  3. **Programación Básica***
     1. Listas, tuplas, diccionarios y conjuntos
     2. Expresiones condicionales, bucles e iteradores
  4. [**Funciones****](4_funciones.md)
     1. Definición, argumentos, retornos y documentación
     2. Funciones básicas de los módulos *math*, *sys*, *os*, *random* y *logging*
     3. Funciones anónimas/lambda
     4. Decoradores
  5. [**Organización del Código****](5_clases.md)
     1. Creación, documentación y uso de módulos y paquetes
     2. Programación orientada a objetos (POO): Clases, atributos, métodos y herencia
  6. [**Aspectos Avanzados**](6_aspectos_avanzados.md)
     1. Expresiones regulares (RegEx)
     2. Gestión de errores
     3. Compresión de listas, diccionarios y conjuntos
  7. [**Análisis de Datos**](7_analisis_datos.md)
     1. NumPy: Arrays, matrices y funciones
     2. Pandas: Series, dataframes y funciones
     3. Lectura, procesado y escritura de ficheros CSV
  8. [**Visualización de Datos**](8_visualizacion_datos.md)

> \* No tiene notas debido a que el contenido estaba previamente adquirido.
> 
> ** Tiene notas parciales o extendidas con respecto al contenido del curso.

Cada sección tiene un fichero Markdown `*.md` asociado que contiene las notas relativas a ella. También existe una carpeta `actividades/` que contienen los ejercicios prácticos realizados para este curso, así como algunos scripts con código de ejemplo para las secciones 7 y 8 del curso.

## Actividades
El contenido de la carpeta `actividades/` se divide en:
- **Actividad 1: Calculadora de promedios**: Aplicación que permite calcular promedios y obtener información sobre calificaciones académicas a través de una CLI. Incorpora gestión de errores.
- **Actividad 2: Sistema de inventario**: Aplicación que permite gestionar un inventario a través de una CLI y una estructura de clases, incorporando gestión de errores.
- **Actividad 3: Análisis de una red de tiendas**: Se procesan varios archivos CSV con información sobre ventas, inventario y satisfacción de clientes de varias tiendas. Se obtienen varias estadísticas divididas por tienda y tipo de producto, algunas de ellas combinando la información obtenida de distintos ficheros. Se usa `NumPy` y `Pandas`.
- **Actividad 4: Visualizaciones**: Muestra varias visualizaciones con `Matplotlib` y `Seaborn` de un conjunto de datos almacenado en un CSV, que es procesado con `Pandas`.
- **Script de ejemplo de la sección 7**: Muestra cómo hacer varias operaciones con `NumPy` y `Pandas`.
- **Scripts de ejemplo de la sección 8**: Hay dos, uno que utiliza `Matplotlib` y otro que utilizar `Seaborn`. Ambos muestran cómo hacer subplots, personalizar las gráficas y crear gráficos univariantes, bivariantes y multivariantes.
- **requirements.txt**: Fichero con la lista de dependencias a instalar para poder ejecutar todos los scripts y iPythonNotebooks en la carpeta. Las versiones utilizadas para desarrollar y testear dichos scripts están especificadas.
