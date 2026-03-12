from clases import *
from datetime import datetime as dt, timedelta
#Creacion de la empresa y departamentos

miEmpresa=Empresa("EDU_TEST_SOFT")
miDepartamento1=Departamento("Recursos Humanos")
miEmpresa.registrarDepartamento(miDepartamento1)
miDepartamento2=Departamento("Tecnologia")
miEmpresa.registrarDepartamento(miDepartamento2)

#Creacion de contratos y empleados

contrato1=Contrato(1,"Indefinido",3000000,dt(2023,1,1),dt(2024,1,1))
empleado1=Administrativo("Recursos Humanos",500000,"12345","Nicolas Ruiz","Gerente")
empleado1.asignarContrato(contrato1)

contrato2=Contrato(2,"Temporal",2000000,dt(2023,6,1),dt(2023,12,1))
empleado2=Operativo("Nocturno",10,"67890","Laura Gomez","Asistente")
empleado2.asignarContrato(contrato2)

# visualizacion de la informacion
print(miEmpresa.nombre)
print(f"Salario de {empleado1.nombre}: {empleado1.calcularSalario()}")
print(f"Salario de {empleado2.nombre}: {empleado2.calcularSalario()}")

print("Listado de empleados por departamento:")
print("="*30)
miDepartamento1.agregarEmpleado(empleado1)
miDepartamento2.agregarEmpleado(empleado2)
miEmpresa.listarDepartamentos() 
print("="*30)
