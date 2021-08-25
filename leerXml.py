from listaSimple import listaEnlazada
import xml.etree.ElementTree as ET
from tkinter import filedialog as FD
listaPrincipal = listaEnlazada()

class coordenateMap:

    def __init__(self, x, y, info):
        self.x = x
        self.y = y
        self.info = info

class dataMaps:
    
    def __init__(self, nombre, iniciox, inicioy, finx, finy, mapa):
        self.nombre = nombre
        self.iniciox = iniciox
        self.inicioy = inicioy
        self.finx = finx
        self.finy = finy
        self.mapa = mapa


class leerXml:

    def saveData():
        #file_path = FD.askopenfilename(title="Abrir")
        xml_doc = ET.parse('archivo.xml')
        root = xml_doc.getroot()

        for branch in root:
            name = ""
            initx = 0
            inity = 0
            endx = 0
            endy = 0
            le = listaEnlazada()

            name =branch.get('nombre')
            for i in branch:
                if i.tag == 'posicioninicio':
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
                #le2.insertar(le)

            listaPrincipal.insertar(dataMaps(name, initx, inity, endx, endy, le))
            
leerXml.saveData()
listaPrincipal.printData()