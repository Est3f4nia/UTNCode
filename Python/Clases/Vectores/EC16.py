masitas = [0] * 1500
precio_masitas = [0] * 1500

gaseosas = [0] * 1500
precio_gaseosas = [0] * 1500

beb_alcoholicas = [0] * 1500
precio_bebA = [0] * 1500

helados = [0] * 1500
precio_helados = [0] * 1500

ent = 1
cont = 0

while ent != 0:
    print("1- Cargar datos.")
    print("2- Mostrar datos.")
    ent = int(input("> "))
    if ent == 1:
        print("Seleccione el tipo de producto:")
        print("1- Masitas.")
        print("2- Gaseosas.")
        print("3- Bebidas alcohólicas.")
        print("4- Helados.")
        product = int(input("> "))
        unidad = int(input("Unidades en stock: "))
        precioU = float(input("Precio por unidad: "))
        if product == 1:
            masitas[cont] = unidad
            precio_masitas[cont] = precioU
        elif product == 2:
            gaseosas[cont] = unidad
            precio_gaseosas[cont] = precioU
        elif product == 3:
            beb_alcoholicas[cont] = unidad
            precio_bebA[cont] = precioU
        elif product == 4:
            helados[cont] = unidad
            precio_helados[cont] = precioU
        else:
            print("Opción inválida.", "\n")

    elif ent == 2:
        print("Salida deseada:")
        print("1- Stock total.")
        print("2- Cantidad de productos (por tipo).")
        salida = int(input("> "))

        total = 0
        sumaM = 0
        sumaG = 0
        sumaBA = 0
        sumaH = 0

        if salida == 1:
            for i in masitas:
                total = total + i
            for j in gaseosas:
                total = total + j
            for k in beb_alcoholicas:
                total = total + k
            for l in helados:
                total = total + l
            print("Total:", total)

        elif salida == 2:
            for i in masitas:
                sumaM = sumaM + i
            print("Masitas:", sumaM)
            for j in gaseosas:
                sumaG = sumaG + j
            print("Gaseosas:", sumaG)
            for k in beb_alcoholicas:
                sumaBA = sumaBA + k
            print("Bebidas alcohólicas:", sumaBA)
            for l in helados:
                sumaH = sumaH + l
            print("Helados:", sumaH)

    else:
        print("Opción inválida.", "\n")