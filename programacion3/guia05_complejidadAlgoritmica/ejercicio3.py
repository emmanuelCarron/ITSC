"""Escriba dos funciones en Python para encontrar el número mínimo en una lista. La
+ primera función debe comparar cada número de una lista con todos los demás de la lista.
O(n2). /se las doy resuelta)"""
import time


def min1(l):
    min = l[0]
    for j in l:
        for k in l:
            if j <= min:
                min = j
    return min

"""
    + La segunda función debe ser lineal O(n).
"""


def min2(l:[])->int:
    minimo, *resto_lista = l
    for num in resto_lista:
        if num < minimo:
            minimo = num
    return minimo


if __name__ == "__main__":
    start_min1 = time.time()
    min1([3, -5, 1]*10000)  # -> n**2
    end_min1 = time.time()
    print(f'Tiempo de min1: {end_min1 - start_min1}')
    start_min2 = time.time()
    min2([3, -5, 1]*10000)  # -> n
    end_min2 = time.time()
    print(f'Tiempo de min2: {end_min2 - start_min2}')


