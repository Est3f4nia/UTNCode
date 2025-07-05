cantidad_equipos = int(input("Ingrese la cantidad de equipos: "))

puntos = [0] * cantidad_equipos

while True:    
    equipo_local = int(input("Ingrese el número del equipo local (0 para terminar): "))
    
    if equipo_local == 0:
        break
    
    equipo_visitante = int(input("Ingrese el número del equipo visitante: "))
    resultado = int(input("Ingrese 1 para Ganador Local, 2 para Empate, 3 para Ganador Visitante: "))
    
    if resultado == 1:  # Ganador Local
        puntos[equipo_local - 1] += 3
    elif resultado == 2:  # Empate
        puntos[equipo_local - 1] += 1
        puntos[equipo_visitante - 1] += 1
    elif resultado == 3:  # Ganador Visitante
        puntos[equipo_visitante - 1] += 3

print("Tabla de puntos:")
for i in range(cantidad_equipos):
    print("Equipo " + str(i + 1) + ": " + str(puntos[i]) + " puntos")

max_puntos = max(puntos)
ganadores = []
for i in range(cantidad_equipos):
    if puntos[i] == max_puntos:
        ganadores.append(i + 1)

premio_total = 200000

contador_ganadores = 0
for ganador in ganadores:
    contador_ganadores += 1

premio_por_equipo = round(premio_total / contador_ganadores)

ganadores_str = ""
for i in range(contador_ganadores):
    if i == 0:
        ganadores_str += str(ganadores[i])
    else:
        ganadores_str += ", " + str(ganadores[i])

print("Equipo/s ganador/es: " + ganadores_str)
print("Premio por equipo: $ " + str(premio_por_equipo))
