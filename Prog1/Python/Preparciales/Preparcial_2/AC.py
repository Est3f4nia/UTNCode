aeropuertos = []

cant_pasajeros = 0
while cant_pasajeros != -1:
    nombre_aeropuerto = input("Aeropuerto: ")
    cant_pasajeros = int(input("Cantidad de pasajeros: "))
    if cant_pasajeros != -1: #evita que se agregen los datos de corte
        aeropuertos.append({
            "nombre": nombre_aeropuerto,
            "pasajeros": cant_pasajeros
        })

max = aeropuertos[0]
min = aeropuertos[0]
for aeropuerto in aeropuertos:
    if aeropuerto["pasajeros"] > max["pasajeros"]:
        max = aeropuerto

    if aeropuerto["pasajeros"] < min["pasajeros"]:
        min = aeropuerto

print("El que más pasajeros recibió fue", max["nombre"], "con", max["pasajeros"], "pasajeros.")
print("El que menos pasajeros recibió fue", min["nombre"], "con", min["pasajeros"], "pasajeros.")
