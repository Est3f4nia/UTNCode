def matriz(matriz, rango, rango2):
	matriz = [[0 for i in range(rango2)] for j in range(rango)]
	return matriz

def rellenar_m(matriz, rango, rango2):
	for i in range(rango):
		for j in range(rango2):
			elem = float(input("Ingrese un número: "))
			matriz[i][j] = elem
	return matriz

# Salidas --------------------------------------

def salida_tabla(rango, rango2, matriz):
	for i in range(rango):
		print("| ", end = "")
		for j in range(rango2):
			print(matriz[i][j], end = " | ")
		print()

# Matriz identidad
for i in range(x):
	for j in range(x):
		m_i[j][j] = 1

# Matriz inversa
for j in range(x):
    m_i[j][(x - 1) - j] = 1

# Matriz identidad + inversa
for j in range(x):
    m_i[j][j] = 2
#	m_i[j][(x - 1) - j] = 1

# Bordes laterales
cont = (dim - 1)
cont2 = 0
for i in range(dim):
	# Borde derecho
    matriz[i][cont] = 1
	# Borde izquierdo
    matriz[i][cont2] = 1
    cont -= 1
    cont += 1

# Bordes superiores
cont = (dim - 1)
cont2 = 0
for i in range(dim):
	# De abajo
    matriz[cont][i] = 1
	# De arriba
    matriz[cont2][i] = 1

# Todos los bordes
cont = (dim - 1)
cont2 = 0
for i in range(dim):
    matriz[cont][i] = 1
    matriz[cont2][i] = 1
    matriz[i][cont] = 1
    matriz[i][cont2] = 1
    cont -= 1
    cont += 1

# Salida en X
cont = (dim - 1)
cont2 = 0
for i in range(dim):
    matriz[i][cont] = 1
    matriz[i][cont2] = 1
    cont -= 1
    cont2 += 1

# Forma de +
cont = (dim - 1)
cont2 = 0
for i in range(dim):
    # Horizontal
    matriz[cont - int((dim/2))][i] = 1
    # Vertical
    matriz[i][cont - int((dim/2))] = 1
    cont -= 1
    cont += 1

# Forma de cuatro puntos centrales
# Sin bucle
    matriz[int((dim/2)) + 1][int((dim/2)) + 1] = 1
    matriz[int((dim/2)) - 1][int((dim/2)) - 1] = 1
    matriz[int((dim/2)) + 1][int((dim/2)) - 1] = 1
    matriz[int((dim/2)) - 1][int((dim/2)) + 1] = 1

# Sumar filas y columnas
for i in range(x):
    for j in range(x):
        suma_filas[i] += matriz[i][j]
        suma_columnas[j] += matriz[i][j]