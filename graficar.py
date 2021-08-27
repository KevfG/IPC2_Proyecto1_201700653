import os

class graph:
    def graficar(body, title):
        textHead = 'digraph H {\n\ta[\n\t\tlabel = <\n\t\t<TABLE BORDER = "0" CELLBORDER = "1" CELLSPACING = "0" >'
        textEnd = '\n\t\t</TABLE >> xlabel = "' + title + '"\n\t]\n}'
        archivo = open("g.dot", "w")
        archivo.write(textHead)
        archivo.write('\n\t\t' + body)
        archivo.write(textEnd)
        archivo.close()
        graph.compilar()
        os.system("graf.jpg")

    def compilar():
        os.system('dot -Tjpg g.dot -o graf.jpg')

#graph.graficar("<TR><TD WIDTH = '30'>1</TD><TD WIDTH = '30'>2</TD></TR>")