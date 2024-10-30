#Area y perimetro

def cuadrado(lado):
    area = lado ** 2
    arear = round(area, 2)
    perimetro = lado * 4
    perimetror = round(perimetro, 2)
    print(f"El perímetro del cuadrado es: {perimetror}.")
    print(f"El área del cuadrado es: {arear}.")
    continuacion()

def triangulo_esc(base, altura, lado1, lado2, lado3):
    area = (base * altura) / 2
    arear = round(area, 2)
    perimetro = lado1 + lado2 + lado3
    perimetror = round(perimetro, 2)
    print(f"El perímetro del triángulo escaleno es: {perimetror}.")
    print(f"El área del triángulo escaleno es: {arear}.")
    continuacion()

def triangulo_equ(lado, base, altura):
    area = (base * altura) / 2
    arear = round(area, 2)
    perimetro = lado * 3
    perimetror = round(perimetro, 2)
    print(f"El perímetro del triángulo equilátero es: {perimetror}.")
    print(f"El área del triángulo equilátero es: {arear}.")
    continuacion()

def rectangulo(lado1, lado2):
    area = lado1 * lado2
    arear = round(area, 2)
    perimetro = (lado1 * 2) + (lado2 * 2)
    perimetror = round(perimetro, 2)
    print(f"El perímetro del rectángulo es: {perimetror}.")
    print(f"El área del rectángulo es: {arear}.")
#---------------------------------------------------------------
def hipotenusa(num1, num2):
    h = (num1 ** 2) 
    h = h + (num2 ** 2)
    h = h ** 0.5
    h = round(h, 2)
    return h