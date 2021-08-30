from listaSimple import listaEnlazada
import xml.etree.ElementTree as ET
from tkinter import filedialog as FD
from yattag import Doc, indent #esta madre va en la lista
listaPrincipal = listaEnlazada()

class coordenateMap:

    def __init__(self, x, y, info):
        self.x = x
        self.y = y
        self.info = info

class dataMaps:
    
    def __init__(self, nombre, iniciox, inicioy, finx, finy, mapa, maxY):
        self.nombre = nombre
        self.iniciox = iniciox
        self.inicioy = inicioy
        self.finx = finx
        self.finy = finy
        self.mapa = mapa
        self.maxY = maxY


class leerXml:
    valorMaxY = 0

    def saveData(opcion):
        if opcion == '1':
            file_path = FD.askopenfilename(title="Abrir")
            xml_doc = ET.parse(file_path)
            root = xml_doc.getroot()            
            for branch in root:
                name = ""
                initx = 0
                inity = 0
                endx = 0
                endy = 0 
                le = listaEnlazada()
                le2 = listaEnlazada()

                name =branch.get('nombre')
                for i in branch:
                    if i.tag == "dimension":
                        for j in i:
                            m = j.text
                    elif i.tag == 'posicioninicio':
                        for j in i:
                            if j.tag == 'x':
                                initx = j.text
                            else:
                                inity = j.text
                    elif i.tag == 'posicionfin':
                        for j in i:
                            if j.tag == 'x':
                                endx = j.text
                            else:
                                endy = j.text
                    else:
                        le.insertar(coordenateMap(i.get('x'), i.get('y'), i.text))
                        #print("x= " + i.get('x'))
                        #print("y= " + i.get('y'))
                        #print("Dato= " + i.text)
                        valorMaxY = int(i.get('y'))
                    le2.insertar(le)
                #print(valorMaxY)
                listaPrincipal.insertar(dataMaps(name, initx, inity, endx, endy, le2, valorMaxY))
            #listaPrincipal.printData()
        if opcion == '2':
            listaPrincipal.chooseList()
        if opcion == '3':
            listaPrincipal.processData()
        if opcion == '4':
            listaPrincipal.processData2()

#esta otra madre tambien va en la lista
    def crearXml():

        doc, tag, text = Doc().tagtext() 
        with tag('terreno', nombre = 'terreno1'):
            with tag('posicioninicio'):
                with tag('x'):
                    text('1')
                with tag('y'):
                    text('1')

            with tag('posicionfin'):
                with tag('x'):
                    text('5')
                with tag('y'):
                    text('5')

            with tag('combustible'):
                text('7')

            i = 0
            while(i < 10):
                with tag('posicion', x='x', y = 'y'): 
                    text(str(i))
                i = i + 1 

        result = indent( 
            doc.getvalue(), 
            indentation = ' '*4, 
            newline = '\r' 
        ) 

        mydata = result
        myfile = open("items2.xml", "w")
        myfile.write(str(mydata))

leerXml.crearXml()