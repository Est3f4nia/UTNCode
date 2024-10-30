# El precio por cada llamada tiene una tarifa telefónica ingresado por el administrador en euros. 
# Si hablamos durante 5 minutos, la llamada nos cuesta 4,35 euros si el precio es 0,87 euros por minuto y 
# la llamada es realizada desde España. Halla la función que nos da el precio total de la llamada según los 
# minutos que estemos hablando, el país, y el precio ingresado por el administrador al ingresar al programa.

def precio_llamada(precio, minutos):
    total = precio * minutos
    return total

precio = 0.87
minutos = float(input("Minutos totales: "))
total = precio_llamada(precio, minutos)
print("El total a pagar es", total, "EUR")