# Escribir un procedimiento que ingresada una cadena, nos informe si la misma es palíndroma.

def es_palindroma(string):
    palabra_reversa = ""
    for char in string:
        palabra_reversa = char + palabra_reversa
    if palabra_reversa == string:
        result1 = print("La palabra es palíndroma.")
        return result1
    else:
        result2 = print("La palabra no es palíndroma.")
        return result2

string = input("Ingrese una palabra: ")
result = es_palindroma(string)
