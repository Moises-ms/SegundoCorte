# main.py
import crear
import leer
import actualizar
import eliminar

# Base de datos local representada como una lista de diccionarios
inventario = []

# 1. CREATE: Registrar productos
print("--- 1. REGISTRANDO PRODUCTOS ---")
crear.agregar_producto(inventario, 101, "Laptop", 850.00, 10)
crear.agregar_producto(inventario, 102, "Mouse", 25.00, 50)
crear.agregar_producto(inventario, 103, "Teclado", 45.00, 0) # Producto sin stock

# 2. READ: Consultar inventario
leer.listar_productos(inventario)
leer.obtener_resumen(inventario)

# 3. UPDATE: Modificar datos
print("\n--- 3. ACTUALIZANDO DATOS ---")
actualizar.modificar_precio(inventario, 101, 799.99)
actualizar.ajustar_stock(inventario, 102, 45)

leer.listar_productos(inventario)

# 4. DELETE: Eliminar elementos
print("\n--- 4. ELIMINANDO REGISTROS ---")
# Eliminar por ID
eliminar.eliminar_por_id(inventario, 102)

# Eliminar productos sin stock
eliminar.eliminar_sin_stock(inventario)

# Estado final
leer.listar_productos(inventario)
leer.obtener_resumen(inventario)