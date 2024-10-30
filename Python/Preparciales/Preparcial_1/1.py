max = 0
min = 0
minutos = 123
contador = 0
total_minutos = 0
while minutos != 0:
    print("Ingrese el nombre de la canción:")
    cancion = input()
    print("Ingrese la cantidad de minutos escuchados:")
    minutos = float(input())
    if minutos != 0:
        if max < minutos or contador == 0:
            max = minutos
            nombre_maximo = cancion
        total_minutos = total_minutos + minutos
    contador = contador + 1
total_canciones = contador - 1

print("La canción que más escuchaste fué: ", nombre_maximo)
print("Escuchaste esa canción por", max , "minutos")
print("El total de minutos escuchados en la temporada es de", total_minutos)
print("Esta temporada escuchaste", total_canciones, "canciones")