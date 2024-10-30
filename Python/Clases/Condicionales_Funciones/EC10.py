monto = float(input())
x = int(monto)

if monto - x != 0:
    monto = x + 1
    print(monto)

if monto >= 10000:
    if monto // 10000 > 1:
        num = monto // 10000
        monto = monto - (10000 * num)
        num = int(num)        
        print(num, "Billetes de $10.000")
    else:
        monto = monto - 10000
        print("1 Billetes de $10.000")
if monto >= 2000 and monto != 0:
    if monto // 2000 > 1:
        num = monto // 2000
        monto = monto - (2000 * num)
        num = int(num)
        print(num, "Billetes de $2000")
    else:
        monto = monto - 2000
        print("1 Billetes de $2000")
if monto >= 1000 and monto != 0:
    if monto // 1000 > 1:
        num = monto // 1000
        monto = monto - (1000 * num)
        num = int(num)
        print(num, "Billetes de $1000")
    else:
        monto = monto - 1000
        print("1 Billetes de $1000")
if monto >= 500 and monto != 0:
    if monto // 500 > 1:
        num = monto // 500
        monto = monto - (500 * num)
        num = int(num)
        print(num, "Billetes de $500")
    else:
        monto = monto - 500
        print("1 Billetes de $500")
if monto >= 200 and monto != 0:
    if monto // 200 > 1:
        num = monto // 200
        monto = monto - (200 * num)
        num = int(num)
        print(num, "Billetes de $200")
    else:
        monto = monto - 200
        print("1 Billetes de $200")
if monto >= 100 and monto != 0:
    if monto // 100 > 1:
        num = monto // 100
        monto = monto - (100 * num)
        num = int(num)
        print(num, "Billetes de $100")
    else:
        monto = monto - 100
        print("1 Billetes de $100")
if monto >= 50 and monto != 0:
    if monto // 50 > 1:
        num = monto // 50
        monto = monto - (50 * num)
        num = int(num)
        print(num, "Billetes de $50")
    else:
        monto = monto - 50
        print("1 Billetes de $50")
if monto >= 20 and monto != 0:
    if monto // 20 > 1:
        num = monto // 20
        monto = monto - (20 * num)
        num = int(num)
        print(num, "Billetes de $20")
    else:
        monto = monto - 20
        print("1 Billetes de $20")
if monto >= 10 and monto != 0:
    if monto // 10 > 1:
        num = monto // 10
        monto = monto - (10 * num)
        num = int(num)
        print(num, "Billetes de $10")
    else:
        monto = monto - 10
        print("1 Billetes de $10")
if monto >= 2 and monto != 0:
    if monto // 2 > 1:
        num = monto // 2
        monto = monto - (2 * num)
        num = int(num)
        print(num, "Monedas de $2")
    else:
        monto = monto - 2
        print("1 Monedas de $2")
if monto < 1 and monto != 0:
    print("1 Monedas de $1")
if monto >= 1 and monto != 0:
    if monto // 1 > 1:
        num = monto // 1
        monto = monto - (1 * num)
        num = int(num)
        print(num, "Monedas de $1")
    else:
        monto = monto - 1
        print("1 Monedas de $1")