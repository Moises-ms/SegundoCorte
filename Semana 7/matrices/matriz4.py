#Dada una matriz cuadrada, convertirla a matriz de identidad
matriz = []
matrizIdentidad = []

# Ingresar los valores de la matriz cuadrada
print("Ingrese los valores de la matriz cuadrada:")
for i in range(3):
    fila = []
    for j in range(3):
        valor = float(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

# Convertir a matriz de identidad
for i in range(3):
    fila = []
    for j in range(3):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matrizIdentidad.append(fila)

print("La matriz de identidad es:")
for fila in matrizIdentidad:
    print(fila)
