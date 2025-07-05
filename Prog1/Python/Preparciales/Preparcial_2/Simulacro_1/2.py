mensaje = "Hola a todos, les informo que el viernes 5/11/2024 habrá una reunión de gabinete en la oficina #2 a las 11:00 am. Llegar puntuales"
resultado = ""

# Invertir el mensaje

numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for caracter in mensaje:
    if caracter in numeros:
        resultado += caracter + "-"
    elif caracter == ' ':
        resultado += "#-"
    elif caracter == '.':
        resultado += "*-"
    else:
        resultado += caracter

resultado_final = ""
for i in range(len(resultado)):
    if i % 3 == 0:
        resultado_final += " "
    elif i % 5 == 0:
        resultado_final += "."
    resultado_final += resultado[i]

mensajeI = resultado_final[::-1]

print(mensajeI)