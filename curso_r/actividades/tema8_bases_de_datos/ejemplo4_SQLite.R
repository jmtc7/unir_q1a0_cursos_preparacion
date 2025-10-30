# Ejemplo de conexión y uso de SQLIte #

# Conexión a una base de datos SQLite para recuperar, procesar y visualizar datos


# 1. CREACIÓN Y POBLADO DE BASE DE DATOS SQLITE

# Cargar paquetes necesarios
library(RSQLite)
library(dplyr)
library(ggplot2)

# Creación de una conexión a una base de datos SQLite
con <- dbConnect(SQLite(), dbname = "mi_base_de_datos.sqlite")

# Creación de una tabla 'autos' e inserción de datos desde el dataset 'mtcars'
dbWriteTable(con, "autos", mtcars, overwrite = TRUE)

# Consulta de los datos de la tabla
autos <- dbReadTable(con, "autos")
print(autos)


# 2. RECUPERAR Y TRANSFORMAR DATOS

# Recuperación de los datos y conexión
autos <- tbl(con, "autos") %>% collect()

# Clasificación de eficiencia de combustible
autos <- autos %>%
mutate(eficiencia = case_when(mpg > 20 ~ "Alta",
                              mpg > 15 ~ "Media",
                              TRUE ~ "Baja"))
print(autos)


# 3. VISUALIZACIÓN DE DATOS

# Histograma del Rendimiento de Combustible (mpg)
# Cómo se distribuye el rendimiento de combustible entre los autos, identificando qué rangos son más comunes.
ggplot(autos, aes(x = mpg)) +
  geom_histogram(binwidth = 3, fill = "blue", color = "black") +
  labs(title = "Distribución del Rendimiento de Combustible (mpg)",
       x = "Millas por Galón (mpg)", y = "Frecuencia")

# Gráfico de Barras de la Eficiencia de Combustible
# Vista clara de cuántos autos caen en cada categoría de eficiencia.
ggplot(autos, aes(x = eficiencia)) +
  geom_bar(fill = "orange", color = "black") +
  labs(title = "Distribución de la Eficiencia de Combustible",
       x = "Eficiencia", y = "Frecuencia")

# Gráfico de Dispersión entre hp (Caballos de Fuerza) y mpg (Rendimiento)
# Correlación negativa -> A mayor cantidad de caballos de fuerza, menor es el rendimiento de combustible.
ggplot(autos, aes(x = hp, y = mpg)) +
  geom_point(color = "red") +
  labs(title = "Relación entre Caballos de Fuerza y Rendimiento",
       x = "Caballos de Fuerza (hp)", y = "Millas por Galón (mpg)")

# Gráfico de Caja (Boxplot) para mpg por Número de Cilindros (cyl)
# Visión clara de la eficiencia según el tamaño del motor.
ggplot(autos, aes(x = as.factor(cyl), y = mpg)) +
  geom_boxplot(fill = "green", color = "black") +
  labs(title = "Rendimiento de Combustible por Número de Cilindros",
       x = "Número de Cilindros", y = "Millas por Galón (mpg)")

# Gráfico de Línea de Promedio de mpg por Peso (wt)
# Los autos más pesados tienden a tener menor eficiencia de combustible.
autos %>% group_by(wt) %>% summarise(mpg_promedio = mean(mpg)) %>%
  ggplot(aes(x = wt, y = mpg_promedio)) +
  geom_line(color = "purple") +
  labs(title = "Rendimiento Promedio de Combustible por Peso",
       x = "Peso (1000 lbs)", y = "Millas por Galón Promedio")
