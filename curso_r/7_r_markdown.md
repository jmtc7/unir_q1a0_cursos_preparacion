# Introducción a R Markdown

## 1. Introducción
Para hacer informes y presentaciones se suelen crear los documentos en Word, Powerpoint, LaTeX, etc., se analizan los datos y se generan gráficos en R, Python, Stata, Excel, etc. y se exportan y se pegan los resultados de estos programas en los documentos de los primeros. Esto resulta ineficiente y fomenta equivocaciones si cambian los datos, lo que motiva el uso del R Markdown.

R Markdown es un **procesador de texto que admite código y gráficos de R**, lo que permite combinar el texto del informe con el procesado y visualización de datos. El resultado final puede **exportarse** en PDF, Word, HTML, etc.

El objetivo de este tema es ser capaz de:
- Crear y editar un documento en R Markdown.
- Insertar tablas y gráficos en R Markdown.
- Elaborar un informe en las distintas opciones de salida (HTML, PDF, etc.).


## 2. Bases del R Markdown (pág. 4)
Los documentos  R Markdown son documentos de texto con extensión `.Rmd`. Al crearse desde RStudio, se nos pedirá el título, el autor y la fecha del documento, aunque también se puede crear un **archivo vacío**. Una vez creado, se utiliza el botón `Knit` para **compilarlo** y generar el fichero de salida. Al hacer esto, internamente el paquete `{rmarkdown}` utiliza el paquete `{knitr}` para ejecutar los bloques de código R y generar las salidas correspondientes, que se pegan en un documento markdown intermedio. Finalmente, se usa *pandoc* para exportar al formato de salida escogido.

Los documentos R Markdown tienen **3 partes**:
- **Encabezado** (*YAML header*): Al principio del documento, delimitado por `---` al principio y al final. Define metadatos como el título, autor, fecha, etc. del documento. En él pueden incluirse muchas opciones para personalizar el documento de salida.
- **Bloques de código** (*chunks*): Para indicar su comienzo se utiliza ```` ```{r} ````, y ```` ``` ```` para cerrarlos. También se puede añadir código en Python, Bash, etc. Desde la barra superior se puede ejectura todo el código, solo el bloque actual, etc.
- **Texto**: Cualquier otra parte del documento será interpretada de acuerdo con la sintaxis markdown clásica. Una particularidad útil del R Markdown es que se pueden generar **tablas** a partir de dataframes con `knitr::kable()`, a las que se les puede dar un título con el argumento `caption`.


## 3. Formatos de salida (pág. 10)
En el **encabezado** del documento debe especificarse el tipo de salida mediante la variable `output`. Todos los **tipos de salida** figuran en la [documentación oficial de R Markdown](https://rmarkdown.rstudio.com/lesson-9.html). Si queremos información adicional sobre alguno de esos formatos, se hace igual que con las funciones de R. Es decir, `?html_document` abrirá la documentación de `html_document`.

Los formatos de salida son como funciones, se le pueden pasar argumentos. Por ejemplo:
```r
---
title: "Mi primer R Markdown"
author: "Nombre del Autor"
date: "`r Sys.Date()`"
output:
    html_document:
        toc: true       # incluir una Table Of Content (toc)
        toc_float: true
        toc_depth: 2    # hasta 2 niveles en el toc (esto es # y ##)
---
```

Una particularidad al trabajar **exportando PDFs** es que estos se generan pasando por un **archivo LaTeX intermedio**. Por defecto, este se elemina, pero el argumento `keep_tex` **permite guardarlo**.

Cabe destacar que al pulsar el botón `Knit` se compilará el **primer tipo de documento** de salida especificado en el encabezado, pero con el menú desplegable se pueden **generar otros tipos de salida**.


## 4. Bloques de Código y Código en Línea (pág. 15)
Como ya se ha mencionado, para indicar **bloques de código** se usa ```` ```{r} ```` y ```` ``` ````. Sin embargo, si queremos mostrar únicamente los resultados de algunas operaciones, se puede utilizar **código en línea** o *inline code*. Para hacer esto, ocultamos el bloque de código con `include = FALSE` de la siguiente manera:
````r
```{r codigo_en_linea, include = FALSE}
res <- mtcars %>% summarize(media = mean(mpg), desvio = sd(mpg), n = length(mpg))
```

La muestra es de tamaño `r res$n`, su media es `r res$media` y su desviación estándar es `r res$desvio`.
````

De esta manera, se computarán las estadísticas sin mostrar el código R utilizado. Además, podemos acceder a los resultados obtenidos desde el texto. Como nota adicional, para **formatear números en textos** se recomienda utilizar `round()`. Por ejemplo: ```` la media es `r round(res$media, 2)` ```` redondeará `res$media` utilizando 2 decimales.

Aunque no es necesario, se le pueden dar **nombres a los bloques** de código utilizando `{r nombre_del_bloque}`, lo que ayuda cuando hay **errores de compilación**.

Además de la ya vista `include`, hay más **opciones para bloques**. Todas están documentadas [aquí](https://yihui.org/knitr/options/), pero las principales son:
- `eval`: **Ejecutar o no** el código. Si no se ejecuta, no se generarán sus resultados ni variables.
- `include`: Mostrar o no el **código y sus resultados** en el documento compilado.
- `echo`: Mostrar o no el **código** en el documento compilado. Si está a `FALSE`, el código no se mostrará, pero sí sus resultados.
- `message`: Mostrar o no los **mensajes** generados por R al ejecutar el código. `TRUE` por defecto.
- `warning`: Mostrar o no los **mensajes de advertencia** generados por R al ejecutar el código. `TRUE` por defecto.
- `results`: Controla cómo se muestran los resultados de la evaluación. Sus posibles valores son las siguientes cadenas de texto:
  - `"hide"`: No mostrar los resultados.
  - `"asis"`: Muestra los resultados línea a línea y los formatea como si fuesen texto.
  - `"hold"`: Muestra todas las salidas al final del bloque de código.
  - `"markup"`: Muestra los resultados línea a línea precedidos de `##`. Es el valor por defecto.
- `error`: Continuar o no con la compilación aunque haya errores en el código.

Si queremos aplicar una o varias opciones a todos los bloques de código utilizamos las **opciones globales** mediante `knitr::opts_chunk$set()` ejecutada en un bloque de código. Por ejemplo: `knitr::opts_chunk$set(echo = FALSE, warning = FALSE, message = FALSE)`. Por convención, todas estas opciones especiales, junto a la inclusión de los paquetes que vayan a utilizarse, suelen colocarse en un bloque especial llamado `setup`.


## 5. Expresiones Matemáticas (pág. 39)
Para incluir expresiones matemáticas se utiliza la sintáxis de [LaTeX](https://www.latex-project.org/). Si queremos que aparezca **en línea** con el texto se encierra entre dos `$` y si queremos que aparezca en una **línea distinta**, abrimos y cerramos la epxresión con `$$`. Como resumen de operaciones básicas:
- Las **potencias** se indican con `^`.
- Las **raíces cuadradas** con `\sqrt{numero}`.
- Las **fracciones** con `\frac{numerador}{denominador}`.
- El **signo ±** con `\pm` (de *plus-minus*).
- El **signo ≠** con `\neq` (de *not equal*).

También se pueden crear matrices declarándolas entre `\begin{array}{formato}` y `\end{array}`. Los **formatos de matrices** son `pmatrix` (`()`), `bmatrix` (`[]`), `Bmatrix` (`{}`), `vmatrix` (`| |`) y `Vmatrix` (`|| ||`). Los **cambios de columna** se indican con `&` y los de **fila** con `\\`. Para indicar tamaños arbitrarios se pueden generar **puntos suspensivos** en distintas direcciones con `\cdots`, `\vdots` o `\ddots`. Por ejemplo:
```r
$$
A_{m, n} = 
    \begin{array}{formato}
        a_{1, 1} & a_{1, 2} & \cdots & a_{1, n} \\
        a_{2, 1} & a_{2, 2} & \cdots & a_{2, n} \\
        \vdots   & \vdots   & \ddots & \vdots   \\
        a_{m, 1} & a_{m, 2} & \cdots & a_{m, n} \\
    \end{array}
$$
```

Para **sistemas de ecuaciones** o **listados de condiciones** podemos utilizar un único **delimitador** con `\left` o `\right`, como en:
```r
$$
|x| = \left\{
    \begin{array}[ccl]
    x, & & \text {si } x \geq 0 \\
    -x, & & \text {si } x < 0
    \end{array}
    \right}
$$
```

Para más detalles, puedes consultar el [Wikibook de LaTeX](https://en.wikibooks.org/wiki/LaTeX/Mathematics).


## 6. Ejercicios (pág. 44)
En los archivos `.Rmd` de la carpeta [actividades/tema7_r_markdown/](actividades/tema7_r_markdown/) se incluye la resolución de los 4 ejercicios propuestos en este tema. En este [vídeo](https://unir.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=7917f8eb-3127-4366-ac66-af2000c27d7d) se soluciona el cuarto ejercicio.
