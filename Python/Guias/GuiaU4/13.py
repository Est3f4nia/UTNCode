# Dadas la base y la altura da un triángulo, calcular la superficie. 
# También conociendo uno de sus ángulos calcular los otros dos lados.

base = float(input("Base: "))
altura = float(input("Altura: "))
angulo = float(input("Ángulo: "))

area = (base * altura) / 2
print("El área es:", area)

if angulo < 180:
    r = 180 - angulo
    b = r / 2
    c = 0 + b

print(angulo)
print(b)
print(c)
suma = angulo + b + c
print(suma)