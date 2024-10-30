# Escribir un algoritmo que permita obtener el número de elementos positivos,
# negativos, nulos, mayores a 250, iguales a 19 e inferiores a 90 de una matriz de
# 50x50 componentes.

matriz = [[0 for i in range(2)] for j in range(2)]

positivos = 0
negativos = 0
nulos = 0
mas250 = 0
mas19 = 0
menos90 = 0

for i in range(2):
    for j in range(2):
        elem = float(input("Ingrese un número: "))
        matriz[i][j] = elem

        if elem > 0:
            positivos += 1
        if elem < 0:
            negativos += 1
        if elem == 0:
            nulos += 1
        if elem > 250:
            mas250 += 1
        if elem > 19:
            mas19 += 1
        if elem < 90:
            menos90 += 1

print("Elementos positivos:", positivos)
print("Elementos negativos:", negativos)
print("Elementos nulos:", nulos)
print("Elementos mayores a 250:", mas250)
print("Elementos mayores a 19:", mas19)
print("Elementos menores a 90:", menos90)