#Agustin Salvador Quintanar de la Mora       A01636142
from time import sleep

def suma(a,b):
    '''
    La funcion recibe 2 matrices de tipo MxM y regresa la suma de estas.
    :param a:
    :param b:
    :return:
    '''
    return [[a[x][y]+b[x][y] for y in range(len(a[x]))] for x in range(len(a))]

def resta(a,b):
    '''
        La funcion recibe 2 matrices de tipo MxM y regresa la resta de estas.
        :param a:
        :param b:
        :return:
        '''
    return [[a[x][y]-b[x][y] for y in range(len(a[x]))] for x in range(len(a))]

def escalar(a,n):
    '''
    La funcion recibe una matriz y un entero, y regresa la matriz escalar de estos.
    :param a:
    :param n:
    :return:
    '''
    return [[a[x][y]*n for y in range(len(a[x]))] for x in range(len(a))]

def multiplicacion(c,d):
    '''
    Esta funcion recibe 2 matrices y regresa la multiplicacion de estas.
    :param c:
    :param d:
    :return:
    '''
    return [[sum([c[x][z]*d[z][y] for z in range(len(c[0]))]) for y in range(len(d[0]))] for x in range(len(d[0]))]

def traspuesta(a):
    '''
    Recibe una matriz, y devuelve la matriz traspuesta de esta.
    :param a:
    :return:
    '''
    return [[a[y][x] for y in range(len(a))] for x in range(len(a[0]))]

def menu(opcion):
    '''
    Funcion que recibe la opcion que desea ejecutar el usuario.
    :param opcion:
    :return:
    '''
    a = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9,10,11,12],
         [13,14,15,16]]

    b = [[1, 2, 5, 6],
         [5, 6,11,23],
         [9,10,2,7],
         [13,14,2,9]]

    c = [[7,9,-1],
         [3,0,5]]

    d = [[2,6],
         [4,-3],
         [1,7]]

    n = 5

    if opcion == '1':
        print(suma(a,b))
    elif opcion == '2':
        print(resta(a,b))
    elif opcion == '3':
        print(escalar(a,n))
    elif opcion == '4':
        print(multiplicacion(c,d))
    elif opcion == '5':
        print(traspuesta(d))
    elif opcion == '6':
        print('Programa finalizado exitosamente')
    else:
        print('Ingrese un a opción válida')

opcion = 0
while opcion != '6':
    sleep(2)
    print('''
    Bienvenido. Porfavor seleccione la opcion que desea ejecutar.
    
    [1] Suma de matrices
    [2] Resta de matrices
    [3] Matriz escalar
    [4] Multiplica matrices
    [5] Matriz traspuesta
    
    [6] Salir''')

    opcion = input('\nOpcion a ejecutar: ')
    menu(opcion)


#Practique el uso de list comprehension.