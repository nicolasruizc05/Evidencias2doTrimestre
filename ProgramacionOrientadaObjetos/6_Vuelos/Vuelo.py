from Pasajero import Pasajero
class Vuelo:
    def __init__(self,numero=None,fecha=None,hora=None,ciudadOrigen=None,ciudadDestino=None):
        self.__numero=numero
        self.__fecha=fecha
        self.__hora=hora
        self.__ciudadOrigen=ciudadOrigen
        self.__ciudadDestino=ciudadDestino
        self.__pasajeros=[]
        
    def getNumero(self):
        return self.__numero
    def setNumero(self,numero):
        self.__numero=numero  
    def getFecha(self):
        return self.__fecha
    def setFecha(self,fecha):
        self.__fecha=fecha
    def getHora(self):
        return self.__hora
    def setHora(self,hora):
        self.__hora=hora
    def getCiudadOrigen(self):
        return self.__ciudadOrigen
    def setCiudadOrigen(self,ciudadOrigen):
        self.__ciudadOrigen=ciudadOrigen
    def getCiudadDestino(self):
        return self.__ciudadDestino
    def setCiudadDestino(self,ciudadDestino):
        self.__ciudadDestino=ciudadDestino

    def registrarPasajero(self,identificacion,nombres,apellidos,correo):
        pasajero=Pasajero(identificacion,nombres,apellidos,correo)
        self.__pasajeros.append(pasajero)
    
    def listarPasajeros(self,numero):
        if self.__numero==numero:
            return self.__pasajeros
    def __str__(self):
        return f"{self.__numero} - {self.__fecha} - {self.__hora}"