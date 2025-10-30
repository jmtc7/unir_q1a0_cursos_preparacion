# Ejemplo de conexión y uso de MySQL #

# Conexión a una base de datos MySQL para recuperar, procesar y visualizar datos


# Cargar paquetes necesarios
library(RMySQL)
library(ggplot2)

# Conexión a la base de datos MySQL
con <- dbConnect(MySQL(), user = "usuario", password = "contraseña", dbname = "mi_base_de_datos", host = "localhost")

# Inserción de varios registros en la tabla clientes
dbWriteTable(con, "clientes",
             data.frame(id = 1:5,
                        nombre = c("Carlos", "Ana", "Luis", "María", "Jorge"),
                        edad = c(25, 30, 35, 40, 45)), append = TRUE)

# Recuperación de todos los registros de la tabla clientes
datos <- dbGetQuery(con, "SELECT * FROM clientes")
print(datos)

# Visualización: Histograma de edades
ggplot(datos, aes(x = edad)) +
  geom_histogram(binwidth = 5, fill = "blue", color = "black") +
  labs(title = "Distribución de Edades", x = "Edad", y = "Frecuencia")

# Visualización: Gráfico de barras por nombre
ggplot(datos, aes(x = nombre)) +
  geom_bar(fill = "purple", color = "black") +
  labs(title = "Cantidad de Personas por Nombre",
       x = "Nombre", y = "Frecuencia")

# Visualización: Gráfico de dispersión edad vs nombre
ggplot(datos, aes(x = edad, y = nombre)) +
  geom_point(color = "red") +
  labs(title = "Edad vs Nombre", x = "Edad", y = "Nombre")

# Cierre de la conexión
dbDisconnect(con)
