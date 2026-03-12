import pandas as pd
import os
import json
datos=pd.read_json("dataset/ventas.json")
def registrar_venta():
    global datos
    os.system("Cls")
    print("\t\tRegistrar Venta")
    vendedor = input("Ingrese el nombre del vendedor: ")
    mes= input("Ingrese el mes de la venta: ")
    monto = float(input("Ingrese el monto de la venta: "))
    nueva_venta = {"vendedor": vendedor, "mes": mes, "ventas": monto}
    datos = pd.concat([datos, pd.DataFrame([nueva_venta])], ignore_index=True)
    print("Venta registrada exitosamente.")
    return datos
def reporte_ventas():
    os.system("Cls")
    print("\t\tReporte de Ventas")
    if datos.empty:
        print("No hay ventas registradas.")
    else:
        print(datos)
def estadisticas():
    os.system("Cls")
    print("\t\tEstadísticas de Ventas")
    total_ventas = datos["ventas"].sum()
    print("Total ventas:", total_ventas)
    promedio_ventas = datos["ventas"].mean()
    print("Promedio ventas:", promedio_ventas )
    mayor_venta = datos["ventas"].max()
    print("Mayor venta:", mayor_venta)
    estadisticasPd=pd.DataFrame({
        "Total Ventas": [total_ventas], 
        "Promedio Ventas": [promedio_ventas],
        "Mayor Venta": [mayor_venta]
    })
    return estadisticasPd

def guardar_reporte_json():
    os.system("Cls")
    print("\t\tGuardar Reporte como JSON")
    datos.to_json("dataset/reporte.json", orient="records", indent=4,force_ascii=False)
    print("Reporte guardado como JSON en 'dataset/reporte.json'.")
    estadisticasPd=estadisticas()
    estadisticasPd.to_json("dataset/estadisticas.json", orient="records", indent=4,force_ascii=False)
    print("Estadísticas guardadas como JSON en 'dataset/estadisticas.json'.")
    
def guardar_reporte_csv():
    os.system("Cls")
    print("\t\tGuardar Reporte como CSV")
    datos.to_csv("dataset/reporte.csv", index=False)
    print("Reporte guardado como CSV en 'dataset/reporte.csv'.")
    estadisticasPd=estadisticas()
    estadisticasPd.to_csv("dataset/estadisticas.csv", encoding="utf-8", index=False)
    print("Estadísticas guardadas como CSV en 'dataset/estadisticas.csv'.")

def menu():
    
    while True:
        os.system("Cls")
        print("\t\tReporte de Ventas")
        print("\t1. Registrar Venta")
        print("\t2. Reporte de Ventas")
        print("\t3. Estadísticas de Ventas")
        print("\t4. Guardar Reporte como JSON")
        print("\t5. Guardar Reporte como CSV")
        print("\t6. Salir")
        opcion = input("Seleccione una opción (1-6): ")
        match opcion:
            case "1":
                registrar_venta()
            case "2":
                reporte_ventas()
            case "3":
                estadisticas()
            case "4":
                guardar_reporte_json()
            case "5":
                guardar_reporte_csv()
            case "6":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
        print("\nPresione Enter para continuar...")
        input()
menu()