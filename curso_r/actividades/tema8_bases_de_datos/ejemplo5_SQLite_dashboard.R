# Ejemplo de conexión y uso de SQLIte avanzado con dashboard #

# 1. Cargar dataset

# Cargar librerías necesarias
library(ggplot2)  # Visualización
library(leaflet)  # Gráficos de mapa
library(RSQLite)
library(shiny)    # Dashboard
library(DBI)

# Leer el dataset desde la URL
dataset_url <- "https://data.cityofnewyork.us/api/views/c3uy-2p5r/rows.csv"
data <- read.csv(dataset_url)

# Mostrar las primeras filas del dataset
head(data)


# 2. Creación de base de datos

# Crear conexión con la base de datos SQLite
con <- dbConnect(RSQLite::SQLite(), "data_analysis.db")

# Guardar el dataset en SQLite
dbWriteTable(con, "data_table", data, overwrite = TRUE)


# 3. Transformación de datos

# Cantidad Total de Medidas por Tipo de Indicador
query <- "SELECT `Indicator ID`, COUNT(*) AS total_measures FROM data_table GROUP BY `Indicator ID` ORDER BY total_measures DESC"
transformed_data <- dbGetQuery(con, query)

# Promedio de Valores de Medidas por Lugar Geográfico
query_avg <- "SELECT `Geo Place Name`, AVG(`Data Value`) AS avg_value FROM data_table GROUP BY `Geo Place Name`"
avg_data <- dbGetQuery(con, query_avg)

# Transformación de Campos Categóricos
data$`Indicator ID` <- as.factor(data$`Indicator ID`)

# Filtrado de Datos por Periodo de Tiempo
query_date <- "SELECT * FROM data_table WHERE Start_Date BETWEEN '2015-01-01' AND '2015-12-31'"
filtered_data <- dbGetQuery(con, query_date)

# Cálculo de Medidas por Tipo de Lugar Geográfico
query_geo <- "SELECT `Geo Type Name`, COUNT(*) AS total_measures FROM data_table GROUP BY `Geo Type Name` ORDER BY total_measures DESC"
geo_data <- dbGetQuery(con, query_geo)

# Crear una nueva columna indicando si el valor de la medida es mayor a 1
data$high_value <- ifelse(data$`Data Value` > 1, "Sí", "No")


# 4. Visualización de los Datos

# Crear gráfico de barras
ggplot(transformed_data, aes(x = reorder(`Indicator ID`, -total_measures), y = total_measures)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  theme_minimal() +
  labs(title = "Cantidad de Medidas por Tipo de Indicador",
       x = "Tipo de Indicador", y = "Cantidad de Medidas") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Crear un mapa interactivo con la ubicación de las medidas (asumiendo latitud y longitud disponibles)
leaflet(data) %>% addTiles() %>%
  addCircles(lng = ~LONGITUDE, lat = ~LATITUDE, popup = ~`Geo Place Name`,
             radius = 50, color = "red", fillOpacity = 0.5) %>%
  setView(lng = -73.935242, lat = 40.730610, zoom = 10)


# 5. Creación del Dashboard con Shiny

# Definir la interfaz de usuario
ui <- fluidPage(
  titlePanel("Dashboard de Análisis de Medidas Ambientales en NYC"),
  sidebarLayout(
    sidebarPanel(
      selectInput("geo_place", "Seleccione un lugar geográfico:", choices =
      unique(avg_data$`Geo Place Name`))
    ),
    mainPanel(
      plotOutput("barPlot"),
      plotOutput("avgPlot")
    )
  )
)

# Definir la lógica del servidor
server <- function(input, output) {
  output$barPlot <- renderPlot({
    ggplot(transformed_data, aes(x = reorder(`Indicator ID`, -total_measures), y = total_measures)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    theme_minimal() +
    labs(title = "Cantidad de Medidas por Tipo de Indicador",
         x = "Tipo de Indicador", y = "Cantidad de Medidas")
  })

  output$avgPlot <- renderPlot({
    filtered_avg_data <- avg_data[avg_data$`Geo Place Name` == input$geo_place, ]

    ggplot(filtered_avg_data, aes(x = `Geo Place Name`, y = avg_value)) +
    geom_bar(stat = "identity", fill = "darkgreen") +
    theme_minimal() +
    labs(title = "Promedio del Valor de Medidas por Lugar Geográfico",
         x = "Lugar Geográfico", y = "Valor Promedio de Medida")
  })
}

# Ejecutar la aplicación Shiny
shinyApp(ui = ui, server = server)