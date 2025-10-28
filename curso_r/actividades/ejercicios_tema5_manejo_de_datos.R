# Ejercicios del tema 5: Manejo de Datos #

# EJEMPLOS #

# Cargar datos desde ficheros TXT en local y en remoto
print("EJEMPLOS: Importar de Datos")
library(readxl)  # Librería para leer hojas de Excel
datos_txt_locales<-read.table("datos/t5/medidas_cuerpo.txt",  # Ruta al archivo
                              header = TRUE,  # Fila con nombres de variables
                              dec = ".", # Separador entre enteros y decimales
                              stringsAsFactors = TRUE,  # Strings en factores
                              comment.char = "#")  # Comienzo de comentarios
datos_txt_web<-read.table("https://www.biostatisticien.eu/springeR/imcenfant.txt",
                          header = TRUE, stringsAsFactors = TRUE)
datos_csv<-read.csv("datos/t5/gapminder_es.csv")
datos_excel<-read_excel("datos/t5/NutritionStudy.xlsx")
datos_esp<-"datos/t5/2024-datos-anuales-panel-consumo-hogares-base2021_v2.xlsx"
datos_excel_hoja<-read_excel(datos_esp, sheet="PRECIO", skip=2 )  # Skip 2 rows

# Mostrar datos importados
cat("\nDatos TXT locales:\n")
print(head(datos_txt_locales))
cat("\nDatos TXT remotos:\n")
print(head(datos_txt_web))
cat("\nDatos CSV:\n")
print(head(datos_csv))
cat("\nDatos Excel:\n")
print(head(datos_excel))
cat("\nDatos Excel por hojas:\n")
print(excel_sheets(datos_esp))
print(head(datos_excel_hoja))


# EJERCICIOS #

# EJERCICIO 2: Utilizar el dataset "storms" de {dplyr} y obtener la velocidad  
# media de viento y el diámetro medio de las zonas afectadas de cada año
library(dplyr)
cat("\nEJERCICIO 2\n")
resumen <- storms %>% group_by(year) %>%  # Agrupar por año
            summarise(viento_medio = mean(wind, na.rm = TRUE),  # Media borrando NAs
                      diametro_medio = mean(tropicalstorm_force_diameter, na.rm = TRUE))

print(tail(resumen))  # [OK] Muchos años sin diámetros


# EJERCICIO 3: Utilizar el dataset "mpg" de {ggplot2} y obtener datos de 
# vehículos compactos de 2004 en adelante y transformar eficiencia a Km/L
library(ggplot2)
cat("\nEJERCICIO 3\n")
conversion <- 1.609/3.78541  # 1 milla = 1.609 Km, 1 gallon = 3.78541 L
datos <- mpg %>% filter(year > 2004, class == "compact")  # Filtrar dataset
# Transformar miles/gallon a Km/L en ciudad y autovía
datos <- datos %>% mutate(cty.kml = cty*conversion)  
datos <- datos %>% mutate(hwy.kml = hwy*conversion)

print(datos)  # [OK]


# EJERCICIO 4: (1)Importar datos de lobsters.txt, (2) calcular media y std de 
# los pesos, (3) obtener media, std y número de observaciones en cada zona y 
# (4) repetir (3) excluyendo langostas por debajo de 500g
cat("\nEJERCICIO 4\n")

# Cargar datos y obtener media y desviación estándar de los pesos
langostas <- read.table("datos/t5/lobsters (2).txt", sep=" ", header=TRUE)
peso_medio = mean(langostas$Peso, na.rm = TRUE)  # Media ignorando NAs
peso_std = sd(langostas$Peso, na.rm = TRUE)      # Desv. estándar ignorando NAs
# Alternativa: langostas %>% summarise(media=mean(Peso), std=sd(Peso))
cat("Peso medio: ", peso_medio, "\n")
cat("Desviación estándar: ", peso_std, "\n")

# Dividir por zona y obtener media y desviación estándar por zona
cat("\nResumen por zonas:\n")
resumen <- langostas %>%
            group_by(Zona) %>%
            summarize(media=mean(Peso), std=sd(Peso), n=n())
print(resumen)

# Repetir para langostas de más de 500g
cat("\nResumen por zonas (> 500g):\n")
resumen2 <- langostas %>% filter(Peso > 0.5) %>%
            group_by(Zona) %>%
            summarize(media=mean(Peso), std=sd(Peso), n=n())
print(resumen2)


# EJERCICIO 5: Utilizar el dataset "airquality" de {datasets} y obtener 
# temperatura media total, temp media mayo, día con más viento, cuántos días 
# hubo más viento que el viento medio y ordenar por temperatura y viento.
cat("\nEJERCICIO 5\n")

t_media <- mean(airquality$Temp, na.rm = TRUE)
t_media_mayo <- mean(airquality$Temp[airquality$Month == 5], na.rm = TRUE)
dia_max_viento <- airquality[which.max(airquality$Wind), "Day"]
v_medio <- mean(airquality$Wind, na.rm = TRUE)  # Viento medio
dias_ventosos <- sum(airquality$Wind > v_medio, na.rm = TRUE)
datos_ordenados <- arrange(airquality, Temp, Wind)

# Mostrar resultados
cat("Temperatura media: ", t_media, "\n")
cat("Temperatura media en mayo: ", t_media_mayo, "\n")
cat("Día más ventoso: ", dia_max_viento, "\n")
cat("Días con más viento que la media: ", dias_ventosos, "\n")
cat("\nDatos ordenados por temperatura y viento:\n")
print(head(datos_ordenados))
