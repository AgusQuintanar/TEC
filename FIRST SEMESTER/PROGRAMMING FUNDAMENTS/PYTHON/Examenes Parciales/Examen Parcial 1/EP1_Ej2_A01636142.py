'''
Agustin Salvador Quintanar de la Mora
A01636142
'''
import random

pancho = 0
romulo = 0
cartas_pancho = 'Las cartas de pancho son: '
cartas_romulo = 'Las cartas de romulo son: '
i = 1 #Variable contadora
while i <= 3:
    carta_pancho = random.randrange(1,11) #Cartas con valores aleatorios con la funcion randrange
    carta_romulo = random.randrange(1,11)
    pancho += carta_pancho
    cartas_pancho += str(carta_pancho) + ' '
    romulo += carta_romulo
    cartas_romulo += str(carta_romulo) + '  '
    i += 1


if (pancho > 15 and romulo > 15) or (pancho == romulo): #Mediante condiciones verifica quien gano
    resultado = 'Empatan'
elif pancho > romulo and pancho <= 15 :
    resultado = 'Gana Pancho'
elif romulo > pancho and romulo <= 15:
    resultado = 'Gana Romulo'
elif pancho < romulo and romulo >= 15:
    resultado = 'Gana Pancho'
else:
    resultado = 'Gana Romulo'

print(cartas_pancho)
print(cartas_romulo)
print('Resultado:',resultado)

