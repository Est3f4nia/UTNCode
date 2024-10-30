# Escribir una función que reciba una matriz de valores enteros y su longitud como parámetros, 
# y retorne el promedio aritmético de los valores contenidos en él.

def prom_arit(long, vector):
    suma = 0
    for i in vector:
        suma = suma + i
    return suma / long


long = int(input("Longitud del vector: "))
vector = [0] * long

cont = 0
while cont < long:
    print("Elemento ", cont, sep = "")
    elem = int(input("> "))
    vector[cont] = elem
    cont += 1

result = prom_arit(long, vector)
print(result)