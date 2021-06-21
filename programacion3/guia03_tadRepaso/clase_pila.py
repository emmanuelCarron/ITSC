class Pila:
    """ Pila es una clase que implemente el tipo abstracto de datos 'pila' del tipo LIFO"""
    def __init__(self):
        """definimos la pila vacia como la lista vacia"""
        self.items = []
    
    def __eq__(self,otra_pila):
        """Definimos cuando dos pilas son iguales"""
        return self.items == otra_pila.items
    
    def __str__(self) -> str:
        return f"{self.items}"

    def esVacia(self):
        """pregunta si no hay niongun dato en la pila"""
        return self.items == []

    def incluir(self, item):
        """agrega un elemento a mi pila"""
        self.items.append(item)

    def extraer(self):
        """extrae un elemento de la pila, en este caso el último de la lsita"""
        return self.items.pop()

    def inspeccionar(self):
        """Ver cual es el tope de la pila"""
        return self.items[-1]

    def tamano(self):
        """me dice al cantidad de elementos que tenemos en la pila"""
        return len(self.items)

    def dar_vuelta(self):
        """invierte el orden de los elementos en la pila"""
        aux = []
        while not self.esVacia():
            aux.append(self.extraer())
        self.items=aux   

    