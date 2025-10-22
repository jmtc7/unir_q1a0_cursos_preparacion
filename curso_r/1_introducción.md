# Introducción
## 1. Introducción
R es un lenguaje interpretado orientado al análisis y visualización de datos. R está disponible para todos los sistemas operativos en su [web oficial](https://www.r-project.org/), al igual que [RStudio](https://posit.co/download/rstudio-desktop/) (*Positron* es el sucesor de RStudio y también soporta Python). La última versión estable de R hasta la fecha es la 4.4.1, publicada en junio de 2024. Algunas de las ventajas de utilizar R son:
- Diseñado desde un principio para manipular datos de forma rápida y precisa.
- Fácilmente automatizable con scripts.
- Es capaz de leer la mayoría de tipos de datos.
- Las visualizaciones son simples y poderosas.
- La comunidad online de R destaca por su amabilidad e inclusividad.
- Es flexible y extensible gracias a los paquetes creados por la comunidad.
- Su IDE, RStudio, permite tener código, resultados y visualizaciones en el mismo lugar. También ofrece  [RStudio Cloud](https://posit.cloud/).
- R es gratuito y ámpliamente utilizado en el ámbito académico, pero también en Google, Facebook, Airbnb, Uber, etc.

## 2.Instalación
La manera de **instalar R** depende del sistema operativo, siempre se usa **CRAN** (*Comprehensive R Archive Network*), que es el respositorio central de R y está compuesto por servidores repartidos por el mundo (también conocidos como *sitios espejo*). Puedes ir al [servidor en la nube de R](https://cloud.r-project.org/), que elegirá el servidor más cercano a ti automáticamente para descargarlo. Para instalarlo en Ubuntu, deberás ejecutar lo siguiente:

```bash
# update indices
sudo apt update -qq
# install two helper packages we need
sudo apt install --no-install-recommends software-properties-common dirmngr
# add the signing key (by Michael Rutter) for these repos
# To verify key, run gpg --show-keys /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc 
# Fingerprint: E298A3A825C0D65DFD57CBB651716619E084DAB9
wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | sudo tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
# add the repo from CRAN -- lsb_release adjusts to 'noble' or 'jammy' or ... as needed
sudo add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"
# install R itself
sudo apt install --no-install-recommends r-base
```

Tras instalar R, se puede proceder a **instalar RStudio**. Para hacerlo, accede a la [web oficial](https://posit.co/download/rstudio-desktop/) y descarga y ejecuta el instalador que corresponda a tu sistema operativo. Por ejemplo, para Ubuntu 22 sería `sudo dpkg -i rstudio-2025.09.1-401-amd64.deb`.

## 3. Utilización Básica
En R, los comentarios empiezan con `#`. Se suelen dejar al menos dos espacios entre las líneas de código y el inicio del comentario. Por claridad, los resultados obtenidos por consola se mostrarán precedidos de `##`. Por ejemplo:
```r
# Asignar variables (todos son equivalentes)
x = 10
x <- 10
10 -> x
# Imprimir el valor de la variable dos veces, 
print(x)
## [1] 10
x
## [1] 10
```

Para **obtener ayuda** de cualquier comando (por ejemplo, `mean`), se puede ejecutar `help(mean)` o `?mean`. Esto abrirá una ventana con la documentación de la función, normalmente junto a ejemplos de uso. También es posible obtener **ayuda de paquetes** con `help(package = "stats")`. Si no se conoce el nombre exacto de una función, se puede buscar en todos los paquetes instalados con `help.search("median")`, o en un paquete específico con `help.search("median", package = "stats")`. Esto es equivalente a hacer `??median`. 
