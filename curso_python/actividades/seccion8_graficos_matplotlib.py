
from mpl_toolkits.mplot3d import Axes3D # Habilita los gráficos 3D
import matplotlib.pyplot as plt         # Creación de gráficos
import seaborn as sns                   # Pares de gráficas (pairplots)
import pandas as pd                     # Generación de DataFrames para los pairplots
import numpy as np                      # Generación de números aleatorios

TAMAÑO = (16, 4)  # Tamaño de figura horizontal

def graficos_univariantes() -> None:
    """
    Genera una figura con 4 subplots mostrando gráficos univariantes. Respectivamente:
    - Histograma
    - Gráfico de sectores (pastel o pie-chart en inglés)
    - Diagrama de Caja y Bigotes (boxplot en inglés)
    - Gráfico de Violín (violin-plot en inglés)
    """
    # Crear una figura con 4 subplots en horizontal
    fig, ax = plt.subplots(1, 4, figsize=TAMAÑO)

    datos = np.random.standard_normal(1000)  # Datos aleatorios
    ax[0].hist(datos, bins=30, color='blue', alpha=0.7, edgecolor='black')  # Otros parámetros: cumulative, density/normalización
    ax[0].set_xlabel('Valor')
    ax[0].set_ylabel('Frecuencia')
    ax[0].set_title('Histograma')

    labels = 'A', 'B', 'C', 'D'
    sizes = [15, 30, 45, 10]
    ax[1].pie(sizes, labels=labels, autopct='%1.1f%%')
    ax[1].set_title('Gráfico de sectores (pastel)')

    data = [np.random.normal(0, std, 100) for std in range(1, 4)]
    ax[2].boxplot(data, vert=True, patch_artist=True, showmeans=True,  # Orientar cajas verticalmente, dar color y mostrar media (verde)
            boxprops=dict(facecolor='lightblue', color='blue'),      # Personalizar cajas
            whiskerprops=dict(color='blue'),                         # Personalizar bigotes (líneas verticales)
            capprops=dict(color='blue'),                             # Personalizar 'caps' (límites de bigotes)
            flierprops=dict(marker='o', color='red', alpha=0.5),     # Personalizar outliers
            medianprops=dict(color='red'))                           # Personalizar mediana
    ax[2].set_title('Diagrama de Caja y Bigotes (boxplot)')
    ax[2].set_xlabel('Grupos')
    ax[2].set_ylabel('Valores')

    parts = ax[3].violinplot(data, showmeans=True, showmedians=True)  # Mostrar medias (verde) y medianas (rojo)
    for pc in parts['bodies']:
        pc.set_facecolor('lightblue')  # Personalizar color del relleno
        pc.set_edgecolor('black')      # Personalizar color de los bordes
        pc.set_alpha(0.7)              # Configurar transparencia
    parts['cmedians'].set_edgecolor('red')
    ax[3].set_title('Gráfico de Violín (violinplot)')
    ax[3].set_xlabel('Grupos')
    ax[3].set_ylabel('Valores')

    plt.show()

def graficos_bivariantes() -> None:
    """
    Genera una figura con 4 subplots mostrando gráficos bivariantes. Respectivamente:
    - Diagrama de dispersión (i.e., gráfico de puntos) con una línea de regresión
    - Gráfico de líneas
    - Gráfico de barras apiladas
    - Gráfico de barras agrupadas
    """
    # Crear una figura con 4 subplots en horizontal
    fig, ax = plt.subplots(1, 4, figsize=TAMAÑO)

    # Diagrama de dispersión con línea de regresión
    x = np.array([5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 5, 6, 7])
    y = np.array([7, 4, 3, 8, 3, 2, 4, 9, 6, 1, 8, 7, 1, 2, 6])
    m, b = np.polyfit(x, y, 1)  # Calcular coeficientes de la línea de regresión
    ax[0].scatter(x, y, color='red', marker='*', label='Muestras')  # Color rojo y '*' como puntos
    ax[0].plot(x, m*x + b, color='blue', label='Regresión')       # Añadir línea de regresión
    ax[0].set_title('Diagrama de dispersión con regresión')
    ax[0].set_xlabel('Variable X')
    ax[0].set_ylabel('Variable Y')
    ax[0].legend()  # Añadir leyenda
    ax[0].grid()    # Añadir cuadrícula grid

    # Gráfico de líneas
    x = [0, 1, 2, 3, 4]
    y1 = [0, 1, 4, 9, 16]
    y2 = [0, 1, 2, 3, 4]
    ax[1].plot(x, y1, marker='x', linestyle='--', color='red', label='Línea 1')  # Linea discontinuea con puntos 'x'
    ax[1].plot(x, y2, marker='s', color='orange', label='Línea 2')                # Linea naranja con puntos cuadrados
    ax[1].set_title('Gráfico de líneas')
    ax[1].set_xlabel('Tiempo')
    ax[1].set_ylabel('Valor')
    ax[1].legend()

    # Gráfico de barras apiladas
    categorias = ['A', 'B', 'C', 'D']
    valores1 = [3, 2, 5, 7]
    valores2 = [4, 6, 2, 5]
    ax[2].bar(categorias, valores1, color='skyblue', label='Conjunto 1', hatch='/')  # Azul claro con patrón
    ax[2].bar(categorias, valores2, bottom=valores1, color='lightgreen', label='Conjunto 2', hatch='\\')  # Verde claro con patrón
    ax[2].set_title('Gráfico de barras apiladas')
    ax[2].set_xlabel('Categorías')
    ax[2].set_ylabel('Valores')
    ax[2].legend()

    # Gráfico de barras agrupadas
    x = np.arange(len(categorias))
    ancho = 0.35  # Ancho de las barras
    ax[3].bar(x - ancho/2, valores1, width=ancho, label='Conjunto 1')
    ax[3].bar(x + ancho/2, valores2, width=ancho, label='Conjunto 2')
    ax[3].set_title('Gráfico de barras agrupadas')
    ax[3].set_xlabel('Categorías')
    ax[3].set_ylabel('Valores')
    ax[3].set_xticks(x, categorias)  # Etiquetar correctamente las posiciones en el eje x.
    ax[3].legend()

    plt.show()

def graficos_multivariantes() -> None:
    """
    Genera una figura con 4 subplots mostrando gráficos univariantes. Respectivamente:
    - Mapa de calor (heatmap en inglés) para 3 variables (x, y, color)
    - Gráfico de dispersión para 4 variables (x, y, size, color)
    - Gráficos de dispersión 3D
    - Gráficos de superfície 3D
    """
    # Crear 1 figura y 4 subplots (2 de ellos en 3D)
    fig = plt.figure(figsize=TAMAÑO)
    ax1 = fig.add_subplot(1, 4, 1)
    ax2 = fig.add_subplot(1, 4, 2)
    ax3 = fig.add_subplot(1, 4, 3, projection='3d')
    ax4 = fig.add_subplot(1, 4, 4, projection='3d')

    # Mapa de calor (heatmap) 3D (x, y, color)
    data = np.random.random((10, 10))  # Valores en forma matricial (e.g., matriz de correlación, imagen, etc.)
    mapa = ax1.imshow(data, cmap='hot', interpolation='nearest')  # Varios colores disponibles (viridis, plasma, inferno, magma, etc.)
    ax1.set_title('Mapa de calor 3D')
    fig.colorbar(mapa, ax=ax1)  # Barra de color (se puede compartir entre varios subplots)

    # Diagrama de dispersión con colores y tamaños 4D (x, y, size, color)
    x = np.random.random(100)             # Variable 1
    y = np.random.random(100)             # Variable 2
    sizes = 100 * np.random.random(100)   # Variable 3
    colors = np.random.random(100)        # Variable 4
    disp4d = ax2.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
    ax2.set_title('Gráfico de dispersión 4D')
    ax2.set_xlabel('Variable X')
    ax2.set_ylabel('Variable Y')
    fig.colorbar(disp4d, ax=ax2)

    # Diagrama de dispersión 5D (x, y, z, size, color)
    z = np.random.random(100)
    disp5d = ax3.scatter(x, y, z, c=colors, s=sizes, cmap='viridis', alpha=0.6)
    ax3.set_title('Gráfico de dispersión 5D')
    ax3.set_xlabel('Variable X')
    ax3.set_ylabel('Variable Y')
    ax3.set_zlabel('Variable Z')
    fig.colorbar(disp5d, ax=ax3)

    # Gráfico de superfície 3D
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))
    superficie = ax4.plot_surface(x, y, z, cmap='coolwarm', edgecolor='none')
    ax4.set_title('Gráfico de superfície 3D')
    ax4.set_xlabel('Variable X')
    ax4.set_ylabel('Variable Y')
    ax4.set_zlabel('Variable Z')
    plt.colorbar(superficie, ax=ax4, label='Valor de Z')

    plt.show()

def graficos_pairplot() -> None:
    """
    Genera una figura mostrando pares de gráficos (pair-plots en inglés) utilizando una variable categórica para dividir (y colorear) las muestras.
    """
    # DataFrame de ejemplo con variable categórica que divida las muestras en 2 grupos
    data = pd.DataFrame({
        'Variable A': np.random.random(100),
        'Variable B': np.random.random(100),
        'Variable C': np.random.random(100),
        'Variable D': np.random.random(100)
    })
    data['Categoría'] = np.random.choice(['Grupo 1', 'Grupo 2'], size=100)

    # Creación del pairplot categórico
    sns.pairplot(data, hue='Categoría')
    plt.show()


if __name__ == '__main__':
    graficos_univariantes()
    graficos_bivariantes()
    graficos_multivariantes()
    graficos_pairplot()
    # TODO: Add world map visualization like https://stackoverflow.com/questions/72598996/indexerror-too-many-indices-for-array-array-is-1-dimensional-but-2-were-index
