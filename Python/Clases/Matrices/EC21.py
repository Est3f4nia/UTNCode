dim = int(input(""))
matriz = [[0 for i in range(dim)] for j in range(dim)]

opcion = int(input())

if opcion == 1:
    for i in range(dim):
        matriz[i][i] = 1

if opcion == 2:
    for i in range(dim):
        matriz[i][(dim - 1) - i] = 1

if opcion == 3:
    cont = (dim - 1)
    cont2 = 0
    for i in range(dim):
        matriz[i][cont] = 1
        matriz[i][cont2] = 1
        cont -= 1
        cont += 1

if opcion == 4:
    cont = (dim - 1)
    cont2 = 0
    for i in range(dim):
        matriz[cont][i] = 1
        matriz[cont2][i] = 1

if opcion == 5:
    cont = (dim - 1)
    cont2 = 0
    for i in range(dim):
        matriz[cont][i] = 1
        matriz[cont2][i] = 1
        matriz[i][cont] = 1
        matriz[i][cont2] = 1
        cont -= 1
        cont += 1

if opcion == 6:
    cont = (dim - 1)
    cont2 = 0
    for i in range(dim):
        matriz[cont - int((dim/2))][i] = 1
        matriz[i][cont - int((dim/2))] = 1
        cont -= 1
        cont += 1

if opcion == 7:
    cont = (dim - 1)
    cont2 = 0
    for i in range(dim):
        matriz[cont][i] = 1
        matriz[cont2][i] = 1
        matriz[i][cont] = 1
        matriz[i][cont2] = 1
        matriz[cont - int((dim/2))][i] = 1
        matriz[i][cont - int((dim/2))] = 1
        cont -= 1
        cont += 1
        matriz[i][(dim - 1) - i] = 1
        matriz[i][i] = 1

for i in range(dim):
	for j in range(dim):
		print(matriz[i][j], end = "")
	print()