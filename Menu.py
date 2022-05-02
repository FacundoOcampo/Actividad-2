from ClaseViajeroFrecuente import ViajeroFrecuente

class ClaseMenu:
    __Num=None
    def __init__(self):
        self.__Num=None
    def opciones(self,Op,xReader,xListaV):
        if Op == 1:
            self.opcion1(xReader,xListaV)
        elif Op== 2:
            self.opcion2(xListaV)
        elif Op==3:
            self.opcion3(xListaV)
        elif Op== 0:
            self.Salir()
        else:
            print("Valor Incorrecto\n")

    def opcion1(self,xReader,xListaV):
        for fila in xReader:
            Num=int(fila[0])
            Dni=int(fila[1])
            Nom=str(fila[2])
            Apell=str(fila[3])
            Mill=int(fila[4])
            NuevoViajero=ViajeroFrecuente(Num,Dni,Nom,Apell,Mill)
            xListaV.append(NuevoViajero)
            print("----------------------------------------------------------")

    def opcion2(self,xListaV):
        xNum=int(input("Ingrese un numero de viajero"))
        b=False
        for i in range(len(xListaV)):
            aux=xListaV[i].GetNum()
            if(xNum == aux):
                while b != True:
                    print("----------------------------------------------------------")
                    xOp=int(input("Seleccione una opcion:\n         1_Consultar Cantidad de Millas.\n         2_ Acumular Millas.\n         3_Canjear Millas.\n         0_para salir\n----------------------------------------------------------\n"))
                    if xOp==1:
                        xListaV[i].CantidadTotalMillas()
                    elif xOp==2:
                        print("----------------------------------------------------------")
                        cant=int(input("Ingrese la cantidad de millas recorridas"))
                        xListaV[i].AcumularMillas(cant)
                    elif xOp==3:
                        print("----------------------------------------------------------")
                        cantCanj=int(input("Ingrese la cantidad de millas a canjear"))
                        xListaV[i].CanjearMillas(cantCanj)
                    else:
                        b=True

        if b==False:
            print("No se encontro el viajero")
    def opcion3(self,xListav):

      for i in range(len(xListav)):
          print("Direccion de memoria: {}\n     Datos almacenados: {}\n".format(hex(id(xListav[i])),xListav[i]))

    def Salir(self):
        print("Se salio con exito\n")
