# leer.py

def listar_productos(inventario):
    """READ: Muestra la lista completa de productos."""
    print("\n--- INVENTARIO DE PRODUCTOS ---")
    if not inventario:
        print("El inventario está vacío.")
        return
    
    for prod in inventario:
        print(f"ID: {prod['id']} | Nombre: {prod['nombre']} | Precio: ${prod['precio']} | Stock: {prod['stock']} uds.")

def obtener_resumen(inventario):
    """READ: Muestra métricas generales del inventario."""
    total_articulos = sum(prod["stock"] for prod in inventario)
    valor_total = sum(prod["precio"] * prod["stock"] for prod in inventario)
    print(f"\nTotal de productos registrados: {len(inventario)}")
    print(f"Unidades totales en stock: {total_articulos}")
    print(f"Valor total del inventario: ${valor_total:.2f}")