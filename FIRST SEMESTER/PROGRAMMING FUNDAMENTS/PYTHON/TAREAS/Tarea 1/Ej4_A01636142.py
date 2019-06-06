#-*- coding: utf-8 -*-
#Agustín Salvador Quintanar de la Mora
#A01636142

#Calculador de interes simple

cantidad = float(input('Ingrese la cantidad a la que le desea calcular el interés simple: '))
años = int(input('Ingrese el número de años con los que desea calcular el interés: '))
interes=float(input('Ingrese el interés aplicado a su cantidad: '))

interes_simple = (cantidad * años * interes) / 100

print('El interés simple es de: ${0:6.2f}'.format(interes_simple))

#Aprendí a calcular el interés simole, así como realizar el formateo tipo Python.