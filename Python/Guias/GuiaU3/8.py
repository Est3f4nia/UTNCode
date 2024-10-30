# Escribir un procedimiento que reciba un vector de N elementos de tipo entero, y su longitud, 
# y que lo retorne cargado con N números multiplicados por un valor constante ingresado por el usuario.

def vector(long, vector):
    cont = 0
    while cont < long:
        print("Elemento ", cont, sep = "")
        elem = int(input("> "))
        vector[cont] = elem
        cont += 1
    
    N = int(input("Valor a multiplicar: "))
    for i in range(long):
        e = i * N
        vector[i] = e
        print(vector)
    return vector

long = int(input("Longitud del vector: "))
vector = [0] * long

vector = vector(long, vector)

print(vector)