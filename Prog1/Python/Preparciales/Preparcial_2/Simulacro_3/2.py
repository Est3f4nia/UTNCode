mensaje = input() #le pido al usuario el mensaje a encriptar
mitad1 = len(mensaje) // 2 #division entera entre 2 para mitad1 exacta, dejando uno de mas del lado derecho
mensaje_encr = "" #inicializo mensaje encriptado como string vacio
for i in range(mitad1):
    # controlo el caracter del lado izquierdo
    if mensaje[i] == "a":
        mensaje_encr += "@"
    elif mensaje[i] == "e":
        mensaje_encr += "$"
    elif mensaje[i] == "i":
        mensaje_encr += "&"
    elif mensaje[i] == "o":
        mensaje_encr += "*"
    elif mensaje[i] == "u":
        mensaje_encr += "#"
    elif mensaje[i] == "@":
        mensaje_encr += "/@"
    elif mensaje[i] == "$":
        mensaje_encr += "/#"
    elif mensaje[i] == "&":
        mensaje_encr += "/&"
    elif mensaje[i] == "*":
        mensaje_encr += "/*"
    elif mensaje[i] == "#":
        mensaje_encr += "/#"
    elif mensaje[i] == "/":
        mensaje_encr += "//"
    else:
        mensaje_encr += mensaje[i] # si no es ninguna de las anteriores, agrego el caracter original
    
    #reptiro el proceso para el caracter en lado derecho
    if mensaje[mitad1+i] == "a":
        mensaje_encr += "@"
    elif mensaje[mitad1+i] == "e":
        mensaje_encr += "$"
    elif mensaje[mitad1+i] == "i":
        mensaje_encr += "&"
    elif mensaje[mitad1+i] == "o":
        mensaje_encr += "*"
    elif mensaje[mitad1+i] == "u":
        mensaje_encr += "#"
    elif mensaje[mitad1+i] == "@":
        mensaje_encr += "/@"
    elif mensaje[mitad1+i] == "$":
        mensaje_encr += "/#"
    elif mensaje[mitad1+i] == "&":
        mensaje_encr += "/&"
    elif mensaje[mitad1+i] == "*":
        mensaje_encr += "/*"
    elif mensaje[mitad1+i] == "#":
        mensaje_encr += "/#"
    elif mensaje[mitad1+i] == "/":
        mensaje_encr += "//"
    else:
        mensaje_encr += mensaje[mitad1+i]

if len(mensaje) % 2 != 0: #si la longitud del mensaje es impar
    #reptiro el proceso para el caracter en lado derecho
    if mensaje[len(mensaje)-1] == "a":
        mensaje_encr += "@"
    elif mensaje[len(mensaje)-1] == "e":
        mensaje_encr += "$"
    elif mensaje[len(mensaje)-1] == "i":
        mensaje_encr += "&"
    elif mensaje[len(mensaje)-1] == "o":
        mensaje_encr += "*"
    elif mensaje[len(mensaje)-1] == "u":
        mensaje_encr += "#"
    elif mensaje[len(mensaje)-1] == "@":
        mensaje_encr += "/@"
    elif mensaje[len(mensaje)-1] == "$":
        mensaje_encr += "/#"
    elif mensaje[len(mensaje)-1] == "&":
        mensaje_encr += "/&"
    elif mensaje[len(mensaje)-1] == "*":
        mensaje_encr += "/*"
    elif mensaje[len(mensaje)-1] == "#":
        mensaje_encr += "/#"
    elif mensaje[len(mensaje)-1] == "/":
        mensaje_encr += "//"
    else:
        mensaje_encr += mensaje[len(mensaje)-1]

print(mensaje_encr)
