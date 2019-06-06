
archivo = open('ppp.csv','r')

def promedio_trafico(hora):
    consumo = 0
    cont = 0
    for x in archivo:
        if x.startswith('"2') == True:
            x1 = x.strip().split(',')
            x2 = x1[0].strip('"').split(' ')
            if x2[1] == hora:
                consumo += float(x1[1])
                cont += 1
    archivo.close()
    return f'Consumo promedio = {consumo/cont}'

print(promedio_trafico('17:30:00'))
