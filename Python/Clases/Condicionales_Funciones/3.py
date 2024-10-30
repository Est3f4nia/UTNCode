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
min_max_cortaconunvalor()