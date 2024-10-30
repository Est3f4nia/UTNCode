# Dados dos lados de un triángulo, calcular la hipotenusa mediante Pitágoras.

lado1 = float(input())
lado2 = float(input())

h = (lado1 ** 2) 
h = h + (lado2 ** 2)
h = h ** 0.5
h = round(h, 2)
print("La hipotenusa es:", h)