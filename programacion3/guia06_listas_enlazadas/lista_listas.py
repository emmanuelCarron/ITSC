class Lista:
    primero = []  # lista vacia

    def vacia(self):
        return self.primero == []

    def agregar(self, dato):
        nodo = [dato, []]  # creo un nodo nuevo con dato y la lista vacia en vez de None
        # nodo[0] -> dato
        # nodo[1] -> siguiente
        nodo[1] = self.primero  # nodo. siguiente = self.primero
        self.primero = nodo

    def imprimir(self):
        nodo = self.primero
        while nodo != []:
           print(nodo[0])  # accedemos al dato
           nodo = nodo[1]

    def tamanio(self):
        nodo = self.primero
        contador = 0
        while nodo != []:
           contador += 1 # sumamos
           nodo = nodo[1]
        return contador
    
    def buscar(self, elemento) -> bool:
        nodo = self.primero
        encontrado = False
        while nodo != [] and not encontrado:
            if nodo[0] == elemento:
                encontrado = True
            nodo = nodo[1]
        return encontrado

    def remover(self, item):
        nodo = self.primero
        encontrado = False
        anterior = []
        while nodo != [] and not encontrado:
            if nodo[0] == item:
                encontrado = True
            else:
                anterior = nodo
                nodo = nodo[1]
        if encontrado:
            if anterior == []:
                self.primero = nodo[1]
            else:
                anterior[1] = nodo[1]

    def indice(self, e) -> int:
        # el método de la lista toma un elemento y si se encuentra devuelve el primer índice en donde se encuentra
        contador = 0
        nodo = self.primero
        encontrado = False
        while nodo != [] and not encontrado:
            if nodo[0] == e:
                encontrado = True
            else:
                nodo = nodo[1]
                contador = contador + 1
        if not encontrado:
            raise ValueError(f"{e} is not in list")
        return contador

    def elem(self, i: int):  # -> e (dato)
        # El método elem toma un índice i y devuelve el i-ésimo elemento de la lista
        if i >= self.tamanio() or i < 0:
            raise IndexError("List index out of range")

        contador = 0
        nodo = self.primero

        while contador < i:
            nodo = nodo[1]
            contador = contador + 1

        return nodo[0]

    def sumar_lista(self) -> int:
        # el metodo sumar toma una lista de enteros y devuelve la suma de todos los elementos de la lista
        suma = 0
        nodo = self.primero
        while nodo != []:
            suma = suma + 1
            nodo = nodo[1]
        return suma

    def concatenar(self, otra_lista) -> None:
        # el método concatenar toma otra lista y la pone al final de la lista actual.
        nodo = self.primero

        while nodo[1] != []:
            nodo = nodo[1]

        nodo[1] = otra_lista.primero


if __name__ == "__main__":
    # nodo.siguiente.siguiente.siguiente.dato -> lista con pares en tren
    # nodo[1][1][1][0] -> lista con lista de listas

    milista = Lista()
    milista.agregar("Matías")
    milista.agregar("Franco")
    milista.agregar("Jessi")

    print(f">>> Integrantes de la lista:")
    milista.imprimir()

    print(f">>> Largo de lista: {milista.tamanio()}")

    for i in ["Matías", "Germán", "Jessi"]:
        print(f">>> {i} esta en la lista: {milista.buscar(i)}")

    milista.remover("Franco")

    print(f">>> Integrantes de la lista:")
    milista.imprimir()


    print(f">>> Jessi esta en la lista: {milista.buscar('Jessi')}")

    milista.imprimir()

    nombre = "Matías"
    print(f"Indice de {nombre}: {milista.indice(nombre)}")

    indice = 1
    print(f"Elemento en la poscición {indice}: {milista.elem(indice)}")

    numeros = Lista()
    numeros.agregar(3)
    numeros.agregar(2)
    numeros.agregar(10)
    print(f"La suma de los números de la lista es: {numeros.sumar_lista()}")

    numeros.concatenar(milista)
    print(f"Listas concatenadas:")
    numeros.imprimir()