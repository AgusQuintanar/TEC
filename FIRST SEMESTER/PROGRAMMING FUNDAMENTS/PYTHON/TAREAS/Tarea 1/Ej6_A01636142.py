#-*- coding: utf-8 -*-
#Agustín Salvador Quintanar de la Mora
#A01636142

#Ejercicio 6

años = int(input('Ingrese el número de año(s) de los que desea calcular los nacimientos y las muertes: '))

nacimientos = (años * 31536000) // 7
muertes = (años * 31536000) // 13

print('')
print('El número estimado de nacimientos en',años,'año(s) es de:',nacimientos)
print('El número estimado de muertes en',años,'año(s) es de:',muertes)

#Aprendí a efectuar la división entera en Python.