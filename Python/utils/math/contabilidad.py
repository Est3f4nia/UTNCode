def impr_etiquetas(nom, venc, precio, ingr, DATOS):
    #Variable "datos" fuera de la función como string. Conviene usar una constante
    print(DATOS)
    print("--------------")
    print(nom)
    print(ingr)
    print(venc)
    print("--------------")
    print("$", precio, "\n",sep="")

def paga_por_dia_extras(horas, costo, extras):
    sueldo_dia = ((horas + horas_extra) * costo)
    print("Su monto a cobrar es: $", sueldo_dia, sep="")

