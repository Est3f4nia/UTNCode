max = 0
min = 0
maxv = 0
mas05 = 0
variacion = 0
city = ""
contador = 0
cant_exit = 0
muestras = 0

while city != "n":
    contador = contador + 1
    variacion = float(input())
    city = input()

    if variacion > 0.5:
        mas05 = mas05 + 1
        if maxv < variacion or contador == 1:
            maxv = variacion
            nombre_maximo = city
    
    if variacion == 0:
        cant_exit += 1
        contador = contador - 1
        muestras = contador
        if muestras < min or contador == 1:
            min = muestras
        if muestras > max or contador == 1:
            max = muestras
            max = max - min

    if city == "exit" and mas05 != 0:
        if cant_exit == 1:
            min = max
            max = min
        print("Alerta! Movimiento detectado por información cruzada")
        print("Hay", mas05, "sismografos que detectan movimiento")
        print("El mayor movimiento detectado es en", nombre_maximo, "con un valor de", maxv)
        print("Mayor muestreo compuesto por", max, "muestras")
        print("Menor muestreo compuesto por", min, "muestras")
        break