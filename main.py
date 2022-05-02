import csv
from Menu import ClaseMenu
from ClaseViajeroFrecuente import ViajeroFrecuente

def Test():
    print("Datos correctos:")
    Fila=[]
    print('     11,44061072,"Francisco","Rojo",5')
    TestViajero=ViajeroFrecuente(11,44061072,"Francisco","Rojo",5)
    print('     43,99466788,"Pedro","Romero",10 ')
    TestViajero=ViajeroFrecuente(43,99466788,"Pedro","Romero",10)
    print('     98,52987412,"Flor","Ramirez",9')
    TestViajero=ViajeroFrecuente(98,52987412,"Flor","Ramirez",9)
    print("\nDatos Incorrectos:")
    print('     "1",58963741,"Ramiro","Fernadez",12 (El primer dato es de tipo string)')
    TestViajero=ViajeroFrecuente("1",58963741,"Ramiro","Fernadez",12)
    print('     "89","45689963","45","Sofia","Cortez",12 (Todo datos de tipo sting)')
    TestViajero=ViajeroFrecuente("89","45689963","Sofia","Cortez","12")
    print('     5,52896374,4554,33445,15 (Todos datos de tipo int)')
    TestViajero=ViajeroFrecuente(5,52896374,4554,33445,15)


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
