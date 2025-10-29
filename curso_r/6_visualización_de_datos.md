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

A continuación se muestra código de ejemplo para generar **múltiples elementos** en un gráfico.
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

Para **gráficos de dispersión** se usa `geom_point()`, al que se le pueden añadir **capas en el mapeo** para personalizarlos. Por ejemplo, se pueden colorear los puntos basándonos en una variable categórica asignándosela a `colour` o cambiar su forma si se le asigna a `shape`. Atributos útiles para variables numéricas son `size` o `alpha`. Cualquiera de estas propiedades puede fijarse manualmente si se asignan fuera de `aes()`.
```r
# Gráficos de dispersión personalizados
ggplot(data = Cars2020) + geom_point(mapping = aes(x = Weight, y = HwyMPG, colour = Type))  # Con variable categórica
ggplot(data = Cars2020) + geom_point(mapping = aes(x = Weight, y = HwyMPG),
                                    shape = 21, colour = "#0098CD", fill = "#C1F5BF", size = 3)  # Con valores fijos
```

Los **gráficos de líneas** se crean con `geom_line()`, los de **barras** con `geom_bar()`, los de **cajas** con `geom_boxplot()`, etc. Una funcionalidad extra de `{ggplot2}` es generar **líneas suavizadas** con la regresión de un conjunto de puntos con `geom_smooth()`, que hace una regresión lineal local cuando hay menos de 1000 puntos. Si quieres una global, debes especificar `method="lm"`.  Todas estas funciones tienen el argumento `mapping` con el que pueden aplicarse la mayoría de las mismas personalizaciones, exceptuando algunas como la forma, que solo puede aplicarse a los puntos.

Todas las geometrías se organizan como capas, por lo que podemos aplicar múltiples capas para generar gráficos combinados con el símbolo `+`. Al hacer esto, se pueden utilizar mismos datos en todas las capas si se especifican en `ggplot()` o pueden filtrarse:
```r
# Mismos datos en todas las geometrías sin necesidad de repetirlos
ggplot(data = Cars2020, aes(x = Weight, y = HwyMPG)) +  # Gráfico de dispersión con las variables "Weight" y "HwyMPG" como coordenadas
    geom_smooth(mapping = aes(linetype = Size)) +       # Regresiones con tipo de línea definido por la variable "Size"
    geom_point(mapping = aes(colour = Drive))           # Color de los puntos definido por la variable "Drive"

# Filtrado de datos
ggplot(data = Cars2020, mapping = aes(x = Weight, y = HwyMPG)) +
    geom_point(data = filter(Cars2020, Drive == "FWD"), mapping = aes(colour = Size)) +  # Solo mostrar datos con Drive="FWD"
    geom_smooth(se = FALSE, colour = '#810BB8', size = 0.8, linetype = 2)
```

A continuación se muestran algunos ejemplos de **gráficos de lína** con `geom_line()` (pág. 58) con el dataset `paises` del paquete `{datos}`:
```r
# Sale bien porque solo hay 1 esperanza de vida por año en Argentina
paises %>% filter(pais == "Argentina") %>%
    ggplot(aes(y = esperanza_de_vida, x = anio)) + geom_line()

# Con varios paises, necesitamos agrupar las esperanzas de vida de cada uno en una línea independiente
paises %>% filter(continente == "Américas") %>%
    ggplot(aes(y = esperanza_de_vida, x = anio)) + geom_line(aes(colour = pais))  # Separar por color
```

En algunas situaciones no es suficiente con hacer gráficos de los datos *crudos*. Podemos **procesar los datos** (pág. 61) para obtener descripciones estadíśticas y mostrar estos resultados:
```r
# Generar la media (de cada continente en cada año), representarla un gráfico de dispersión y añadir regresión
paises %>% group_by(continente, anio) %>% summarise(esperanza_de_vida_media = mean(esperanza_de_vida)) %>%
    ggplot(aes(anio, esperanza_de_vida_media)) +
    geom_point(aes(colour = continente)) +
    geom_smooth(method = "lm", colour = '#67BF4C')
```

Para **diagramas de caja** se utiliza `geom_boxplot()` (pág. 63). Si además queremos las barras de error o *bigotes*, se combina con `stat_boxplot()`. Como siempre, se pueden personalizar. Aquí se muestran varios ejemplos:
```r
# Diagrama de caja sin valores en el eje X
ggplot(data = Cars2020, aes(x = "", y = Length)) + geom_boxplot()

# Agregar las barras de error horizontales en los bigotes (ancho personalizado)
ggplot(data = Cars2020, aes(x = "", y = Length)) + stat_boxplot(geom = "errorbar", width = 0.15) + geom_boxplot()

# Diagrama de caja y bigotes personalizado
ggplot(Cars2020, aes(x = "", y = Length)) +
    stat_boxplot(geom = "errorbar",
                width = 0.1,
                color = "#090D45") +  # Color barras error
    geom_boxplot(fill = "#E0F2FC",           # Color de relleno de la caja
                alpha = 0.5,                 # Transparencia
                color = "#090D45",           # Color del borde de la caja
                outlier.colour = "#0098CD",  # Color de los outliers
                width = 0.2)                 # Ancho de la caja

# Diagrama de caja y bigotes en función de una variable categórica (Size)
ggplot(Cars2020, aes(x = Size, y = Length)) +
    stat_boxplot(geom = "errorbar",
                width = 0.1,
                color = "#090D45") +  # Color barras error
    geom_boxplot(fill = "#E0F2FC",           # Color de relleno de la caja
                color = "#090D45",           # Color del borde de la caja
                outlier.colour = "#0098CD",  # Color atípicos
                width = 0.4) +
    geom_point(stat = "summary", fun = "mean", colour = "red", size = 3) +
    scale_x_discrete(labels=c("Grande", "Mediano", "Pequeño"))  # Size renombrado a "Grande", "Mediano" y "Pequeño"
```

Para **histogramas** se utiliza `geom_histogram()` (pág. 68). Por defecto muestran la **frecuencia** con la que un rango de valores aparece en las muestras, pero si se especifica `y = ..density..`, se puede obtener un histograma de **densidades** o de probabilidad. Por defecto, se utilizan **30 bins** (barras o intervalos), configurable con `bins`. Su **ancho** es configurable con `binwidth`. También es posible agrupar las barras basándose en los valores de una **variable categórica**. Al hacer esto, las barras se **solapan**, por lo que se recomienda utilizar o `position = "identity"` con `alpha` para que tengan algo de transparencia, `position = "dodge"` para que las barras estén **contiguas** o adosadas o `position = "stack"` para que estén **apliladas**. Algunos ejemplos de uso son:
```r
# Histograma con frecuencias absolutas
ggplot(Cars2020, aes(x = Length)) +
    geom_histogram(colour = "white", fill = "blue") +  # Barras azules con bordes blancos
    labs(x = "Longitud del vehículo", y = "Frecuencia Absoluta") +
    theme(axis.title = element_text(size = 10, face = "bold"))

# Histograma de densidades
ggplot(Cars2020, aes(x = Length)) +
    geom_histogram(aes(y = ..density..), colour = "white", fill = "blue") +
    labs(x = "Longitud del vehículo", y = "Densidad")

# Histograma por grupos con barras superpuestas (position = "identity")
ggplot(Cars2020, aes(x = Length, colour = Size, fill = Size)) +
    geom_histogram(binwidth = 10, alpha = 0.5, position = "identity") +
    labs(title = 'position = "identity"', x = "Longitud del vehículo", y = "Frecuencia") +
    theme(plot.title = element_text(color="#615E5E", size=11,
    face="bold.italic", hjust = 0.5))

# Histograma por grupos con barras adosadas (position = "dodge")
ggplot(Cars2020, aes(x = Length, colour = Size, fill = Size)) +
    geom_histogram(binwidth = 10, alpha = 0.5, position = "dodge") +
    xlab("Longitud del vehículo") +
    ylab("Frecuencia") +
    ggtitle(label = 'position = "dodge"') +
    theme(plot.title = element_text(color="#615E5E", size=11, face="bold.italic", hjust = 0.5))
```

Para los **diagramas de barras** se utiliza `geom_bar()` (pág. 73). Por defecto, **cuenta las ocurrencias** de cada valor de la variable. Si ya tenemos el **recuento hecho**, debemos utilizar `stat = "identity"`. Por defecto, las barras se ordenan de mayor a menor, pero se pueden **reordenar** utilizando `scale_x_discrete()`. Para añadir **etiquetas** se utiliza `geom_text()` con `label = ..count..`. Otra opción es colorear las barras conforme a otra variable utilizando `fill` (o `scale_fill_manual()` si se quiere usar colore personalizados). Por ejemplo:
```r
# Gráfico de barras con datos crudos
ggplot(Cars2020, aes(x = Drive)) + geom_bar()

# Gráfico de barras con tabla de frecuencias (y)
df_aux = data.frame(traccion = c("Delantera", "Trasera", "Total"), frecuencias = c(25, 5, 80))
ggplot(df_aux, aes(x = traccion, y = frecuencias)) + geom_bar(stat = "identity")

# Gráfico de barras reordenado (scale_x_discrete())
ggplot(Cars2020, aes(x = Drive)) + geom_bar() +
    scale_x_discrete(limits = c("FWD", "RWD", "AWD"),
                    labels = c("FWD" = "Delantera", "RWD" = "Trasera", "AWD" = "Total"))

# Etiquetas encima de cada barra (geom_text())
ggplot(Cars2020, aes(x = factor(Drive, levels = c("FWD", "RWD", "AWD")))) +
    geom_bar() +
    geom_text(aes(label = ..count..),
            stat = "count",
            vjust = -1,
            colour = "black",
            size = 3) +
    ylim(c(0, 85)) +  # Incrementar límites del eje Y si es necesario
    labs(x="Tracción del vehículo", y="Número de autos")

# Colorear barras con elección manual de colores (fill = Drive)
ggplot(Cars2020, aes(x = Drive, fill = Drive)) +
    geom_bar() +
    scale_x_discrete(limits = c("FWD", "RWD", "AWD"),
                    labels = c("FWD" = "Delantera", "RWD" = "Trasera", "AWD" = "Total")) +  # Renombrar barras
    scale_fill_manual(values = c("FWD" = "#DB8100", "RWD" = "#CD0098", "AWD" = "#0098CD"))  # Colores manuales
```

Como apunte adicional, `{ggplot2}` ofrece **múltiples [temas](https://ggplot2.tidyverse.org/reference/ggtheme.html)** (pág. 77) que pueden ser utilizados en los títulos como argumento de `ggtitle()` o de toda la gráfica si se utilizan como una **capa adicional**. El paquete `{ggthemes}` ofrece **temas adicionales** (algunos de los cuales replican el estilo de *The Economist* o *Stata*). **Ejemplos** de código y visualizaciones de este paquete pueden encontrarse [aquí](https://yutannihilation.github.io/allYourFigureAreBelongToUs/ggthemes/). Otros paquetes de temas son `{hrbrthemes}` y `{bbplot}`.


# 6. Ejercicios (pág. 80)
En el archivo [actividades/ejercicios_tema6_visualización_de_datos.R](actividades/ejercicios_tema6_visualización_de_datos.R) se incluye la resolución de los 6 ejercicios propuestos en este tema. En el [video 11](https://unir.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=5556e93b-4a16-4df6-aff9-af1f008ca585) se solucionan los ejercicios 1 y 2.
