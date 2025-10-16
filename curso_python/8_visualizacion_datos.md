# Visualización de Datos
En esta sección se profundizará en `Matplotlib` y `Seaborn`. Veremos qué tipos de gráficos proponen, sus conceptos fundamentales, etc.

## 8.1. Introducción
`Matplotlib` propone varios tipos de gráficos según el número de variables implicadas:
- **Gráficos univariantes**: Histogramas, diagramas de barras, diagramas circulares y gráficos de líneas. Suelen usarse para descubrir distribuciones y tendencias.
- **Gráficos bivariantes**: Diagramas de dispersión, gráficos de líneas múltiples y gráficos de barras agrupadas. Útiles para relacionar dos variables.
- **Gráficos multivariantes**: Gráficos 3D, gráficos de contorno, mapas de calor y gráficos de burbujas.

Veremos cómo organizarlos con varios `subplot` y `GridSpec`, controlar los ejes, escalas y proyecciones, aplicar temas, paletas de colores y estilos, añadir títulos, etiquetas, anotaciones y leyendas y guardar gráficos con alta calidad.

`Seaborn` es una extensión de `Matplotlib` especializada en visualización estadística con estilos atractivos, integración con `Pandas` y visualizaciones complejas. Propone:
- **Gráficos univariantes**: Diagramas de distribución (histogramas, KDE), boxplots, violinplots y countplots.
- **Gráficos bivariantes**: Scatterplots, regplots, lmplots y jointplots.
- **Gráficos multivariantes**: Pairplots, heatmaps, clustermap y visualizaciones categóricas facetadas.

Veremos cómo personalizar temas, paletas y estilos con más facilidad que con `Matplotlib`, controlar títulos, etiquetas y leyendas y crear gráficos compuestos con FacetGrid, PairGrid y JointGrid.


# 8.2. Matplotlib
`Matplotlib` ofrece una **API orientada a objetos** para crear y manipular objetos como objetos como figuras y ejes. Es fácilmente integrable con `NumPy` y `Pandas` y permite **exportar los gráficos** generados en múltiples formatos (`PNG`, `PDF`, `SVG`, `EPS`, etc) con alta calidad. También ofrece **gráficos interactivos**

Además de su interfaz orientada a objetos, `Matplotlib` ofrece `PyPlot`, otra inferfaz similar a MATLAB para crear gráficos rápidamente. Un ejemplo básico de uso de `PyPlot` es:

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [10, 20, 25, 30])  # Mostrar datos
plt.set_title('Título del gráfico')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()  # Mostrar gráfico
```

La interfaz orientada a objetos ofrece más control y se usa cuando queremos sub-gráficos o si se busca la modularidad. Un ejemplo de esta sería:
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # Crear figura y ejes en los que dibujar gráficos (podríamos generar sub-gráficos usando argumentos
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])  # Mostrar datos
ax.set_title('Título del gráfico')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
plt.show()  # Mostrar gráfico
```

Respecto a los **tipos de gráficos**, en las siguientes imágenes se muestran los tipos de gráficos univariantes, bivariantes y multivariantes que propone `Matplotlib` (el código para generarlos está en [actividades/seccion8_graficos_matplotlib.py](actividades/seccion8_graficos_matplotlib.py)). Es necesario precisar que para utilizar los gráficos en 3D, se necesita utilizar el módulo `mpl_toolkits.mplot3d` e inicializar un objeto `Axes3D`.

<img src="imgs/8_visualizacion__graficos_univariantes.png" width="1000">
<img src="imgs/8_visualizacion__graficos_bivariantes.png" width="1000">
<img src="imgs/8_visualizacion__graficos_multivariantes.png" width="1000">

Otro tipo de visualización son los **pares de gráficos** o *pairplots*, que consisten en combinar múltiples variables (4 en el ejemplo) y representar un gráfico de dispersión para cada posible combinación de variables, generando una matriz de gráficos. La **diagonal** de dicha matriz suele ser un histograma que represente la distribución de valores de cada variable. `Seaborn` permite utilizar una **variable categórica** para colorear los puntos, lo que puede ser útil si las muestras de cada variable pertenecen a categorías diferenciadas. Aquí se muestran ejemplos de ambos casos (el código también está en [actividades/seccion8_graficos_matplotlib.py](actividades/seccion8_graficos_matplotlib.py)):

<img src="imgs/8_visualizacion__pairplot.png" height="600">

En el script [actividades/seccion8_graficos_matplotlib.py](actividades/seccion8_graficos_matplotlib.py) se utiliza `plt.subplots()` para organizar **múltiples visualizaciones** en una sola figura. Sin embargo, `Matplotlib` ofrece un control más detallado mediante:
- `plt.subplots_adjust()` y sus parámetros `wspace` y `hspace`, que controlan el espacio entre subplots.
- `GridSpec`, que permite extender subpots sobre múltiples columnas o filas.

Los **ejes** es donde mostramos los gráficos y ofrecen varios elementos configurables, como:
- `set_xlim()` y `set_ylim()` para establecer los números mínimos y máximos de cada eje. Otra opción es `margins()`, que añade un margen alrededor de los datos mostrados sin necesidad de especificar los límites manualmente.
- `set_xscale()` y `set_xscale()` para establecer la escala (linear, logarítmica, etc.). Algunas escalas aceptan el parámetro `linthresh`, que permite mantener una escala lineal hasta cierto punto.
- `set_xlabel()`, `set_xlabel()` y `set_title()` para ponerles etiquetas a los ejes y al gráfico.
- `set_xticks()`, `set_yticks()`, `set_xticklabels()` y `set_yticklabels()` para elegir dónde aparecen las marcas de los ejes y su contenido.

Para guardar los gráficos generados, se utiliza `fig.savefig('grafico.png', dpi=300)` (72 dpi es suficiente para visualizaciones en pantalla, 300 es común para impresiones de alta calidad). Utilizar formatos vectoriales como SVG o PDF es mejor si los gráficos van a incluirse en documentos. Otros argumentos útiles son:
- `metadata`, para incluir un título o un autor en los metadatos de la imagen generada.
- `bbox_inches`, a la que se puede asignar `tight` para minimizar el espacio en blanco alrededor del gráfico.

# 8.3. TODO

# 8.4. TODO

# 8.5. TODO

# 8.6. TODO

# 8.7. TODO

# 8.8. TODO

# 8.9. TODO

# 8.10. TODO

# 8.11. TODO

# 8.12. TODO

# 8.13. TODO

# 8.14. TODO

# 8.15. TODO

# 8.16. TODO

# 8.17. TODO

# 8.18. TODO


