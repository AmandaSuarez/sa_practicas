# main.py
# Importamos la clase Producto y las funciones del inventario
from producto import Producto
from inventario import registrar_producto, reporte_iva, mostrar_inventario

def main():
    # Registramos los productos usando la clase limpia
    registrar_producto(Producto("Laptop", 800, 5, "Tecnología"))
    registrar_producto(Producto("Cuaderno", 2.5, 50, "Útiles"))
    
    print("-" * 50)
    mostrar_inventario()
    print("-" * 50)
    reporte_iva()

if __name__ == "__main__":
    main()