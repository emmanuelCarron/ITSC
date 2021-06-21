class Punto:
    """Un punto en el espacio bi dimensional:
    - coordenada x
    - coordenada y

    Tiene algunos métodos especiales:
    - __str__ (para poder imprimirlo de forma apropiada)
    - __eq__ (para poder compararlo con otro objeto Punto)
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, otro):
        """Devolver True si self es igual a otro."""
        return self.x == otro.x and self.y == otro.y

    def __str__(self):
        """Devolver un string con la representación del punto."""
        return '({},{})'.format(self.x, self.y)

def dame_un_entero(prompt):
    while True:
        try:
            respuesta = int(input(prompt))
        except ValueError as e:
            print(e)
        else:
            return respuesta


if __name__ == '__main__':  ## me llamaron a mí desde la terminal
    x1 = dame_un_entero('Punto 1: ingrese el valor de x: ')
    y1 = dame_un_entero('Punto 1: ingrese el valor de y: ')

    x2 = dame_un_entero('Punto 2: ingrese el valor de x: ')
    y2 = dame_un_entero('Punto 2: ingrese el valor de y: ')

    punto1 = Punto(x1, y1)
    punto2 = Punto(x2, y2)

    print('Los puntos ingresados son: ', punto1, punto2)
    if punto1 == punto2:
        print('Los puntos ingresados son iguales')
    else:
        print('Los puntos ingresados son diferentes')
