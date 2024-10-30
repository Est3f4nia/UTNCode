def calc_imc(altura, peso):
    #Cálculo en metros, agregar (peso / (altura ** 2)) * 10000 para calcular en cm
    imc = (peso / (altura ** 2))
    imcr = round(imc ,1)
    return imcr
