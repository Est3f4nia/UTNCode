# Escribir un programa que lea un vector de números enteros y lo modifique sumándole 
# una centena a cada elemento.

dim = int(input("Dimensión del vector: "))
vector = [0] * dim

a = dim - 1
cont = 0
while cont <= a:
    elem = int(input("Elemento del vector: "))
    vector[cont] = elem
    cont += 1

suma = 0
for i in vector:
    suma = i + 100
    print("Suma de elementos: ", suma)
    suma = 0

print(vector)