campo = [[50 for i in range(7)] for i in range(7)] # usamos 50 como valor inicial

fila = 0
while fila != -1: # corte en -1
    fila = int(input())
    if fila != -1:
        columna = int(input())
        humedad = int(input())
        campo[fila][columna] = humedad # acceso aleatorio

print(campo)

suma = 0

for i in range(7):
    for j in range(7):
        suma += campo[i][j]

promedio = suma / 49

i_max = 0
j_max = 0
contador_mayor_promedio = 0

for i in range(7):
    for j in range(7):
        if campo[i][j] < campo[i_max][j_max]:
            i_max = i
            j_max = i
        if campo[i][j] < promedio:
            contador_mayor_promedio += 1

print("Promedio de humedad en el campo:", promedio, "%")
print("Parcela con menor humedad: (", i_max, ", ", j_max, ") con ", campo[i_max][j_max], "%", sep="")
print("Cantidad de parcelas con humedad por debajo del promedio:", contador_mayor_promedio)
