# Escribir un programa que declare un vector de 10 números enteros, pida al usuario cada uno de sus Componentes y luego:
# Los escriba por pantalla.
# Los escriba en orden inverso.
# Muestre por pantalla la suma y la media.

vector = [0] * 10

cont = 0
while cont <= 9:
    elem = int(input("Elemento del vector: "))
    vector[cont] = elem
    cont += 1

print("----------------------------------------")
print(vector)

# Vector inverso
print("[", vector[9], sep = "", end = ", ")
for i in range(8, 0, -1):
    print(vector[i], end = ", ")
print(vector[0], end = "]")
print()

suma = 0
for k in vector:
    suma = suma + k
print("Suma de elementos:", suma)
prom = suma / 10
print("Promedio:", prom)