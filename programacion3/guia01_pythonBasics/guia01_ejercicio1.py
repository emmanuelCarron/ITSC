#a)
def g(a, b): #Define una función, con el nombre g, que recibe dos argumentos
    c = 0 #Inicializa una variable de nombre c y le asigna 0 
    for d in a: #Itera sobre "a" elemento a elemento asignandolo a "d"
        if d == b: # si el valor del elemento "d" es igual al elemento "b" ingresará al IF
            c += 1 #Incrementa en 1 el valor de la variable c.
    return c #Retorna el valor asignado a c.


#b) Computa cuantas veces se encuentra "b" dentro de "a"

#c)
def count_b_in_a(iterable, element):
    counter = 0
    for item in iterable:
        if item == element:
            counter += 1
    return counter

"""d)
g([1, 2, 3, 4], 5)  -------------------> 0
g([4, 1, 4, 4], 4) --------------------> 3
g(‘hola’, ‘o’) ------------------------> 1
g([[1, 2], [2, 3], [1, 2]], [1, 2]) ---> 2
"""
#e)

if __name__ == "__main__":
    assert 0 == g([1, 2, 3, 4], 5)
    assert 3 == g([4, 1, 4, 4], 4)
    assert 1 == g('hola', 'o')
    assert 2 == g([[1, 2], [2, 3], [1, 2]], [1, 2])

    assert 0 == count_b_in_a([1, 2, 3, 4], 5)
    assert 3 == count_b_in_a([4, 1, 4, 4], 4)
    assert 1 == count_b_in_a("hola", 'o')
    assert 2 == count_b_in_a([[1, 2], [2, 3], [1, 2]], [1, 2])