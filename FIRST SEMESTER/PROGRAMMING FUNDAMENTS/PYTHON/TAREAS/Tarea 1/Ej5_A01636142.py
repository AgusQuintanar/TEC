#-*- coding: utf-8 -*-
#Agustín Salvador Quintanar de la Mora
#A01636142

#Ejercicio 5

segundos = int(input('Ingrese el tiempo en segundos dentro del rango (1 a 86400) que desea convertir al formato de 24 horas: '))

while segundos < 1 or segundos > 86400:
    segundos = int(input('Ingrese un número de segundos dentro del rango: '))

horas=0
minutos=0


while segundos >= 3600:
    segundos -= 3600
    horas += 1

while segundos >= 60:
    segundos -= 60
    minutos += 1

print(horas,'horas,',minutos,'minutos,',segundos,'segundos')


#Practiqué el uso de ciclos WHILE en Python.







