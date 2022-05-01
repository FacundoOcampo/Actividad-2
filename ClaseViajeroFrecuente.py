class ViajeroFrecuente:
    __num_viajero=None
    __dni=None
    __nombre=None
    __apellido=None
    __millas_acum=None
    def __init__(self,num_viajero,dni,nombre,apellido,millas_acum):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas_acum
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
