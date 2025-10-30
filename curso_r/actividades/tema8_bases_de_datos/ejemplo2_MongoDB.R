# Ejemplo de conexión y uso de MongoDB #

# Conexión a una base de datos MongoDB para recuperar, procesar y visualizar datos


# Cargar paquetes necesarios
library(mongolite)
library(ggplot2)

# Conexión a la base de datos MongoDB
con <- mongo(collection = "mi_coleccion", db = "mi_base_de_datos", url = "mongodb://localhost:27017")

# Inserción de varios documentos JSON
con$insert('[
  { "nombre": "Carlos", "edad": 25, "profesion": "Analista" },
  { "nombre": "María", "edad": 29, "profesion": "Data Scientist" },
  { "nombre": "Luis", "edad": 35, "profesion": "Ingeniero" }
  ]')

# Recuperación de todos los documentos de la colección
datos <- con$find()
print(datos)

# Visualización: Histograma de edades
ggplot(datos, aes(x = edad)) +
  geom_histogram(binwidth = 5, fill = "blue", color = "black") +
  labs(title = "Distribución de Edades", x = "Edad", y = "Frecuencia")

# Visualización: Gráfico de barras por profesión
ggplot(datos, aes(x = profesion)) +
  geom_bar(fill = "green", color = "black") +
  labs(title = "Cantidad de Personas por Profesión",
       x = "Profesión", y = "Frecuencia")

# Visualización: Gráfico de dispersión edad vs profesión
ggplot(datos, aes(x = edad, y = profesion)) +
  geom_point(color = "red") +
  labs(title = "Edad vs Profesión", x = "Edad", y = "Profesión")

# Cierre de la conexión
con$disconnect()
