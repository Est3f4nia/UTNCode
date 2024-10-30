# Leer tres números, calcular e imprimir los seis posibles cocientes.
# No es el mejor código, pero anda :)

def calc_cociente(num1, num2, num3):
    coc1 = num1 / num2
    coc2 = num1 / num3
    coc3 = num2 / num3
    coc4 = num1 / num1
    coc5 = num2 / num2
    coc6 = num3 / num3
    print(coc1, coc2, coc3, coc4, coc4, coc5, coc6, sep="\n")

num1 = float(input("Inserte un número: "))
num2 = float(input("Inserte otro número: "))
num3 = float(input("Inserte un tercer número: "))
calc_cociente(num1, num2, num3)