# -*- coding: utf-8 -*-
def min_max(elems):
    """Devolver el mínimo y el máximo elemento de una lista."""
    if not elems:
        raise ValueError('Secuencia vacía no tiene mínimo ni máximo')
    min_ = max_ = elems[0]
    for elem in elems:
        if elem < min_:
            min_ = elem
        #if max_ > elem: necesito evaluar si elem esta por encima de max_
        if elem > max_:
            #elem = max_ no me "actualiza" el valor maximo
            max_ = elem
    return (min_,max_)
    
if __name__ == '__main__':
    assert min_max([1]) == (1,1)
    assert min_max([2]) == (2,2)
    assert min_max([1,1]) == (1,1)
    assert min_max([1,30,100]) == (1,100)