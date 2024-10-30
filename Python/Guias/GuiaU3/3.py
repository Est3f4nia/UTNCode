# Escribir una función que me permita validar si la cantidad de dígitos ingresados de un DNI son correctos.

def contar_carac(string):
    contador = 0
    for carac in string:
        contador += 1
    return contador

dni = input()
total = contar_carac(dni)

if total == 8:
    print("DNI válido.")
else:
    print("DNI inválido.")