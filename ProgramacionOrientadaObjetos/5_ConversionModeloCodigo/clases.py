class Contrato():
    def __init__(self,numeroContrato,tipoContrato,salario,fechaInicio,fechaFin):
        self.numeroContrato = numeroContrato
        self.tipoContrato = tipoContrato
        self.salario=salario
        self.fechaInicio=fechaInicio
        self.fechaFin=fechaFin

class Empleado():
    def __init__(self,identificacion,nombre,cargo):
        self.__identificacion=identificacion
        self.nombre=nombre
        self.cargo=cargo
        self.contrato= None
        
    def getIdentificacion(self):
        return self.__identificacion
    def setIdentificacion(self,identificacion):
        self.__identificacion=identificacion
    def asignarContrato(self,contrato):
        self.contrato=contrato
        
    def calcularSalario(self):
        if self.contrato:
            return self.contrato.salario
        else:
            return 0

class Administrativo(Empleado):
    def __init__(self,area,bonoMensual,identificacion,nombre,cargo):
        super().__init__(identificacion,nombre,cargo)
        self.area=area
        self.bonoMensual=bonoMensual
    def calularBono(self):
        return self.bonoMensual
    def calcularSalario(self):
        salarioBase=super().calcularSalario()
        bono=self.calularBono()
        return salarioBase+bono
        
class Operativo(Empleado):
    def __init__(self,turno,horasExtras,identificacion,nombre,cargo):
        super().__init__(identificacion,nombre,cargo)
        self.turno=turno
        self.horasExtras=horasExtras
    def calcularHorasExtras(self):
        return self.horasExtras * 10000
    def calcularSalario(self):
        salarioBase=super().calcularSalario()
        horasExtras=self.calcularHorasExtras()
        return salarioBase+horasExtras
        
class Departamento():
    def __init__(self,nombre):
        self.nombre=nombre
        self.listaEmpleados=[]
    def agregarEmpleado(self,empleado):
        self.listaEmpleados.append(empleado)
    def listarEmpleados(self):
        for empleado in self.listaEmpleados:
            print(f"Empleado: {empleado.nombre}, Cargo: {empleado.cargo}, Contrato: {empleado.contrato.tipoContrato}")

class Empresa():
    def __init__(self,nombre):
        self.nombre=nombre
        self.listaDepartamentos=[]
    def registrarDepartamento(self,departamento):
        self.listaDepartamentos.append(departamento)
    def listarDepartamentos(self):
        for departamento in self.listaDepartamentos:
            print(f"Departamento: {departamento.nombre}")
            departamento.listarEmpleados()
