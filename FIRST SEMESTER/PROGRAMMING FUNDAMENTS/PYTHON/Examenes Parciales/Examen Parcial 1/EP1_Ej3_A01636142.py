'''
Agustin Salvador Quintanar de la Mora
A01636142
'''
valores_Dentro_Rango = 0
rango_Minimo = int(input('Ingrese el limite inferior del rango: '))
rango_Maximo = int(input('Ingrese el limite maximo del rango: '))
valor = rango_Minimo + 1
#Depura el programa hasta que el rango maximo sea mayor al rango minimo
while True:
    if rango_Maximo <= rango_Minimo:
        rango_Maximo = int(input('Ingrese el limite maximo del rango: '))
    else:
        break

while valor > rango_Minimo and valor < rango_Maximo:
    valor = int(input('Ingrese un valor: '))
    if valor > rango_Minimo and valor < rango_Maximo: #Concatena los valores dentro del rango
        valores_Dentro_Rango += 1

print('Valores dentro del rango:',valores_Dentro_Rango)