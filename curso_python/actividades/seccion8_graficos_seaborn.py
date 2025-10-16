import matplotlib.pyplot as plt  # Mostrar gráficos
import seaborn as sns            # Generar gráficos
import pandas as pd              # Generar datos
import numpy as np               # Generar datos


def graficos_seaborn() -> None:
    # Diagrama de dispersión con variable categórica (género)
    sns.set_theme()  # Configurar el tema de Seaborn
    datos = sns.load_dataset('tips')  # Cargar un conjunto de datos de ejemplo
    sns.scatterplot(data=datos, x='total_bill', y='tip', hue='time')
    plt.title('Diagrama de dispersión con variable categórica')
    plt.xlabel('Total de la cuenta ($)')
    plt.xlabel('Propina ($)')
    plt.show()  # Mostrar el gráfico

    # Histograma con estimación de densidad (Kernel Density Estimation)
    sns.histplot(data=datos, x='total_bill', kde=True)
    plt.show()

    # Boxplot de la cuenta total por día de la semana
    sns.boxplot(data=datos, x='day', y='total_bill')
    plt.show()

    # Violinplot de la cuenta total por tiempo de comida
    sns.violinplot(data=datos, x='time', y='total_bill')
    plt.show()

    # Pairplot con variable categórica (género)
    sns.pairplot(data=datos, hue='sex')
    plt.show()

    # Gráfico de barras con estilo y paleta de colores personalizados
    sns.set_style('whitegrid')
    sns.set_palette('bright')
    sns.barplot(data=datos, x='day', y='total_bill', hue='sex')
    plt.show()

def datos_numpy_y_pandas() -> None:
    # Diagrama de dispersión con datos de NumPy
    x = np.random.random(100)
    y = np.random.random(100)
    sns.scatterplot(x=x, y=y)
    plt.show()

    # Gráfico de barras con datos de Pandas
    datos = pd.DataFrame({'edad': [23, 45, 12, 36, 22],
                          'ingresos': [50000, 80000, 20000, 60000, 45000],
                          'sexo': ['M', 'F', 'M', 'F', 'M']})
    sns.barplot(data=datos, x='sexo', y='ingresos')
    plt.show()

    # Gráfico de línea con datos e indexación de Pandas
    ventas = pd.DataFrame({'fecha': pd.date_range(start='2023-01-01', periods=12, freq='ME'),
                           'monto': np.random.integers(1000, 5000, size=12)})
    ventas.set_index('fecha', inplace=True)  # Convertir la columna 'fecha' en el índice del DF
    sns.lineplot(data=ventas, x=ventas.index, y='monto')  # Usar indexación de Pandas
    plt.show()

    # Crear un gráfico de barras con agregación de Pandas (mean)
    sns.barplot(data=datos, x='sexo', y='ingresos', estimator=np.mean)
    plt.show()

    # Gráfico de dispersión con datos filtrados (indexación booleana)
    datos_filtrados = datos[datos['edad'] > 30]
    sns.scatterplot(data=datos_filtrados, x='edad', y='ingresos')
    plt.show()

def graficos_univariantes() -> None:
    """
    Genera una figura con 3 subplots mostrando gráficos univariantes. Respectivamente:
    - Histograma
    - Diagramas de caja y bigotes (boxplot) con swarmplot
    - Gráfico de violín con swarmplot
    """
    # Cargar el conjunto de datos y crear subplots
    super_titulo = 'Gráficos Univariantes'
    fig, ax = plt.subplots(1, 3, figsize=(18, 4), num=super_titulo)
    df = sns.load_dataset('tips')
    fig.suptitle(super_titulo)

    # Histograma con KDE
    sns.histplot(data=df, x='total_bill', bins=20, kde=True, ax=ax[0])
    ax[0].set_title('Histograma con KDE')
    ax[0].set_xlabel('Variable 1')
    ax[0].set_ylabel('Frecuencia')

    # Diagrama de caja y bigotes (box-plot) con swarm-plot
    sns.boxplot(data=df, x='total_bill', ax=ax[1])
    sns.swarmplot(data=df, x='total_bill', color='orange', size=3, ax=ax[1])  # Añadir todas las muestras
    ax[1].set_title('Boxplot con swarmplot')
    ax[1].set_xlabel('Variable 1')

    # Gráfico de violín (violin-plot) con swarm-plot
    sns.violinplot(data=df, x='total_bill', inner='quartile', ax=ax[2])  # Mostrar cuartiles en el interior
    sns.swarmplot(data=df, x='total_bill', color='orange', size=3, ax=ax[2])
    ax[2].set_title('Violinplot con swarmplot')
    ax[2].set_xlabel('Variable 1')

    plt.show()

def graficos_bivariantes() -> None:
    """
    Genera una figura con múltiples subplots mostrando gráficos bivariantes. Respectivamente:
    - Histograma con variable categórica
    - Histograma bidimensional
    - Diagramas de caja y bigotes (boxplot) con variable categórica
    - Gráfico de violín (violinplot) con variable categórica
    """
    # Cargar el conjunto de datos y crear subplots
    super_titulo = 'Gráficos Bivariantes'
    fig, ax = plt.subplots(2, 4, figsize=(16, 8), num=super_titulo)
    df = sns.load_dataset('tips')
    fig.suptitle(super_titulo)

    # Histograma con variable categórica y KDE
    sns.histplot(data=df, x='total_bill', bins=20, kde=True, hue='sex', multiple='stack', ax=ax[0, 0])  # Con multiple='dodge' los bins no se apilan
    ax[0, 0].set_title('Histograma categórico con KDE')
    ax[0, 0].set_xlabel('Variable 1')
    ax[0, 0].set_ylabel('Frecuencia')

    # Histograma bidimensional
    hist = sns.histplot(data=df, x='total_bill', y='tip', ax=ax[0, 1])
    ax[0, 1].set_title('Histograma bidimensional')
    ax[0, 1].set_xlabel('Variable 1')
    ax[0, 1].set_ylabel('Variable 2')

    # Diagrama de caja y bigotes (box-plot) con variable categórica
    sns.boxplot(data=df, x='day', y='total_bill', hue='day', palette='Set2', ax=ax[0, 2])  # Paleta de colores personalizada (hue = x)
    ax[0, 2].set_title('Boxplot con variable categórica')
    ax[0, 2].set_xlabel('Variable 1')
    ax[0, 2].set_ylabel('Variable 2')

    # Gráfico de violín con variable categórica
    sns.violinplot(data=df, x='day', y='total_bill', hue='day', palette='Set2', ax=ax[0, 3])  # Paleta de colores personalizada (hue = x)
    ax[0, 3].set_title('Violinplot con variable categórica')
    ax[0, 3].set_xlabel('Variable 1')
    ax[0, 3].set_ylabel('Variable 2')

    # Gráfico de línea sin suavizar
    df = sns.load_dataset('fmri')  # Cargar nuevos datos con serie temporal
    sns.lineplot(data=df, x='timepoint', y='signal', estimator=None, units='subject', ax=ax[1, 0])  # NO suavizar
    ax[1, 0].set_title('Gráfico de línea SIN suavizar')
    ax[1, 0].set_xlabel('Variable 1')
    ax[1, 0].set_ylabel('Variable 2')

    plt.show()

def graficos_multivariantes() -> None:
    """
    Genera una figura con 4 subplots mostrando gráficos multivariantes. Respectivamente:
    - Diagramas de caja y bigotes (boxplot) con 2 variables categóricas
    - Gráfico de violín (violinplot) con 2 variables categóricas
    - Gráfico de línea con variable categórica
    """
    # Cargar el conjunto de datos y crear subplots
    super_titulo = 'Gráficos Multivariantes'
    fig, ax = plt.subplots(1, 4, figsize=(16, 4), num=super_titulo)
    df = sns.load_dataset('tips')
    fig.suptitle(super_titulo)

    # Diagrama de caja y bigotes (box-plot) con 2 variables categórica
    sns.boxplot(data=df, x='day', y='total_bill', hue='time', ax=ax[0])
    ax[0].set_title('Boxplot 3D')
    ax[0].set_xlabel('Variable 1')
    ax[0].set_ylabel('Variable 2')
    ax[0].legend(title='Comida')

    # Gráfico de violín (violin-plot) con 2 variables categórica
    sns.violinplot(data=df, x='day', y='total_bill', hue='sex', split=True, ax=ax[1])  # `split` divide el violín en dos partes
    ax[1].set_title('Violinplot 3D')
    ax[1].set_xlabel('Variable 1')
    ax[1].set_ylabel('Variable 2')
    ax[1].legend(title='Género')

    # Gráfico de línea con 2 variables categóricas (4D)
    df = sns.load_dataset('fmri')  # Cargar nuevos datos con serie temporal
    sns.lineplot(data=df, x='timepoint', y='signal', hue='region', style='event', markers=True, ax=ax[2])  # Categóricas: Región y eventos
    ax[2].set_title('Gráfico de línea')
    ax[2].set_xlabel('Variable 1')
    ax[2].set_ylabel('Variable 2')

    plt.show()

def grafico_pairplot() -> None:
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
    grafico_pairplot()
