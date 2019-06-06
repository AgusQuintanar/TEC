#-*- coding: utf-8 -*-
#Agustín Salvador Quintanar de la Mora
#A01636142

#Ejercicio 8

resistencia_1 = float(input('Ingrese el valor de la resistencia 1: '))
resistencia_2 = float(input('Ingrese el valor de la resistencia 2: '))
resistencia_3 = float(input('Ingrese el valor de la resistencia 3: '))

resistencia_final = ((resistencia_1**-1)+(resistencia_2**-1)+(resistencia_3**-1))**-1

print('')

print('''
Resistencia Total =           1
                       ________________
                        1  +  1  +  1
                       –––   –––   –––          ''')
print('                      ',str(int(resistencia_1))+'   '+str(int(resistencia_2))+'   '+str(int(resistencia_3)))

print('')
print('El valor de la resistencia total del circuito es de:',resistencia_final,'ohmios')

#Practiqué el uso de prints multilíneas.