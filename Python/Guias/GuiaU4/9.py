# Leer un número, calcular el cuadrado imprimiéndolo junto con el número leído.

num = float(input())

x = num % 1
if x != 0:
    num = num
else:
    num = round(num)
total = num ** 2
total = round(total, 2)

print(num, " ^2 = ", total, sep = "")