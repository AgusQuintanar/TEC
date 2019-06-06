#Agustin Slavador Quintanar de la Mora       A01636142

import random
from time import sleep

def simulacion():
    '''
    Esta funcion genera una lista anidada con 0s y 1s aleatorios y los escribe en un archivo de texto plano.
    :return:
    '''
    estacionamiento = [[random.randint(0,1) for y in range(15) ] for x in range(10)]
    archivo = open('estacionamiento_generado.txt','w')
    for x in range(len(estacionamiento)):
        for y in range(len(estacionamiento[x])):
            estacionamiento[x][y] = str(estacionamiento[x][y])
        archivo.write(','.join(estacionamiento[x])+'\n')
    archivo.close()

def lee_archivo():
    '''
    Regresa lista anidada del archivo estacionamiento_generado.txt
    :return:
    '''
    archivo = open('estacionamiento_generado.txt','r')
    estacionamiento = [(x.rstrip()).split(',') for x in archivo]
    archivo.close()
    return estacionamiento

def genera_vacios(est):
    '''
    Regresa la lista de lugares disponibles en el estacionamiento de manera alfanumerica.
    :param est:
    :return:
    '''
    return [chr(x + 65) + str(y + 1) for x in range(len(est)) for y in range(len(est[x])) if est[x][y] == '0']

def escribe_vacios(lista_vacios):
    'Escribe los lugares vacios de la lista que retorns genera_vacios en un archivo de texto plano llamada vacios.txt'
    archivo = open('vacios.txt', 'w')
    archivo.write(', '.join(lista_vacios))
    archivo.close()


simulacion()
print('Datos recibidos del sistema de sensores...')
sleep(1)
lista_estacionamiento = lee_archivo()
print('Lectura de archivo completada...')
sleep(1)
lista_vacios = genera_vacios(lista_estacionamiento)
print('Lista de lugares vacios generada...')
sleep(1)
escribe_vacios(lista_vacios)
print('Escritura del archivo vacios.txt completada...')

