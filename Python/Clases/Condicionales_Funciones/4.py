def min_max_cortaconunvalor():
    # Modificar contador y condiciones.
    contador = 0
    maxi = 0
    mini = 0
    nota = float(input())
    nombre = input()
    while nota != 0:
        if maxi < nota or contador == 0:
            maxi = nota
            nombre_maximo = nombre
        if mini > nota or contador == 0:
            mini = nota
            nombre_minimo = nombre
        nota = float(input())
        nombre = input()
        contador =+ 1
    print("La nota maxima fué un", maxi, "obtenida por", nombre_maximo)

min_max_cortaconunvalor()