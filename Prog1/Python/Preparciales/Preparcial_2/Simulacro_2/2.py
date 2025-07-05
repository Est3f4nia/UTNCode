def longitud(cadena):
    contador = 0
    for i in cadena:
        contador += 1
    return contador

def generar_nombre_especie():
    progenitor1 = input("")
    progenitor2 = input("")

    parte1 = progenitor1[:3]
    longitud_progenitor2 = longitud(progenitor2)
    mitad_progenitor2 = longitud_progenitor2 // 2

    if longitud_progenitor2 % 2 == 0:
        parte2 = progenitor2[mitad_progenitor2:]
    else:
        parte2 = progenitor2[mitad_progenitor2 + 1:]

    parte3 = progenitor1[-1]
    nuevo_nombre = parte1 + parte2 + parte3

    if nuevo_nombre[-1] == 's':
        nuevo_nombre = nuevo_nombre[:-1] + "son"

    nuevo_nombre = nuevo_nombre[0].upper() + nuevo_nombre[1:].lower()
    print("Nombre de salida:", nuevo_nombre)

generar_nombre_especie()
