# Escribir una función que reciba como parámetros un vector de números reales y su longitud, y devuelva al máximo valor contenido en él.
def max_max_vector(vector):
    max = 0
    for i in vector:
        if i > max:
            max = i
    print("El elemento máximo fue:", max)

def max_vector(long):
    vector = [0] * long

    cont = 0
    while cont < long:
        print("Elemento ", cont, sep = "")
        elem = float(input("> "))
        vector[cont] = elem
        cont += 1
    if cont == long:
        max_max_vector(vector)

long = int(input("Longitud del vector: "))
max_vector(long)