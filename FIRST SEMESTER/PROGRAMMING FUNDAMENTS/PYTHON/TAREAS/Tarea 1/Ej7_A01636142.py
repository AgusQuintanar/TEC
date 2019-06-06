#-*- coding: utf-8 -*-
#Agustín Salvador Quintanar de la Mora
#A01636142

#Ejercicio 7

import math

lado_a = float(input('Ingrese la medida del lado (a) del triangulo: '))
lado_b = float(input('Ingrese la medida del lado (b) del triangulo: '))
lado_c = float(input('Ingrese la medida del lado (c) del triangulo: '))

semiperimetro = (lado_a+lado_b+lado_c)/2

area = math.sqrt(semiperimetro*(semiperimetro-lado_a)*(semiperimetro-lado_b)*(semiperimetro-lado_c))

print('')
print('El área del triangulo es de:',area)

#Aprendí a calcular la ley de Herón en Python, y utilicé la función SQRT de la libreria Math.