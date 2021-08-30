from leerXml import leerXml
import time
class main:

    def inicio():
        while(True):
            print('--------------------------------------------------------------------')
            print("1. Cargar Archivo")
            print("2. Procesar Archivo")
            print("3. Escribir archivo de salida")
            print("4. Mostrar datos estudiante")
            print("5. Generar Grafica")
            print("6. Salida")
            
            seleccion = input('Seleccione la opcion por favor: ')
            if seleccion == '1':
                leerXml.saveData('1')
            elif seleccion == '2':
                print('procesando datos...')
                time.sleep(1)
                leerXml.saveData('3')
            elif seleccion == '3':
                leerXml.saveData('4')
            elif seleccion == '4':
                main.datosEstudiante()
            elif seleccion == '5':
                leerXml.saveData('2')
            elif seleccion == '6':
                break
            print('--------------------------------------------------------------------')

    def datosEstudiante():
        print('--------------------------------------------------------------------')
        print('Kevyn Josue Giron Jimenez')
        print('201700653')
        print('Introduccion a la programacion y computacion seccion "C"')
        print('Ingenieria en ciencias y sistemas')
        print('4to semestre')
        print('--------------------------------------------------------------------')

    
main.inicio()
