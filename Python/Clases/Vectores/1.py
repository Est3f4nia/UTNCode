# Código visto en clase
cantidad_pasajeros = int(input())
edades = [0] * cantidad_pasajeros
nombres = [0] * cantidad_pasajeros
suma_edades = 0

for vuelta in range(cantidad_pasajeros):
    edad = int(input("Ingrese edad: "))
    nombre = input("Ingrese nombre: ")
    edades[vuelta] = edad
    nombres[vuelta] = nombre
    suma_edades += edad

# Comprobación de vectores
print(edades)
print(nombres)

promedio = suma_edades / cantidad_pasajeros

supera_promedio = 0
iguala_promedio = 0
menor_promedio = 0
mas_de_70 = 0
menos_de_12 = 0
pares = 0
impares = 0
pos_maximo = 0
pos_minimo = 0

for i in range(cantidad_pasajeros):
    if edades[i] > promedio:
        supera_promedio += 1
    if edades[i] < promedio:
        menor_promedio += 1
    if edades[i] == promedio:
        iguala_promedio += 1
    
    if edades[i] > 70:
        mas_de_70 += 1
    if edades[i] < 12:
        menos_de_12 += 1
    
    if edades[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if edades[i] > edades[pos_maximo]:
        pos_maximo = i
        
    if edades[i] < edades[pos_minimo]:
        pos_minimo = i
    
print("Promedio: ", promedio)
print("Superan el promedio: ", supera_promedio)
print("Iguala al promedio: ", iguala_promedio)
print("Menor al promedio: ", menor_promedio)
print("Más de 70: ", mas_de_70)
print("Menor de 12: ", menos_de_12)
print('Edades pares: ', pares)
print("Edades impares: ", impares)
print("Edad máxima: ", edades[pos_maximo])
print("Edad mínima: ", pos_maximo + 1)
print("Nombre del máximo: ", nombres[pos_maximo])
print("Nombre del mínimo: ", edades[pos_minimo])
print("Edad mínima: ", pos_minimo + 1)
print("Nombre del mínimo", nombres[pos_minimo])