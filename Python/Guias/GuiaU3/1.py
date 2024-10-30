# Escribir una función que me permita calcular la edad de una persona.

def edad(year_nacimiento, year):
    edad = year - year_nacimiento
    return edad

year = int(input("Año actual: "))
year_nacimiento = int(input("Año de nacimiento: "))
total = edad(year_nacimiento, year)
print("Su edad es", total)