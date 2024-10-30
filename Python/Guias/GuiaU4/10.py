# Leer un número positivo, calcular su cuadrado y su cubo. Imprimir los resultados.

num = float(input())

x = num % 1
if x != 0:
    num = num
else:
    num = round(num)

total = num ** 2
total = round(total, 2)

total2 = num ** 3
total2 = round(total2, 2)

print(num, " ^2 = ", total, sep = "")
print(num, " ^3 = ", total2, sep = "")