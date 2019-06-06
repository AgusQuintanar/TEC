#-*- coding: utf-8 -*-
#Agustín Salvador Quintanar de la Mora
#A01636142






def conversor_de_temperatura(temperatura_celcius):
    print('Bienvenido al conversor de temperaturas')

    temperatura_farenheit = (temperatura_celcius * 1.8) + 32
    temperatura_kelvin = temperatura_celcius + 273

    print('')
    print('Temperatura en Celcius:', temperatura_celcius)
    print('Temperatura en Farenheit:', temperatura_farenheit)
    print('Temperatura en Kelvin:', temperatura_kelvin)




    # En esta practica practiqué el uso de variables, inputs y operaciones básicas.

def indice_masa_corporal():
    # Indice de masa corporal

    print('Bienvenido al calculador del IMC')

    peso = float(input('Ingrese su peso en kilogramos: '))
    estatura = float(input('Ingrese su estatura en centimetros: '))
    estatura_metros = estatura / 100

    imc = peso / (estatura_metros ** 2)

    print('')
    print('-------------------------------------------------------------------------------------')
    print('RESULTADOS')
    print('-------------------------------------------------------------------------------------')
    print('')

    print('Su peso es de ' + str(peso) + ' kilogramos')
    print('Su estatura es de ' + str(estatura_metros) + ' metros')
    print('')
    print('Su IMC es de ' + str(imc))

    # Aprendí a calcular el IMC



def menu():

    print('''
    
    MENU
    
    1 - Conversor de unidades
    2 - Calculador de IMC
    
''')



seleccion = int(input('''MENU
    
    1 - Conversor de unidades
    2 - Calculador de IMC
    
Seleccione el número del menú que desea ejecutar: '''))

if seleccion == 1:
    t_c = float(input('Ingrese su la temperatura en Celcius que desea convertir a Farenheit y a Kelvin: '))
    conversor_de_temperatura(t_c)
    print('')

    salir = int(input(
        'Si desea volver al menú principal escriba \'1\',si desea volver a ejecutar el programa escriba cualquier caracter: '))
    while salir == 1:
        menu()

    t_c = float(input('Ingrese su la temperatura en Celcius que desea convertir a Farenheit y a Kelvin: '))
    conversor_de_temperatura(t_c)
