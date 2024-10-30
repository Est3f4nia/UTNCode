cp_pbaja = 20
cp_sbnvl1 = 40
cp_p1 = 50
cp_sbnvl2 = 50
t_vehiculos = 0

while t_vehiculos <= 160:
    boton = int(input())
    vehiculo = 1
    
    if boton == 1:
        if vehiculo <= 20 and cp_pbaja != 0:
            cp_pbaja = cp_pbaja - vehiculo
            print("Estacionar en Planta baja")
            if vehiculo > 20 and cp_pbaja != 0:
                vehiculo = vehiculo - cp_pbaja
                print("Estacionar en Planta baja")
        elif vehiculo <= 40 and cp_sbnvl1 != 0:
            cp_sbnvl1 = cp_sbnvl1 - vehiculo
            print("Estacionar en Subnivel 1")
            if vehiculo > 40 and cp_sbnvl1 != 0:
                vehiculo = vehiculo - cp_sbnvl1
                print("Estacionar en Subnivel 1")
        elif vehiculo <= 50 and cp_p1 != 0:
            cp_p1 = cp_p1 - vehiculo
            print("Estacionar en Piso 1")
            if vehiculo > 50 and cp_p1 != 0:
                vehiculo = vehiculo - cp_p1
                print("Estacionar en Piso 1")
        elif vehiculo <= 50 and cp_sbnvl2 != 0 and cp_p1 == 0:
            cp_sbnvl2 = cp_sbnvl2 - vehiculo
            print("Estacionar en Subnivel 2")
            if vehiculo > 50 and cp_sbnvl2 != 0:
                vehiculo = vehiculo - cp_sbnvl2
                print("Estacionar en Subnivel 2")
        t_vehiculos = t_vehiculos + 1
    if boton == 0:
        print("Subnivel 2: ", cp_sbnvl2, "/50", sep = "")
        print("Subnivel 1: ", cp_sbnvl1 ,"/40", sep = "")
        print("Planta baja: ", cp_pbaja, "/20", sep = "")
        print("Piso 1: ", cp_p1, "/50", sep = "")
        print("Capacidad total: ", (160 - t_vehiculos), "/160", sep = "")
        break