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


# 8.2. Introducción e Instalación de Matplotlib
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

Respecto a los **tipos de gráficos**, tenemos los siguientes (el código para generarlos está en [actividades/seccion8_graficos_matplotlib.py](actividades/seccion8_graficos_matplotlib.py)):

<img src="imgs/8_visualizacion__graficos_univariantes.png" height="300">

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


