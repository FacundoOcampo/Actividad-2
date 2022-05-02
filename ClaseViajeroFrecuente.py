class ViajeroFrecuente:
    __num_viajero=None
    __dni=None
    __nombre=None
    __apellido=None
    __millas_acum=None
    def __init__(self,fila):
        if len(fila)==5:
            self.__num_viajero=int(fila[0])
            self.__dni=int(fila[1])
            self.__nombre=str(fila[2])
            self.__apellido=str(fila[3])
            self.__millas_acum=int(fila[4])
            print("Viajero cargado con exito")
        else:
            print("Error al crear Viajero")
    def CantidadTotalMillas(self):
        print("----------------------------------------------------------")
        print("La cantidad de millas acumulada es: {}".format(self.__millas_acum))
    def AcumularMillas(self,cant):
        acum=self.__millas_acum+cant
        self.__millas_acum=acum
        print("----------------------------------------------------------")
        print("La cantidad nueva de millas acumuladas es: ",acum)
    def CanjearMillas(self,CantC):
        if(CantC<=self.__millas_acum):
            self.__millas_acum=self.__millas_acum-CantC
            print("La cantidad nueva de millas acumuladas es:",self.__millas_acum)
        elif(CantC>self.__millas_acum):
            print("----------------------------------------------------------")
            print("La cantidad de millas a canjear es mayor a la acumulada")
        else:
            print("----------------------------------------------------------")
            print("Error")
    def MostrarDatos(self):
        print(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum)
    def GetNum(self):
        return self.__num_viajero
