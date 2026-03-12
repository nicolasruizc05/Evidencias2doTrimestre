import csv
#Crear el archivo con el encabezado 
def crearArchivo():
    
    try:
        with open("datoCSV\estudiante.csv","x",newline='',encoding="Utf-8") as archivo:
            encabezado=["nombre","edad","sexo","programa","promedio"]
            nuevo=csv.writer(archivo)
            nuevo.writerow(encabezado)
    except IOError as error:
        print(str(error))
    
#Registrar Estudiantes
def estudiantes():
    nombre=input("Ingrese su nombre:\t")
    edad=int(input("Ingrese su edad:\t"))
    sexo=input("Ingrese su genero:M(Mujer), H(hombre):\t")
    programa=input("Ingrese su programa:\t")
    promedio=input("Ingrese su promedio:\t")
    try:
        with open("datoCSV\estudiantes.csv","a",newline='',encoding="Utf-8") as archivo:
            new=csv.writer(archivo)
            new.writerow([nombre,edad,sexo,programa,promedio])
            print("Registro de estudiante exitosamente")
    except IOError as error:
        print(str(error))
    return()
    
#Leer el archivo y mostrar datos
def lectura():
    try:
        with open("datosCSV\estudiantes.csv",newline='',encoding="Utf-8") as archivo:
            lector=csv.DictReader(archivo)
            print("===Lista de estudiantes===")
            for fila in lector:
                print("="*20)
                print(f"Nombre:\t{fila['nombre']}") 
                print(f"Edad:\t{fila['edad']}")
                print(f"Genero:\t{fila['sexo']}")
                print(f"Programa:\t{fila['programa']}")
                print(f"Promedio:\t{fila['promedio']}")   
    except IOError as error:
        print(str(error))  
    return()
#Calcular promedio general 
def promedioGrupo():   
    try:
        with open("datosCSV\estudiantes.csv",newline='',encoding="Utf-8") as archivo:
                lector=csv.reader(archivo)
                suma=0
                i=0
                contador=0
                for fila in lector:
                    if i!=0:
                        suma=suma+float(fila[4])
                        contador+=1
                promedio=suma/contador
                print(f"El promedio general del grupo es:\t{promedio}")
    except IOError as error:
        print(str(error))
        
def mostrarEstudiantes():
    try:
        with open("datosCSV\estudiantes.csv",newline='',encoding="Utf-8") as archivo:
                lector=csv.DictReader(archivo)
                i=0
                for fila in lector:
                    if i!=0:
                        print(f"Nombre:\t{fila['nombre']}") 
                        print(f"Edad:\t{fila['edad']}")
                        print(f"Genero:\t{fila['sexo']}")
                        print(f"Programa:\t{fila['programa']}")
                        print(f"Promedio:\t{fila['promedio']}") 
                        i+=1
                
    except IOError as error:
        print(str(error))
                    

#Menu de opciones
opcion=0
while opcion!=5:
    print("===Menu de opciones===")
    print("1. Crear archivo")
    print("2. Registrar estudiante")
    print("3. Mostrar estudiantes")
    print("4. Calcular promedio general del grupo")
    print("5. Salir")
    print("="*20)
    
    opcion=int(input("Ingrese una opcion:\t"))
    
    match opcion:
        case 1: 
            crearArchivo()
        case 2:
            estudiantes()   
        case 3:
            mostrarEstudiantes()
        case 4:
            promedioGrupo()
        case 5:
            print("Saliendo del programa...")       
            
                
                


        

