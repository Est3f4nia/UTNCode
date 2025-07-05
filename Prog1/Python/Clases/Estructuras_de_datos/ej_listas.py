mediciones = []
entrada = 0 # inicializamos entrada
suma = 0

while entrada != -1: # corte en -1
    entrada = int(input()) 
    if entrada != -1:
        mediciones.append(entrada) # almacenar datos
        suma = suma + entrada

print(mediciones)

promedio = suma / len(mediciones)

i_max = 0
contador_mayor_promedio = 0

for i in range(len(mediciones)):
    if mediciones[i] > mediciones[i_max]:
        i_max = i
    if mediciones[i] > promedio:
        contador_mayor_promedio += 1

print("Total de energía generada:", suma,"kWh")
print("Promedio de energía por intervalo:", promedio, "kWh")
print("Mayor generación:", mediciones[i_max], "kWh en el intervalo", i_max + 1 )
print("Intervalos con generación superior al promedio:", contador_mayor_promedio)
