def es_perfecto(n):
    cont = 1
    divisores = []
    while cont < n:
        if n % cont == 0:
            divisores.append(cont)
        cont += 1
    if sum(divisores) == n:
        return True
    return False

def cuales_perfectos(listaNumeros):
    return [listaNumeros[x] for x in range(len(listaNumeros)) if es_perfecto(listaNumeros[x]) == True]

def divide_matriculas(listaMatriculas):
    matriculas_separadas = [['Pares:'],['Impares:']]
    for x in range(len(listaMatriculas)):
        if int(listaMatriculas[x][-1])%2 == 0:
            matriculas_separadas[0].append(listaMatriculas[x])
        else: matriculas_separadas[1].append(listaMatriculas[x])
    return matriculas_separadas

def frecuencia_entidad(lista_curps):
    entidades = []
    for x in range(len(lista_curps)):
        if lista_curps[x][11:13].split() not in entidades:
            entidades.append(lista_curps[x][11:13].split())
        lista_curps[x] = lista_curps[x][11:13]

    for y in range(len(entidades)):
        entidades[y].append(lista_curps.count(''.join(entidades[y])))

    return entidades

def mezcla_ordenada(lista1,lista2):
    return sorted(lista1+lista2)

def ganador_etapa(lista_jugadores,lista_tiempos):
    ganadores = []
    for x in range(len(lista_tiempos[0])):
        ganadores.append(lista_jugadores[[lista_tiempos[y][x] for y in range(len(lista_jugadores))].index(min([lista_tiempos[y][x] for y in range(len(lista_jugadores))]))])
    return ganadores

def cuenta_frases(texto):
    return len(texto.split('.'))-1

def reporte(lista_tareas):
    return [str(x+1)+'-'+''.join(['' + ['Lu','Ma','Mi','Ju','Vi'][y] for y in range(len(lista_tareas[x])) if tareas[x][y] == 0]) for x in range(len(lista_tareas))]



tareas_a = open('tareas.txt','r')


tareas = []
for x in tareas_a:
    x1 = x.rstrip()
    x2 = x1.split(',')
    x3 = list(map(int,x2))
    tareas.append(x3)
tareas_a.close()
print(tareas)
print(reporte(tareas))
'''
print(cuenta_frases('hola.que.hace.'))
print(ganador_etapa(['Juan','Pedro','Poncho'],[[12,32,23,12,45],[14,25,25,16,35],[13,29,21,12,48]]))
print(mezcla_ordenada([ 4, 6, 8, 12],[1, 3, 10, 15]))
print(frecuencia_entidad(['AECJ940429HCHRRS01','AIHP911101MCHRRR03','BAVC840614HJLRLR04','CAMJ900421HCHRRN05','CAMJ900421HCHRRN00']))
print(divide_matriculas(['A01636142','A01635155','A01636166','A4']))
print(es_perfecto(28))
print(cuales_perfectos([1,14,28,56, 496, 8128, 8130,6]))
'''