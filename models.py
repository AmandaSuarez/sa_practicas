from dataclasses import dataclass

@dataclass
class Producto:
    codigo_barras: str  # Nuevo campo requerido
    nombre: str
    precio: float
    stock: int
    categoria: str