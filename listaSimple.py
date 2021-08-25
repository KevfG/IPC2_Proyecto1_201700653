class nodo:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class listaEnlazada:

    def __init__(self):
        self.head = None

    def insertar(self, nuevo):

        if not self.head:
            self.head = nodo(data=nuevo)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = nodo(data=nuevo)
    
    def print(self):
        aux = self.head

        while aux != None:
            print(aux.data)
            aux = aux.next

    def printData(self):
        aux = self.head

        while aux != None:
            print(aux.data.nombre)
            print(aux.data.iniciox)
            print(aux.data.inicioy)
            print(aux.data.finx)
            print(aux.data.finy)
            aux.data.mapa.printPos()
            print("----------------------------------")
            aux = aux.next

    def printPos(self):
        aux = self.head

        while aux != None:
            #print(aux.data.x)
            #print(aux.data.y)
            print(aux.data.info, end= ' | ')
            aux = aux.next
        print()

    def printList(self):
        aux = self.head
        while aux != None:
            print(aux.data.print())
            aux = aux.next
#lista2.print()