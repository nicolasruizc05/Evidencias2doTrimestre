from Empresa import Empresa
from Vuelo import Vuelo
from Pasajero import Pasajero
from datetime import datetime
import os
import pandas as pd
import json

miEmpresa= Empresa("XYZ")
def ExisteVuelo(numero):
    for vuelo in miEmpresa.getVuelos():
        if vuelo.getNumero()==numero:
            return True
        else:
            return False
def crearVuelo():
    os.system("cls")
    print("Creacion de Vuelo")
    try:
        numero=input("Ingrese el numero de vuelo:  ")
        #buscar si existe un vuelo con ese codigo
        if not ExisteVuelo(numero):
            fecha=input("Ingrese fecha de vuelo (yyyy-mm-dd):  ")
            fecha_obj=datetime.strptime(fecha,'%Y-%m-%d')
            hora=input("Ingrese hora de vuelo (hh:mm):  ")
            hora_obj=datetime.strptime(hora,'%H:%M').time()
            ciudadOrigen=input("Ingrese ciudad Origen:  ")
            ciudadDestino=input("Ingrese ciudad Destino: ")
            miEmpresa.registrarVuelo(numero,fecha_obj,hora_obj,ciudadOrigen,ciudadDestino)
            print("El vuelo ha sido creado exitosamente")
        else:
            print(f"No se puede crear vuelo Ya existe un vuelo con el numero {numero}")
    except Exception as ex:
        print(str(ex))
def listarVuelos():
    os.system
    print("LISTA TOTAL DE VUELOS")
    try:
        for vuelo in miEmpresa.getVuelos():
            print(vuelo)
    except Exception as ex:
        print(str(ex))    
def registrarPasajeroVuelo():
    os.system("Cls")
    print("REGISTRAR PASAJERO A VUELO")
    numeroVuelo=input("Ingrese numero de vuelo:  ")
    vuelo=miEmpresa.consultarVueloPorCodigo(numeroVuelo)
    if (vuelo):
        # pedir datos del pasajero
        identificacion=input("Ingrese identificacion del pasajero: ")
        nombres=input("Ingrese nombre del pasajero: ")
        apellidos=input("Ingrese apellidos del pasajero: ")
        correo=input("Ingrese correo del pasajero")
        vuelo.regisrarPasjero(identificacion,nombres,apellidos,correo)
        print("Pasajero registrado de manera existosa")
    else:
        print(f"Vuelo con el número {numeroVuelo} no existe ")
        
def listarPasajerosVuelos():
    os.system("Cls")
    print(f"LISTA DE PASAJEROS DE UN VUELO")
    numeroVuelo=input("Ingrese numero de vuelo: ")
    vuelo=miEmpresa.consultarVueloPorCodigo(numeroVuelo)
    if(vuelo):
        for pasajero in vuelo.
def menu():
    while(True):
        os.system("cls")#Limpiar pantalla
        print("\t\tMENU OPCIONES")
        print("\t 1. Crear Vuelo")
        print("\t 2. Listar Vuelo")
        print("\t3. Registrar pasajero a un vuelo")
        print("\t4. Consultar vuelo por código")
        print("\t5. Listar los vuelos por fecha")
        print("\t6. Listar pasajeros de un vuelo")
        print("\t7.Salir")
        
        opcion= int(input("Ingrese opcion (1-6): "))
        match opcion:
            case 1:
                crearVuelo()
            case 2:
                listarVuelos()
            case 3:
                registrarPasajeroVuelo()
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion incorrecta, por favor seleccione una opcion entre 1-6: ")
                
        enter=input("Presione enter para continuar")
menu()