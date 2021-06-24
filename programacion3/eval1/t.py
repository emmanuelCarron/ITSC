"""Defina una función que tome una lista y
devuelva la mayor longitud de elementos repetidos de manera continua
junto con el valor que se repite."""

def max_rep(items:list)->int:
    counted = []
    c = 1
    item = items[0]
    for i in range(len(items)-1):
        if items[i] == items[i+1]:
            c += 1
        else:
            counted.append([item, c])
            item = items[i+1]
            c = 1

    counted.sort(key=lambda x:x[1])
    return (counted[-1][0], counted[-1][1])




assert max_rep([1,1,4,4,4,2,2,4,4,1,2]) == (4,3)

