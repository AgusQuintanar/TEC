#-*- coding: utf-8 -*-
#Agustín Salvador Quintanar de la Mora
#A01636142

#Indice de masa corporal

print('Bienvenido al calculador del IMC')

peso_en_libras = float(input('Ingrese su peso en libras: '))
estatura_en_pulgadas = float(input('Ingrese su estatura en pulgadas: '))

peso_en_kilos = peso_en_libras * 0.453592
estatura_en_metros = (estatura_en_pulgadas * 0.0254)


imc = peso_en_kilos/(estatura_en_metros**2)

print('')
print('-------------------------------------------------------------------------------------')
print('RESULTADOS')
print('-------------------------------------------------------------------------------------')
print('')

print('Su peso es de ' + str(peso_en_kilos) + ' kilogramos')
print('Su estatura es de ' + str(estatura_en_metros) + ' metros')
print('')
print('Su IMC es de ' + str(imc))

#Aprendí a efectuar coversiones en Python
