#leer una cadena de texto y buscar una palabra o texto

def buscar(cadena, valor):
    posicion = cadena.find(valor)
    if posicion >= 0:
        return f"Se encontró el valor buscado"
    else:
        return f"No se encuentra el valor buscado"

cadena = input("Dime una frase. ")
valor = input("Dime el dato a buscarr: ")

print(buscar(cadena, valor))