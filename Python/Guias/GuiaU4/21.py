# Ingresar por teclado los precios correspondientes a cinco artículos y las cantidades vendidas 
# de cada uno de ellos. Calcular e imprimir el importe total de ventas de cada uno y un importe total 
# de lo vendido.

precio = 0
art = 0
total = 0

while art <= 4:
    cant = int(input())
    precio = float(input())
    total = total + (cant * precio)
    art = art + 1

print(total)