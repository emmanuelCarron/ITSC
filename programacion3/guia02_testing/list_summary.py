def min_max(lista):
    # min_ = 0
    # max_ = 0
    #Al inicializar min en 0 si todos los elementos son mayores que 0
    #devolvemos como minimo un valor que no pertenece a la lista dada
    #Analogamente con max si los valores de la lista son todos negativos

    min_ = max_ = lista[0]
    for elem in lista:
        if elem < min_:
            min_ = elem
            continue
        if elem > max_:
            max_ = elem
    return min_, max_


def promedio(lista):
    #return lista[0] el promedio no necesariamente es el valor del primer elemento
    return sum(lista)/len(lista)


def imprimir_resumen(lista):
    print('La lista tiene {} elementos'.format(len(lista)))
    #max_, min_ = min_max(lista) la funcion retorna primero el min
    min_, max_ = min_max(lista)
    print('Elemento máximo: ', max_)
    print('Elemento mínimo: ', min_)
    print('Promedio: ', promedio(lista))


def construir_lista(n):
    def dame_un_entero(prompt):
        while True:
            try:
                respuesta = int(input(prompt))
            except ValueError as e:
                print(e)
            else:
                return respuesta

    resultado = []
    while n > 0:
        resultado.append(dame_un_entero('Introduzca un entero: '))
        n -= 1
    return resultado


if __name__ == '__main__':
    lista = construir_lista(10)
    imprimir_resumen(lista)
