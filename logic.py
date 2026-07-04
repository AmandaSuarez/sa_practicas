from models import Producto

def calcular_iva(categoria: str, precio: float) -> float:
    # IVA 12% para tecnología, 15% el resto
    tasa = 0.12 if categoria == "Tecnología" else 0.15
    return precio * tasa

def calcular_precio_final(producto: Producto) -> float:
    precio_con_iva = producto.precio + calcular_iva(producto.categoria, producto.precio)
    if producto.categoria == "Tecnología":
        return precio_con_iva * 0.90  # 10% descuento
    return precio_con_iva

def validar_producto(p: Producto) -> bool:
    return p.nombre != "" and p.precio > 0 and p.stock >= 0 and p.codigo_barras != ""