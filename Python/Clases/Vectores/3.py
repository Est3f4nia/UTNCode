# En realidad, el ejercicio era con 3 ciclos.

cant_alumnos = int(input("Ingrese la cantidad de alumnos: "))

notas_teorico = [0] * cant_alumnos
notas_practico = [0] * cant_alumnos
notas_finales = [0] * cant_alumnos

nota_teorico = 0
nota_practico = 0
nota_final = 0
contador = 0

while cant_alumnos != 0:
    nota_teorico = float(input("Puntuación del examen teórico: "))
    notas_teorico[contador] = nota_teorico

    nota_practico = float(input("Puntuación del examen práctico: "))
    notas_practico[contador] = nota_practico

    nota_final = (nota_practico + nota_teorico) / 2
    nota_final = round(nota_final)
    notas_finales[contador] = nota_final

    cant_alumnos = cant_alumnos - 1
    contador = contador + 1

max = 0

for i in notas_finales:
    print(i, end = " | ")
    if i > max:
        max = i
print("")
print("La nota máxima fue: ", max)
