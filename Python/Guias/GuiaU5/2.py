# Leer una serie de cincuenta números enteros. Informar cuantos son mayores que 100.

num = int(input("Ingrese un número entero: "))
total = num + 51
for i in range(num, total):
    if i > 100:
        print("Mayor a 100")
        print(i)
    else:
        print(i)