vector = []
vector.append(2)
vector.append(6)
vector.append(4)
print(vector)
#tamaño 
print("Tamaño", len(vector))

#mostrar el doble de cada elemento
print("Doble de cada elemento")
for i in range(len(vector)):
    if i != (len(vector) - 1):
        print(vector[i] * 2, end= ", ") #end= " " evita que se haga un salto de línea después de cada elemento
    else:
        print(f"{vector[i] * 2}.") #f-string permite formatear el texto de salida   

#añadir en la posición 1 
vector.insert(1, "Moises")
print(vector)

#añadir en la posición 0
vector.insert(0, "Juan")
print(vector)

#añadir en ela posición 0 nuevamente
vector.insert(0, "Alee")
print(vector)

#modificar la segunda posición
vector[1] = "Jorge"
print(vector)

print("Eliminar un elemento")
vector.remove("Jorge")
print(vector)

print("Eliminar por posición")
del vector[1]
print(vector)

print("Eliminar el último elemento")
vector.pop()
print(vector)   