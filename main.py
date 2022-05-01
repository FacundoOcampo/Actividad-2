import csv
from Menu import ClaseMenu


if __name__ == '__main__':
    Archivo=open("Lista.csv","r")
    Reader=csv.reader(Archivo,delimiter=",")
    ListaV=[]
    NuevoMenu=ClaseMenu()
    print("------------------------Menu------------------------------")
    op = int(input("Ingrese una opcion. \n1_Cargar Archivo(Necesaria Para ejecutar el programa)\n2_Leer Numero de Viajero\n3_Mostrar datos en la memoria\n0_Salir\n----------------------------------------------------------\n"))
    NuevoMenu.opciones(op,Reader,ListaV)
    while op != 0:
        print("------------------------Menu------------------------------")
        op = int(input("Ingrese una opcion. \n1_Cargar Archivo\n2_Leer Numero de Viajero\n3_Mostrar datos en la memoria\n0_Salir\n----------------------------------------------------------\n"))
        print("----------------------------------------------------------")
        NuevoMenu.opciones(op,Reader,ListaV)
    Archivo.close()
