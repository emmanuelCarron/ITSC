from time import time

def prueba1(n):
    l = []

    for i in range(n):
        l = l + [i]


def prueba2(n):
    l = []

    for i in range(n):
        l.append(i)


def prueba3(n):
    l = [i for i in range(n)]


def prueba4(n):
    l = list(range(n))


if __name__ == "__main__":

    # Calcule los tiempos de ejecución de las diferentes funciones para n 1000, 2000, hasta 20000
    functions = {
        1: prueba1,
        2: prueba2,
        3: prueba3,
        4: prueba4
    }

    separator = '___END___'

    for i in range(1, 5):
        print(f'{functions[i]} is running...\n')
        for j in range(1000, 20001, 1000):
            start_time = time()
            functions[i](j)
            end_time = time()
            print(str(end_time - start_time).replace('.', ','))
        print(f'{separator:^30}')


