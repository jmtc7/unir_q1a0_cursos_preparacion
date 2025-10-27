# Visualización de Datos
# 1. Introducción
R cuenta con funciones para generar gráficos de nubes de puntos, líneas, barras, circulares, etc. También se pueden crear histogramas y curvas de densidad. Estos gráficos son útiles para explorar los datos y encontrar patrones. Todos pueden ser almacenados para reutilizarlos posteriormente.

Los objetivos de este tema son:
- **Generar gráficos** adaptados al tipo de dato a visualizar (gráficos de barras, histogramas, diagramas de dispersión, diagramas de líneas y diagramas de caja) con R base y el paquete `{ggplot2}`.
- Entender la **gramática básica de los gráficos**, incluyendo estética, capas geométricas, estadísticas, escalas, colores, etc.

# 2. Gráficos Básicos con plot() (pág. 4)
La función `plot()` permite generar varios tipos de gráfico. Utilizando **dos vectores** con las coordenadas en X y en Y de una serie de puntos se puede obtener un **diagrama de dispersión**. También puede utilizarse para representar una **función**. Algunos de los **argumentos** más útiles de `plot()` son:
- `type`: Elige el tipo de gráfico a mostrar (`p` para puntos, `l` para líneas, `h` para histograma, `b` para líneas con puntos (*both*), `s` para barras (*steps*), etc.)
- **Personalizar los puntos**: `pch` permite elegir el **tipo** de puntos utilizado (hay 25 opciones), `cex` cambia su **tamaño** y con `col` escogemos el **color**. También podemos cambiar el **grosor de los bordes** con `lwd` (excepto en los tipos del 15 al 18). Los tipos de puntos del 21 al 25 permiten un **color de borde** diferente al del relleno, configurable con `bg`.
  - Podemos especificar **colores** por su **nombre** o por sus **códigos hexadecimales**. También existe el paquete `{colourpicker}`, que abre una **paleta de colores** para elegir colores y exporta sus nombres y códigos hexadecimales en código R. Una vez instalado el paquete, se accede a él a través del botón ***addins*** en la barra superior de RStudio.
- **Personalizar las líneas** es posible con `lty`, que permite 7 **tipos de línea**: `blank`, `solid`, `dashed`, `dotted`, `dotdash`, `longdash` o `twodash` (también pueden escogerse con números del 0 al 6). `lwd` se utiliza para elegir el **grosor de la línea**.
- Para **añadir títulos** se usa `main` para el título del gráfico y `xlab` e `ylab` para las etiquetas de los ejes. En ambos se puede utilizar `expression()` para incluir símolos o fórmulas matemáticas.
- `xaxp` y `yaxp` permiten modifiar los ***ticks*** de los ejes. Espera los valores mínimo y máximo que deben marcarse y la cantidad de marcadores a crear. Si se le da el valor `n`, no se mostrará ninguna marca en el eje.
- Para cambiar el **formato de los títulos** se utilizan `cex.main`, `cex.sub`, `cex.lab` y `cex.axis` para el **tamaño** del título, subtítulo, etiquetas de ejes y marcadores/*ticks* en los ejes. `font.main`, `font.sub`, `font.lab` y `font.axis` son para la **fuente** de los mismos elementos (`1` para texto plano/normal, `2` para negrita, `3` para cursiva y `4` para negrita y cursiva). `col.main`, `col.sub`, `col.lab` y `col.axis` configuran los **colores**.
- `bty`: Configura la **caja exterior**. Sus opciones son `o` para una caja entera (valor por defecto), `7` para bordes superior y derecho, `L` para bordes inferior e izquierdo, `U` para todos excepto el superior, `C` para todos excepto el derecho o `n` para no utilizar caja.

A continuación se muestran algunos ejemplos de distintos usos de `plot()` y de sus argumentos.
```r
# Crear datos
x <- 0:10
y = dbinom(x, size = 10, p = 0.3)

# Representación de una función
f <- function(x){x^2 +1}
plot(f)         # X entre 0 y 1 por defecto
plot(f, -1, 4)  # Rango de X personalizado entre -1 y 4

# Tipos de gráficos
plot(x, y, type = "p", main = "type = 'p'")  # Gráfico de dispersión/puntos
plot(x, y, type = "l", main = "type = 'l'")  # Gráfico de líneas
plot(x, y, type = "h", main = "type = 'h'")  # Histograma
plot(x, y, type = "b", main = "type = 'b'")  # Gráfico de líneas con puntos (both)
plot(x, y, type = "s", main = "type = 's'")  # Gráfico de barras (steps)
plot(x, y, type = "n", main = "type = 'n'")  # Gráfico vacío

# Tipos de puntos/marcadores
plot(x, y,
    pch = 21,         # tipo de punto
    col = "#0098CD",  # color de borde
    bg  = "#B8E5F5",  # color de fondo
    cex = 1.5,        # tamaño del punto
    lwd = 2)          # ancho del borde

# Títulos de gráfico y de ejes
x <- seq(-4, 4, length.out = 101)
y <- sin(x)
plot(x, y, type = "l",
    xaxp = c(-4, 4, 8),  # 8+1 marcas desde -4 hasta 4 en el eje X
    yaxp = "n",          # NO utilizar marcas en el eje Y
    ylab = expression(italic(sen) ~ '( ' * phi~')'),  # Títulos de ejes con fórmulas
    xlab = expression(paste("Angulo de fase ", phi)),
    main = 'El título', col.main = "#0098CD")  # Título del gráfico
```

# 3. Añadir Elementos a un Gráfico Existente (pág. 25)
Con `plot()` podemos crear un gráfico pero, en ocasiones, queremos añadir elementos adicionales a los gráficos existentes. Para ello, se utilizan las siguientes funciones (todas usan los **mismos parámetros de personalización que** `plot()`):
- `lines()` genera las líneas que unen a los puntos que recibe como argumentos, al igual que `plot(x, y, type = "l")`.
- `abline()` añade una recta a un gráfico. Si se le dan dos parámetros (`a` y `b`) generará la **recta** `y = a*x + b`. Si se le da sólo el parámetro `v` generará una recta **vertical** y si solo se le da el `h`, una **horizontal**.
- `curve()` con `add = TRUE` añade una **curva**. Espera una función algebraica con variable `x`.
- `points()` genera **puntos** nuevos.
- `text()` y `mtext()` generan **texto**. `text()` lo inserta en las **coordenadas** que se le indiquen mientras que `mtext()` tiene varias **posiciones predefinidas** (1=abajo, 2=izquierda, 3=arriba, 4=derecha).
- `legend()` añade una **leyenda** al gráfico. Espera recibir la posición con coordenadas o con las palabras clave: `bottomright`, `bottom`, `bottomleft`, `left`, `topleft`, `top`, `topright`, `right` o `center`. Al argumento `legend` se le asigna un vector con los nombres a mostrar. Con `cex`, `fill`, `col` y `border` se personaliza.

A continuación se muestra código de ejemplo para generar **múltiples línas** en un gráfico.
```r
# Gráfico de dispersión de base
set.seed(23)
x <- rnorm(50)
y <- 2*x +3 + rnorm(50)  # y = 2x + 3 con ruido
par(pty="s")
plot(x, y,
    pch = 21, col = "#0098CD", bg = "#B3B3B3", cex = 1.2, bty = "n",  # Formato puntos y quitar caja exterior
    xlim = c(-2,8), ylim = c(-2,8), xaxp = c(-4, 8, 6), yaxp = c(-4, 8, 6),  # Rango y ticks en ejes
    main = 'Grafico de dispersión', cex.axis = 0.8, cex.main = 0.9, col.lab = "#00566C")  # Título y formato

# Conectar todos los puntos (línea discontinua)
lines(x, y, col = "grey", lty = "dashed")

# Añadir línea y = 2x + 3, líneas verticales y horizontales y una grilla 
abline(a = 3, b = 2, col = "#EE9A00", lty = "dashed", lwd = 2)  # Personalizar color, tipo y ancho de línea
abline(v = 3, col = "blue", lty = "dashed", lwd = 2)            # Línea vertical
abline(h = 3, col = "violetred2", lty = "dashed", lwd = 2)      # Línea horizontal
abline(h = -2:8, v = -2:8, col = "lightgray", lty = "dotted")   # Grilla punteada en gris claro
```

Aquí se muestra un ejemplo de una **curva**:
```r
# Crear el gráfico
x <- sample(x = seq(-3, 3, 0.1), size = 10)
y <- dnorm(x)
plot(x, y, pch = 19, col = '#0098CD', ylim = c(0, 0.4), xlim = c(-3,3) )

# Añadir curva normal estándar
curve(dnorm(x), col = 'darkgreen', lty = "dashed", add = TRUE)
```

# 4. Otros Gráficos (pág. 35)
Los **histogramas** son muy útiles para visualizar las distribuciones de las variables continuas. En R se generan utilizando la función `hist()`. Algunos detalles a considerar son:
- Con `breaks` podemos elegir la **cantidad de barras** o *bins* a utilizar. Si no se especifica, R la elegirá automáticamente. También admite **otros valores** como los puntos de corte entre cada barra, una función para generar los puntos de corte, el nombre de uno de los algoritmos aceptados para calcular los intervalos (`Sturges`, `Scott` o `Freedman-Diaconis`), etc.
- **Por defecto**, muestra la **frecuencia** (es decir, cuántos elementos hay entre cada rango de valores), pero se puede utilizar `freq = FALSE` o `prob = True` para que el área de cada rectángulo represente la **probabilidad** de que un elemento perteneza a ese rango de valores (el área de todo el histograma será 1).
- El argumento `labels` añade una etiqueta con la **altura de cada barra**.
- La mayoría de **argumentos de** `plot()` son también válidos para `hist()` y también se pueden superponer lineas, puntos, textos, etc.

```r
# Histograma simple
NutritionStudy <- read_csv("datos/t5/NutritionStudy.csv")

hist(NutritionStudy$Fiber, freq = FALSE,
    border = 'grey', col = '#E5F8FF',
    xlab = 'Fibras (gr/sem)', ylab = 'Densidad',
    labels = TRUE, ylim = c(0,0.1),
    main = 'Hstograma de la variable Fiber',
    cex.main = 0.9, cex.lab = 0.9, cex.axis = 0.8,
    font.main = 4, font.lab = 2, font.axis = 3,
    col.lab = 'gray27', col.axis = 'midnightblue')

lines(density(Fiber), col = 'red')
```

Los **diagramas de caja y bigotes** o *boxplot* en inglés (pág. 39) permiten resumir varias características de una variable, como su simetría, su posición y su dispersión. Estos diagramas representan:
- **Primer y tercer cuartiles** con los lados inferior y superior de la **caja**, por lo que la caja representa el **50% central de los valores**.
- La **mediana** con la **línea central** en la caja.
- Los **límites** de lo que se consideran ***inliers***. Estos se determinan basándose en los cuartiles (se rechazan los valores más allá de 2 veces la altura de la caja). A estos se les denominan **bigotes**.
- Los ***outliers*** o puntos aislados que están más allá de los bigotes.

```r
# Diagrama de caja y bigotes personalizado
boxplot(NutritionStudy$Fiber, horizontal = FALSE, boxwex = 0.3, staplewex = 0.3, width=4, 
        col = "#E5F8FF", border = "#1D6786", col.axis = "#0A335D", cex.axis = 0.8)
title("Fibras consumidas (g/sem)",adj = 0.4,line=1)

# Múltiples boxplots en un mismo gráfico
boxplot(NutritionStudy$Fiber, NutritionStudy$Fat, col = "#E5F8FF",
        border="#1D6786", names = c("Fibras", "Grasas"))

# Múltiples boxplots segmentados por variable categórica (Sex)
boxplot(NutritionStudy$Fiber ~ NutritionStudy$Sex,
        col = rainbow(2, alpha = 0.5), names = c("Mujeres", "Varones"),
        xlab = 'Sexo', ylab = "Fibras consumidas (g/sem)")
```

Los **gráficos de barras** (pág. 42) son el equivalente de los histogramas para las variables categóricas o cualitativas. Sus argumentos son:
- `height`: **Alturas** de las barras a dibujar. Suelen ser la frecuencia con la que aparece cada valor de la variable a analizar.
- `names.arg`: **Etiquetas** de las barras.
- `legend.text`: Puede ser un **booleano** para activar o desactivar la leyenda o un vector con **nombres personalizados** para la leyenda.
- `beside`: Booleano para elegir si representar las barras apiladas o adosadas. `FALSE` por defecto.
- `horiz`: Booleano para elegir si representar el diagrama horizontal o vertical. `FALSE` por defecto.

```r
# Gráfico de barras con frecuencias relativas
bp <- barplot(tabla_prop, # datos
                main = "Gráfico de barras",                      # título del gráfico
                xlab = "Tracción",                               # Etiqueta del eje X
                names.arg = c("Total", "Delantera", "Trasera"),  # Etiquetas de las barras
                ylab = "Frecuencia relativa",                    # Etiqueta eje Y
                col = c("#C9A340", "#008FBF", "#F50A8BD4"),      # Color para cadabarra
                density = 50, angle = 45,                        # Densidad e inclinación de las líneas de sombreado de cada barras
                border = "white",                                # color del borde de las barras
                cex.names = 0.8)
text(bp, 0, round(tabla_abs, 1), cex=0.9, pos=3)                 # Texto con las frecuencias absolutas de cada barra

# Gráfico de barras apiladas (`beside = FALSE` por defecto)
# Si usamos `beside = TRUE`, las barras aparecerán adosadas
color <- c("#C9A340", "#008FBF", "#F50A8BD4")
leyenda <- ifelse(leyenda == 'AWD', "Total", ifelse(leyenda == "FWD", "Delantera", "Trasera"))
barplot(tabla2C_prop,
        main = "Gráfico de barras apiladas",
        xlab = "Size",
        names.arg = c("Grande", "Mediano", "Pequeño"),
        col = color,
        density = 50, angle = 45,
        border = "white",
        cex.names = 0.8,
        legend.text = leyenda,
        args.legend = list(x = "topleft",
                            bty = 'n',
                            cex = 0.9,
                            border = "white",
                            density = 50, angle = 45))
```

En la web [From Data to Viz](https://www.data-to-viz.com/) se pueden explorar más tipos de gráficos junto a un árbol de decisión para escoger cuál es el más apropiado. Además, en la [Galería Gráfica de R](https://r-graph-gallery.com/) podrás encontrar todos los gráficos que se pueden hacer con R junto con ejemplos y visualizaciones.

# 5. Gráficos de GGPlot2  (pág. 47)
El paquete `{ggplot2}` ofrece alternativas a las funciones del R básico para crear gráficos complejos y estéticos más fácilmente. Usa la **gramática de gráficos** y espera recibir tablas de **datos en formato *tidy*** (una variable por columna y una observación por fila). Para usar este paquete es muy útil tener a mano la [guía rápida de GGPLOT2](https://raw.githubusercontent.com/rstudio/cheatsheets/main/translations/spanish/data-visualization_es.pdf). Para trabajar con `{ggplot2}` es importante diferenciar entre los **3 elementos principales**:
- **Datos**: El conjunto de datos a representar.
- **Geometría**: Elementos visuales. Posibles geometrías son diagrama de barras, histograma, densidades suaves (*smooth densities* en inglés), gráfico Q-Q y diagrama de cajas.
- **Mapeo estético**: Mapeo entre las variables de los datos y las propiedades visuales de la gráfica. Por ejemplo, los rangos de los ejes, el tamaño/forma/color de los puntos, etc.

En resúmen, un **gráfico** asigna **datos** a los **atributos estéticos** (tamaño, forma, color, etc.) de los **objetos geométricos** (puntos, lineas, barras, etc.). Para construir gráficos con `{ggplot2}` se conectan argumentos con `+`. Por ejemplo: `ggplot(data = Cars2020) + geom_point(mapping = aes(x = Weight, y = HwyMPG))`, donde elegimos los **datos** en `Cars2020` y creamos **objetos geométricos** (puntos) con `geom_point` (que utilizan `Weight` y `HwyMPG` como coordenadas).

# 6. Ejercicios (pág. 80)

