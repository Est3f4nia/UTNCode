# Leer un vector de enteros y sacar por pantalla primero todos los elementos pares y 
# después todos los impares.

dim = int(input("Dimensión del vector: "))
vector = [0] * dim

cont = 0
a = dim - 1
while cont <= a:
    elem = int(input("Elemento del vector: "))
    vector[cont] = elem
    cont += 1

print("\nElementos pares:")
for i in range(dim):
    if vector[i] % 2 == 0:
        print(vector[i], end=" ")
print("\nElementos impares:")
for i in range(dim):
    if vector[i] % 2 != 0:
        print(vector[i], end=" ")