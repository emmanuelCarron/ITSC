#a)
def f(x): #Define una funcion f que recibe un arguemento "x" de tipo int
    '''
        Esta función imprime en parantalla la cadena "hola"
        x cantidad de veces.
    '''
    for _ in range(x): #Itera sobre el objeto range, que recibe como argumento "x"
        print('hola') #Imprime en pantalla la cadena tantas veces como elementos tenga el rango de range(x)


f(12) #Llama a la funcion "f" enviando el argumento (12 para este caso).
