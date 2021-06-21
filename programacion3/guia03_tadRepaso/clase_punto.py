#Primera implementacion
class Punto:
    """Un punto en el espacio bi dimensional:
    - coordenada x
    - coordenada y
    """

    def __init__(self, x=0, y=0): # si no paso x e y se considera que el punto es (0,0) 
        self.x=x
        self.y=y

    def __eq__(self, otro):
        """Devolver True si self es igual a otro."""
        return (self.x==otro.x) and (self.y==otro.y)

    def __str__(self):
        """Devolver un string con la representación del punto."""
        return "({},{})".format(self.x, self.y)
    
    def es_origen(self):
        """Me dice si el punto corresponde al origen del plano"""
        return (self.x==0 and self.y==0)
    
    def mover(self,dx,dy):
        """Mueve el punto dx lugares en x y dx lugares en y"""
        self.x = self.x + dx
        self.y = self.y + dy
    
    def distancia(self,otro):
        return (((self.x-otro.x)**2) + ((self.y-otro.y)**2))**(1/2)

