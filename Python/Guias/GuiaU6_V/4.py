# Leer un vector de enteros y sacar por pantalla primero todos los elementos introducidos en 
# posiciones pares y después todos los de posiciones impares.

dim = int(input("Dimensión del vector: "))
vector = [0] * dim

cont = 0
a = dim - 1
while cont <= a:
    elem = int(input("Elemento del vector: "))
    vector[cont] = elem
    cont += 1
print()

for i in range(0, dim, 2):
    print(vector[i], end = " ")
print()
for j in range(1, dim, 2):
    print(vector[j], end = " ")