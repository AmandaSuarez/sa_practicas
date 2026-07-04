from models import Producto
from logic import validar_producto, calcular_precio_final
from storage import cargar_datos, guardar_datos

def registrar_producto(nuevo_prod: Producto):
    if not validar_producto(nuevo_prod):
        print("Error: Datos inválidos.")
        return
    
    lista = cargar_datos()
    lista.append(nuevo_prod)
    guardar_datos(lista)
    print(f"Producto {nuevo_prod.nombre} registrado con éxito.")

def listar_productos():
    productos = cargar_datos()
    for p in productos:
        alerta = "¡STOCK BAJO!" if p.stock < 5 else "OK"
        precio_final = calcular_precio_final(p)
        print(f"{p.codigo_barras} | {p.nombre} | {p.stock} un. | {alerta} | Total: ${precio_final:.2f}")

def main():
    # Ejemplo de uso
    registrar_producto(Producto("12345", "Laptop", 800.0, 3, "Tecnología"))
    listar_productos()

if __name__ == "__main__":
    main()