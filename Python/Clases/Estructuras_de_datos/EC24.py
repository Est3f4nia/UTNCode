cad1 = input()
cad2 = input()

print("1. Cadena 1 completa: ", end = "")
for carac in cad1:
    print(carac, end = "")
print()

print("2. Cadena 2 completa: ", end = "")
for carac2 in cad2:
    print(carac2, end = "")
print()

print("3. Subcadena de Cadena 1 (índices 1 a 5): ", end = "")
for i in range(1, len(cad1)):
    if i < 5:
        print(cad1[i], end = "")
print()

print("4. Subcadena de Cadena 2 (cada segundo carácter): ", end = "")
for j in range(0, len(cad2), 2):
    print(cad2[j], end = "")
print()

print("5. Subcadena de Cadena 1 (desde el índice 2): ", end = "")
for k in range(2, len(cad1)):
    print(cad1[k], end = "")
print()

print("6. Subcadena de Cadena 2 (desde el inicio hasta el índice 4): ", end = "")
for l in range(len(cad2)):
    if l < 4:
        print(cad2[l], end = "")
print()

str_mitad = ""
for m in range(len(cad2)):
    if m == 0:
        primer = cad1[m]

    mitad = len(cad2) // 2
    if m < mitad:
        str_mitad += cad2[m]

ultimo = cad1[len(cad1) - 1]
concatenacion = primer + str_mitad + ultimo
print("7. Concatenación:", concatenacion)

cont = len(cad1)
result = ""
while cont != 0:
    cont -= 1
    result = result + cad1[cont]
print("8. Cadena 1 revertida:", result)

vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
vocales_encontradas = []
cont_vocales = 0
for n in range(len(cad2)):
    if cad2[n] in vocales and cad2[n] not in vocales_encontradas:
        vocales_encontradas.append(cad2[n])
        cont_vocales += 1
print("9. Cantidad de vocales en Cadena 2:", cont_vocales)

print("10. Cadena 1 en mayúsculas:", cad1.upper())