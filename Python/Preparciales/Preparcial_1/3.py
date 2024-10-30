cp_pbaja = 20
cp_sbnvl1 = 40
cp_p1 = 50
cp_sbnvl2 = 50
t_vehiculos = 0

while t_vehiculos <= 160:
    vehiculo = 1
    boton = int(input())
    
    if boton == 1:
        if vehiculo <= 20 and cp_pbaja != 0:
            cp_pbaja = cp_pbaja - vehiculo
            print("Estacionar en planta baja")
            if vehiculo > 20 and cp_pbaja != 0:
                vehiculo = vehiculo - cp_pbaja
                print("Estacionar en planta baja")
        elif vehiculo <= 40 and cp_sbnvl1 != 0:
            cp_sbnvl1 = cp_sbnvl1 - vehiculo
            print("Estacionar en subnivel 1")
            if vehiculo > 40 and cp_sbnvl1 != 0:
                vehiculo = vehiculo - cp_sbnvl1
                print("Estacionar en subnivel 1")
        elif vehiculo <= 50 and cp_p1 != 0:
            cp_p1 = cp_p1 - vehiculo
            print("Estacionar en piso 1")
            if vehiculo > 50 and cp_p1 != 0:
                vehiculo = vehiculo - cp_p1
                print("Estacionar en piso 1")
        elif vehiculo <= 50 and cp_sbnvl2 != 0 and cp_p1 == 0:
            cp_sbnvl2 = cp_sbnvl2 - vehiculo
            print("Estacionar en Subnivel 2")
            if vehiculo > 110 and cp_sbnvl2 != 0:
                vehiculo = vehiculo - cp_sbnvl2
                print("Estacionar en Subnivel 2")
        t_vehiculos = t_vehiculos + 1
    
    elif boton == 2:
        vehiculo = vehiculo / 4
        if vehiculo <= 20 and cp_pbaja != 0:
            cp_pbaja = cp_pbaja - vehiculo
            print("Estacionar en planta baja")
            if vehiculo > 20 and cp_pbaja != 0:
                vehiculo = vehiculo - cp_pbaja
                print("Estacionar en planta baja")
            cp_pbaja = round(cp_pbaja)
        elif vehiculo <= 40 and cp_sbnvl1 != 0:
            cp_sbnvl1 = cp_sbnvl1 - vehiculo
            print("Estacionar en subnivel 1")
            if vehiculo > 40 and cp_sbnvl1 != 0:
                vehiculo = vehiculo - cp_sbnvl1
                print("Estacionar en subnivel 1")
            cp_sbnvl1 = round(cp_sbnvl1)
        elif vehiculo <= 50 and cp_p1 != 0:
            cp_p1 = cp_p1 - vehiculo
            print("Estacionar en piso 1")
            if vehiculo > 50 and cp_p1 != 0:
                vehiculo = vehiculo - cp_p1
                print("Estacionar en piso 1")
            cp_p1 = round(cp_p1)
        elif vehiculo <= 50 and cp_sbnvl2 != 0 and cp_p1 == 0:
            cp_sbnvl2 = cp_sbnvl2 - vehiculo
            print("Estacionar en Subnivel 2")
            if vehiculo > 110 and cp_sbnvl2 != 0:
                vehiculo = vehiculo - cp_sbnvl2
                print("Estacionar en Subnivel 2")
            cp_sbnvl2 = round(cp_sbnvl2)
        t_vehiculos = t_vehiculos + 0.25
    
    elif boton == 3:
        vehiculo = vehiculo * 2
        if vehiculo <= 20 and cp_pbaja != 0:
            cp_pbaja = cp_pbaja - vehiculo
            print("Estacionar en planta baja")
            if vehiculo > 20 and cp_pbaja != 0:
                vehiculo = vehiculo - cp_pbaja
                print("Estacionar en planta baja")
        elif vehiculo <= 40 and cp_sbnvl1 != 0:
            cp_sbnvl1 = cp_sbnvl1 - vehiculo
            print("Estacionar en subnivel 1")
            if vehiculo > 40 and cp_sbnvl1 != 0:
                vehiculo = vehiculo - cp_sbnvl1
                print("Estacionar en subnivel 1")
        elif vehiculo <= 50 and vehiculo < 110 and cp_p1 != 0:
            cp_p1 = cp_p1 - vehiculo
            print("Estacionar en piso 1")
            if vehiculo > 50 and vehiculo < 110 and cp_p1 != 0:
                vehiculo = vehiculo - cp_p1
                print("Estacionar en piso 1")
        elif vehiculo <= 50 and cp_sbnvl2 != 0 and cp_p1 == 0:
            cp_sbnvl2 = cp_sbnvl2 - vehiculo
            print("Estacionar en Subnivel 2")
            if vehiculo > 110 and cp_sbnvl2 != 0:
                vehiculo = vehiculo - cp_sbnvl2
                print("Estacionar en Subnivel 2")
        t_vehiculos = t_vehiculos + 2

    t_c_motos = t_vehiculos
    t_c_motos = round(t_c_motos)
    t_c_motos = int(t_c_motos)
    
    if boton == 0:
        print("Subnivel 2: ", cp_sbnvl2, "/50", sep = "")
        print("Subnivel 1: ", cp_sbnvl1 ,"/40", sep = "")
        print("Planta baja: ", cp_pbaja, "/20", sep = "")
        print("Piso 1: ", cp_p1, "/50", sep = "")
        print("Capacidad total: ", (160 - t_c_motos), "/160", sep = "")
        break