# inventario.py
from producto import Producto

# Lista para almacenar los productos registrados
productos = []

# Código Limpio: Usamos una constante para el IVA en vez de números mágicos
TASA_IVA = 0.15 

def calcular_iva(precio):
    return precio * TASA_IVA

def registrar_producto(producto):
    productos.append(producto)
    print("Producto registrado.")

def reporte_iva():
    # Suma el IVA de cada producto en la lista
    total_iva = sum(calcular_iva(producto["precio"] if isinstance(producto, dict) else producto.precio) for producto in productos)
    print(f"IVA acumulado: ${total_iva:.2f}")

def mostrar_inventario():
    # Función extra para imprimir los productos en pantalla de forma limpia
    for p in productos:
        # Validamos si es diccionario o un objeto de clase por seguridad
        nom = p["nombre"] if isinstance(p, dict) else p.nombre
        pre = p["precio"] if isinstance(p, dict) else p.precio
        cant = p["cantidad"] if isinstance(p, dict) else p.cantidad
        cat = p["categoria"] if isinstance(p, dict) else p.categoria
        
        total_con_iva = pre + calcular_iva(pre)
        print(f"{nom} | ${pre} | {cant} | {cat} | ${total_con_iva:.2f}")