#A01636142
#Agustin Salvador Quintanar de la Mora

def a_segundos(dias,horas,minutos,segundos):
    '''Recibe 4 parametros y los suma'''
    total_segundos = segundos + minutos*60 + horas*3600 + dias*24*3600
    return total_segundos

def eratostenes(n):
    lista_numeros = list(range(2,n+1))
    lista_numeros_primos = []
    for x in range(0,n-2):
        a = 0
        for y in range(0,n-2):
            if lista_numeros[x] % lista_numeros[y] == 0:
                a += 1
        if a == 1:
            lista_numeros_primos.append(lista_numeros[x])

    return lista_numeros_primos

def producto_interno(vector1,vector2):
    '''
    Recibe 2 listas, y las multiplica vectorialmente
    :param vector1:
    :param vector2:
    :return:
    '''
    vector_resultante = []
    for x in range(len(vector1)):
        vector_resultante.append(vector1[x]*vector2[x])
    return vector_resultante

def riman(lista1, lista2):
    'Recibe 2 listas y realiza su multiplicacion vectorial'
    lista_resultados = []

    for x in range(len(lista1)):
        if lista1[x] == lista2[x]:
            lista_resultados.append(1)
        elif lista1[x][len(lista1[x])-3:] == lista2[x][len(lista2[x])-3:]:
            lista_resultados.append(2)
        elif lista1[x][len(lista1[x])-2:] == lista2[x][len(lista2[x])-2:]:
            lista_resultados.append(3)
        else:
            lista_resultados.append(0)

    return lista_resultados

def menu(opcion):
    'Recibe la opcion ingresada por el usuario y la procesa'
    if opcion == '1':
        dias = int(input('Ingrese los dias: '))
        horas = int(input('Ingrese las horas: '))
        minutos = int(input('Ingrese los minutos: '))
        segundos = int(input('Ingrese los segundos: '))

        print('Total de segundos es igual a: '+str(a_segundos(dias,horas,minutos,segundos)))

    elif opcion == '2':
        n = input('Ingrese el limite numerico: ')
        print(eratostenes(n))

    elif opcion == '3':
        vector1 = [1,3,5,7,9]
        vector2 = [2,4,6,8,10]
        print('Vector 1: '+str(vector1))
        print('Vector 2: ' + str(vector2))
        print('\nEl producto interno de los vectores es igual a '+str(producto_interno(vector1,vector2)))

    elif opcion == '5':
        lista1 = ['corazon', 'libre', 'peso', 'cochinito', 'paz']
        lista2 = ['retozon', 'pez', 'caso', 'ninito', 'paz']
        print('Lista resultado: '+str(riman(lista1,lista2)))
    elif opcion == '4':
        print('Finalizado exitosamente.')

    else:
        print('Ingrese una opcion valida.')

opcion = '0'
while opcion != '4':
    print('''
    Menu
    
    [1] A segundos
    [2] Criba de Eratostenes
    [3] Producto Interno
    [5] Riman
    
    [4] Salir
    ''')
    opcion = str(input('Ingrese opcion a ejecutar: '))
    menu(opcion)