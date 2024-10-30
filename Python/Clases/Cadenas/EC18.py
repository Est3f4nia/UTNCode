# Escribir un programa que lea dos números enteros, X e Y. Imprimir todos los números entre X e Y que, 
# dividiéndolo por 5, el resto sea igual a 2 o 3.

num1 = int(input())
num2 = int(input())

if num1 > num2:
    dim = (num1 - num2) - 1
    inicio = num2 + 1
else:
    dim = (num2 - num1) - 1
    inicio = num1 + 1

nums = [0] * dim
for i in range(dim):
    nums[i] = inicio    
    inicio += 1
    
    div = nums[i] % 5
    if div >= 2 and div <= 3:
        print(nums[i])
