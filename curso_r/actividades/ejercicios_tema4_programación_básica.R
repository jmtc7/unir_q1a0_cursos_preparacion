# Ejercicios del tema 4: Programación Básica #

# EJERCICIO 1: Determinar calificación de un alumno dada su nota numérica
# 0-5 suspenso, 5-7 aprobado, 7-9 notable, 9-10 sobresaliente
print("EJERCICIO 1")
notas <- c(4, 6, 9)

califs <- ifelse(notas<5, "suspenso",
                 ifelse(notas<7, "aprobado",
                        ifelse(notas<9, "notable",
                               ifelse(notas>10, "indefinido", "sobresaliente"))))

print(califs)  # [OK]


# EJERCICIO 2: Predecir el valor de 'x'
# Respuesta: 3, porque la función es definida, pero no llamada.
cat("\nEJERCICIO 2\n")

x <- 3
my_func <- function(y) {
  x <- 5
  y+5
}

print(x)  # [OK]


# EJERCICIO 3: Programar el cálculo del número inverso del producto de dos
# números a y b y el número inverso de la suma de dichos números. Se debe
# verificar si el inverso existe.
cat("\nEJERCICIO 3\n")

calcular_inversos <- function(a, b) {
  producto <- a * b
  suma <- a + b
  
  # Si el inverso existe, calcularlo. Si no, devolver infinito (división por 0)
  inv_prod = ifelse(producto != 0, 1/producto, Inf)
  inv_sum = ifelse(suma != 0, 1/suma, Inf)
  
  return(list(inv_prod, inv_sum))
}

print(calcular_inversos(1, 2))   # Ambos inversos existen [OK]
print(calcular_inversos(0, 0))   # Ningún inverso existe [OK]
print(calcular_inversos(1, -1))  # Solo 1 inverso existe [OK]


# EJERCICIO 4: Escribir una función con 1 argumento que sume todos los cuadrados
# de todos los números desde 1 hasta n y otra función que haga lo mismo pero que
# cada número esté elevado a sí mismo.
cat("\nEJERCICIO 4\n")

cuadrados_n <- function(n) {
  # Solución propuesta: sum((1:n)^2)
  cuadrados = 0
  for(i in 1:n) {
    cuadrados <- cuadrados + i^2
  }
    
  return(cuadrados)
}

comprobar_identidad <- function(n) {
  suma_cuadrados = cuadrados_n(n)
  formula = (n * (n+1) * (2*n + 1)) / 6
  
  return(suma_cuadrados == formula)
}

potencias_n <- function(n) {
  # Solución propuesta: sum((1:n)^(1:n))
  potencias = 0
  for(i in 1:n) {
    potencias <- potencias + i^i
  }
  
  return(potencias)
}

print(cuadrados_n(3))  # [OK] 1^2+2^2+3^2 = 1+4+9 = 14
print(potencias_n(3))  # [OK] 1^1+2^2+3^3 = 1+4+27 = 32
print(cuadrados_n(5))  # [OK] 1^2+2^2+3^2+4^2+5^2 = 1+4+9+16+25 = 55
print(potencias_n(5))  # [OK] 1^1+2^2+3^3+4^4+5^5 = 1+4+27+256+3125 = 3413
print(comprobar_identidad(5))  # [OK] TRUE

# EJERCICIO 5: Definir un vector vacío de 30 elementos donde se almacenen los 
# resultados de usar la función cuadrados_n() del ejercicio 4 utilizando un 
# bucle for. Repetir lo mismo utilizando sapply().
cat("\nEJERCICIO 5\n")

# Otras opciones: vector("numeric", 30) o rep(NA, 30)
s_n1 <- numeric(30)  # Elementos a 0 por defecto
print(s_n1)

# Rellenar 1er vector con bucle for
for(i in 1:30) {
  s_n1[i] <- cuadrados_n(i)
}

# Rellenar 2o vector con sapply()
s_n2 <- sapply(1:30, cuadrados_n)

print(s_n1)  # [OK] - (1, 5, 14, ..., 7714, 8555, 9455)
print(s_n2)  # [OK] - (1, 5, 14, ..., 7714, 8555, 9455)


# EJERCICIO 6: Escribir una función que resuelva una ecuación de segundo grado
cat("\nEJERCICIO 6\n")

# a*x + b = 0
resolver_1er_grado <- function(a, b) {
  return(ifelse(a==0, Inf, -b/a))
}

# a*x^2 + b*x + c = 0
resolver_2o_grado <- function(a, b, c) {
  # Gestión de casos especiales
  if(a == 0) {
    if(b == 0) {
      # Si a = b = 0, c también debe ser 0 y hay infinitas soluciones
      return(list(0, 0))  # Devolver 0s
    } else {
      # Si a es 0 pero b no es 0, es una ecuación de 1er grado
      x <- resolver_1er_grado(b, c)
      return(list(x, x))
    }
  }
  
  # Caso general
  raiz <- sqrt(b^2 - 4*a*c)
  x1 <- (-b + raiz) / (2 * a)
  x2 <- (-b - raiz) / (2 * a)
  
  return(list(x1, x2))  # Devuelve NaN para resultados complejos
}

print(resolver_2o_grado(1, 2, -3))  # [OK] x1 = 1, x2 = -3
print(resolver_2o_grado(0, 2, 3))   # [OK] x1 = x2 = -1.5
print(resolver_2o_grado(0, 0, 0))   # [OK] x1 = x2 = 0
print(resolver_2o_grado(1, 2, 3))   # [OK] NaN (resultados complejos)
