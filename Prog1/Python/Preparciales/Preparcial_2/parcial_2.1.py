total_kg = [0] * 10

suma = 0
for i in range(10):
    cant_kg = int(input())
    total_kg[i] = cant_kg
    
    suma = suma + cant_kg

promedio = suma / 10

kg_max = total_kg[0]
cont_max = 0

for j in range(10):
    if total_kg[j] > kg_max:
        kg_max = total_kg[j]
        cont_max = j

print("Total de mineral extraído:", suma, "kg")
print("Promedio de extracción por turno:", promedio, "kg")
print("Mayor extracción:", kg_max, "kg en el turno", cont_max + 1)
