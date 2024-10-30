# Llenar un vector
cont = 0
a = dim - 1
while cont <= a:
    elem = int(input())
    vector[cont] = elem
    cont += 1

# Modificar salida del vector
for i in range(a):
    print(vector[i], end = " | ")
print(vector[a])

# Máximo y mínimo
min = 1000000000000
max = 0
for i in vector:
    if max < i:
        max = i
    if min > i:
        min = i

# Imprimir posiciones pares
for i in range(0, dim, 2):
    print(vector[i])

# Imprimir posiciones impares
for j in range(1, dim, 2):
    print(vector[j])

# Imprimir elementos pares
for i in range(dim):
    if vector[i] % 2 == 0:
        print(vector[i], end=" ")

# Imprimir elementos impares
for i in range(dim):
    if vector[i] % 2 != 0:
        print(vector[i], end=" ")