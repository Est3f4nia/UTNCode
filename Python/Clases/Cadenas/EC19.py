# No toma números ni carácteres especiales

cadena = input()
result = ""

for i in range(len(cadena)):
    if cadena[i] == "*":
        result = result + " "

    if cadena[i].isupper():
        result = result + cadena[i].upper()
        
    if cadena[i].islower():
        result = result + cadena[i].lower()
    
    if cadena[i] == "." and cadena[i + 1] == "-":
        result = result + ""
        if cadena[i+1] == "-":
            result = result + "-"
    
    # Está mal, pero no tan mal
    if cadena[i] == "1":
        result = result + cadena[i]
    if cadena[i] == "?":
        result = result + cadena[i]

# Invertir cadena
cont = len(result)
resultt = ""
while cont != 0:
    cont -= 1
    resultt = resultt + result[cont]
print(resultt)