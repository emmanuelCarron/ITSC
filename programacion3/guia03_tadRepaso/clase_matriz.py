class Matriz:

    def __init__(self, f: int, c: int, val=None):
        self.filas = f
        self.columnas = c
        self.matriz = [[val for _ in range(self.columnas)] for _ in range(self.filas)]

    def __str__(self):
        return str(self.matriz)

    def dimension(self):
        return (self.filas, self.columnas)

    def sumar_matriz(self, otra):
        aux = Matriz(len(self.matriz), len(self.matriz[0]))
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[0])):
                aux.matriz[fila][col] = self.matriz[fila][col] + otra.matriz[fila][col]
        return aux

if __name__ == "__main__":

    A = Matriz(2, 2, 2)
    print(A)
    B = Matriz(2, 2, 3)
    print(B)
    C = A.sumar_matriz(B)
    print(C)