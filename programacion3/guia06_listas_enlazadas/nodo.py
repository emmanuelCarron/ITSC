class Nodo:
    """Tiene un dato y una referencia al siguiente nodo"""
    dato = None #no tiene informacion
    siguiente = None # no apunta a apunta a nada

    def __init__(self,datoInicial):
        self.dato = datoInicial

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

