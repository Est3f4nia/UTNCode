# Leer dos números reales, calcular e imprimir los dos posibles cocientes entre ellos.

num1 = float(input("Inserte un número: "))
num2 = float(input("Inserte otro número: "))

div1 = (num1 / num2)
div2 = (num2 / num1)
print(div1, div2, sep="\n")