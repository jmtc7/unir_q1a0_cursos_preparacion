# Introducción

## 1. Introducción
Los objetivos del curso son:
- Contextualizar Python desde su historia y sus características.
- Comprender el problema de las versiones que ha existido hasta este año.
- Conocer los pasos para instalar Python en nuestro equipo.
- Conocer las distintas herramientas existentes para programar en Python.
- Comprender el entorno de desarrollo de Jupyter Notebook.

La evaluación consistirá en:
- 4 actividades autocorregibles (2 puntos cada una) con intentos ilimitados.
- 8 test autocorregibles (0,25 puntos cada uno) con intentos ilimitados.

## 2. Qué es Python?
Existe una guía de estilo oficial llamada [PEP 8](https://peps.python.org/pep-0008/)  (Python Enhancement Proposal). La [PEP257](https://peps.python.org/pep-0257/) describe cómo deben hacerse las *docstrings*, aunque el [formato Sphynx](https://www.sphinx-doc.org/en/master/usage/domains/python.html) es algo más detallado y permite documentación automática, por lo que es cada vez más utilizado.

Algunas características de Python son el tipado dinámico (los tipos de las variables no los especifica el usuario), ser un lenguaje multiparadigma (permite programación orientada a objetos, programación imperativa y programación funcional), es interpretado (no compilado, lo que le permite ser multiplataforma) y es extensible (tiene muchos módulos). Algunos de los módulos más comunes (divididos por campo de aplicación) son:
- **Ciencia y análisis de datos**: NumPy (estructuras de datos eficientes), Pandas(procesar datos tabulares), MatPlotLib y Seaborn (visualización), SciKit-Learn (aprendizaje automático o *Machine Learning*), TensorFlow, PyTorch y Keras (aprendizaje profundo o *Deep Learning*), NLTK, SpaCy y Transformers (procesamiento de lenguaje natural) y OpenCV (visión por computador).
- **Desarrollo web**: Django (framework completo con patrón MTV, Model-Template-View, con ORM, autenticación y panel de administración), Flask (framework minimalista), FastAPI (framework adaptado a APIs con validación automática, documentación y alto rendimiento) y otras herramientas como SQLAlchemy (interactuar con bases de datos relacionales), Celery (gestión de tareas asíncronas y en segundo plano) o Jinja2 (motor de plantillas HTML).
- **Automatización y scripting**: Procesado de archivos CSV y JSON, interactuación con el sistema operativo (os, shutil, datetime, etc.), web scraping (request y BeautifulSoup), automatización de tests software (PyTest, Selenium webdriver), etc.
- **Aplicaciones gráficas**: TKinter (biblioteca estándar sencilla), PyQT (más moderna y personalizable), wxPython (para apariencia nativa en diferentes sistemas operativos).
- **DevOps y administración de sistemas**: Automatización de despliegues (Ansible, Fabric y Paramiko), gestión de código (Pulumi y AWS CDK) y monitorización y análisis de sistemas y logs.

Actualmente estamos en la versión 3 de Python, la 1 y la 2 han sido descontinuadas en 2020 (la última fue 2.7). En este curso usaremos Python 3.8.

**Comparándolo con R**, R se especializa en estadística y visualización de datos, mientras que Python ofrece un enfoque más generalista, aunque es más eficiente si se tratan muchos datos, es más intuitivo y es mejor para el aprendizaje automático.

## 3. Instalación
Puedes instalar Python 3 desde la [web oficial](https://www.python.org/downloads/) o utilizando [Anaconda](https://www.anaconda.com/download) o [Microbamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html) (versión más ligera y optimizada de Anaconda).

## 4. Herramientas
Para programar en Python podemos usar IDEs como [Visual Studio Code](https://code.visualstudio.com/) (otras opciones son PyCharm (puede ejecutar tanto scripts como notebooks), Eclipse o Spyder) o herramientas más interactivas como los [Jupyter Notebooks](https://jupyter.org/). También es posible usar editores de texto (como Nano (UNIX), Vim (UNIX), Bloc de Notas (Windows), Sublime, Atom, Notepad++ (Windows) o Visual Code) para hacer pequeñas modificaciones rápidas.

### 4.1. Jupyter Notebook
Es una aplicación web que permite ejecutar código Python de forma interactiva. Tambien permite añadir bloques de comentarios en Markdown y navegar por las carpetas de nuestro ordenador.

Esta será la herramienta utilizada para el curso.