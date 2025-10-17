import matplotlib.pyplot as plt  # Generar figuras y ejes
import seaborn as sns            # Generar gráficos
import numpy as np               # Generar datos

PULGADAS_POR_GRAFICO = 5  # Ppulgadas que debe usarse para cada gráfica

def graficos_univariantes(pulgadas: int=5) -> None:
    """
    Genera una figura con 3 subplots mostrando gráficos univariantes. Respectivamente:
    - Histograma
    - Diagramas de caja y bigotes (boxplot) con swarmplot
    - Gráfico de violín con swarmplot

    :param pulgadas: Tamaño en pulgadas que debe usarse para cada gráfica en la ventana.
    """
    # Configuración de la ventana y creación de subplots
    COLS         = 3
    FILAS        = 1
    FIGSIZE      = (pulgadas*COLS, pulgadas*FILAS)
    SUPER_TITULO = 'Gráficos Univariantes'
    fig, ax      = plt.subplots(FILAS, COLS, figsize=FIGSIZE, num=SUPER_TITULO)
    fig.suptitle(SUPER_TITULO)

    # Cargar datos
    df = sns.load_dataset('tips')

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

def graficos_bivariantes(pulgadas: int=5) -> None:
    """
    Genera una figura con múltiples subplots mostrando gráficos bivariantes. Respectivamente:
    - Gráfico de regresión lineal
    - Gráfico de distribución residual
    - Gráfico de líneas (sin suavizar)
    - Gráfico de barras
    - Histograma con 1 variable categórica
    - Histograma bidimensional
    - Diagramas de caja y bigotes (boxplot) con 1 variable categórica
    - Gráfico de violín (violinplot) con 1 variable categórica

    :param pulgadas: Tamaño en pulgadas que debe usarse para cada gráfica en la ventana.
    """
    # Configuración de la ventana y creación de subplots
    COLS         = 4
    FILAS        = 2
    FIGSIZE      = (pulgadas*COLS, pulgadas*FILAS)
    SUPER_TITULO = 'Gráficos Bivariantes'
    fig, ax      = plt.subplots(FILAS, COLS, figsize=FIGSIZE, num=SUPER_TITULO)
    fig.suptitle(SUPER_TITULO)

    # Cargar datos
    datos_propinas = sns.load_dataset('tips')  # Cargar datos de propinas
    datos_fmri     = sns.load_dataset('fmri')  # Cargar datos FMRI (serie temporal)


    # Gráfico de regresión lineal
    sns.regplot(data=datos_propinas, x='total_bill', y='tip', line_kws={'color': 'orange'}, ax=ax[0, 0])  # Línea de regresión naranja
    ax[0, 0].set_title('Gráfico de regresión lineal')
    ax[0, 0].set_xlabel('Variable 1')
    ax[0, 0].set_ylabel('Variable 2')

    # Gráfico de distribución residual
    sns.residplot(data=datos_propinas, x='total_bill', y='tip', ax= ax[0, 1])
    ax[0, 1].set_title('Gráfico de distribución residual')
    ax[0, 1].set_xlabel('Variable 1')
    ax[0, 1].set_ylabel('Residuo')

    # Gráfico de línea sin suavizar
    sns.lineplot(data=datos_fmri, x='timepoint', y='signal', estimator=None, units='subject', ax=ax[0, 2])  # NO suavizar
    ax[0, 2].set_title('Gráfico de línea SIN suavizar')
    ax[0, 2].set_xlabel('Variable 1')
    ax[0, 2].set_ylabel('Variable 2')

    # Gráfico de barras
    sns.barplot(data=datos_propinas, x='day', y='tip', estimator=sum, errorbar=None, ax=ax[0, 3])  # Total propinas por día sin intervalos de confianza
    ax[0, 3].set_title('Gráfico de barras')
    ax[0, 3].set_xlabel('Variable 1')
    ax[0, 3].set_ylabel('Variable 2')


    # Histograma con variable categórica y KDE
    sns.histplot(data=datos_propinas, x='total_bill', bins=20, kde=True, hue='sex', multiple='stack', ax=ax[1, 0])  # Con multiple='dodge' los bins no se apilan
    ax[1, 0].set_title('Histograma categórico con KDE')
    ax[1, 0].set_xlabel('Variable 1')
    ax[1, 0].set_ylabel('Frecuencia')

    # Histograma bidimensional
    hist = sns.histplot(data=datos_propinas, x='total_bill', y='tip', ax=ax[1, 1])
    ax[1, 1].set_title('Histograma bidimensional')
    ax[1, 1].set_xlabel('Variable 1')
    ax[1, 1].set_ylabel('Variable 2')

    # Diagrama de caja y bigotes (box-plot) con variable categórica
    sns.boxplot(data=datos_propinas, x='day', y='total_bill', hue='day', palette='Set2', ax=ax[1, 2])  # Paleta de colores personalizada (hue = x)
    ax[1, 2].set_title('Boxplot con variable categórica')
    ax[1, 2].set_xlabel('Variable 1')
    ax[1, 2].set_ylabel('Variable 2')

    # Gráfico de violín con variable categórica
    sns.violinplot(data=datos_propinas, x='day', y='total_bill', hue='day', palette='Set2', ax=ax[1, 3])  # Paleta de colores personalizada (hue = x)
    ax[1, 3].set_title('Violinplot con variable categórica')
    ax[1, 3].set_xlabel('Variable 1')
    ax[1, 3].set_ylabel('Variable 2')

    plt.show()

def graficos_multivariantes(pulgadas: int=5) -> None:
    """
    Genera una figura múltiples subplots mostrando gráficos multivariantes. Respectivamente:
    - Gráfico de violín (violinplot) 3D - 2 variables categóricas
    - Gráfico de línea 3D - 1 variable categórica
    - Gráfico de línea 4D - 2 variables categóricas
    - Gráfico de dispersión (puntos) 4D - 2 variables categóricas (podrían ser 3)
    - Heatmap
    - Heatmap de una matriz de correlación con máscara
    - Gráfico de barras agrupadas 3D
    - Gráfico de barras apiladas 3D con porcentajes

    :param pulgadas: Tamaño en pulgadas que debe usarse para cada gráfica en la ventana.
    """
    # Configuración de la ventana y creación de subplots
    COLS         = 4
    FILAS        = 2
    FIGSIZE      = (pulgadas*COLS, pulgadas*FILAS)
    SUPER_TITULO = 'Gráficos Multivariantes'
    fig, ax      = plt.subplots(FILAS, COLS, figsize=FIGSIZE, num=SUPER_TITULO)
    fig.suptitle(SUPER_TITULO)

    # Cargar datos
    datos_propinas = sns.load_dataset('tips')     # Cargar datos de propinas
    datos_fmri     = sns.load_dataset('fmri')     # Cargar datos FMRI (serie temporal)
    datos_flores   = sns.load_dataset('iris')     # Cargar datos flores (divididas por especie)
    datos_vuelos   = sns.load_dataset('flights')  # Cargar datos de vuelos (diferenciados por años)


    # Gráfico de violín (violin-plot) con 2 variables categórica
    sns.violinplot(data=datos_propinas, x='day', y='total_bill', hue='sex', split=True, ax=ax[0, 0])  # `split` divide el violín en dos partes
    ax[0, 0].set_title('Violinplot 3D')
    ax[0, 0].set_xlabel('Variable 1')
    ax[0, 0].set_ylabel('Variable 2')
    ax[0, 0].legend(title='Género')

    # Gráfico de línea con variable categórica (3D)
    sns.lineplot(data=datos_vuelos, x='month', y='passengers', hue='year', palette='coolwarm', ax=ax[0, 1])  # Categórica: Año
    ax[0, 1].set_title('Gráfico de línea 3D')
    ax[0, 1].set_xlabel('Variable 1')
    ax[0, 1].set_ylabel('Variable 2')
    ax[0, 1].legend(title='Año')

    # Gráfico de línea con 2 variables categóricas (4D)
    sns.lineplot(data=datos_fmri, x='timepoint', y='signal', hue='region', style='event', markers=True, ax=ax[0, 2])  # Categóricas: Región y eventos
    ax[0, 2].set_title('Gráfico de línea 4D')
    ax[0, 2].set_xlabel('Variable 1')
    ax[0, 2].set_ylabel('Variable 2')

    # Gráfico de disperisón (puntos) con 2 variables categóricas (4D) -> Con el estilo podrían ser 5
    # Variables categóricas: Especie (color) y ancho del sépalo (tamaño)
    sns.scatterplot(data=datos_flores, x='petal_length', y='petal_width', hue='species', size='sepal_width', sizes=(20, 200), style='species', alpha=0.7, ax=ax[0, 3])
    ax[0, 3].set_title('Gráfico de dispersión 4D')
    ax[0, 3].set_xlabel('Variable 1')
    ax[0, 3].set_ylabel('Variable 2')


    # Mapa de calor (heatmap)
    media = datos_vuelos['passengers'].mean()
    tabla_pivote = datos_vuelos.pivot(index='month', columns='year', values='passengers')    # Poner años en filas, meses en columnas, y #pasajeros en valores
    sns.heatmap(tabla_pivote, cmap='YlGnBu', center=media, vmin=100, vmax=700, ax=ax[1, 0])  # Colores YlGnBu centrados en media de pasajeros y colores en [100; 700]
    ax[1, 0].set_title('Mapa de calor')
    
    # Mapa de calor (heatmap) como matriz de correlación
    matriz_correlacion = datos_propinas.select_dtypes(include=[np.number]).corr()
    mascara = np.triu(np.ones_like(matriz_correlacion, dtype=bool))  # Mascara para la mitad superior de la matriz (porque es simétrica). Se podría filtrar por valor
    ticks = np.arange(len(matriz_correlacion))
    sns.heatmap(matriz_correlacion, cmap='coolwarm', annot=True, mask=mascara, ax=ax[1, 1])  # Colores coolwarm con valores anotados y máscara
    ax[1, 1].set_xticks(ticks, labels=matriz_correlacion.keys(), rotation=45)                # Rotar etiquetas del eje X
    ax[1, 1].set_yticks(ticks, labels=matriz_correlacion.keys(), rotation=0)                 # NO rotar etiquetas del eje Y
    ax[1, 1].set_title('Matriz de correlación')
    ax[1, 1].set_xlabel('Variable 1')
    ax[1, 1].set_ylabel('Variable 2')

    # Gráfico de barras agrupadas (bar-plot) con variable categórica
    sns.barplot(data=datos_propinas, x='day', y='tip', hue='sex', palette='Set2', errorbar=None, ax=ax[1, 2])  # No mostrar barras de error
    ax[1, 2].set_title('Barplot 3D agrupado')
    ax[1, 2].set_xlabel('Variable 1')
    ax[1, 2].set_ylabel('Variable 2')
    ax[1, 2].legend(title='Género')

    # Gráfico de barras apiladas (bar-plot) con variable categórica y porcentajes
    tabla_pivot = datos_propinas.pivot_table(values='tip', index='day', columns='sex', aggfunc='sum', observed=False)  # Semanas en filas, sexo en columnas y propinas en valores
    tabla_porcentajes = tabla_pivot.div(tabla_pivot.sum(axis=1), axis=0)
    barras = tabla_porcentajes.plot(kind='bar', stacked=True, color=['#ff9999','#66b3ff'], ax=ax[1, 3])                # Apilar barras con colores personalizados
    ax[1, 3].set_title('Barplot 3D apilado con porcentajes')
    ax[1, 3].set_xlabel('Variable 1')
    ax[1, 3].set_ylabel('Variable 2')
    ax[1, 3].legend(title='Género')
    for container in barras.containers:
        labels = [f'{v.get_height()*100:.1f}%' for v in container]       # Crear etiquetas con porcentajes
        barras.bar_label(container, labels=labels, label_type='center')  # Añadir etiquetas

    plt.show()

def grafico_jointplot() -> None:
    """
    Genera una figura mostrando un gráficos conjunto (gráfico de regresión con la distribución marginal de cada variable).
    """
    datos = sns.load_dataset('tips')
    jp = sns.jointplot(data=datos, x='total_bill', y='tip', kind='reg')
    plt.setp(jp.ax_joint.lines, color='orange')                        # Cambiar color de la línea de regresión
    plt.setp(jp.ax_marg_x.lines + jp.ax_marg_y.lines, color='orange')  # Cambiar color de las KDEs
    plt.title('Regresión con distribuciones')
    plt.xlabel('Variable 1')
    plt.ylabel('Variable 2')
    plt.tight_layout()  # Evitar que el título se superponga
    plt.show()

def grafico_pairplot() -> None:
    """
    Genera una figura mostrando pares de gráficos (pair-plots en inglés) utilizando una variable categórica para dividir (y colorear) las muestras.
    """
    datos = sns.load_dataset('penguins')
    datos = datos.dropna()                                                                         # Gestionar NaNs (si no, se ignorarán todas sus filas)
    variables_interes = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']                   # Seleccionar sólo algunas de las variables del conjunto
    pp = sns.pairplot(datos, vars=variables_interes, hue='species', corner=True, diag_kind='kde')  # Sólo mostrar mitad inferior y la densidad en la diagonal
    pp.figure.suptitle("Mitad inferior de un pairplot", fontsize=16)                               # Agregar un título a toda la figura
    pp.figure.tight_layout()                                                                       # Evitar que el título se superponga
    plt.show()


if __name__ == '__main__':
    graficos_univariantes(pulgadas = PULGADAS_POR_GRAFICO)
    graficos_bivariantes(pulgadas = PULGADAS_POR_GRAFICO)
    graficos_multivariantes(pulgadas = PULGADAS_POR_GRAFICO)
    grafico_jointplot()
    grafico_pairplot()
