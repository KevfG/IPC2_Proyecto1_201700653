from graficar import graph as gph
from yattag import Doc, indent
doc, tag, text = Doc().tagtext()
titulo = ""

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

#-------------------------------------------------------------------------------------------------
    def processData2(self):
        aux = self.head
        

        while aux != None:
            print(aux.data.nombre)
            aux = aux.next

        aux = self.head
        nombre = input("Seleccione el mapa: ")

        while aux != None:
            if nombre == aux.data.nombre:
                with tag('terreno', nombre = aux.data.nombre):
                    with tag('posicioninicio'):
                        with tag('x'):
                            text(aux.data.iniciox)
                        with tag('y'):
                            text(aux.data.inicioy)

                    with tag('posicionfin'):
                        with tag('x'):
                            text(aux.data.finx)
                        with tag('y'):
                            text(aux.data.finy)
                aux.data.mapa.printPos3(aux.data.maxY, aux.data.nombre)
                break
            aux = aux.next

    def printPos3(self, valor, titulo):
        aux = self.head
        contador = 0

        while contador != 1:
            # print(aux.data.x)
            # print(aux.data.y)
            aux.data.printInfo3(valor)
            contador += 1
            aux = aux.next
        print()
        contador = 0

    def printInfo3(self, valor):
        combustible = 0
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
                if int(aux.data.info) < 3:
                    combustible = int(aux.data.info) + combustible
                    with tag('posicion', x=aux.data.x, y = aux.data.y): 
                        text(aux.data.info)
            else:
                if int(aux.data.info) < 3:
                    with tag('posicion', x=aux.data.x, y = aux.data.y): 
                        text(aux.data.info)
                contador = 0
            aux = aux.next
            contador = contador + 1
        print()
        with tag('combustible'): 
                        text(combustible)
        result = indent( 
            doc.getvalue(), 
            indentation = ' '*4, 
            newline = '\r' 
        ) 

        mydata = result
        myfile = open("items2.xml", "w")
        myfile.write(str(mydata))
        myfile.close()
#-------------------------------------------------------------------------------------------------
    def processData(self):
        aux = self.head

        while aux != None:
            print(aux.data.nombre)
            aux = aux.next

        aux = self.head
        nombre = input("Seleccione el mapa: ")

        while aux != None:
            if nombre == aux.data.nombre:
                aux.data.mapa.printPos2(aux.data.maxY, aux.data.nombre)
                break
            aux = aux.next

    def printPos2(self, valor, titulo):
        aux = self.head
        contador = 0

        while contador != 1:
            # print(aux.data.x)
            # print(aux.data.y)
            aux.data.printInfo2(valor)
            contador += 1
            aux = aux.next
        print()
        contador = 0

    def printInfo2(self, valor):
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
                if int(aux.data.info) >= 3:
                    print('0', end=' | ')
                else:
                    print('1', end=' | ')
                contador = contador + 1
            else:
                if int(aux.data.info) >= 3:
                    print('0', end=' | ')
                else:
                    print('1', end=' | ')
                print()
                contador = 0
            aux = aux.next
            contador = contador + 1
        print()

    def chooseList(self):
        aux = self.head

        while aux != None:
            print(aux.data.nombre)
            aux = aux.next

        aux = self.head
        nombre = input("Seleccione el mapa: ")

        while aux != None:
            if nombre == aux.data.nombre:
                aux.data.mapa.printPos(aux.data.maxY, aux.data.nombre)
                break
            aux = aux.next

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