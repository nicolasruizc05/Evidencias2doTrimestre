class Pasajero:
    def __init__(self,identificacion=None,nombres=None,apellidos=None,correo=None):
        self.__identificacion=identificacion
        self.__nombres=nombres
        self.__apellidos=apellidos
        self.__correo=correo
    def getIdentificacion(self):
        self.__identificacion
    def setIdentificacion(self,identificacion):
        self.__identificacion=identificacion
    def getNombres(self):
        self.__nombres
    def setNombres(self,nombres):
        self.__nombres=nombres
    def getApellidos(self):
        self.__apellidos
    def setApellidos(self,apellidos):
        self.__apellidos=apellidos
    def getCorreo(self,correo):
        self.__correo
    def setCorreo(self,correo):
        self.__correo=correo
        