# Leer la base y altura de un rectángulo, calcular e imprimir la superficie.

lado1 = float(input())
lado2 = float(input())

perimetro = (lado1 * 2) + (lado2 * 2)
perimetro = round(perimetro, 2)
print(f"El perímetro del rectángulo es: {perimetro}.")