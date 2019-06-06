#-*- coding: utf-8 -*-
#Agustín Salvador Quintanar de la Mora
#A01636142

#Indice de masa corporal

print('Bienvenido al calculador del IMC')

peso = float(input('Ingrese su peso en kilogramos: '))
estatura_metros = float(input('Ingrese su estatura en metros: '))


imc = peso/(estatura_metros**2)

print('')
print('-------------------------------------------------------------------------------------')
print('RESULTADOS')
print('-------------------------------------------------------------------------------------')
print('')

print('Su peso es de ' + str(peso) + ' kilogramos')
print('Su estatura es de ' + str(estatura_metros) + ' metros')
print('')
print('Su IMC es de ' + str(imc))

#Aprendí a calcular el IMC y practiqué el casting de variables

