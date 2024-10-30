# entrada = input()
entrada = "Dh*UUoJlaHDG#SDcSADuEASrSADAsASDoQWE" # Hola curso
resultado = ""

for i in range(len(entrada)):
    if entrada[i].islower():
        if entrada[i+1] == "*":
            resultado = resultado + entrada[i].upper()
        else:
            resultado = resultado + entrada[i]
    if entrada[i] == "#":
        resultado = resultado + " "
print(entrada)
print(resultado)