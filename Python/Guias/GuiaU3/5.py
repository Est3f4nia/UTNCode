# Escribir un procedimiento que calcule el factorial de un número natural pasado como parámetro, 
# en forma iterativa. Realizar todas las validaciones que considere necesarias.

def calc_factorial(num):
    fac = 1
    x = 1
    num = num - 1
    for i in range(num):
        x = x + 1
        result = fac * x
        fac = result
        print(result)
    return result

num = int(input())
total = calc_factorial(num)
print(total)