def min_max_cortaconunvalor_nombre():
    max = 0
    min = 0
    nota = 187123
    contador = 0
    while nota != 0:
        print("Ingrese 3 notas")
        nota_parcial_1 = float(input())
        nota_parcial_2 = float(input())
        nota_parcial_3 = float(input())
        nota = (nota_parcial_1 + nota_parcial_2 + nota_parcial_3) / 3
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

min_max_cortaconunvalor_nombre()