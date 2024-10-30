edades = []

edad = 0
cont = 0
while edad != -1:
    edad = int(input())
    edades.append(edad)
    cont += 1
print(edades)

stredad = str(edades)
edades_encontradas = []
cont_edades = 0
for i in range(len(edades)):
    if edades[i] in stredad and edades[i] not in edades_encontradas:
        vocales_encontradas.append(edades[i])
        cont_edades += 1

print(cant_edad1)
print(cant_edades)

