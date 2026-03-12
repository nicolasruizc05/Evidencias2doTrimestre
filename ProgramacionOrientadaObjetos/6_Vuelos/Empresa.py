from Vuelo import Vuelo
class Empresa:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__vuelos=[]
    
    def getNombre(self,nombre):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    def getVuelos(self):
        return self.__vuelos
    def registrarVuelo(self,numero,fecha,hora,ciudadOrigen,ciudadDestino):
        vuelo=Vuelo(numero,fecha,hora,ciudadOrigen,ciudadDestino)
        self.__vuelos.append(vuelo)
    
    def listarVuelosFecha(self,fecha):
        lista=[]
        for vuelo in self.getVuelos():
            if vuelo.getFecha()==fecha:
                lista.append(vuelo)
        return lista
    
    def consultarVueloPorCodigo(self,numero):
        for vuelo in self.getVuelos():
            if vuelo.getNumero()==numero:
                return vuelo
        else:
            return None