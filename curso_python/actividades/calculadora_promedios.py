def ingresar_calificaciones():
  """
  Genera 2 listas, una con nombres de materias y otra con las calificaciones obtenidas.
  Ambas introducidas por el usuario.
  """
  materias = []
  calificaciones = []
  continuar = True
  while continuar:
    calificacion = -1
    desea_continuar = None
    materia = input('Introduzca el nombre de la materia: ')
    
    while not (calificacion>=0 and calificacion<=10):
      calificacion = input(f'Introduzca la nota de la materia {materia} (0-10): ')
      calificacion = float(calificacion)

    # Append to lists
    materias.append(materia)
    calificaciones.append(calificacion)

    # Ask if user wants to give more inputs
    while desea_continuar not in ['S', 's', 'N', 'n']:
      desea_continuar = input('Quieres introducir más materias? [S/N]: ')
      if desea_continuar in ['S', 's']:
        continuar = True
      elif desea_continuar in ['N', 'n']:
        continuar = False

  return materias, calificaciones

def calcular_promedio(calificaciones: list[float]):
  """Calcula el promedio de una lista de calificaciones"""
  n_califs = len(calificaciones)
  califs_sum = 0
  for calificacion in calificaciones:
    califs_sum += calificacion
  
  promedio = califs_sum/n_califs
  return promedio

def determinar_estado(calificaciones: list[float], umbral: float=5.0):
  """
  Genera dos listas, una con los índes de las materias aprobadas y otra con los de las materias reprobadas.
  El 'umbral' determina si una materia está aprobada o reprobada.  
  """
  idxs_aprobadas = []
  idxs_reprobadas = []
  for c_idx, calificacion in enumerate(calificaciones):
    if calificacion >= umbral:
      idxs_aprobadas.append(c_idx)
    else:
      idxs_reprobadas.append(c_idx)
      
  return idxs_aprobadas, idxs_reprobadas

def encontrar_extremos(calificaciones: list[float]):
  """Devuelve los índices de la materia con la mejor y la peor nota, respectivamente."""
  max_calif = max(calificaciones)
  min_calif = min(calificaciones)
  
  max_calif_idx = calificaciones.index(max_calif)
  min_calif_idx = calificaciones.index(min_calif)
  
  return max_calif_idx, min_calif_idx

def main():
  """
  Solicita al usuario introducir los nombres de las materias y las calificaciones obtenidas.
  Se calcula la nota promedio, se verifican qué materias están aprobadas y reprobadas y se encuentran qué materias tienen mejor y peor nota.
  Se imprime un resumen con toda la información obtenida.
  """
  materias, calificaciones = ingresar_calificaciones()
  promedio = calcular_promedio(calificaciones)
  idxs_aprobadas, idxs_reprobadas = determinar_estado(calificaciones)
  max_calif_idx, min_calif_idx = encontrar_extremos(calificaciones)

  materias_aprobadas = [materias[idx] for idx in idxs_aprobadas]
  materias_reprobadas = [materias[idx] for idx in idxs_reprobadas]

  print('Resumen final:')
  print(f'\t- Materias: {materias}')
  print(f'\t- Calificaciones: {calificaciones}')
  print(f'\t- Promedio general: {promedio}')
  print(f'\t- Materias aprobadas: {materias_aprobadas}')
  print(f'\t- Materias reprobadas: {materias_reprobadas}')
  print(f'\t- Materia con mejor calificación: {materias[max_calif_idx]} ({calificaciones[max_calif_idx]})')
  print(f'\t- Materia con peor calificación: {materias[min_calif_idx]} ({calificaciones[min_calif_idx]})')


if __name__ == '__main__':
  main()
