cantidad_pasajeros = int(input())
edades = [0] * cantidad_pasajeros
nombres = [0] * cantidad_pasajeros
alturas = [0] * cantidad_pasajeros
pesos = [0] * cantidad_pasajeros
equipajes = [0] * cantidad_pasajeros
total_e = 0
eq_max = 0
nombre_eq = ""
alt_maxima = 0
nombreAM = ""
alt_minima = 0
nombreAMi = ""
peso_maximo = 0
nombrePM = ""
peso_minimo = 0
nombrePMi = ""

for i in range(cantidad_pasajeros):
    edad = int(input("Ingrese edad: "))
    nombre = input("Ingrese nombre: ")
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))
    equipaje = int(input("Cantidad de equipaje: "))

    nombres[i] = nombre
    edades[i] = edad
    alturas[i] = altura
    pesos[i] = peso
    equipajes[i] = equipaje

    total_e += equipaje

    if equipajes[i] > equipajes[eq_max]:
        eq_max = i
        nombre_eq = nombre

    if alturas[i] > alturas[alt_maxima]:
        alt_maxima = i
        nombreAM = nombre
    if alturas[i] < alturas[alt_minima]:
        alt_minima = i
        nombreAMi = nombre

    if pesos[i] > pesos[peso_maximo]:
        peso_maximo = i
        nombrePM = nombre
    if pesos[i] < pesos[peso_minimo]:
        peso_minimo = i
        nombrePMi = nombre

# Salida
print(nombres)
print(edades)
print("Altura --------------------------")
print("Nombre de altura máxima:", nombreAM)
print("Altura:", alturas[alt_maxima])
print("Nombre de altura mínima:", nombreAMi)
print("Altura:", alturas[alt_minima])
print("Peso --------------------------")
print("Nombre de peso máximo:", nombrePM)
print("Peso:", pesos[peso_maximo])
print("Nombre de peso mínima:", nombrePMi)
print("Altura:", pesos[peso_minimo])
print("Equipaje --------------------------")
print("Carga total:", total_e)
print("Nombre de equipaje máximo:", nombre_eq)
print("Cantidad:", equipajes[eq_max])