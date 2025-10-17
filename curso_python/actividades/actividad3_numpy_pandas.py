"""
DESCRIPCION
Este reto consiste en analizar los datos de ventas, los inventarios y la satisfacción del cliente para una cadena de tiendas minoristas; utilizando Pandas, para la manipulación de datos, y Numpy, para realizar cálculos estadísticos y simulaciones. El objetivo es ayudar a optimizar el rendimiento de las tiendas a través del análisis de estos datos.

RECURSOS DESCARGABLES

REQUISITOS
El proyecto debe cumplir con los siguientes requisitos:

    Utilizar el lenguaje de programación Python.
    Utilizar las librerías Pandas y Numpy para el análisis de datos y las operaciones numéricas.
    Implementar el proyecto en Visual Studio Code utilizando el plugin de Jupyter para trabajar con archivos .ipynb.
    Cargar los datos desde los archivos CSV que están presentes en el proyecto. Las rutas de los archivos deben ser absolutas, como se muestra a continuación:
        /workspace/sales.csv
        /workspace/inventories.csv
        /workspace/satisfaction.csv
    Procesamiento de los datos:
        Limpiar los datos eliminando filas con valores nulos.
        Asegurar que los DataFrames tengan la estructura correcta y estén listos para su análisis.
    Realizar los siguientes análisis estadísticos utilizando Pandas:
        Calcular las ventas totales por tienda.
        Calcular la rotación de inventarios por tienda.
        Filtrar las tiendas con inventarios críticos (menos del 10% en ventas respecto al inventario disponible).
        Analizar la satisfacción del cliente y filtrar las tiendas con una satisfacción menor al 60%.
    Realizar cálculos numéricos con Numpy:
        Calcular la mediana de las ventas totales.
        Calcular la desviación estándar de las ventas.
        Simular proyecciones de ventas futuras usando arrays aleatorios de Numpy.
    El código debe estar bien organizado y comentado, explicando los pasos importantes del análisis y las operaciones realizadas.
    El proyecto debe contener un archivo Jupyter Notebook (.ipynb) donde se implementen y expliquen los pasos, análisis y resultados obtenidos en cada sección.



INSTRUCCIONES
La empresa ficticia RetailNow, que gestiona una cadena de tiendas minoristas, desea realizar un análisis detallado del rendimiento de sus diferentes sucursales en varias ciudades. Para ello, han recopilado datos de las ventas, los inventarios y la satisfacción del cliente en archivos CSV. Tu misión será procesar, explorar y analizar estos datos usando Pandas y Numpy para ayudar a la dirección a tomar decisiones estratégicas sobre la optimización del rendimiento de las tiendas.
1. Preparar el entorno de trabajo:
    Abre Visual Studio Code y asegúrate de tener instalado el plugin de Jupyter.
    Crea un nuevo archivo Jupyter Notebook llamado analisis_red_tiendas.ipynb.
2. Importar las librerías necesarias:
    Importa las librerías Pandas y Numpy que necesitarás para realizar el análisis.
3. Cargar los datos (lectura y procesamiento de datos - Pandas):
    Utiliza Pandas para cargar los archivos CSV: sales.csv, inventories.csv y satisfaction.csv.
    Guarda los datos en tres DataFrames distintos.
    Limpia los datos eliminando filas con valores nulos utilizando el método dropna(). Esto te permitirá trabajar solo con datos válidos.
4. Exploración de datos (Pandas)
    Calcula las ventas totales por producto y por tienda.
    Calcula los ingresos totales por tienda, multiplicando la cantidad vendida por el precio unitario.
    Genera un resumen estadístico de las ventas utilizando el método describe() para obtener la media, mediana y otras métricas clave.
        Si los productos están clasificados por categorías, calcula el promedio de ventas por tienda y categoría de productos.
    Utiliza groupby() en Pandas para calcular las ventas totales por tienda o por categoría.
5. Análisis de inventarios (Pandas)
    Calcula la rotación de inventarios para cada tienda. Esto se hace dividiendo las ventas totales por el stock disponible de cada producto.
    Almacena los resultados en una nueva columna dentro del DataFrame de inventarios.
    Filtra y muestra las tiendas con niveles críticos de inventario, es decir, aquellas tiendas donde el porcentaje de productos vendidos sea menor al 10% del stock disponible.
    Utiliza groupby() y operaciones matemáticas para calcular la rotación de inventarios.
    Aplica filtros con Pandas para identificar las tiendas con niveles críticos.
6. Satisfacción del cliente (Pandas)
    Realiza un análisis de la satisfacción de los clientes en cada tienda. Relaciona estos datos con el rendimiento de las ventas.
    Filtra las tiendas con niveles bajos de satisfacción (< 60%) y haz recomendaciones para mejorar el rendimiento de estas tiendas.
7. Operaciones con Numpy
    Usar Numpy para realizar los siguientes cálculos sobre las ventas:
        Mediana de las ventas totales.
        Desviación estándar de las ventas totales.
    Para los cálculos, convierte la columna Total_Ventas del DataFrame de Pandas a un array de Numpy usando .to_numpy (o .values si lo prefieres).
    Genera arrays aleatorios utilizando la biblioteca Numpy para simular proyecciones de ventas futuras.
    Usa el módulo de aleatoriedad de Numpy y asegúrate de establecer una semilla (seed) para obtener resultados reproducibles.
Estructura del proyecto
Archivo principal: analisis_red_tiendas.ipynb

Este notebook será el archivo donde se importan y procesan los datos, se realizan los análisis solicitados, y se muestran los resultados. Incluirá el procesamiento con Pandas y cálculos con Numpy.
Archivos CSV:
    sales.csv: datos de ventas.
    inventories.csv: datos de inventarios.
    satisfaction.csv: datos de satisfacción de clientes.

    

CRITERIOS DE CALIFICACIÓN

Carga y manejo de datos (Pandas)
Cargar correctamente los datos de los archivos CSV (sales.csv, inventories.csv, satisfaction.csv) en Pandas. Limpiar los datos eliminando filas con valores nulos y verificar que los DataFrames tengan la estructura correcta para el análisis.
Peso: 30%
Análisis de datos (Pandas)
Realizar correctamente el análisis de ventas totales, rotación de inventarios y satisfacción del cliente. Filtrar correctamente las tiendas con niveles críticos de inventario (<10%) y con baja satisfacción del cliente (<60%).
Peso: 30%
Cálculos estadísticos (Numpy)
Utilizar Numpy para calcular la mediana y desviación estándar sobre las ventas. El objetivo es comprobar que sabes usar Numpy, aunque la operación se pueda hacer igualmente en Pandas debes usar Numpy.
Peso: 20%
Simulación de datos (Numpy)
Simular proyecciones de ventas futuras utilizando arrays aleatorios de Numpy y calcular estadísticas básicas sobre esas proyecciones.
Peso: 20%    
"""
