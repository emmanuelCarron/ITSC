from math import pi
from clase_punto import Punto
from clase_pila import Pila
from clase_matriz import Matriz


# Ejercicio 1
"""Utilizando los ejemplo de la clase punto y rectanculo implemente la clase circulo"""
class Circulo(Punto):
    """ Esta clase modela un circulo en el plano. """

    def __init__(self, radio, origen):
        """ radio (número) es la longitud del radio,
            origen (Punto) es el punto del plano de su esquina
            inferior izquierda. """
        self.radio = radio
        self.origen = Punto(origen)

    def trasladar(self, dx = 0, dy = 0):
        self.origen.mover(dx, dy)
    
    def diametro(self):
        return self.radio * 2
    
    def area(self):
        return pi * (self.radio ** 2)
    
    def perímetro(self):
        return pi * self.diametro()
    
    def __str__(self):
        """ muestra el circulo """
        return "Un circulo"

    def __eq__(self,otro):
        """ Este método indica cuando dos circulos son iguales """
        return self.radio == otro.radio and self.origen == otro.origen

# Ejercicio 2
"""Escribir una función Reemplazar que tenga como argumentos una
pila con tipo de elemento int y dos valores int: nuevo y viejo de
forma que si el segundo valor aparece en algún lugar de la pila,
sea reemplazado por el segundo.
Ejemplo:
pila -> [4,5,2,8]
reemplazar (pila,5,10) -> [4,10,2,8]
"""

def reemplazar (pila: Pila, viejo, nuevo):
       
    pila_aux = Pila()
    while not pila.esVacia():
        if pila.inspeccionar() == viejo:
            pila_aux.incluir(nuevo)
            pila.extraer()
        else:
            pila_aux.incluir(pila.inspeccionar())
            pila.extraer()
    
    pila_aux.dar_vuelta()
    return pila_aux


# Ejercicio 3
""" Escribir una funcion que tome dos listas y cree una nueva
alternando los elementos"""
def alternar(lista_1,lista_2):
    lista_nueva = Pila()

    while len(lista_1) > 0 or len(lista_2) > 0:
        #saco un elemento de cada lista
        #y lo agrego a la pila
        if len(lista_1) > 0:
            lista_nueva.incluir(lista_1.pop())
        if len(lista_2) > 0:
            lista_nueva.incluir(lista_2.pop())
    return list(lista_nueva)


# Ejercicio 4
""" Escribir una funcion incrementart que tome una matriz de enteros y un
numero e incremente en ese valor a todos los elementos de la matriz
Ej
A = [[1,2],
    [3,4]]
valor = 2
incrementar (A,valor) = [[3,4],[5,6]]
"""
def incrementar (matriz: Matriz, valor):
    filas, columnas = matriz.dimension()
    return matriz.sumar_matriz(Matriz(filas, columnas, valor))


if __name__ == "__main__":
    pila = Pila()
    for i in [4,5,2,8]:
        pila.incluir(i)
    print(reemplazar(pila,5,10)) # [4,10,2,8]
    