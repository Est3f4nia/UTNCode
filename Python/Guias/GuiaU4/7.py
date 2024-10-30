# Ingresar un número por teclado e imprimir el valor absoluto del número.

def valor_absoluto(num):
    if num == -num:
        num = +num
    else:
        num = -num
    return num

num = float(input())
total = valor_absoluto(num)
print(total)