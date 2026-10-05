vector = ["j","u","a","n"]
print(type(vector))

for letra in vector:
    print(letra)

nombre = "juan"
print("*"*13)
for letra in nombre:
    print(letra)


print(len(vector))
print(len(nombre))

def convertirAMayusculas(texto):
    return f"El texto {texto} en mayúsculas es: {texto.upper()}"

def convertirAMinusculas(texto):
    return f"El texto {texto} en minúsculas es: {texto.lower()}"

def capitalizar(texto):
    return f"El texto {texto} capitalizado es: {texto.capitalize()}"

def titulo(texto):
    return f" {texto.title()}"
print(convertirAMayusculas(nombre))
print(convertirAMinusculas(nombre))
#print(convertirAMayusculas(vector)) no se puede convertir un vector a mayusculas, solo se puede convertir un string

for each in vector:
    print(convertirAMayusculas(each), end="   ")