cont = 0
productos = []

while cont <= 4:
    nombre = input()
    precio = float(input())
    cantidad = int(input())
    
    productos.append({
        "nombre" : nombre,
        "precio" : precio,
        "cantidad" : cantidad
    })
    cont += 1

max = 0
for i in range(len(productos)):
    x = float(productos[i]["precio"])
    if x > x:
        max = i

print("El producto más caro es:")
print("Nombre: ", productos[max]["nombre"], ", Precio: ", productos[max]["precio"], ", Cantidad: ", productos[max]["cantidad"], sep = "")