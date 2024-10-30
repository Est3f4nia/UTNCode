def contar_carac(string):
    contador = 0
    for carac in string:
        contador += 1
    return contador

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

