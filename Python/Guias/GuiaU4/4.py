# Teniendo como dato el lado de un cuadrado, calcular e imprimir la superficie y perímetro.

def area_cuadrado(lado):
    area = lado ** 2
    arear = round(area, 2)
    print(f"El área del cuadrado es: {arear}")

def perimetro_cuadrado(lado):
    perimetro = lado * 4
    perimetror = round(perimetro, 2)
    print(f"El perímetro del cuadrado es: {perimetror}")

lado = float(input("Inserte la longitud de un lado del cuadrado: "))
area_cuadrado(lado)
perimetro_cuadrado(lado)