alm = [[0 for i in range(5)] for j in range(5)]

coordX = 0
coordY = 0
suma = 0

while coordX != -1:
    coordX = int(input())
    if coordX != -1:
        coordY = int(input())
        cant_art = int(input())
        alm[coordX][coordY] += cant_art

        suma += cant_art

i_max = 0
j_max = 0

for i in range(5):
    for j in range(5):
        if alm[i][j] > alm[i_max][j_max]:
            i_max = i
            j_max = j

print("Total de artículos en el almacén:", suma)
print("Casilla con mayor cantidad: (", i_max, ", ", j_max, ") con ", alm[i_max][j_max], " artículos", sep="")
