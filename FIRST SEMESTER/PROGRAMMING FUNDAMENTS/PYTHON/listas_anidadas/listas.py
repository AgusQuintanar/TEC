#Agustin Salvador Quintanar de la Mora         A01636142

def creaMatriz1(n):
    '''
     Funcion la cual recibe un entero n que representa el número de renglón y columnas. La función devuelve una lista
    que representa una matriz de nXn y cada localidad de la matriz tiene asignado el valor de -1.
    :param n:
    :return:
    '''
    return  [n*[-1]]*n

def creaMatriz2(n):
    '''
    Funcion la cual recibe un entero n que representa el número de renglón y columnas. La función devuelve una lista que
     representa una matriz de nXn y cada localidad de la matriz tiene asignado el número de su respectiva columna.
    :param n:
    :return:
    '''
    return [list(range(n))]*n

def creaMatriz3(n):
    '''
    Funcion la cual recibe un entero n que representa el número de renglón y columnas. La función devuelve una lista que
    representa una matriz de nXn y cada localidad de la matriz tiene asignado el valor de su correspondiente renglón
    :param n:
    :return:
    '''
    return [n*[x] for x in range(n)]

def creaMatriz4(n):
    '''
    Funcion la cual recibe un entero n que representa el número de renglón y columnas. La función devuelve una lista que
     representa una matriz de nXn y cada localidad de la matriz tiene asignado un número consecutivo a partir de uno.
    :param n:
    :return:
    '''
    return [list(range(1,(n**2)+1,n)) for x in range(n)]

def cuentaPares(lista_para_contar):
    '''
    Funcion la cual recibe como parámetro una lista anidada de números y regresa cuántos números pares hay dentro de la lista
    :param lista_para_contar:
    :return:
    '''
    return len(list(filter(lambda x: x % 2 - 1, [x for y in lista_para_contar for x in y])))

def sumaMatriz(lista_para_sumar):
    '''
     Funcion que recibe como parámetro una lista anidada de números. El método regresa el resultado de sumar los valores de cada
     una de las localidades.
    :param lista_para_sumar:
    :return:
    '''
    return sum([x for y in lista_para_sumar for x in y])

def cuentaPositivos(lista_para_contar):
    '''
    Funcion que recibe como parámetro una lista anidada de números. El método regresa el número de valores mayores o
    iguales que cero almacenados en la lista.
    :param lista_para_contar:
    :return:
    '''
    return len(list(filter(lambda x: x>= 1, [x for y in lista_para_contar for x in y])))

def cambiaNegativos(l_neg):
    '''
    Funcion que recibe como parámetro una lista anidada de números. El método modifica la lista, asignando el valor de
     0 a cada localidad que contenga un valor menor a cero.
    :param l_neg:
    :return:
    '''
    return [[0 if l_neg[x][y] < 0 else l_neg[x][y] for y in range(len(l_neg[x]))] for x in range(len(l_neg))]

def cuentaRepeticiones(l_repeticion,n):
    '''
    Funcion que recibe como parámetro una lista anidada de números y un valor entero x. El método regresa el número de
     veces que se repite el valor de x en la lista.
    :param l_repeticion:
    :param n:
    :return:
    '''
    return [x for y in l_repeticion for x in y].count(n)

def busca(lista_buscar, n):
    '''
    Funcion que recibe como parámetro una lista anidada de números y un valor entero x. El método regresa el valor
    true si el valor de x existe en una localidad de la matriz y false sino existe.
    :param lista_buscar:
    :param n:
    :return:
    '''
    return True if n in [x for y in lista_buscar for x in y] else False

def sumaMayores5(lista_mayor5):
    '''
    Funcion que recibe como parámetro una lista anidada de números. El método deberá de devolver la suma de todos
    aquellos números que haya dentro de la matriz que sean mayores a 5.
    :param lista_mayor5:
    :return:
    '''
    return sum(list(filter(lambda x: x > 5, [x for y in lista_mayor5 for x in y])))

def cambiaCeros(lista_cambia0):
    '''
    Funcion que recibe como parámetro una lista anidada de números. El método deberá sustituir todos aquellos ceros que
    haya dentro de la matriz por el resultado de la suma de su número de renglón por su número de columna.
    :param lista_cambia0:
    :return:
    '''
    return [[x+y+2 if lista_cambia0[x][y] == 0 else lista_cambia0[x][y] for y in range(len(lista_cambia0[x]))] for x in range(len(lista_cambia0))]
