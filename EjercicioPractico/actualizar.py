# actualizar.py

def modificar_precio(inventario, id_producto, nuevo_precio):
    """UPDATE: Cambia el precio de un producto específico."""
    for prod in inventario:
        if prod["id"] == id_producto:
            precio_anterior = prod["precio"]
            prod["precio"] = nuevo_precio
            print(f" Precio de '{prod['nombre']}' actualizado: ${precio_anterior} ➔ ${nuevo_precio}")
            return
    print(f"❌ No se encontró ningún producto con ID: {id_producto}")

def ajustar_stock(inventario, id_producto, nuevo_stock):
    """UPDATE: Actualiza la cantidad disponible en stock."""
    for prod in inventario:
        if prod["id"] == id_producto:
            prod["stock"] = nuevo_stock
            print(f" Stock de '{prod['nombre']}' ajustado a {nuevo_stock} uds.")
            return
    print(f" No se encontró ningún producto con ID: {id_producto}")