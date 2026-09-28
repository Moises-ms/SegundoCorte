# eliminar.py

def eliminar_por_id(inventario, id_producto):
    """DELETE: Remueve un producto específico mediante su ID."""
    for i, prod in enumerate(inventario):
        if prod["id"] == id_producto:
            eliminado = inventario.pop(i)
            print(f" Producto '{eliminado['nombre']}' (ID: {id_producto}) ha sido eliminado.")
            return
    print(f" No se encontró ningún producto con ID: {id_producto}")

def eliminar_sin_stock(inventario):
    """DELETE: Remueve todos los productos cuyo stock sea 0."""
    inventario[:] = [prod for prod in inventario if prod["stock"] > 0]
    print(" Se han depurado los productos agotados (stock 0).")