# Leer un número e informar si es entero.

def es_entero(num):
    x = num % 1
    if x != 0:
        return False
    else:
        return True

num = float(input())
total = es_entero(num)

if total == True:
    print("Es entero.")
else:
    print("Es decimal.")
