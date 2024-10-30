# Leer una matriz de 3 por 3 elementos y calcular la suma de cada una de sus filas y
# columnas, dejando dichos resultados en dos vectores, uno de la suma de filas y otro
# de las columnas

def rellenar_m(rango, rango2, matriz):
	for i in range(rango):
		for j in range(rango2):
			elem = float(input("Ingrese un número: "))
			matriz[i][j] = elem
	return matriz

matriz = [[0 for i in range(3)] for j in range(3)]
mat = rellenar_m(3, 3, matriz)
suma_filas = [0] * 3
suma_columnas = [0] * 3

for i in range(3):
    for j in range(3):
        suma_filas[i] += matriz[i][j]
        suma_columnas[j] += matriz[i][j]

print("Matriz -------")
for i in range(3):
		print("| ", end = "")
		for j in range(3):
			print(matriz[i][j], end = " | ")
		print()
print("Sumas -------")
print("Filas:", suma_filas)
print("Columnas:", suma_columnas)