# Conceptos Básicos
## 1. Introducción
El objetivo de este tema es familiarizarse con R y con RStudio. Estos son los objetivos concretos:
- Familiarizarse con el entorno de RStudio.
- Describir el propósito y el uso de cada panel de RStudio.
- Establecer el directorio de trabajo para una sesión de RStudio.
- Definir variables y asignarle valores.
- Conocer funcionalidades básicas de la consola de R.
- Crear, guardar y abrir scripts de código R.
- Comprender la utilidad de trabajar con proyectos autocontenidos.
- Gestionar paquetes.

## [2. RStudio](https://unir.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=aa800c11-0d46-4efc-9d3c-af170096fbc3)
A pesar de que es posible hacer todo desde una consola interactiva de R y un editor de texto, utilizar un IDE como RStudio facilita enormemente las tareas. Al abrirlo, encontraremos **3 paneles**. Una con una **terminal de R**, otra con el **entorno e historial** y otra con un **explorador de archivos y gráficos**. También existe un cuarto panel, el **editor de sintaxis**. Para acceder a él, debemos crear un nuevo archivo.

Aunque esa es la configuración por defecto, se puede personalizar desde el menú `Tools/Global Options/`. Por ejemplo, se puede cambiar el tema desde `Appearance/Editor theme/` a `Tomorrow Night Bright`. Desde `Pane Layout` podemos cambiar la disposición de los paneles.

Desde el **editor de sintaxis** podemos editar scripts. Es posible ejecutar todas las líneas, una parte de ellas, o una única línea con los botones de la parte superior derecha. Al hacerlo, veremos las salidas generadas en el panel con la **terminal**. Si queremos limpiar la terminal, podemos utilizar `Ctrl+L`.

También veremos aparecer los objetos creados en el panel ***Environment***, junto a su tipo, longitud, etc. Desde el botón `List/Grid` de la parte superior derecha podemos cambiar la visualización de las variables. Desde los botones arriba a la izquierda podemos **exportar o importar sesiones de trabajo** (archivos `.RData`). Otra opción muy útil es la de **importar datasets** desde distintos formatos. También podemos **borrar objetos** de la sesión de trabajo. Desde el mismo panel se puede acceder al ***History***, que mostrará todas las operaciones realizadas (en la sesión actual y en sesiones anteriores), lo que permite reutilizarlas. Esta pestaña incluye un buscador en su esquina superior derecha. También incluye botones para elminar comandos del historial. La última pestaña es la de ***Tutorial***, que enseña las bases de R y RStudio con pequeños ejercicios interactivos.

El último panel contiene las siguientes pestañas:
- ***Files***: Explorador local de los archivos del **directorio de trabajo** actual. Permite cambiar el directorio de trabajo. También es posible obtenerlo con la instrucción `getwd()` y cambiarlo con `setwd()`.
- ***Plots***: Visualizador de los gráficos generados. Permite navegar entre los distintos gráficos creados, abrirlos en una ventana grande e independiente, exportarlos como imagen, PDF o al portapapeles y borrar uno o todos los gráficos creados.
- ***Packages***: Explorador de los paquetes instalados. Los paquetes seleccionados son los que están disponibles en la sesión actual. También permite **instalar o actualizar*** paquetes.
- ***Help***: Contiene múltiples links útiles hacia cursos, manuales, listas de paquetes, *cheat sheets*, foros, etc. También tiene un buscador donde podemos buscar funciones o paquetes.
- ***Viewer*** y **Presentation***: Permiten visualizar archivos específicos, como R Markdown.

## 3. Variables y Tipos
La asignación de valores a variables en R se puede realizar de tres maneras: `x = 10`, `x <- 10` o `10 -> x`, pero la forma tradicional es `x <- 10` (o `x = 10` cuando se pasan argumentos a funciones). Al igual que en Python, todo son objetos (variables, funciones, etc.). Los elementos más básicos se denominan **objetos atómicos** y son:
- `character`: Caracteres individuales y cadenas de texto. Aunque R soporta las comillas simples ('), por convención, se usan las dobles (").
- `numeric`: Todos los tipos numéricos (enteros, con coma flotante, expresados en notación exponencial, constantes `Inf` y `NaN`, etc.).
- `integer`: Por defecto, en R todos los números se tratan como `double`. Para crear enteros, debemos utilizar `as.integer()`.
- `complex`: Valores con parte imaginaria (denotada por el sufijo `i`).
- `Logical`: Valores booleanos, representados con palabras reservadas `TRUE` y `FALSE`.

Normalmente, **la clase y el tipo** de todos los objetos coinciden, excepto para los objetos cuya clase es `numeric`, ya que pueden ser de tipo `integer` o `double`. Podemos obtenerlos ejecutando `class(objeto)` y `typeof(objeto)`.

Es posible ***coercionar*** los tipos de datos, es decir, convertir de un tipo a otro. Para ello, usamos funciones como `as.logical()`, `as.integer()`, `as.numeric()`, `as.complex()`, `as.characte()` o `as.factor()`. Hay más de 100 en el paquete base. Podemos verlas todas con `ls(pattern = "^as", baseenv())`. Las coerciones deben hacerse desde los tipos más sencillos hacia los más complejos, es decir: `logical` -> `integer` -> `numeric` -> `character`.

## [4. Scripts](https://unir.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=b04c2716-119e-4be3-90d9-af1800c0d7a9)
Los scripts son esenciales para poder automatizar procesos y evitar así tener que ejecutar todos los comandos a través de la consola uno a uno. Tienen la extensión `.R`.

En RStudio utilizamos el **editor de sintaxis** para crear y editar scripts. Este presenta varias funcionalidades, como el coloreado de distintos elementos del script (comentarios, valores, identificadores, paréntesis, etc.), autocompletado, sugerencias de argumentos (utilizando el tabulador), etc. También permite guardar, ejecutar y abrir los scripts creados.

## [5. Proyectos](https://unir.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=335d7c45-9231-45cb-9552-af1800cdf339)
Los proyectos permiten organizar el trabajo en R en carpetas. Se pueden crear nuevos proyectos desde la pestaña `File` en la barra superior de RStudio. Al crear un nuevo proyecto, el **directorio de trabajo** será la carpeta del proyecto. Además, dentro de dicha carpeta se habrá creado un archivo `.Rproj`, que será el archivo a abrir si queremos abrir el proyecto.

## [6. Biblioteca de R y Paquetes](https://unir.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=a350a466-bd71-4f37-a3e8-af19009fbd7a)
A menudo vamos a necesitar funcionalidades que no están disponibles nativamente en R. Es por ello que utilizamos los **paquetes externos**. Como ejemplo, usaremos el **paquete [{datos}](https://cran.r-project.org/web/packages/datos/readme/README.html)**, que es la versión en español de unos datos que se suelen usar para hacer ejemplos en R. Si conocemos el nombre exacto del paquete a **instalar**, podemos ejecutar la **función** `insta.packages("datos", dependencies = TRUE)`. El argumento `dependencies` permite elegir si queremos descargar las dependencias del paquete o no. Si no conocemos el nombre exacto del paquete, podemos utilizar el **instalador del explorador de paquetes**, que permite buscar. También ofrece la opción de instalar o no las dependencias del paquete mediante un *checkbox*. La última opción es utilizar la opción `Tools/Install Packages/`, que abrirá la misma interfaz que el explorador de paquetes.

Una vez hemos instalado un paquete, podemos **cargarlo** utilizando `library(datos)`. Tras hacer eso, en la ventana del explorador de paquetes veremos nuestro paquete seleccionado. Otra opción es seleccionarlo en el explorador de paquetes. Como clarificación, la ***librería*** a la que se refiere la función `library()` es la carpeta de nuestro ordenador en la que se almacenan todos los paquetes instalados. Los paquetes NO son librerías. Los paquetes están contenidos en la librería de nuestro sistema.

Para **actualizar** los paquetes, se utiliza el explorador de paquetes.
