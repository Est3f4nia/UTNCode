# Escribir un programa solicite al usuario 100 valores enteros y los almacene en un vector.
# Posteriormente, debe calcular el valor máximo, mínimo y la media.

vector = [0] * 100

cont = 0
while cont <= 99:
    ent = int(input('Elemento del vector: '))
    vector[cont] = ent
    cont += 1

min = 1000000000000
max = 0
for i in vector:
    if max < i:
        max = i
    if min > i:
        min = i

suma = 0
for j in vector:
    suma = suma + j
prom = suma / 100

print("Valor máximo:", max)
print("Valor mínimo:", min)
print("Promedio:", prom)