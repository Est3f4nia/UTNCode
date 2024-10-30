# Crear una función, que ingresa una cadena como parámetro, y calcule 
# la longitud de la misma. No se permite el uso de la función interna LEN.

def contar_carac(string):
    contador = 0
    for carac in string:
        contador += 1
    return contador

string = input()
total = contar_carac(string)
print(total)