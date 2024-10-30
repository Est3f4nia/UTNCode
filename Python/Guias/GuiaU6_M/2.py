# Rellenar una matriz de identidad de 4 por 4.
m_i = [[0 for i in range(4)] for j in range(4)]

# Matriz identidad
for i in range(4):
    for j in range(4):
        m_i[j][3-j] = 1

for i in range(4):
	print("| ", end = "")
	for j in range(4):
		print(m_i[i][j], end = " | ")
	print()