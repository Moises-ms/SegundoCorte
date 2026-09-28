filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        elemento = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        fila.append(elemento)
    matriz.append(fila)

print("La matriz ingresada es:")
for fila in matriz:
    print(fila)