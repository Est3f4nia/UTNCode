# Revisar en algún momento

silo1 = 0
silo2 = 0
silo3 = 0
carga = 0
total = 0

while carga != -1:
    carga = int(input("Ingrese la carga (kg): "))

    if carga == -1:
        total = total
    else:
        total = total + carga
    
    if carga <= 200 and carga < 200 - silo1:
        if carga == -1:
            silo1 = silo1
        else:
            print("La carga debe almacenarse en el silo 1")
            silo1 = silo1 + carga
    
    elif carga <= 150 and carga > 200 - silo1:
        if carga == -1:
            silo2 = silo2
        else:
            silo2 = silo2 + carga
            if carga < silo2:
                print("La carga no puede ser almacenada")
                total = total - carga
                silo2 = silo2 - carga
            else:
                print("La carga debe almacenarse en el silo 2")
    
    elif carga <= 250 and carga > 200 - silo1 and carga > 150 - silo2 and carga != 150:
        if carga == -1:
            silo3 = silo3
        else:
            silo3 = silo3 + carga
            print("La carga debe almacenarse en el silo 3")
    
    else:
        total = 0
        print("La carga no puede ser almacenada.")

if carga == -1:
    print("Carga del Silo 1: ", silo1, " /200 kg", sep = "")
    print("Carga del Silo 2: ", silo2, " /150 kg", sep = "")
    print("Carga del Silo 3: ", silo3, " /250 kg", sep = "")
    print("Carga total: ", total, " /600 kg", sep = "")