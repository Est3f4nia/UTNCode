cant_vendedores = int(input("Cantidad de vendedores atendiendo: "))
comision_vendedores = [0] * cant_vendedores

venta = 1
while venta != 0:
    num_vendedor = int(input("Número del vendedor: "))
    num_vendedor -= 1

    while num_vendedor > cant_vendedores:
            print("Vendedor inexistente.")
            num_vendedor = int(input("Número del vendedor: "))
    
    venta = float(input("Monto de la venta: "))
    comision = venta * 0.01
    comision_vendedores[num_vendedor] = comision_vendedores[num_vendedor] + comision

if num_vendedor == 0 and venta == 0:
    for i in comision_vendedores:
        print(i)