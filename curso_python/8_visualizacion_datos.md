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
ax.set_title('Título del gráfico')
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

Respecto a los **tipos de gráficos**, tenemos los siguientes:
```python
import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.plot(x, y)  # Gráfico de líneas
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Gráfico de líneas')
plt.show()

categorias = ['A', 'B', 'C', 'D', 'E']
plt.bar(categorias, x)  # Gráfico de barras
plt.xlabel('Categoría')
plt.ylabel('Valor')
plt.title('Gráfico de barras')
plt.show()

datos = np.random.standard_normal(1000)  # Datos aleatorios
plt.hist(datos, bins=30)  # Histograma
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma')
plt.show()

x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 5, 6, 7]
y = [7, 4, 3, 8, 3, 2, 4, 9, 6, 1, 8, 7, 1, 2, 6]
plt.scatter(x, y)  # Diagrama de dispersión (gráfico de puntos)
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Diagrama de dispersión')
plt.show()

labels = 'A', 'B', 'C', 'D'
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')  # Gráfico de sectores (pastel)
plt.title('Gráfico de sectores')
plt.show()

data = np.random.random((10, 10))  # Generar datos aleatorios
plt.imshow(data, cmap='hot', interpolation='nearest')  # Mapa de calor (o imágenes)
plt.colorbar()
plt.title('Mapa de calor')
plt.show()
```

> TODO: IMPLEMENTARLO EN SUBPLOTS DE 2x3 y MOSTRAR IMAGEN RESULTANTE
> TODO 2: Continuar por subsección "Guardar gráficos en diferentes formatos"


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


