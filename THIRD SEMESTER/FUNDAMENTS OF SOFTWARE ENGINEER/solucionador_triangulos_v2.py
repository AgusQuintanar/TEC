###################################################################
#   Autor: Agustín Salvador Quintanar de la Mora                  #  
#   Matricula: A01636142                                          #  
#   Fecha de creacion: 3 de Septiembre del 2019                   #
#   Solucionador de triangulo                                     #
################################################################### 

from math import sqrt

def calcular_distancia_entre_2_puntos(coor1,coor2):
    return sqrt((float(coor2[0])-float(coor1[0]))**2 + (float(coor2[1])-float(coor1[1]))**2)

def pedir_datos():

    coor1 = input("Ingrese las coordenadas del vertice 1 separadas por una coma: ").split(',')
    coor2 = input("Ingrese las coordenadas del vertice 2 separadas por una coma: ").split(',')
    coor3 = input("Ingrese las coordenadas del vertice 3 separadas por una coma: ").split(',')1

    lado1 = calcular_distancia_entre_2_puntos(coor1,coor2)
    lado2 = calcular_distancia_entre_2_puntos(coor2,coor3)
    lado3 = calcular_distancia_entre_2_puntos(coor1,coor3)
    return [lado1,lado2,lado3]

def calcular_area_triangulo():
    opcion = '1'
    while opcion == '1':
        datos = pedir_datos()
        a = datos[0]
        b = datos[1]
        c = datos[2]
        s = (a+b+c)/2

        area = sqrt(s*(s-a)*(s-b)*(s-c))

        print('El area del triangulo es de:',area,'unidades cuadradas.')

        print('Desea volver a calcular el area de un triangulo?\n\n[1] Si\n[2] No')
        opcion = input('Opcion a ejecutar:')
        while opcion != '1' and opcion != '2':
            print('Ingrese una opcion valida.')
            opcion = input('Opcion a ejecutar:')
    menu(2)

def menu(opcion_seleccionada):
    
    print('''
MENU GENERAL

    [1] Calcular el area de un triangulo
    [2] Salir

        ''')
    

    if opcion_seleccionada == '1':
        calcular_area_triangulo()
    elif opcion_seleccionada == '2':
        print('Programa finalizado exitosamente.')
 
        

def main():
    print('Bienvenido al solucionador de triangulos.\nFavor de seleccionar un opcion a ejecutar.')

    opcion_seleccionada = 0
    while opcion_seleccionada != '2':
        menu(opcion_seleccionada)
        opcion_seleccionada = input('Opcion a ejecutar: ')
        while opcion_seleccionada != '1' and opcion_seleccionada != '2':
            print('Opcion no valida.')
            opcion_seleccionada = input('Opcion a ejecutar: ')

main()