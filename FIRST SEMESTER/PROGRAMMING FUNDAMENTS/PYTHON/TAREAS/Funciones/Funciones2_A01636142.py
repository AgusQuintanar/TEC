# Agustin Salvador Quintanar de la Mora
#A01636142
from time import sleep

def energia(masa):
    '''Esta funcion recibe un parametro llamado masa, lo multiplica por la velocidad de la luz
        al cuadrado, y devuelve el resultado.'''
    energia_total = float(masa)*(299792458**2)
    return energia_total

def multiplos_comunes(n1,n2,limite):
    ''' Esta funcion recibe 3 parametros (numero 1, numero 2 y un limite), en un ciclo for recorrer todos
     los valores del rango de 1 al limite, y verifica que los dos numeros sean multiplos comunes
     (se saca el modulo 2 de cada uno, y los 2 tienen que ser igual a cero para que esto se cumpla)
     Y finalmente agrega esos valores a una lista y la regresa. '''
    multiplos_comunes_lista = []
    for i in range(1,limite):
        if i % n1 == 0 and i % n2 == 0:
            multiplos_comunes_lista.append(i)
    return multiplos_comunes_lista

def ofertas(monto_a_recargar):
    ''' Esta funcion recibe el parametro de un monto de recarga telefonica, el cual es verificado si esta
        dentro de los montos de recarga válida, y posteriormente le agrega el bonus otorgado por la compañia,
        y lo regresa.'''
    monto_adicional = ['5', 0, '10', 0, '25', 3, '50', 8, '100', 20]
    if monto_a_recargar not in monto_adicional[::2]:
        monto_a_recargar = 'No se pudo completar la recarga. Monto de recarga no válido'
    else:
        monto_a_recargar = 'Recarga existosa de $'+str(monto_adicional[monto_adicional.index(monto_a_recargar)+1]+int(monto_a_recargar))+' USD (Monto:'+monto_a_recargar+' Bonus:'+str(monto_adicional[monto_adicional.index(monto_a_recargar)+1])+')'
    return monto_a_recargar

def barra_progreso(segundos):
    ''' Esta funcion recibe el parametro de segundos, el cual se usa como rango de un ciclo for,
     para posteriormente imprimir una X en la misma linea, con un sleep (delay) de 10 segundos.'''
    for x in range(int(segundos)//10):
        sleep(10)
        print('X',end='')
    return ''

def validacion_float(entrada):
    ''' Valida que los inputs float sean validos'''
    while True:
        try:
            float(entrada)
            break
        except ValueError:
            print("Oops!  Entrada no valida.  Intentelo de nuevo...")
            entrada = input('Nueva entrada: ')
    return entrada

def validacion_int(entrada):
    ''' Valida que los inputs int sean validos'''
    while True:
        try:
            int(entrada)
            break
        except ValueError:
            print("Oops!  Entrada no valida.  Intentelo de nuevo...")
            entrada = input('Nueva entrada: ')
    return entrada

def menu(opcion):
    '''Esta es la funcion del menu, la cual recibe la opción seleccionada por el usuario, y
     la procesa en la seccion de condiciones y ejecuta la funcion seleccionada con un delay de
     3 segundos implementado en el ciclo while exterior a la funcion.
    '''
    if opcion == '1':
        masa  = validacion_float(input('Ingrese la masa en kilogramos: '))
        print('La energia es de: '+ str(energia(masa))+' metros-kilogramos-segundos')
    elif opcion == '2':
        n1 = validacion_int(input('Ingrese el número 1: '))
        n2 = validacion_int(input('Ingrese el número 2: '))
        limite = validacion_int(input('Ingrese el limite: '))

        print('Los multiplos comunes son: '+ (str(multiplos_comunes(int(n1),int(n2),int(limite)))))
    elif opcion == '3':
        monto = input('Ingrese el monto de dolares a recargar: $')
        print(ofertas(monto))
    elif opcion == '4':
        segundos = validacion_float(input('Ingrese el rango de segundos: '))
        print(barra_progreso(segundos))
    elif opcion == '5':
        print('Finalizado exitosamente')
    else:
        print('Ingrese una opción valida')

opcion = 0
while opcion != '5':
    sleep(3)
    print('''
    Bienvenido 

    MENU

    1.- Calculador de energia
    2.- Calculador de multiplos comunes con limites
    3.- Recarga telefonica
    4.- Barra de progreso

    5-. Salir
    ''')
    opcion = input('Ingrese opción a ejecutar: ')
    menu(opcion)


'''
En esta practica reforcé el uso de condiciones, funciones, ciclos For, Whiles e inputs.
Y aprendi el uso de la funcion sleep de la libreria de time.'''
