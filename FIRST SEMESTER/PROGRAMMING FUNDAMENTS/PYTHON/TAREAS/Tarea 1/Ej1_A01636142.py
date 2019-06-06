#-*- coding: utf-8 -*-
#Agustín Salvador Quintanar de la Mora
#A01636142

#Conversor de temperatura

print('Bienvenido al conversor de temperaturas')
temperatura_celcius = float(input('Ingrese su la temperatura en Celcius que desea convertir a Farenheit y a Kelvin: '))

temperatura_farenheit = (temperatura_celcius*1.8)+32
temperatura_kelvin = temperatura_celcius + 273

print('')
print('Temperatura en Celcius: %1.2f'%(temperatura_celcius)+'º')
print('Temperatura en Farenheit: %1.2f'%(temperatura_farenheit)+'º')
print('Temperatura en Kelvin: %1.2f'%(temperatura_kelvin)+'º')

#En esta practica practiqué el uso de variables, inputs, operaciones básicas y el formateo "The Old Way or the non-existing printf and sprintf"