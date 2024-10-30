# Escriba una función que reciba un valor de temperatura en precisión real, y la escala de temperaturas de destino, 
# y realice la conversión paramétrica del valor.
def conv_temp(valor, unidad, unidad_conv):
    if unidad == 1:
        if unidad_conv == 1:
            total = unidad
        elif unidad_conv == 2:
            total = (unidad * 1.8) + 32
        elif unidad_conv == 3:
            total = valor + 273
    if unidad == 2:
        if unidad_conv == 2:
            total = unidad
        elif unidad_conv == 1:
            total = (valor * (-17.22))
        elif unidad_conv == 3:
            total = valor * 255.93
    if unidad == 3:
        if unidad_conv == 3:
            total = unidad
        elif unidad_conv == 2:
            total = valor * (-457.87)
        elif unidad_conv == 1:
            total = (valor * (-272.15))
    return total

valor = float(input("Valor numérico: "))
print("Unidad inicial", "1- Celcius", "2- Farenheit", "3- Kelvin", sep = "\n")
unidad = int(input("Opción: "))
print("Unidad a convertir", "1- Celcius", "2- Farenheit", "3- Kelvin", sep = "\n")
unidad_conv = int(input("Opción: "))
total = conv_temp(valor, unidad, unidad_conv)
print(total)