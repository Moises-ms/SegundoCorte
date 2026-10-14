stack = []

def push(item, capacity):
    if not is_full(capacity):
        stack.append(item)
        return "Elemento apilado..."
    return "La pila está llena..."

def isEmpty():
    return not len(stack)

def is_full(capacity):
    return len(stack) == capacity

capacity = int(input("Ingrese la capacidad de la pila: "))
while True:
    item = input("dime un valor: ")
    print(push(item, capacity)) 
    0000000000+ 