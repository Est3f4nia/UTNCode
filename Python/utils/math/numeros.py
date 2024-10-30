def num_par_impar (num):
    if num % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

def juego_closer(num1, num2, num_adivinar):
    if num_1 and num_2 == num_adivinar:
        print("Empate")
    elif num_1 > num_adivinar:
        if num_1 - num_adivinar > num_2 - num_adivinar:
            print("Ganador Jugador 2")
        else:
            print("Ganador Jugador 1")
    elif num_2 > num_adivinar:
        if num_2 - num_adivinar > num_1 - num_adivinar:
            print("Ganador Jugador 1")
        else:
            print("Ganador Jugador 2")
    elif num_adivinar - num_1 > num_adivinar - num_2:
        print("Ganador Jugador 2")
    elif num_adivinar - num_2 > num_adivinar - num_1:
        print("Ganador Jugador 1")
    #if num_1 and num_2 == num_adivinar:
        #print("Empate")
    #elif num_1 - num_adivinar == num_2 - num_adivinar or num_2 - num_adivinar == num_1 - num_adivinar:
        #print("Empate")

def min_max():
    maxi = 0
    mini = 0
    n = int(input())
    for contador in range(n):
        nota = float(input())
        if maxi < nota or contador == 0:
            maxi = nota
        if mini > nota or contador == 0 and nota:
            mini = nota
    print(mini)
    print(maxi)

def min_max_cortaconunvalor():
    # Modificar contador y condiciones.
    contador = 0
    maxi = 0
    mini = 0
    nota = float(input())
    while nota != 0:
        if maxi < nota or contador == 0:
            maxi = nota
        if mini > nota or contador == 0:
            mini = nota
        nota = float(input())
        contador =+ 1
    print(mini)
    print(maxi)

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
    print("La nota máxima fue un", max,"obtenida por", nombre_maximo)
    print("La nota mínima fue un", min,"obtenida por", nombre_minimo)

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
    print("La nota máxima fue un", max,"obtenida por", nombre_maximo)
    print("La nota mínima fue un", min,"obtenida por", nombre_minimo)

def mostrar_num(num):
    # num = int(input("Ingrese un entero: "))
    # num = num + 1
    for i in range(1, num):
        print(i)

def calc_factorial(num):
    fac = 1
    x = 1
    num = num - 1
    for i in range(num):
        x = x + 1
        result = fac * x
        fac = result
        print(result)
    return result

def compr_float_redondearMas1(valor):
    # Valor como float
    x = int(valor)
    if valor - x != 0:
        valor = x + 1
        print(valor)

def es_entero(num):
    x = num % 1
    if x != 0:
        return False
    else:
        return True

