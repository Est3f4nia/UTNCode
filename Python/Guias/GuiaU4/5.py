# Si un lote de terreno tiene X metros de frente por Y metros de fondo: 
# calcular e imprimir la cantidad da metros de alambre para cercarlo. 
# (X e Y serán leídos al comenzar el programa).

def calc_perimetro (lado1, lado2):
    perimetro = lado1 + lado2
    round(perimetro, 2)
    return perimetro

lado1 = float(input("Largo del lado 1: "))
lado2 = float(input("Largo del lado 2: "))
perimetro = calc_perimetro (lado1, lado2)
print(f"La cantidad de alambre a poner es de: {perimetro} metros.")