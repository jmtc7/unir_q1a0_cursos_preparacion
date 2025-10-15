
from datetime import datetime  # Generate sequences of dates
import pandas as pd  # Generate and manipulate dataframes
import numpy as np  # Making random choices

def tipos_datos() -> None:
  """
  Crea un DataFrame de Pandas que contenga información sobre ventas de productos. El DataFrame debe tener las siguientes columnas: 'producto', 'precio', 'unidades_vendidas' y 'fecha_venta'.

  Incluye al menos 5 productos diferentes con sus respectivos datos. Las fechas de venta deben estar en formato datetime y corresponder al año actual.

  Una vez creado el DataFrame, realiza las siguientes operaciones:

      Añade una nueva columna llamada 'ingresos_totales' que calcule el producto entre 'precio' y 'unidades_vendidas'.
      Muestra los productos ordenados de mayor a menor ingreso total.
      Calcula y muestra el precio promedio de todos los productos.
      Identifica y muestra el producto con más unidades vendidas.
  """
  df = pd.DataFrame({'producto': ['jabón', 'galletas', 'leche', 'mandarinas', 'pollo'],
                      'precio': [4, 2, 1, 3, 5],
                      'unidades_vendidas': [10, 20, 35, 15, 7],
                      'fecha_venta': [datetime(2025, 3, 30),
                                      datetime(2025, 5, 12),
                                      datetime(2025, 6, 7),
                                      datetime(2025, 7, 20),
                                      datetime(2025, 10, 14)]})

  # Añadir columna 'ingresos_totales'
  df.eval('ingresos_totales = precio*unidades_vendidas', inplace=True)

  # Ordenar productos por ingresos ingresos_totales (max -> min)
  df_ordenado = df.sort_values(by='ingresos_totales', ascending=False)
  print(f'Pruductos ordenados de mayor a menor ingreso total: {df_ordenado.loc['producto']}')

  # Mostrar precio promedio
  print(f'Precio promedio: {df.loc['precio'].mean()}')

  # Mostrar producto más vendido
  idx_max_ventas = df['unidades_vendidas'].idxmax()
  print(f'Producto más vendido: {df.iloc[idx_max_ventas]}')


###################################################################################################

def unir_dataframes() -> None:
  """
  Tienes dos DataFrames con información de ventas y productos. El primer DataFrame ventas contiene las columnas 'id_producto', 'fecha' y 'unidades_vendidas'. El segundo DataFrame productos contiene las columnas 'id_producto', 'nombre' y 'precio'. Debes realizar las siguientes tareas:

      Crea los dos DataFrames con los siguientes datos:

      ventas: id_producto (A1, A2, A3, A4, A2), fecha (usar fechas consecutivas desde '2023-01-01'), unidades_vendidas (10, 5, 8, 12, 7)
      productos: id_producto (A1, A2, A3, A5), nombre ('Laptop', 'Monitor', 'Teclado', 'Mouse'), precio (1200, 300, 100, 50)

      Realiza una unión (merge) de tipo 'inner' entre ambos DataFrames usando la columna 'id_producto'.

      Realiza una unión (merge) de tipo 'left' entre ambos DataFrames.

      Realiza una unión (merge) de tipo 'outer' entre ambos DataFrames.

      Crea una nueva columna 'valor_total' en el resultado de la unión 'inner' que multiplique las 'unidades_vendidas' por el 'precio'.

  Muestra el resultado de cada operación.
  """
  # Crear dataframes
  ventas = pd.DataFrame({'id_producto': ['A1', 'A2', 'A3', 'A4', 'A2'],
                      'fecha': pd.date_range(start='2023-01-01', periods=5, freq='D'),
                      'unidades_vendidas': [10, 5, 8, 12, 7]})

  productos = pd.DataFrame({'id_producto': ['A1', 'A2', 'A3', 'A5'],
                          'nombre': ['Laptop', 'Monitor', 'Teclado', 'Mouse'],
                          'precio': [1200, 300, 100, 50]})


  # Merge de tipo 'inner' usando la columna 'id_producto'
  inner_merge = pd.merge(ventas, productos, on='id_producto', how='inner')
  print(f'Inner merge:\n{inner_merge}\n')

  # Merge de tipo 'left'
  left_merge = pd.merge(ventas, productos, how='left')
  print(f'Left merge:\n{left_merge}\n')

  # Merge de tipo 'outer'
  outer_merge = pd.merge(ventas, productos, how='outer')
  print(f'Outer merge:\n{outer_merge}\n')

  # Crear columna 'valor_total' en el resultado del merge 'inner' (unidades_vendidas*precio)
  inner_merge['valor_total'] = inner_merge['unidades_vendidas'] * inner_merge['precio']
  print(f'Inner merge con "valor_total" añadido:\n{inner_merge}')

def filtrar_dataframes() -> None:
  """
  Crea un DataFrame de ventas con las siguientes columnas: 'producto', 'categoria', 'precio' y 'stock'. Incluye al menos 8 productos de diferentes categorías (por ejemplo: 'Electrónica', 'Ropa', 'Hogar'). Luego, realiza las siguientes operaciones de filtrado:

      Filtra los productos que pertenecen a la categoría 'Electrónica'.
      Encuentra los productos con precio mayor a 50 y stock menor a 20.
      Selecciona los productos que contengan la letra 'a' en su nombre.
      Utiliza el método query() para encontrar productos de la categoría 'Hogar' con precio menor a 30.

  Muestra el resultado de cada filtrado por separado.
  """
  ventas = pd.DataFrame({'producto': ['Teléfono', 'Camiseta', 'Sábana', 'Ordenador', 'Chaqueta', 'Sartén', 'Auriculares', 'Pantalones'],
                      'categoria': ['Electrónica', 'Ropa', 'Hogar', 'Electrónica', 'Ropa', 'Hogar', 'Electrónica', 'Ropa'],
                      'precio': [400, 30, 15, 1000, 100, 20, 50, 50],
                      'stock': [10, 5, 8, 9, 6, 11, 12, 7]})

  productos_elect = ventas[ventas['categoria'] == 'Electrónica']
  print(f'Productos de electrónica:\n{productos_elect}\n')

  caros_exclusivos = ventas[(ventas['precio'] > 50) & (ventas['stock'] < 20)]
  print(f'Productos con precio>50 y stock<20:\n{caros_exclusivos}\n')

  productos_a = ventas[ventas['producto'].str.contains('a', case=False)]
  print(f'Productos con "a" en el nombre:\n{productos_a}\n')

  hogar_baratos = ventas.query("categoria == 'Hogar' and precio < 30")
  print(f'Productos hogar con precio<30:\n{hogar_baratos}\n')

def tablas_pivotantes() -> None:
  """
  Utilizando Pandas, crea una tabla pivotante que analice datos de ventas por categoría de producto y región.

  Primero, crea un DataFrame con los siguientes datos:

      'categoría': Distribuye 30 valores entre ['Electrónica', 'Ropa', 'Hogar']
      'región': Distribuye 30 valores entre ['Norte', 'Sur', 'Este', 'Oeste']
      'ventas': 30 valores aleatorios entre 100 y 1000
      'unidades': 30 valores aleatorios entre 1 y 20

  Luego, crea una tabla pivotante que muestre:

      La suma total de ventas para cada combinación de categoría y región
      Incluye totales por fila y columna (usando el parámetro margins)
      Reemplaza los valores NaN con ceros
  """
  # Listas para hacer la selección aleatoria más adelante
  categorias = ['Electrónica', 'Ropa', 'Hogar']
  regiones = ['Norte', 'Sur', 'Este', 'Oeste']

  # Generar 30 registros aleatorios
  data = {
      'categoría': np.random.choice(categorias, size=30),
      'región': np.random.choice(regiones, size=30),
      'ventas': np.random.randint(100, 1001, size=30),
      'unidades': np.random.randint(1, 21, size=30)
  }

  df = pd.DataFrame(data)

  # Sumar ventas para cada combinación de categoría y región
  tabla_compleja = df.pivot_table(values='ventas',
                                  index='categoría',
                                  columns='región',
                                  aggfunc={'ventas': 'sum'},
                                  fill_value=0,
                                  margins=True)

def main() -> None:
  tipos_datos()
  unir_dataframes()
  filtrar_dataframes()
  tablas_pivotantes()


if __name__ == '__main__':
  main()
