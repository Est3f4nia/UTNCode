def nota_prom_nombre():
    max = 0
    min = 0
    nota = 187123
    contador = 0
    while nota != 0:
        print("Ingrese notas")
        nota_parcial = 786123
        suma_de_notas = 0
        cantidad_de_notas = 0
        while nota_parcial != 0:
            nota_parcial = float(input())
            suma_de_notas = suma_de_notas + nota_parcial
            cantidad_de_notas = cantidad_de_notas + 1
        nota = (suma_de_notas) / (cantidad_de_notas - 1)
        print("ingrese nombre")
        nombre = input()
        if nota != 0:
            if max < nota or contador == 0:
                max = nota
                nombre_maximo = nombre
            if min > nota or contador == 0:
                min = nota
                nombre_minimo = nombre
        contador = contador + 1
    print("La nota maxima fué un", max,"obtenida por", nombre_maximo)
    print(nombre_minimo, min)

min_max_cortaconunvalor()