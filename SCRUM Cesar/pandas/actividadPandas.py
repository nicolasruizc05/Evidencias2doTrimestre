import pandas as pd
#Importar archivo y lectura del mismo
estudiantes=pd.read_csv("dataset/estudiantes.csv")

 
def Primerosregistros():
    print(estudiantes.head(10))

def ListarestudiantesPromedioMayor42():
    promedioMayor42=estudiantes[estudiantes['promedio']>4.2]
    print(promedioMayor42)

def ListarsexoMayor21():
    opcion=int(input("1. Masculino\n2. Femenino\nSeleccione: "))
    
    if opcion == 1:
        filtro = estudiantes[(estudiantes['sexo']=="Masculino") & (estudiantes['edad']>21)]
        print(filtro)
        
    elif opcion == 2:
        filtro = estudiantes[(estudiantes['sexo']=="Femenino") & (estudiantes['edad']>21)]
        print(filtro)
        
    else:
        print("Opción no válida")
        
def PromedioPorSexo():
    promedio_m = estudiantes[estudiantes['sexo']=="Masculino"]['promedio'].mean()
    promedio_f = estudiantes[estudiantes['sexo']=="Femenino"]['promedio'].mean()
    
    print("Promedio Masculino:", promedio_m)
    print("Promedio Femenino:", promedio_f)

def MayorEdad():
    mayor = estudiantes[estudiantes['edad'] == estudiantes['edad'].max()]
    print(mayor)
    

def Edad20promedio45():
    filtro = estudiantes[(estudiantes['edad']==20) | (estudiantes['promedio']>4.5)]
    print(filtro)
            

def Nuevoarchivo():
    alto = estudiantes[estudiantes['promedio']>4.5]
    alto.to_csv("dataset/alto_rendimiento.csv", index=False)
    print("Archivo alto_rendimiento.csv creado correctamente")


print("Bienvenido al programa de estudiantes")
print("==============================")
print(" 1. Leer archivo y mostrar primeros 10 registros")
print(" 2. Listar estudiantes con promedio mayor a 4.2")
print(" 3. Listar estudiantes de sexo masculino o femenino mayores a 21 años")
print(" 4. Mostrar promedio por sexo")
print(" 5. Mostrar estudiante con mayor edad")
print(" 6. Mostrar estudiantes de 20 años con promedio mayor a 4.5")
print(" 7. Crear archivo de alto rendimiento")  
print(" 0. Salir")
print("==============================")
opcion=0  
salir=False
while salir==False: 
    opcion=int(input("Seleccione una opción: "))
    match(opcion):
        case 1:
            Primerosregistros()
        case 2:
            ListarestudiantesPromedioMayor42()
        case 3:
            ListarsexoMayor21()
        case 4:
            PromedioPorSexo()
        case 5:
            MayorEdad()
        case 6:
            Edad20promedio45()
        case 7:
            Nuevoarchivo()
        case 0:
            print("Saliendo...")
            salir=True  
