# Escribir un procedimiento, que ingresando 2 números, calcule (sus 2 posibles operaciones matemáticas): 
# sumas, restas, multiplicaciones, divisiones, potencias, raíces.

def calc_sum_res_mult_div_pot_rai(num1, num2):
    suma = num1 + num2
    resta1 = num1 - num2
    resta2 = num2 - num1
    mult = num1 * num2
    div1 = num1 / num2
    div1 = round(div1, 2)
    div2 = num2 / num1
    div2 = round(div2, 2)
    pot1 = num1 ** num2
    pot2 = num2 ** num1
    raiz1 = num1 ** (1 / num2)
    raiz1 = round(raiz1, 2)
    raiz2 = num2 ** (1 / num1)
    raiz2 = round(raiz2, 2)
    print(suma, resta1, resta2, mult, div1, div2, pot1, pot2, raiz1, raiz2, sep = "\n")

num1 = float(input())
num2 = float(input())
calc_sum_res_mult_div_pot_rai(num1, num2)