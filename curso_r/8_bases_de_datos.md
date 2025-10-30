# R y Bases de Datos

## 1. Introducción
Una de las principales ventajas de R es su **capacidad para comunicarse con bases de datos relacionales y no relacionales**. A lo largo de este tema veremos cómo:
- Conectarse a bases de datos relacionales (MySQL y SQLite) y no relacionales (MongoDB).
- Manipular y limpiar bases de datos.
- Analizar y visualizar de datos recuperados de bases de datos.
- Generar reportes automatizados.


## 2. Conexión con Diferentes Bases de Datos (pág. 5)
Los **principales paquetes** de R para interactuar con bases de datos son:
- `{DBI}`: Interfaz **genérica** para conectarse a bases de datos y hacer **consultas SQL** eficientes.
- `{RMySQL}` y `{RMariaDB}`: Paquetes específicos para **MySQL y MariaDB**. Permiten consultas SQL y recuperar datos en R.
- `{RSQLite}`: Para bases de datos **SQLite**, que no requieren de servidor. Son útiles para hacer pruebas con pocos datos.
- `{mongolite}`: Para **MongoDB**. Permite consultar y manipular documentos en JSON.

En la carpeta [actividades/tema8_bases_de_datos/](actividades/tema8_bases_de_datos/) hay **ejemplos** de cómo conectarse a bases de datos MySQL, MongoDB y SQLite para recuperar, procesar y visualizar datos.


## 3. Ejemplo con MySQL (pág. 7)
El paquete `{RMySQL}` permite conectarse a bases MySQL, ejecutar consultas o *queries* y realizar operaciones CRUD (*Create, Read, Use, and Delete*).

Para **conectarnos** utilizamos `dbConnect()` especificando argumentos como `user`, `password`, `dbname` y `host`. Las **operaciones** que podemos realizar son:
- **Insertar datos** en una tabla: Utilizamos `dbWriteTable()` o `dbSendQuery()` y una consulta de inserción. Por ejemplo: `dbWriteTable(con, "clientes", data.frame(id = 1:3, nombre = c("Ana", "Luis", "María"), edad = c(28, 35, 42)), append = TRUE)` o `dbSendQuery(con, "INSERT INTO clientes (id, nombre, edad) VALUES (4, 'Carlos', 30)")`.
- **Consultar datos** con `dbGetQuery()`. Por ejemplo: `resultado <- dbGetQuery(con, "SELECT * FROM clientes WHERE edad > 30")`.
- **Actualizar datos** con `dbSendQuery()` y una consulta de actualización. Por ejemplo: `dbSendQuery(con, "UPDATE clientes SET edad = 36 WHERE nombre = 'Luis'")`.
- **Borrar datos** con `dbSendQuery()` y una consulta de borrado. Por ejemplo: `dbSendQuery(con, "DELETE FROM clientes WHERE nombre = 'Ana'")`.

En el archivo [ejemplo1_MySQL.R](actividades/tema8_bases_de_datos/ejemplo_MySQL.R) hay un **ejemplo** de cómo conectarse a una base de datos MySQL para recuperar, procesar y visualizar datos.


## 4. Ejemplo con MongoDB (pág. 10)
Para **conectarnos** a MongoDB desde R se utiliza la función `mongo()` del paquete `{mongolite}`, especificando la colección, la base de datos y el servidor a utilizar. Por ejemplo: `con <- mongo(collection = "mi_coleccion", db = "mi_base_de_datos", url = "mongodb://localhost:27017")`. Una vez conectados, podemos realizar las siguientes operaciones:
- **Insertar** documentos JSON en una colección con `insert()`. Por ejemplo: `con$insert('{"nombre": "Ana", "edad": 28, "profesion": "Diseñadora"}')`.
- **Consultar** o recuperar documentos con `find()`. Por ejemplo: `datos <- con$find('{"profesion": "Ingeniero"}')`.
- **Actualizar** documentos existentes con `update()`. Debemos especificar el filtro y los nuevos valores. Por ejemplo: `con$update('{"nombre": "Juan"}', '{"$set": {"edad": 31}}')`.
- **Borrar** docuemntos con `remove()`. Por ejemplo: `con$remove('{ "nombre": "Ana" }')`.

En el archivo [ejemplo2_MongoDB.R](actividades/tema8_bases_de_datos/ejemplo_MongoDB.R) hay un **ejemplo** de cómo conectarse a una base de datos MongoDB para recuperar, procesar y visualizar datos. Además, en [ejemplo3_MongoDB_informe.Rmd](actividades/tema8_bases_de_datos/ejemplo_MongoDB_informe.Rmd) se proporciona un ejemplo de cómo **automatizar un informe con R Markdown**.


## 5. Ejemplo con SQLite y Dashboard (pág. 16)
En esta sección veremos cómo crear un ***dashboard* interactivo** que cuente una historia a partir de datos obtenidos de una base de datos SQLite. Algunos paquetes útiles para este propósito son `{ggplot2}`, `{shiny}` y `{dplyr}`.

En el archivo [ejemplo4_SQLite.R](actividades/tema8_bases_de_datos/ejemplo4_SQLite.R) hay un **ejemplo** de cómo conectarse a una base de datos SQLite para crear, recuperar, procesar y visualizar datos.

En el [ejemplo5_SQLite_dashboard.R](actividades/tema8_bases_de_datos/ejemplo5_SQLite_dashboard.R) hay otro **ejemplo más avanzado** en el que se realizan varias **consultas SQLite** y se genera un *dashboard* con `{shiny}`.


## 6. Ejercicios (pág. 27)
En este tema se proporcionan **dos códigos a ejecutar y comprender**. Ambos se encuentra en la carpera [actividades/tema8_bases_de_datos/](actividades/tema8_bases_de_datos/) como notebooks de RStudio.
