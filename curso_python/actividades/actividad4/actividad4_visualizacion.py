# Importar dependencias
from os.path import exists, isfile
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

PATH_CSV = 'superstore_dataset2012.csv'

def cargar_datos(path_csv: str) -> None:
    """
    Verifica si el CSV a cargar existe y es un fichero y carga los datos en un DataFrame.

    :param path_csv: Path hacia el CSV que contiente los datos.
    """
    if not exists(path_csv) or not isfile(path_csv):
        raise SystemExit('El CSV de entrada no existe o no es un fichero.')

    return pd.read_csv(path_csv)

def explorar_y_preparar(datos: pd.DataFrame) -> None:
    """
    Corrige el formato de las columnas con fechas y elimina filas con valores NAN.

    :param datos: DataFrame que contiente los datos.
    """
    datos['Order Date'] = pd.to_datetime(datos['Order Date'], format='mixed', dayfirst=True)
    datos['Ship Date'] = pd.to_datetime(datos['Ship Date'], format='mixed', dayfirst=True)
    datos = datos.dropna()

    # Ordenar datos por fecha de compra
    datos.sort_values(by=['Order Date'], inplace=True)

    print('Muestra de los datos:')
    print(datos.head())

    return datos

def multiples_graficos(datos: pd.DataFrame, super_titulo: str='Visualizaciones de Datos') -> None:
    """
    Genera múltiples gráficos, guarda la figura generada en PNG y la muestra.

    :param datos: DataFrame que contiente los datos.
    :param super_titulo: Titulo para la ventana.
    """
    # Preparar ventana
    fig, ax = plt.subplots(2, 3, figsize=(15, 10), num=super_titulo)
    fig.suptitle(super_titulo)

    # Visualización univariante con Matplotlib #
    # Conclusión: Hay muchas más ventas pequeñas que grandes.
    ax[0, 0].hist(datos['Sales'], bins=10)
    ax[0, 0].set_title('Histograma de ventas')
    ax[0, 0].set_xlabel('Ventas')
    ax[0, 0].set_ylabel('Frecuencia')

    # Conclusión: Hay más ventas o con envío estándar o con envío en el mismo día
    ax[0, 1].bar(datos['Ship Mode'], datos['Sales'])
    ax[0, 1].set_title('Ventas por Tipo de envio')
    ax[0, 1].set_xlabel('Tipo de envio')
    ax[0, 1].set_ylabel('Ventas')

    # Visualización univariante con Seaborn #
    # Conclusión: Vemos muchísima más variabilidad de ventas en envíos con prioridad media
    sns.violinplot(data=datos, x='Sales', y='Order Priority', hue='Ship Mode', palette='Set2', ax=ax[0, 2])
    ax[0, 2].set_title('Ventas y prioridad por Tipo de envio')
    ax[0, 2].set_xlabel('Ventas')
    ax[0, 2].set_ylabel('Prioridad')
    ax[0, 2].legend()

    # Visualización bivariante con Matplotlib #
    # Conclusión: Los mayores beneficios los encontramos en las ventas grandes
    ax[1, 0].scatter(datos['Sales'], datos['Profit'], color='red', marker='*', label='Muestras')  # Color rojo y '*' como puntos
    ax[1, 0].set_title('Ventas vs beneficio')
    ax[1, 0].set_xlabel('Ventas')
    ax[1, 0].set_ylabel('Beneficio')

    # Conclusión: Las ventas se concentran en momentos específicos de cada mes. Hay picos en mayo, noviembre y diciembre
    ax[1, 1].plot(datos['Order Date'], datos['Sales'])
    ax[1, 1].set_title('Evolución de las ventas')
    ax[1, 1].set_xlabel('Fecha de pedido')
    ax[1, 1].set_ylabel('Ventas')

    # Visualización bivariante con Seaborn #
    # Conclusión: Los mayores beneficios los encontramos en las ventas grandes
    sns.regplot(data=datos, x='Profit', y='Sales', line_kws={'color': 'orange'}, ax=ax[1, 2])
    ax[1, 2].set_title('Regresión lineal de ventas por beneficio')
    ax[1, 2].set_xlabel('Beneficio')
    ax[1, 2].set_ylabel('Ventas')

    # Guardar figura y mostrar
    plt.savefig('multiplot.png')
    plt.show()

def grafico_pairplot(datos: pd.DataFrame, columnas: list, var_categorica: str) -> None:
    """
    Genera una figura mostrando pares de gráficos (pair-plots en inglés) utilizando una variable categórica para dividir (y colorear) las muestras.
    
    :param datos: DataFrame que contiente los datos.
    :param columnas: Columnas a utilizar para el pairplot.
    :param var_categorica: Columna a utilizar para agrupar los puntos del pairplot.
    """
    # Conclusión: Sobretodo pedidos con envío estándar. Los pedidos caros tienen cantidades y descuentos pequeños.
    pp = sns.pairplot(datos, vars=columnas, hue=var_categorica, corner=True, diag_kind='kde')  # Sólo mostrar mitad inferior y la densidad en la diagonal
    pp.figure.suptitle("Mitad inferior de un pairplot", fontsize=16)                           # Agregar un título a toda la figura
    pp.figure.tight_layout()                                                                   # Evitar que el título se superponga
    plt.show()

def visualizar_datos(path_csv: str) -> None:
    """
    Genera múltiples visualizaciones de los datos contenidos en un CSV.

    :param path_csv: Path hacia el CSV que contiente los datos.
    """
    datos = cargar_datos(path_csv)
    datos = explorar_y_preparar(datos)

    multiples_graficos(datos)
    grafico_pairplot(datos, ['Sales', 'Quantity', 'Discount', 'Profit'], 'Ship Mode')

if __name__ == '__main__':
    visualizar_datos(PATH_CSV)
