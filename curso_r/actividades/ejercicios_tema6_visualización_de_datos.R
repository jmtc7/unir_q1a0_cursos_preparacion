# Ejercicios del tema 6: Visualización de Datos #

# EJERCICIO 1: Utilizar los datos "paises" de {datos} y R base para hacer un 
# gráfico de dispersión con "anio" en X y "esperanza_de_vida" en Y coloreados 
# por "continente" con tamaño de 0.7 y un suavizado (regresión)

library(datos)
library(dplyr)
cat("\nEJERCICIO 1\n")
print(head(paises))  # Mostrar algunas filas de los datos a procesar
par(mar = c(5, 4, 4, 6),  # Márgenes con más espacio a la derecha (2 -> 6)
    xpd = TRUE)           # Permitir elementos gráficos fuera de la caja

# Añadir gráfico de dispersión
plot(paises$anio, paises$esperanza_de_vida,
     col = paises$continente,
     cex = 0.7,  # Tamaño de puntos
     pch = 19,   # Tipo de puntos
     bty = "n",  # Quitar caja para mejorar estética
     main = 'Ejercicio 1',
     ylab = "Esperanza de vida",
     xlab = "Año")

# Añadir leyenda
continentes_diferentes <- unique(paises$continente)
legend("topright", 
       legend = continentes_diferentes,
       col = continentes_diferentes,
       title = "Continentes",
       bty = "n",  # Quitar caja para mejorar estética
       pch = 19,   # Tipo de puntos (mismo que en el gráfico)
       inset = c(-0.3, 0))  # Mover leyenda horizontalmente

# Verificar que los colores de los puntos y la leyenda sean los mismos
# La menor esperanza es en Asia y en ese año el punto más abajo es verde [OK]
# Podemos cambiar el año o usar arrange(desc()) para comprobar más años/zonas
print(paises %>%
        filter(anio == 1952) %>%  # Seleccionar un año
        arrange(esperanza_de_vida))  # Ordenar por esperanza de vida

# Hacer una regresión/suavizado
# NOTA: Necesitamos ordenar los años y las esperanzas para dibujar la linea
idx = order(paises$anio)  # Obtener los índices de un hipotético X ordenado
modelo = loess(esperanza_de_vida[idx] ~ anio[idx], data = paises)
f = predict(modelo, se = TRUE)  # "se" -> Errores estándares
lines(paises$anio[idx], y=f$fit)


# EJERCICIO 2: Repetir el 1er ejercicio utilizando ggplot2
library(ggplot2)

print(ggplot(paises, aes(x = anio, y = esperanza_de_vida)) +
        geom_point(aes(colour = continente), size = 0.7) +
        geom_smooth() +
        ggtitle(label = 'Ejercicio 2') +
        xlab("Año") +
        ylab("Esperanza de vida"))


# EJERCICIO 3: Completar el código dado para obtener el gráfico objetivo
mis_paises <- paises %>%
  group_by(continente, anio) %>%  # Agrupar por continente y año
  summarize(esperanza_de_vida_media = mean(esperanza_de_vida))  # Calcular media

print(ggplot(mis_paises, aes(anio, esperanza_de_vida_media)) +
        geom_point(aes(color = continente), size = 3, shape = 8) +  # Forma asterisco
        geom_smooth(aes(color = continente), se = FALSE) +  # Quitar error estándar
        ggtitle(label = 'Ejercicio 3') +
        xlab("Año") +
        ylab("Esperanza de vida media"))


# EJERCICIO 4: Usar los datos "paises" y crear un gráfico de la evolución de la 
# esperanza media y máxima de vida mundial con color y tipo de lineas diferentes
mis_paises2 <- paises %>%
  group_by(continente, anio) %>%
  summarize(esperanza_de_vida_media = mean(esperanza_de_vida),
            esperanza_de_vida_max = max(esperanza_de_vida))

print(ggplot(mis_paises2, aes(x = anio, color = continente)) +
        geom_line(aes(y = esperanza_de_vida_media, linetype = "Media")) +
        geom_line(aes(y = esperanza_de_vida_max, linetype = "Máxima")) +
        scale_linetype_manual(name = "Esperanza de vida",
                              values = c("Media" = "solid", "Máxima" = "dashed")) +
        ggtitle(label = 'Ejercicio 4') +
        xlab("Año") +
        ylab("Esperanza de vida"))


# EJERCICIO 5: Con los datos "mpg" de {ggplot2} generar un gráfico de caja y 
# bigotes (hwy vs class) con los puntos coloreados por drv y la media de hwy
print(ggplot(mpg, aes(x = class, y = hwy)) +
        stat_boxplot(geom = "errorbar") +  # Bigotes
        geom_boxplot() +  # Cajas
        geom_point(stat = "summary", fun = "mean") +  # Media
        geom_point(aes(colour = drv)) +  # Puntos
        ggtitle(label = 'Ejercicio 5') +
        xlab("Clase") +
        ylab("Consumo en autovía"))


# EJERCICIO 6: Con los datos "diamantes" de {datos} generar histogramas con 
# "precio" con barras violetas con borde gris, un histograma por color de 
# diamante, cambiar intensidad de color y nombres de ejes en español
print(ggplot(diamantes, aes(x = precio, fill = color)) +
        geom_histogram(alpha = 0.5, position = "stack",
                       colour = "gray") +
        ggtitle(label = 'Ejercicio 6') +
        xlab("Precio del diamante") +
        ylab("Frecuencia"))
