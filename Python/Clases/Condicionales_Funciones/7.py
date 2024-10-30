vuelto = int(input("Ingrese el vuelto: "))

if vuelto > 10000:
    billetes = vuelto // 10000
    vuelto = vuelto % 10000
    print(billetes, "Billetes de $10.000")
if vuelto > 5000:
    billetes = vuelto // 5000
    vuelto = vuelto % 5000
    print(billetes, "Billetes de $5.000")
if vuelto > 2000:
    billetes = vuelto // 2000
    vuelto = vuelto % 2000
    print(billetes, "Billetes de $2.000")
if vuelto > 1000:
    billetes = vuelto // 1000
    vuelto = vuelto % 1000
    print(billetes, "Billetes de $1.000")
if vuelto > 500:
    billetes = vuelto // 500
    vuelto = vuelto % 500
    print(billetes, "Billetes de $500")
if vuelto > 100:
    billetes = vuelto // 100
    vuelto = vuelto % 100
    print(billetes, "Billetes de $100")
if vuelto > 50:
    billetes = vuelto // 50;
    vuelto = vuelto % 50
    print(billetes, "Billetes de $50")
if vuelto > 10:
    billetes = vuelto // 10
    vuelto = vuelto % 10
    print(billetes, "Billetes de $10")
if vuelto > 2:
    billetes = vuelto // 2
    vuelto = vuelto % 2
    print(billetes, "Moneda de $2")
if vuelto > 1:
    billetes = vuelto // 1
    vuelto = vuelto % 1
    print(billetes, "Moneda de $1")