import csv
from Menu import ClaseMenu
from ClaseViajeroFrecuente import ViajeroFrecuente

def Test():
    print("Datos correctos:")
    Fila=[]
    print("     11,44061072,Francisco,Rojo,5")
    Fila=[11,44061072,"Francisco","Rojo",5]
    TestViajero=ViajeroFrecuente(Fila)
    print("     43,99466788,Pedro,Romero,10 ")
    Fila=[43,99466788,"Pedro","Romero",10]
    TestViajero=ViajeroFrecuente(Fila)
    print("     98,52987412,Flor,Ramirez,9")
    Fila=[98,52987412,"Flor","Ramirez",9]
    TestViajero=ViajeroFrecuente(Fila)
    print("\nDatos Incorrectos:")
    print("     58963741,Ramiro,Fernadez,12")
    Fila=[58963741,"Ramiro","Fernadez",12]
    TestViajero=ViajeroFrecuente(Fila)
    print("     89,45689963,45,Sofia,Cortez,12")
    Fila=[ 89,45689963,45,"Sofia","Cortez",12]
    TestViajero=ViajeroFrecuente(Fila)


if __name__ == '__main__':
    Archivo=open("Lista.csv","r")
    Reader=csv.reader(Archivo,delimiter=",")
    ListaV=[]
    NuevoMenu=ClaseMenu()
    Num=int(input("¿Quiere ejecutar el test? 1_Si \ 2_NO\n"))
    if(Num==1):
        Test()
    print("------------------------Menu------------------------------")
    op = int(input("Ingrese una opcion. \n1_Cargar Archivo(Necesaria Para ejecutar el programa)\n2_Leer Numero de Viajero\n3_Mostrar datos en la memoria\n0_Salir\n----------------------------------------------------------\n"))
    NuevoMenu.opciones(op,Reader,ListaV)
    while op != 0:
        print("------------------------Menu------------------------------")
        op = int(input("Ingrese una opcion. \n1_Cargar Archivo\n2_Leer Numero de Viajero\n3_Mostrar datos en la memoria\n0_Salir\n----------------------------------------------------------\n"))
        print("----------------------------------------------------------")
        NuevoMenu.opciones(op,Reader,ListaV)
    Archivo.close()
