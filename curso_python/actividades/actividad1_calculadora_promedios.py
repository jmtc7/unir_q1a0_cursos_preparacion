def ingresar_calificaciones() -> tuple[list[str], list[float]]:
    """
    Genera 2 listas, una con nombres de materias y otra con las calificaciones obtenidas.
    Ambas introducidas por el usuario.

    :return: Las 2 listas generadas
    """
    materias = []
    calificaciones = []
    continuar = True
    while continuar:
        materia = ''
        calificacion = -1
        desea_continuar = None

        # Check against empty strings
        while not materia:
            materia = input('Introduzca el nombre de la materia: ')
        
        # Solo aceptar números entre el 0 y el 10 como calificaciones
        calif_es_float = False
        while not calif_es_float or not (calificacion>=0 and calificacion<=10):
            calificacion = input(f'Introduzca la nota de la materia {materia} (0-10): ')
            try:
                calificacion = float(calificacion)
                calif_es_float = True
            except ValueError:
                print('La calificación debe ser un número entre el 0 y el 10.')
                calif_es_float = False
            

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

def calcular_promedio(calificaciones: list[float]) -> float:
    """
    Calcula el promedio de una lista de calificaciones.

    :param calificaciones: Lista con las calificaciones (en float)
    :return: El promedio de las calificaciones
    """
    n_califs = len(calificaciones)
    califs_sum = sum(calificaciones)

    # Evitar división por 0 (aunque el programa ya verifica que haya al menos 1 materia)
    if n_califs > 0:
        promedio = califs_sum/n_califs
    else:
        print('El numero de calificaciones NO es superior a 0, por lo que no se puede calcular el promedio. Se devolverá 0.')
        promedio = 0

    return promedio

def determinar_estado(calificaciones: list[float], umbral: float=5.0) -> tuple[list[int], list[int]]:
    """
    Genera dos listas, una con los índes de las materias aprobadas y otra con los de las materias reprobadas.

    :param calificaciones: Lista con las calificaciones (en float)
    :param umbral: Umbral para determinar si una materia está aprobada o reprobada, defaults to 5.0
    :return: Las dos listas generadas
    """
    idxs_aprobadas = []
    idxs_reprobadas = []
    for c_idx, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            idxs_aprobadas.append(c_idx)
        else:
            idxs_reprobadas.append(c_idx)
        
    return idxs_aprobadas, idxs_reprobadas

def encontrar_extremos(calificaciones: list[float]) -> tuple[int, int]:
    """
    Devuelve los índices de la materia con la mejor y la peor nota, respectivamente.

    :param calificaciones: Lista con las calificaciones (en float)
    :return: Los índices de las materias con mejor y peor notas
    """
    max_calif = max(calificaciones)
    min_calif = min(calificaciones)

    max_calif_idx = calificaciones.index(max_calif)
    min_calif_idx = calificaciones.index(min_calif)

    return max_calif_idx, min_calif_idx

def imprimir_resumen(materias: list[str], calificaciones: list[float], promedio: float, idxs_aprobadas: list[int],
                     idxs_reprobadas: list[int], max_calif_idx: int, min_calif_idx: int) -> None:
    """
    Imprime un resumen de las materias y calificaciones e informaciones diversas obtenidas a partir de ellas.

    :param materias: Lista con los nombres de las materias
    :param calificaciones: Lista con las calificaciones (en float)
    :param promedio: Promedio de las calificaciones
    :param idxs_aprobadas: Lista de los índices de las materias aprobadas
    :param idxs_reprobadas: Lista de los índices de las materias reprobadas
    :param max_calif_idx: Índice de la materia con la nota más alta
    :param min_calif_idx: Índice de la materia con la nota más baja
    """
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


def main() -> None:
    """
    Solicita al usuario introducir los nombres de las materias y las calificaciones obtenidas.
    Se calcula la nota promedio, se verifican qué materias están aprobadas y reprobadas y se encuentran qué materias tienen mejor y peor nota.
    Se imprime un resumen con toda la información obtenida.
    """
    materias, calificaciones = ingresar_calificaciones()

    # Verificar que haya materias (aunque el código obliga a introducir al menos una)
    if len(materias) > 0:
        promedio = calcular_promedio(calificaciones)
        idxs_aprobadas, idxs_reprobadas = determinar_estado(calificaciones)
        max_calif_idx, min_calif_idx = encontrar_extremos(calificaciones)

        imprimir_resumen(materias, calificaciones, promedio, idxs_aprobadas, idxs_reprobadas, max_calif_idx, min_calif_idx)
    else:
        print('No se ha introducido ninguna materia, por lo que no se pueden generar ninguna información.')

if __name__ == '__main__':
    main()
