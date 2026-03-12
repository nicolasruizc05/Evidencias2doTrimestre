import json
import pandas as pd

ventas=[
    
  {"vendedor": "Carlos", "mes": "Enero", "ventas": 12000},
  {"vendedor": "Laura", "mes": "Enero", "ventas": 15000},
  {"vendedor": "Andres", "mes": "Enero", "ventas": 9800},
  {"vendedor": "Sofia", "mes": "Enero", "ventas": 13200},
  {"vendedor": "Miguel", "mes": "Enero", "ventas": 11000},

  {"vendedor": "Carlos", "mes": "Febrero", "ventas": 14000},
  {"vendedor": "Laura", "mes": "Febrero", "ventas": 16000},
  {"vendedor": "Andres", "mes": "Febrero", "ventas": 10500},
  {"vendedor": "Sofia", "mes": "Febrero", "ventas": 13800},
  {"vendedor": "Miguel", "mes": "Febrero", "ventas": 12000},

  {"vendedor": "Carlos", "mes": "Marzo", "ventas": 15000},
  {"vendedor": "Laura", "mes": "Marzo", "ventas": 17000},
  {"vendedor": "Andres", "mes": "Marzo", "ventas": 11200},
  {"vendedor": "Sofia", "mes": "Marzo", "ventas": 14500},
  {"vendedor": "Miguel", "mes": "Marzo", "ventas": 13000},

  {"vendedor": "Carlos", "mes": "Abril", "ventas": 15500},
  {"vendedor": "Laura", "mes": "Abril", "ventas": 17500},
  {"vendedor": "Andres", "mes": "Abril", "ventas": 11800},
  {"vendedor": "Sofia", "mes": "Abril", "ventas": 15000},
  {"vendedor": "Miguel", "mes": "Abril", "ventas": 13500},

  {"vendedor": "Carlos", "mes": "Mayo", "ventas": 16000},
  {"vendedor": "Laura", "mes": "Mayo", "ventas": 18000},
  {"vendedor": "Andres", "mes": "Mayo", "ventas": 12000},
  {"vendedor": "Sofia", "mes": "Mayo", "ventas": 15500},
  {"vendedor": "Miguel", "mes": "Mayo", "ventas": 14000},

  {"vendedor": "Carlos", "mes": "Junio", "ventas": 16500},
  {"vendedor": "Laura", "mes": "Junio", "ventas": 18500},
  {"vendedor": "Andres", "mes": "Junio", "ventas": 12500},
  {"vendedor": "Sofia", "mes": "Junio", "ventas": 16000},
  {"vendedor": "Miguel", "mes": "Junio", "ventas": 14500}
]

with open("dataset/ventas.json","w",encoding="utf-8") as archivo:
    json.dump(ventas,archivo,indent=4,ensure_ascii=False)

venta=pd.read_json("dataset/ventas.json")
#1. Total de ventas por vendedor
def total_ventas_por_vendedor(venta):
       
      totalVentasVendedor=venta.groupby("vendedor")["ventas"].sum()
      print(totalVentasVendedor)
      totalVentasVendedor.to_json("dataset/total_ventas_vendedor.json",orient="index",indent=4,force_ascii=False)
      return totalVentasVendedor 

#2 promedio ventas por mes
def promedio_ventas_por_mes(venta):
      promedioVentasMes=venta.groupby("mes")["ventas"].mean()
      print(promedioVentasMes)
      promedioVentasMes.to_json("dataset/promedio_ventas_mes.json",orient="index",indent=4,force_ascii=False) 

#3. Vendedor con mayores ventas
def vendedor_con_mayores_ventas(venta):
        
      mayorVentas=total_ventas_por_vendedor(venta).max()
      vendedorMayorVentas=total_ventas_por_vendedor(venta)[total_ventas_por_vendedor(venta)==mayorVentas]
      print(f"Vendedor con mayores ventas: {vendedorMayorVentas}")
      vendedorMayorVentas.to_json("dataset/vendedor_mayor_ventas.json",orient="index",indent=4,force_ascii=False)

#Nuevo rankings de vendedores por ventas totales
def Nuevo_ranking_vendedores(venta):
      ranking=total_ventas_por_vendedor(venta).sort_values(ascending=False)
      print(f"Ranking de vendedores por ventas totales: {ranking}")
      ranking.to_json("dataset/ranking_vendedores.json",orient="index",indent=4,force_ascii=False)
      
def menu():
  while True:
    print("Seleccione una opción:")
    print("1. Total de ventas por vendedor")
    print("2. Promedio de ventas por mes")
    print("3. Vendedor con mayores ventas")
    print("4. Nuevo ranking de vendedores por ventas totales")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    match opcion:
      case "1":
        total_ventas_por_vendedor(venta)
      case "2":
        promedio_ventas_por_mes(venta)
      case "3":
        vendedor_con_mayores_ventas(venta)
      case "4":
        Nuevo_ranking_vendedores(venta)
      case "5":
        print("Saliendo del programa...")
        break
      case _:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
    
menu()