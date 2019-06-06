'''
Agustin Salvador Quintanar de la Mora
A01636142
'''
#Se inicializa el menu en 0
menu = '0'
while menu != '3': #Mientras que el menu no sea igual a 3, este corre indefinidamente
    print('''
    MENU
    
    1.- Convertidor de Kilos a Libras
    2.- Convertidor a gruesas y docenas
    
    3.- Salir
    ''')
    
    menu = input('Ingrese el número de indice del menu, que desea ejecutar: ')
    #Mediante condicionales se  crea el menu
    if menu == '1':
        kilogramos = float(input('Ingrese la cantidad en kilogramos que desea convertir: '))
        libras = kilogramos/.453592
        print(kilogramos,'kilogramos =','{0:.2f} libras'.format(libras))
    
    elif menu == '2':
        cantidad = int(input('Ingrese una cantidad entera: '))
        gruesas = cantidad // 144
        docenas = (cantidad % 144)//12
        unidades = cantidad - gruesas*144 - docenas*12
        print(gruesas,'gruesas,',docenas,'docenas,',unidades,'unidades')

    elif menu =='3':
        print('\nHa salido del programa exitosamente')

    else: #Se utiliza para los valores fuera del rango del menu
        print('\n¡¡¡Ingrese un número de indice dentro del rango!!!')






