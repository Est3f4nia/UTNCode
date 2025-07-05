def calcular_ganancia(unidades, precio, porcentaje_ganancia):
    return unidades * precio * (porcentaje_ganancia / 100)

cant_productos = int(input())
productos = []
for i in range(cant_productos):
    nombre = input()
    unidades = int(input())
    precio = float(input())
    porcentaje_ganancia = float(input())
    productos.append({
        "nombre": nombre,
        "unidades": unidades,
        "precio": precio,
        "porcentaje_ganancia": porcentaje_ganancia,
        "ganancia": calcular_ganancia(unidades, precio, porcentaje_ganancia)
    })

max_unidades = productos[0]
max_ganancias = productos[0]
for producto in productos:
    if producto["unidades"] > max_unidades["unidades"]:
        max_unidades = producto

    if producto["ganancia"] > max_ganancias["ganancia"]:
        max_ganancias = producto

print("Producto con mayor ganancia total:", max_ganancias["nombre"])
print("Producto con más unidades vendidas:", max_unidades["nombre"])
