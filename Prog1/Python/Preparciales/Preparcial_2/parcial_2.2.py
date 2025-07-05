nombre_p = input()
fecha = input()

id_u = ""
for caracter in nombre_p[:2:]:
    id_u += caracter.upper()

for caracter in fecha[-2::]:
    id_u += caracter

for i in range(len(fecha)):
    if i == 3:
        id_u += fecha[i] + fecha[i+1]

for i in range(len(fecha)):
    if i == 0:
        id_u += fecha[i] + fecha[i+1]
        
print("Código de identificación:", id_u)
