# crear.py

def agregar_producto(inventario, id_producto, nombre, precio, stock):
    """CREATE: Agrega un nuevo producto al inventario."""
    producto = {
        "id": id_producto,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    inventario.append(producto)
    print(f" Producto '{nombre}' añadido con éxito.")