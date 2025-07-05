satelites = []

km_mar = 0
while km_mar != -1:
    nombre_satelite = input()
    km_mar = int(input())
    if km_mar != -1:
        satelites.append({
            "nombre": nombre_satelite,
            "km": km_mar
        })

suma = 0
for satelite in satelites:
    suma = suma + satelite["km"]
prom = suma / len(satelites)

encima_prom = 0
for satelite in satelites:
    if satelite["km"] > prom:
        encima_prom += 1

max = satelites[0]
for satelite in satelites:
    if satelite["km"] > max["km"]:
        max = satelite

print("Satélites por encima del promedio:", encima_prom)
print("Primer satélite con altitud máxima:", max["nombre"])
