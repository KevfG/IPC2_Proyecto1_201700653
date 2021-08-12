matrizPrueba = [
    [1, 1, 5, 3, 2],
    [4, 1, 4, 2, 6],
    [3, 1, 1, 3, 3],
    [5, 2, 3, 1, 2],
    [2, 1, 1, 1, 1]
]



class main:

    def inicio():
        print("1. Cargar Archivo")
        print("2. Procesar Archivo")
        print("3. Escribir archivo de salida")
        print("4. Mostrar datos estudiante")
        print("5. Generar Grafica")
        print("6. Salida")

    def algoritmo():
        a = 9
        b = []
        c = []
        d = 0
        e = 0

        while(d <= a):
            if e < 3:
                c.append(d)
                d += 1
                e += 1
            else:
                b.append(c)
                c = []
                e = 0

        for i in b:
            print(i)

    def imprimirTerreno():

        for i in matrizPrueba:
            for j in i:
                print("|" + str(j) + "|", end=" ")
            print()

    def recorrer():

        x = 0

        for i in matrizPrueba:
            y = 0
            for j in i:
                print("fila: " + str(x))
                print("Columna: " + str(y))
                print("Valor actual: " + str(matrizPrueba[x][y]))
                
                if (y - 1) >= 0:
                    print("Valor izquierda: " + str(i[y - 1]))
                else:
                    print("Valor izquierda: No hay")

                if (y + 1) < len(i):
                    print("Valor derecha: " + str(i[y + 1]))
                else:
                    print("Valor derecha: No hay")

                if (x - 1) >= 0:
                    print("Valor arriba: " + str(matrizPrueba[x - 1][y]))
                else:
                    print("Valor arriba: No hay")

                if (x + 1) < len(matrizPrueba):
                    print("Valor abajo: " + str(matrizPrueba[x + 1][y]))
                else:
                    print("Valor abajo: No hay")
                print("----------------------------------")
                y = y + 1
            x = x + 1

    def recorrerTerreno():
        a = []
        b = []

        x = 0

        for i in matrizPrueba:
            y = 0
            for j in i:
                print("fila: " + str(x))
                print("Columna: " + str(y))
                print("Valor actual: " + str(matrizPrueba[x][y]))
                
                if (y - 1) >= 0:
                    print("Valor izquierda: " + str(i[y - 1]))

                if (y + 1) < len(i):
                    print("Valor derecha: " + str(i[y + 1]))

                if (x - 1) >= 0:
                    print("Valor arriba: " + str(matrizPrueba[x - 1][y]))

                if (x + 1) < len(matrizPrueba):
                    print("Valor abajo: " + str(matrizPrueba[x + 1][y]))

                print("----------------------------------")
                y = y + 1
            x = x + 1

# main.inicio()
main.recorrer()
