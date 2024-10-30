# Leer un número e imprimirlo junto con sus primeros múltiplos, 
# ejemplifique para los primeros 4 múltiplos del número ingresado.

def imprimir_multiplos(num):
    mul = 1
    mul1 = num * mul
    mul2 = num * (mul + 1)
    mul3 = num * (mul + 2)
    mul4 = num * (mul + 3)
    print(mul1, mul2, mul3, mul4, sep="\n")

num = int(input("Por favor ingrese un número entero: "))
imprimir_multiplos(num)