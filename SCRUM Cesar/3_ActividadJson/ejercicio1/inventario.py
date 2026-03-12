import json
import pandas as pd

#Crear documento JSON

productos = [
    {"producto": "Laptop básica", "precio_unitario": 1800000, "cantidad": 2},
    {"producto": "Mouse inalámbrico", "precio_unitario": 45000, "cantidad": 10},
    {"producto": "Teclado mecánico", "precio_unitario": 220000, "cantidad": 5},
    {"producto": "Monitor 24 pulgadas", "precio_unitario": 650000, "cantidad": 3},
    {"producto": "Disco duro externo 1TB", "precio_unitario": 320000, "cantidad": 4},
    {"producto": "Memoria USB 64GB", "precio_unitario": 35000, "cantidad": 12},
    {"producto": "Audífonos inalámbricos", "precio_unitario": 180000, "cantidad": 6},
    {"producto": "Tablet", "precio_unitario": 900000, "cantidad": 3},
    {"producto": "Smartphone gama media", "precio_unitario": 1200000, "cantidad": 4},
    {"producto": "Cargador portátil (Power Bank)", "precio_unitario": 80000, "cantidad": 7},
    {"producto": "Router WiFi", "precio_unitario": 150000, "cantidad": 5},
    {"producto": "Cámara web HD", "precio_unitario": 95000, "cantidad": 6},
    {"producto": "Micrófono USB", "precio_unitario": 160000, "cantidad": 4},
    {"producto": "Tarjeta microSD 128GB", "precio_unitario": 70000, "cantidad": 8},
    {"producto": "Cable HDMI", "precio_unitario": 25000, "cantidad": 10},
    {"producto": "Base refrigerante para laptop", "precio_unitario": 85000, "cantidad": 4},
    {"producto": "Parlantes para PC", "precio_unitario": 120000, "cantidad": 5},
    {"producto": "SSD 500GB", "precio_unitario": 280000, "cantidad": 6},
    {"producto": "Impresora multifuncional", "precio_unitario": 750000, "cantidad": 2},
    {"producto": "Smartwatch", "precio_unitario": 350000, "cantidad": 3}
  ]

with open("dataset/productos.json","w",encoding="Utf8") as archivo:
    json.dump(productos,archivo,indent=4,ensure_ascii=False)  # Ensure_ascii para que aparezcan las entonaciones y la ñ en el archivo creado
    
productos=pd.read_json("dataset/productos.json")  

def valorTotalProductos(productos):
    productos["valor_total"]=productos["precio_unitario"]*productos["cantidad"]
    valorTotal=productos[["producto","valor_total"]]
    return valorTotal

def TotalInventario(productos):
    productos["valor_total"]=productos["precio_unitario"]*productos["cantidad"]
    valorTotalInventario = productos["valor_total"].sum()
    return valorTotalInventario
def productosBajoStock(productos):
    bajoStock=productos[productos["cantidad"]<5]  
    return bajoStock

def menu():
    print("Menú de opciones:")
    print("1. Calcular valor total por producto")
    print("2. Calcular valor total del inventario")
    print("3. Exportar productos con bajo stock (cantidad < 5)")
    print("4. Salir")
    while True:
        opcion=input("Seleccione una opción (1-4): ")
        match opcion:
            case "1":
                resultado=valorTotalProductos(productos)
                resultado.to_json("dataset/valor_total_producto.json",orient="records",indent=4,force_ascii=False)
                print(f"Valor total por producto: \n{resultado}\n")
            case "2":
                inventario=TotalInventario(productos)
                data = {
                    "valor_total_inventario": int(inventario)
                }
                with open("dataset/valor_total_inventario.json", "w", encoding="utf-8") as archivo:
                    json.dump(data, archivo, indent=4, ensure_ascii=False)
                print(f"Valor total del inventario: {inventario}\n")
            case "3":
                bajoStock=productosBajoStock(productos)
                bajoStock.to_json("dataset/productos_bajo_stock.json",orient="records",indent=4,force_ascii=False)
                print(f"Productos con bajo stock (cantidad < 5): \n{bajoStock}\n")
            case "4":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
menu()
