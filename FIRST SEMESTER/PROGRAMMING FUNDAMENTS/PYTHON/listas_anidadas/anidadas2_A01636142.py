#Agustin Salvador Quintanar de la Mora       A01636142
def lugares_vacios(est):
    '''
    Esta funcion recibe una lista anidada, que representa un estacionamiento, y regresa las posiciones vacias, con el formato especificado.
    :param est:
    :return:
    '''
    return [chr(x+65)+str(y+1) for x in range(len(est)) for y in range(len(est[x])) if est[x][y] == 0]

estacionamiento = [
    [0,1,1,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,1,1,0,1,1,1,1,1,1,1,1,0,1,1],
    [1,1,0,1,1,1,1,1,1,1,0,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,0,1,1,1],
    [1,1,1,1,1,0,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,0,1,1,1,1,0,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,0,1,1,1],
    [1,1,1,1,1,1,1,0,1,1,1,1,1,1,0],
    [1,1,0,1,0,1,1,1,1,0,1,0,1,1,1]
]
print(lugares_vacios(estacionamiento))

#Practique el uso de list comprehension.