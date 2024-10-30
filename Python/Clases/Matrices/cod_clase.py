cant_notas = int(input("Cantidad de notas: "))
cant_alumnos = int(input("Cantidad de alumnos: "))
notas = [[0 for i in range(cant_notas)] for j in range(cant_alumnos)]

for i in range(cant_alumnos):
    for j in range(cant_notas):
        print("Ingrese la nota #", j + 1, "del alumno #", i + 1)
        nota = int(input("> "))
        notas[i][j] = round(nota)

# Imprimir como tabla
for i in range(cant_alumnos):
	print("| ", end = "")
	for j in range(cant_notas):
		print(notas[i][j], end = " | ")
	print()