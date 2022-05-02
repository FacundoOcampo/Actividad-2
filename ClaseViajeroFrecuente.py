class ViajeroFrecuente:
    __num_viajero=None
    __dni=None
    __nombre=None
    __apellido=None
    __millas_acum=None
    def __init__(self,Num,Dni,Nom,Apell,Millas):
        if ((type(Num)==int)&(type(Dni)==int)&(type(Nom)==str)&(type(Apell)==str)&(type(Millas)==int)):
            self.__num_viajero=Num
            self.__dni=Dni
            self.__nombre=Nom
            self.__apellido=Apell
            self.__millas_acum=Millas
            print("Viajero cargado con exito")
        else:
            print("Error al crear Viajero")
    def CantidadTotalMillas(self):
        print("----------------------------------------------------------")
        print("La cantidad de millas acumulada es: {}".format(self.__millas_acum))
    def AcumularMillas(self,cant):
        if(type(cant)==int):
            acum=self.__millas_acum+cant
            self.__millas_acum=acum
            print("----------------------------------------------------------")
            print("La cantidad nueva de millas acumuladas es: ",acum)
        else:
            print("Error al ingresar la cantidad de millas a acumular")
    def CanjearMillas(self,CantC):
        if(type(CantC)==int):
            if(CantC<=self.__millas_acum):
                self.__millas_acum=self.__millas_acum-CantC
                print("La cantidad nueva de millas acumuladas es:",self.__millas_acum)
            else:
                print("----------------------------------------------------------")
                print("La cantidad de millas a canjear es mayor a la acumulada")
        else:
            print("----------------------------------------------------------")
            print("Error")
    def MostrarDatos(self):
        print(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum)
    def GetNum(self):
        return self.__num_viajero
