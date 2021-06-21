from typing import List


def product(numbers: List[int]) -> int:
    if not numbers:
        return 1
    else:
        return numbers[0] * product(numbers[1:])


assert product([5, 2, 6, 8, 3]) == 1440


def length(numbers: List[int]) -> int:
    if not numbers:
        return 0
    else:
        return 1 + length(numbers[1:])


assert length([5, 2, 6, 8, 3]) == 5


"""
    2) Dada la siguiente lista: [-20,1,4,9,12,15,23]
1. Devuelva la secuencia de comparaciones que tiene que
hacer para saber si el 12 esta presente en la lista
ejecutando busqueda lineal

    1 - -20 == 12?
    2 - 1 == 12?
    3 - 4 == 12?
    4 - 9 == 12?
    5 - 12 == 12?
    El 12 si pertenece a la lista!

2. Devuelva la secuencia de comparaciones que tiene que
hacer para saber si el 12 esta presente en la lista
ejecutando busqueda binaria
    
    1 - tomo como valor de referencia 9, 12 == 12?, 12 < 9?
    2 - considero una sublista (recursion) apartir del 9 y 
        su valor central como referencia, 12 == 15?, 12 < 15?
    3 - me queda para evaluar una lista compuesta por solamente el 12,
        12 == 12?
    El 12 si pertenece a la lista!

3. Devuelva la secuencia de comparaciones que tiene que
hacer para saber si el 8 esta presente en la lista
ejecutando busqueda lineal

    1 - -20 == 8?
    2 - 1 == 8?
    3 - 4 == 8?
    4 - 9 == 8?
    5 - 12 == 8?
    6 - 15 == 8?
    7 - 23 == 8?
    El 8 no pertenece a la lista!

4. Devuelva la secuencia de comparaciones que tiene que
hacer para saber si el 8 esta presente en la lista
ejecutando busqueda binaria

    
    1 - tomo como valor de referencia 9, 8 == 12?, 8 < 9?
    2 - considero una sublista (recursion) hasta el 9 y 
        su valor central como referencia, 8 == 1?, 8 < 1?
    3 - me queda para evaluar una lista compuesta por solamente el 4,
        8 == 4?
    El 8 no pertenece a la lista!

5. ¿Cuál es mas rápida? y ¿Por qué?
    
    Es mas rapida la busqueda binaria ya que al descartar la mitad de elementos
    en cada comparacion, obtenemos en menos pasos el resultado de la 
    busqueda.

------------------------------------------------------------------------------

    3) Dada la lista [54,26,93,17,77,31,44,55,20]
    a) devolver la lista que tenemos como resultado de ejecutar
    3 pasadas del algoritmo de inserción
    
    [54,26,93,17,77,31,44,55,20]
    1er pasada inserto 26
    [26,54,93,17,77,31,44,55,20]
    2da pasada inserto 93
    [26,54,93,17,77,31,44,55,20]
    3er pasada inserto 17
    [17,26,54,93,77,31,44,55,20]
    
    b) devolver la lista que tenemos como resultado de ejecutar
    3 pasadas del algoritmo de selección
    
    [54,26,93,17,77,31,44,55,20]
    1er pasada
    [26,54,93,17,77,31,44,55,20]
    2da pasada
    [17,54,93,26,77,31,44,55,20]
    3er pasada
    [17,26,93,54,77,31,44,55,20]
    
    c) devolver la lista que tenemos como resultado de ejecutar
    3 pasadas del algoritmo de quicksort

    [54,26,93,17,77,31,44,55,20]
    1er pasada Pivote 54
    [54,26,20,17,77,31,44,55,93]
    2da pasada
    [54,26,20,17,44,31,77,55,93]
    3er pasada
    [31,26,20,17,44,54,77,55,93]
"""

