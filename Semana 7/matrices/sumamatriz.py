"""Leer 2 matrices 3x3 y sumarlas"""
matriz1 = []
matriz2 = []
matriz3 = []

# Leer la primera matriz
for i in range(3):
    fila = []
    for j in range(3):
        elemento = int(input(f"Ingrese el elemento [{i}][{j}] de la primera matriz: "))
        fila.append(elemento)
    matriz1.append(fila)

# Leer la segunda matriz
for i in range(3):
    fila = []
    for j in range(3):
        elemento = int(input(f"Ingrese el elemento [{i}][{j}] de la segunda matriz: "))
        fila.append(elemento)
    matriz2.append(fila)

# Sumar las matrices
for i in range(3):
    fila = []
    for j in range(3):
        fila.append(matriz1[i][j] + matriz2[i][j])
    matriz3.append(fila)

# Mostrar el resultado
print("La suma de las matrices es:")
for fila in matriz3:
    print(fila)