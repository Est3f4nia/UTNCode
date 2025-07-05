satelites = []

nombre = ""
while nombre != "FIN":
    nombre = input()
    if nombre != "FIN":      
        orbita = int(input()) - 1
        estado = input()

        satelites.append({
            "nombre": nombre,
            "orbita": orbita,
            "estado": estado
        })

if nombre == "FIN":
    activos = [0] * 5
    inactivos = [0] * 5

    for satelite in satelites:
        if satelite["estado"] == "activo":
            activos[satelite["orbita"]] += 1
        
        if satelite["estado"] == "inactivo":
            inactivos[satelite["orbita"]] += 1

max_inactivos = inactivos[0]
max_activos = activos[0]
for i in range(5):
    if inactivos[i] > max_inactivos:
        max_inactivos = i
    if activos[i] > max_activos:
        max_activos = i

n_activos = ""
cont = 0
for satelite in satelites:
    if satelite["orbita"] == max_activos:
        n_activos += satelite["nombre"] + ", "
        cont += 1

print("Cantidad total de satélites registrados:", len(satelites))
print("Satélites activos por órbita:")
print("Órbita 1:", activos[0])
print("Órbita 2:", activos[1])
print("Órbita 3:", activos[2])
print("Órbita 4:", activos[3])
print("Órbita 5:", activos[4])
print("Órbita con más satélites inactivos:", max_inactivos)
print("Satélites activos de la órbita con más actividad (órbita ", max_activos, "): ", n_activos, sep="", end="")
