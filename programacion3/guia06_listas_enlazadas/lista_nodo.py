from nodo import Nodo


class Lista:
    primero = None  # Nulo

    def vacia(self) -> bool:
        return self.primero == None

    def agregar(self, dato):  #creo un nodo nuevo y lo agrego al principio
        nodo = Nodo(dato)  # creo un nodo nuevo
        nodo.siguiente = self.primero  # el siguiente del nodo nuevo es el nodo que estaba primero
        self.primero = nodo  # el nodo nuevo es el primero

    def imprimir(self):  # recorro todos los nodos y los voy imprimiendo
        nodo = self.primero  # creo una variable para recorrer los nodos
        while nodo != None:  # mientras haya nodos para recorrer
          print(nodo.dato)  # imprimo la informacion que hay en el nodo
          nodo = nodo.siguiente  # paso al siguiente nodo

    def tamanio(self) -> int:
        nodo = self.primero  # creo una variable para recorrer los nodos
        contador = 0
        while nodo != None:  # mientras haya nodos para recorrer
          contador = contador + 1  # contador += 1
          nodo = nodo.siguiente  # paso al siguiente nodo
        return contador

    def buscar(self, elemento) -> bool:
        nodo = self.primero
        encontrado = False
        while nodo != None and not encontrado:
            if nodo.dato == elemento:
                encontrado = True
            nodo = nodo.siguiente
        return encontrado

    def remover(self, item):
        nodo = self.primero  # creo un nodo para recorrer
        encontrado = False  # flag que indique si encontre el item
        anterior = None  # otro nodo que inique cual es el anterior del actual
        while nodo != None and not encontrado:  # si no se me acabó la lista y si todavia no encontre el item
            if nodo.dato == item:  # si encuentro el item
                encontrado = True  # sale del ciclo
            else:  # si no encuentro el item
                anterior = nodo  # nodo anterior apunta al actual
                nodo = nodo.siguiente  # nodo actual apunta al que sigue
        # el while puede terminar por 2 motivos 
        # 1) Nodo == Nulo -> termino de recorrer y no estaba el item (incluso si la lista estaba vacia)
        # 2) encontrado == True
        if encontrado:  # Jessi -> Franco -> Matías y borro Jessi
            if anterior == None:
                self.primero = nodo.siguiente
            else:
                anterior.siguiente = nodo.siguiente

    def indice(self, e) -> int:
        # el método de la lista toma un elemento y si se encuentra devuelve el primer índice en donde se encuentra
        contador = 0
        nodo = self.primero
        encontrado = False
        while nodo != None and not encontrado:
            if nodo.dato == e:
                encontrado = True
            else:
                nodo = nodo.siguiente
                contador = contador + 1
        if not encontrado:
            raise ValueError(f"{e} is not in list")
        return contador

    def elem(self, i: int): # -> e (dato)
        # El método elem toma un índice i y devuelve el i-ésimo elemento de la lista
        if i >= self.tamanio() or i < 0:
            raise IndexError("List index out of range")

        contador = 0
        nodo = self.primero

        while contador < i:
            nodo = nodo.siguiente
            contador = contador + 1

        return nodo.dato

    def sumar_lista(self) -> int:
        # el metodo sumar toma una lista de enteros y devuelve la suma de todos los elementos de la lista
        suma = 0
        nodo = self.primero
        while nodo != None:
            suma = suma + nodo.dato
            nodo = nodo.siguiente
        return suma

    def concatenar(self, otra_lista) -> None:
        # el método concatenar toma otra lista y la pone al final de la lista actual.
        nodo = self.primero

        while nodo.siguiente != None:
            nodo = nodo.siguiente

        nodo.siguiente = otra_lista.primero

if __name__ == "__main__":
    """
    Locomotora->None
    agregar(vagon1)
    locomotora->vagon1->None
    locomotora->vagon2->vagon1->none
    """

    milista = Lista()
    milista.agregar("Matías")
    milista.agregar("Franco")
    milista.agregar("Jessi")
    # Jessi -> Franco -> Matías

    print(f">>> Integrantes de la lista:")
    milista.imprimir()

    print(f">>> Largo de lista: {milista.tamanio()}")

    for i in ["Matías", "Germán", "Jessi"]:
        print(f">>> {i} esta en la lista: {milista.buscar(i)}")

    milista.remover("Jessi")

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
