from graficar import graph as gph

class nodo:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class listaEnlazada:
    # ----------------------------------Lo principal en la lista---------------------------------
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
# -------------------------------------------Fin--------------------------------------------------

    def printData(self):
        aux = self.head

        while aux != None:
            print(aux.data.nombre)
            print(aux.data.iniciox)
            print(aux.data.inicioy)
            print(aux.data.finx)
            print(aux.data.finy)
            print("Maximo: " + str(aux.data.maxY))
            aux.data.mapa.printPos(aux.data.maxY, aux.data.nombre)
            print("----------------------------------")
            aux = aux.next

    def printPos(self, valor, titulo):
        aux = self.head
        contador = 0

        while contador != 1:
            # print(aux.data.x)
            # print(aux.data.y)
            aux.data.printInfo(valor, titulo)
            contador += 1
            aux = aux.next
        print()
        contador = 0

    def printInfo(self, valor, titulo):
        aux = self.head
        contador = 0
        control = 0
        bodyDocument = ""
        bodyAux = ''
        while aux != None:
            # print(aux.data.x)
            # print(aux.data.y)
            if valor % 2 == 0:
                control = 1
            else:
                control = 2
            # --------------------------------------------------------------------
            if contador <= (valor + control):
                print(aux.data.info, end=' | ')
                bodyAux = bodyAux + "<TD WIDTH = '30'>" + str(aux.data.info) + "</TD>"
                contador = contador + 1
            else:
                print(aux.data.info, end=' | ')
                bodyAux = bodyAux + "<TD WIDTH = '30'>" + str(aux.data.info) + "</TD>"
                bodyDocument = bodyDocument + '<TR>' + bodyAux + '</TR>\n'
                print()
                bodyAux = ""
                contador = 0
            aux = aux.next
            contador = contador + 1
        print()
        gph.graficar(bodyDocument, titulo)

    def printList(self):
        aux = self.head
        while aux != None:
            print(aux.data.print())
            aux = aux.next
# lista2.print()