# Un pintor sabe que con una pintura determinada puede pintar 3,6 metros cuadrados por cada medio litro. 
# Sabiendo la altura y el largo de la pared a pintar, informar cuántos litros de pintura utilizará. 
# (Altura y Largo en metros).

# No estoy segura del cálculo, lo hice a papel y con calculadora y me dio lo mismo. Apliqué la regla de
# tres simple. 

def calc_pintura(alto, largo):
    area = alto * largo
    litro = (area * 0.5) / 3.6
    litror = round(litro, 2)
    return litror

alto = float(input("Altura (en metros): "))
largo = float(input("Largo (en metros): "))
total = calc_pintura(alto, largo)
print(total)