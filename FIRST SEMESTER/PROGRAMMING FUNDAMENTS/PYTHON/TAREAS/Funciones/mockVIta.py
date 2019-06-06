import random
import os
from time import sleep
print('''
    Bienvenido.
    Porfavor seleccione su sistema operativo.

    [1] Windows
    [2] Mac
    [3] Linux
    ''')
entrada_opcion_os = input('Numero de opcion a ejecutar: ')

def os_clear(entrada_os):
    while True:
        try:
            int(entrada_os)
        except ValueError:
            print("Entrada no valida.  Intentelo de nuevo...")
            entrada_os = input('Nueva entrada: ')
        else:
            while (int(entrada_os) not in range(1, 4)):
                print("Entrada no valida.  Intentelo de nuevo...")
                entrada_os = input('Nueva entrada: ')
            return entrada_os


def validacion_categoria(entrada):
    while True:
        try:
            int(entrada)
        except ValueError:
            print("Entrada no valida.  Intentelo de nuevo...")
            entrada = input('Nueva entrada: ')
        else:
            while (int(entrada) not in range(1, 9)):
                print("Entrada no valida.  Intentelo de nuevo...")
                entrada = input('Nueva entrada: ')
        return int(entrada)


lista_categorias = ['Paises', 'Animales', 'Peliculas', 'Libros', 'Comida', 'Deportes',
                    'Nombres de empresas', 'Videojuegos']


def menu():
    print('''
    Bienvenido.

    Seleccione la categoria que desea ejecutar.

    [1] Paises
    [2] Animales
    [3] Peliculas
    [4] Libros
    [5] Comida
    [6] Deportes
    [7] Nombres de empresas
    [8] Videojuegos

    [9] Salir
    ''')

    categoria = input('Numero de opcion a ejecutar: ')

    print('Ha seleccionado la categoria de:', lista_categorias[validacion_categoria(categoria) - 1])


print(menu())