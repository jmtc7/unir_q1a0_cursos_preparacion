import matplotlib.pyplot as plt
import numpy as np

def graficos_univariantes() -> None:
  fig, ax = plt.subplots(1, 4)  # 1 row with 4 columns

  datos = np.random.standard_normal(1000)  # Datos aleatorios
  ax[0].hist(datos, bins=30, color='blue', alpha=0.7, edgecolor='black')  # Otros parámetros: cumulative, density/normalización
  ax[0].set_xlabel('Valor')
  ax[0].set_ylabel('Frecuencia')
  ax[0].title.set_text('Histograma')

  labels = 'A', 'B', 'C', 'D'
  sizes = [15, 30, 45, 10]
  ax[1].pie(sizes, labels=labels, autopct='%1.1f%%')
  ax[1].title.set_text('Gráfico de sectores (pastel)')

  data = [np.random.normal(0, std, 100) for std in range(1, 4)]
  ax[2].boxplot(data, vert=True, patch_artist=True, showmeans=True,  # Orientar cajas verticalmente, dar color y mostrar media (verde)
            boxprops=dict(facecolor='lightblue', color='blue'),         # Personalizar cajas
            whiskerprops=dict(color='blue'),                            # Personalizar bigotes (líneas verticales)
            capprops=dict(color='blue'),                                # Personalizar 'caps' (límites de bigotes)
            flierprops=dict(marker='o', color='red', alpha=0.5),        # Personalizar outliers
            medianprops=dict(color='red'))                              # Personalizar mediana
  ax[2].title.set_text('Diagrama de Caja y Bigotes (boxplot)')
  ax[2].set_xlabel('Grupos')
  ax[2].set_ylabel('Valores')
  
  parts = ax[3].violinplot(data, showmeans=True, showmedians=True)  # Mostrar medias (verde) y medianas (rojo)
  for pc in parts['bodies']:
      pc.set_facecolor('lightblue')  # Personalizar color del relleno
      pc.set_edgecolor('black')      # Personalizar color de los bordes
      pc.set_alpha(0.7)              # Configurar transparencia
  parts['cmedians'].set_edgecolor('red')
  ax[3].title.set_text('Gráfico de Violín (violinplot)')
  ax[3].set_xlabel('Grupos')
  ax[3].set_ylabel('Valores')

  plt.show()

def graficos_bivariantes() -> None:
  fig, ax = plt.subplots(1, 4)  # Grid of 1 row with 4 columns

  x = np.array([5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 5, 6, 7])
  y = np.array([7, 4, 3, 8, 3, 2, 4, 9, 6, 1, 8, 7, 1, 2, 6])
  m, b = np.polyfit(x, y, 1)  # Calcular coeficientes de la línea de regresión
  ax[0].scatter(x, y, color='red', marker='*', label='Samples')  # Color rojo y '*' como puntos
  ax[0].plot(x, m*x + b, color='blue', label='Regression')  # Añadir línea de regresión
  ax[0].grid()  # Add grid
  ax[0].legend()  # Add legend
  ax[0].set_xlabel('Variable X')
  ax[0].set_ylabel('Variable Y')
  ax[0].title.set_text('Diagrama de dispersión con regresión')

  x = [0, 1, 2, 3, 4]
  y1 = [0, 1, 4, 9, 16]
  y2 = [0, 1, 2, 3, 4]
  ax[1].plot(x, y1, marker='x', linestyle='--', color='red', label='Linea 1')  # Linea discontinuea con puntos 'x'
  ax[1].plot(x, y2, marker='s', color='orange', label='Lina 2')                # Linea naranja con puntos cuadrados
  ax[1].legend()  # Add legend
  ax[1].set_xlabel('Tiempo')
  ax[1].set_ylabel('Valor')
  ax[1].title.set_text('Gráfico de líneas')

  categorias = ['A', 'B', 'C', 'D']
  valores1 = [3, 2, 5, 7]
  valores2 = [4, 6, 2, 5]
  ax[2].bar(categorias, valores1, color='skyblue', label='Conjunto 1', hatch='/')  # Azul claro con patrón
  ax[2].bar(categorias, valores2, bottom=valores1, color='lightgreen', label='Conjunto 2', hatch='\\')  # Verde claro con patrón
  ax[2].title.set_text('Gráfico de barras apiladas')
  ax[2].set_xlabel('Categorías')
  ax[2].set_ylabel('Valores')
  ax[2].legend()

  x = np.arange(len(categorias))
  ancho = 0.35  # Ancho de las barras
  ax[3].bar(x - ancho/2, valores1, width=ancho, label='Conjunto 1')
  ax[3].bar(x + ancho/2, valores2, width=ancho, label='Conjunto 2')
  ax[3].title.set_text('Gráfico de barras agrupadas')
  ax[3].set_xlabel('Categorías')
  ax[3].set_ylabel('Valores')
  ax[3].set_xticks(x, categorias)  # Etiquetar correctamente las posiciones en el eje x.
  ax[3].legend()

  plt.show()

def graficos_multivariantes() -> None:
  """
  heatmaps de múltiples variables (x, y, color)
  dispersion + tamaño y color (x, y, size, color)
  pares de gráficas (pairplots)
  gráficos de dispersión 3d
  gráficos de superfície 3d
  """
  fig, ax = plt.subplots(1, 4)  # Grid of 1 row with 4 columns

  data = np.random.random((10, 10))
  ax[0].imshow(data, cmap='hot', interpolation='nearest')
  ax[0].title.set_text('Mapa de calor')
  plt.show()

if __name__ == '__main__':
   graficos_univariantes()
   graficos_bivariantes()
   graficos_multivariantes()
   # TODO: Add world map visualization like https://stackoverflow.com/questions/72598996/indexerror-too-many-indices-for-array-array-is-1-dimensional-but-2-were-index
