dimension = int(input())

matriz = [[0 for i in range(dimension)] for j in range(dimension)]

for i in range(dimension):
    matriz[0][i] = int(input())

for i in range(1, dimension):
    for j in range(dimension):
        
        if j < dimension - 1:
            matriz[i][j] = matriz[i - 1][j] + matriz[i - 1][j + 1]
        if j == dimension - 1:  # Para la última columna
            matriz[i][j] = matriz[i - 1][j] + matriz[i - 1][0]
        


for i in range(dimension):
	print("| ", end = "")
	for j in range(dimension):
		print(matriz[i][j], end = " | ")
	print()

suma_diag = 0
for i in range(dimension):
    suma_diag += matriz[i][i]

print("Suma de valores:", suma_diag)