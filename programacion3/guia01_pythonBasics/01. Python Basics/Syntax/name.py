i = input("Ingrese un número entero no negativo:\n>>>") # se debe inicializar la variable i. En este caso pide un valor

while i >= 0:
    print(i)
    i -= 1 #Para evitar un loop infinito añadimos este decremento.
