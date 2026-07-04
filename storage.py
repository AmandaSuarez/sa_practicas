import json
import os
from models import Producto

ARCHIVO_INVENTARIO = "datos_inv.json"

def guardar_datos(lista_productos):
    with open(ARCHIVO_INVENTARIO, "w") as archivo:
        json.dump([vars(p) for p in lista_productos], archivo)

def cargar_datos():
    if not os.path.exists(ARCHIVO_INVENTARIO):
        return []
    with open(ARCHIVO_INVENTARIO, "r") as archivo:
        data = json.load(archivo)
        return [Producto(**p) for p in data]