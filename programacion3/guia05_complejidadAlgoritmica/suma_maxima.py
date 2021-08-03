import time
from timeit import timeit


def sol1(numbers):
    n = len(numbers)
    if n < 3:
        raise ValueError('Necesito al menos 3 números')
    i = 0
    result = None

    while i < n:
        j = i + 1
        while j < n:
            k = j + 1
            while k < n:
                total = numbers[i] + numbers[j] + numbers[k]
                if result is None or total > result:
                    result = total
                k += 1
            j += 1
        i += 1

    return result

def sol2(numbers):
    if len(numbers) < 3:
        raise ValueError('Necesito al menos 3 números')

    a = b = c = None

    for n in numbers:
        if a is None or n > a:
            c = b
            b = a
            a = n
        elif b is None or n > b:
            c = b
            b = n
        elif c is None or n > c:
            c = n
    return a + b + c

"""
    1- Las funciones devuelven lo mismo. A medida que agrandamos la lista de números
    sol1 se vuelve más lenta, ya que realiza todas las sumas posibles con los elementos
    de la lista dada. Sol2 primero busca los 3 números más grandes y luego retorna la suma.
"""
nums = [1, 2, 3, 4, 5] # para acceder desde terminal con timeit

"""
    2- La función sol2 es la que mejor desempeño ofrece a mededia que aumanta el tamaño de la lista de números.
    En el gráfico se expone estadísticamente lo percibido en el ítem 1. 
"""

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sol1(nums))
    print(sol2(nums))


