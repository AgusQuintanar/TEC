# Agustin Salvador Quintanar de la Mora
#A01636142

import random
import os

rojo = '\033[91m'
salmon = '\033[31m'
endcolor = '\033[0m'
verde  = '\33[32m'
amarillo = '\33[33m'
azul_bajito   = '\33[96m'
azul_agua = '\033[36m'

violeta = '\33[35m'
fondo = azul_bajito

ahorcado_soga = fondo+'''

 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        || 
| |/         || 
| |          ||  
| |         ()()
| |        ()  ()
| |        ()  ()
| |         ()()
| |     
| |     
| |     
| |     
| |     
| |     
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .

'''+endcolor

ahorcado_cara = fondo+'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.´´´´.
| |/         |/  _   \\
| |          ||  `/,
| |          (\\\`_.
| |           `-- '
| |      
| |     
| |     
| |     
| |     
| |     
| |     
| |     
| |     
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .

'''+endcolor

ahorcado_cuerpo = fondo+'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.´´´´.
| |/         |/  _   \\
| |          ||  `/,
| |          (\\\\`_
| |         .-`-- '.
| |          Y   Y
| |          |   | 
| |          |   |  
| |          | _ |  
| |                 
| |                 
| |                 
| |                 
| |                
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .

'''+endcolor
ahorcado_brazo_izquierdo =fondo+ '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.´´´´.
| |/         |/  _   \\
| |          ||  `/,
| |          (\\\\`_.
| |         .-`-- '.
| |        /Y     Y
| |       // |   | 
| |      //  |   | 
| |     ')   | _ |
| |         
| |         
| |         
| |         
| |         
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .

'''+endcolor
ahorcado_brazo_derecho = fondo+'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.´´´´.
| |/         |/  _   \\
| |          ||  `/,
| |          (\\\\`_.
| |         .-`-- '.
| |        /Y     Y\\
| |       // |   | \\\\
| |      //  |   |  \\\\
| |     ')   | _ |   (`
| |         
| |         
| |         
| |         
| |         
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .

'''+endcolor
ahorcado_pierna_izquierda = fondo+'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.´´´´.
| |/         |/  _   \\
| |          ||  `/,
| |          (\\\\`_.
| |         .-`-- '.
| |        /Y     Y\\
| |       // |   | \\\\
| |      //  |   |  \\\\
| |     ')   | _ |   (`
| |          || 
| |          || 
| |          || 
| |          || 
| |         / | 
""""""""""|_`-'     |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .

'''+endcolor
ahorcado_completo =fondo+'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.´´´´.
| |/         |/  _   \\
| |          ||  `/,
| |          (\\\\`_.
| |         .-`-- '.
| |        /Y     Y\\
| |       // |   | \\\\
| |      //  |   |  \\\\
| |     ')   | _ |   (`
| |          || ||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \\
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .

'''+endcolor

#Esto es una lista que contiene los distintos acertijos separados por categoria y dificultad.
acertijos = [
    [
        ['Mexico','Estados Unidos','Canada','Argentina', 'Chile', 'Paraguay', 'Francia', 'Alemania', 'Italia',
                'España', 'China', 'Rusia', 'Japon', 'Brasil'],
        ['Costa Rica', 'Panama', 'Australia', 'Reino Unido', 'Marruecos', 'Egipto', 'Finlandia', 'Suecia',
                'El Salvador', 'Guatemala', 'Nicaragua'],
        ['Tuvalu', 'Samoa', 'Yibuti', 'Kirguistan', 'Dominica', 'Maldivas', 'Tonga', 'Vanuatu', 'Timor Oriental',
                'Santo Tome y Pricipe', 'San Vicente y las Granadinas', 'San Cristobal y nieves']
    ],

    [
        ['Vaca', 'Oso', 'Leon', 'Gallo', 'Gato', 'Oveja', 'Toro', 'Topo', 'Perro', 'Zorro', 'Mono', 'Pato',
                'Rana', 'Raton', 'Burro', 'Foca', 'Loro' ],
        ['Aguila', 'Ballena', 'Avispa', 'Caballo', 'Canario', 'Elefante', 'Serpiente', 'Hipopotamo','Jabali',
                'Tortuga', 'Caracol', 'Jirafa', 'Mosquito'],
        ['Golondrina', 'Saltamontes', 'Chimpance', 'Ormitorrinco', 'Jerboa', 'Falangero', 'Dragon de Komodo',
                'Triglidae', 'Oso Hormiguero', 'Rape', 'Gavial']
    ],

    [
        ['Titanic', 'El rey leon', 'Shrek', 'El hombre Araña', 'Harry Potter', 'Monsters Inc', 'Mi pobre angelito',
                'Forrest Gump', 'Jurassic Park', 'Star Wars', 'Batman', 'Buscando a Nemo'],
        ['El Señor de los Anillos', 'La pasion de Cristo', 'El sexto sentidp', 'Los hombres de negro',
                'Transformers', 'Indiana Jones', 'El dia de la Independencia', 'The Matrix', 'Jaws'],
        ['La parada de los monstruos', 'Los Violentos de Kelly', 'Solaris', 'Almas de metal', 'El Jinete Palido',
                'Las aventuras del Baron Munchausen', 'Stalingrado', 'Perfect Blue', 'El reino prohibido' ]
    ],

    [
        ['La Biblia', 'Harry Potter', 'El Señor de los Anillos', 'El Alquimista', 'El Codigo da Vinci', ' Crepusculo',
                'Lo que el viento se llevo', 'El diario de Ana Frank', 'El principito', 'Divina Comedia'],
        ['Las mil y una noches', 'Decameron', 'Don Quijote de la Mancha', 'Cien años de soledad', 'El viejo y el mar',
                'Diario de un loco', 'Moby Dick', '1984', 'Edipo rey', 'Ramayana', 'Hamlet', 'La montaña magica'],
        ['Libro del desasosiego', 'Genji Monogatari', 'Pippi Calzaslargas', 'En busca del tiempo perdido',
                'Vida y opiniones del caballero Tristram Shandy', 'Mahabharata', 'La señora Dalloway']
    ],

    [
        ['Pizza', 'Hamburguesa', 'Tacos', 'Sushi', 'Donas', 'Galletas', 'Ensalada', 'Nuggets', 'Papas a la Francesa',
                'Burrito', 'Fajitas', 'Ceviche', 'Crepa'],
        ['Milanesa', 'Pollo a la naranja', 'Fondue de queso', 'Huevo estrellado', 'Lasagna', 'Quesadillas',
                'Falafel', 'Vegemite', 'Poutine', 'Bacalao', 'Paella'],
        ['Wiener Schnitzel', 'Schweinshaxe', 'Chili con carne', 'El pabellon criollo', 'Silpancho', 'Pato laqueado',
                'Lahmacun', 'Bulgogi', 'Borsch', 'Cuscus', 'Baba Ghanoush']
    ],

    [
        ['Tennis', 'Futbol', 'Voleibol', 'Natacion', 'Baloncesto', 'Beisbol', 'Badmiton', 'Beisbol', 'Balonmano',
                'Hockey', 'Rugby', 'Boxeo', 'Surf'],
        ['Tiro con arco', 'Ciclismo', 'Paracaidismo', 'Gimnasia', 'Waterpolo', 'Karate', 'Futbol americano',
                'Equitacion', 'Patinaje sobre hielo', 'Frontenis', 'Judo'],
        ['Muay Thai', 'Rafting', 'Windsurf', 'Parapente', 'Kendo', 'Piraguismo', 'Halterofilia', 'Crocket',
                'Sokatira', 'Bobsleigh', 'Motonautica', 'Lacrosse']
    ],

    [
        ['Apple', 'Samsung', 'Facebook', 'Amazon', 'Youtube', 'Tesla', 'Coca Cola', 'Adidas', 'Nike',
                'KFC', 'McDonalds', 'Gerber', 'Disney', 'Gillete', 'Kodak'],
        ['General Electric', 'AT&T', 'Nestle', 'HP', 'Lenovo', 'Burger King', 'Mater Card',
                'Kleenex', 'Intel', 'Visa', 'Gucci', 'Oral B', 'Fedex', 'Subway'],
        ['Budweiser', 'Sony Ericsson', 'Alibaba', 'Bank Of America', 'Chupa Chups', 'Castrol', 'Unilever',
                'Napster', 'Hudson Bay Company', 'Dischord Records', 'Quirky', ]
    ],

    [
        ['Call of Duty', 'Fallout', 'FIFA', 'GTA', 'Tetris', 'Minecraft', 'Fortnite', 'Pac Man', 'Pong',
                'Mortal Kombat', 'PUBG', 'Final Fantasy', 'League of Legends'],
        ['The last of Us', 'God of War', 'Super Mario World', 'Counter Strike', 'Wii Sports', 'Battlefield',
                'The legend of Zelda', 'Destiny', 'Overwatch', 'Space Invaders'],
        ['StarCraft', 'Monster Hunter', 'Horizon Zero Down', 'Bayonetta', 'Age of Empires', 'Shadow of the Colossus',
                'Dragon Ball FighterZ', 'Donkey Kong Country', 'Metal Slug']
    ]

]

def clear():
    '''
    Esta funcion se encarga de limpiar la pantalla de la consola
    :return:
    '''
    os.system("cls" if os.name == "nt" else "clear")

def validacion_categoria (entrada):
    '''
    Esta funcion se encarga de recibir el input de la variable categoria y validar que sea un entero dentro del
    rango permitido.
    :param entrada:
    :return:
    '''
    while True:
        try:
            int(entrada)
        except ValueError:
            print("Entrada no valida.  Intentelo de nuevo...")
            entrada = input('Nueva entrada: ')
        else:
            if int(entrada) not in range (1,10):
                print("Entrada no valida.  Intentelo de nuevo...")
                entrada = input('Nueva entrada: ')
            else:
                clear()
                return int(entrada)

def validacion_menu_principal (entrada):
    '''
    Esta funcion se encarga de comprobar que el input del menu principal sea valido y este dentro del rango permitido.
    :param entrada:
    :return:
    '''
    while True:
        try:
            int(entrada)
        except ValueError:
            print("Entrada no valida.  Intentelo de nuevo...")
            entrada = input('Nueva entrada: ')
        else:
            if int(entrada) not in range (1,5):
                print("Entrada no valida.  Intentelo de nuevo...")
                entrada = input('Nueva entrada: ')
            else:
                clear()
                return int(entrada)

def validacion_dificultad(entrada):
    '''
    Esta funcion se encarga de comprobar que el input de la dificultad sea valido y este dentro del rango permitido.
    :param entrada:
    :return:
    '''
    while True:
        try:
            int(entrada)
        except ValueError:
            print("Entrada no valida.  Intentelo de nuevo...")
            entrada = input('Nueva entrada: ')
        else:
            if int(entrada) not in range (1,4):
                print("Entrada no valida.  Intentelo de nuevo...")
                entrada = input('Nueva entrada: ')
            else:
                clear()
                return int(entrada)


lista_categorias = ['Paises', 'Animales', 'Peliculas', 'Libros', 'Comida', 'Deportes',
                   'Nombres de empresas', 'Videojuegos']
lista_dificultad = ['Fácil','Intermedia','Díficil']

mono_ahocardo = [ahorcado_completo, ahorcado_pierna_izquierda, ahorcado_brazo_derecho,
                 ahorcado_brazo_izquierdo, ahorcado_cuerpo, ahorcado_cara, ahorcado_soga]

def seleccion_categoria():
    '''
    Esta funcion imprime las diversas categorias al usuario, para posteriormente retornarla cuando se necesite.
    :return:
    '''
    print('\33[1m'+salmon+'''
Seleccione la categoria que desea ejecutar.'''+'\n'

+'\n'+azul_agua+'''[1]'''+endcolor+''' Paises'''
+'\n'+azul_agua+'''[2]'''+endcolor+''' Animales'''
+'\n'+azul_agua+'''[3]'''+endcolor+''' Peliculas'''
+'\n'+azul_agua+'''[4]'''+endcolor+''' Libros'''
+'\n'+azul_agua+'''[5]'''+endcolor+''' Comida'''
+'\n'+azul_agua+'''[6]'''+endcolor+''' Deportes'''
+'\n'+azul_agua+'''[7]'''+endcolor+''' Nombres de empresas'''
+'\n'+azul_agua+'''[8]'''+endcolor+''' Videojuegos'''
+'\n'
+'\n'+azul_agua+'''[9]'''+endcolor +''' Regresar al menu principal'''+'\n')

    categoria = validacion_categoria(input(verde+'Numero de opcion a ejecutar: '+endcolor))
    if categoria == 9:
        clear()
        menu_general()
    else:
        clear()
        return categoria

def seleccion_dificultad():
    '''
    Esta funcionimprime las diversas dificultades al usuario, para posteriormente retornarla cuando se necesite
    :return:
    '''
    print('\33[1m'+salmon+'''
Selecciona la dificultad que desea jugar.'''+'\n'

+'\n'+azul_agua+'''[1]'''+endcolor+'''Facil'''
+'\n'+azul_agua+'''[2]'''+endcolor+'''Intermedio'''
+'\n'+azul_agua+'''[3]'''+endcolor+'''Díficil'''
   +'\n')
    dificultad = validacion_dificultad(input('Numero de opcion a ejecutar: '))
    return dificultad



def ahorcado(palabra_a_adivinar):
    '''
    Esta funcion se encarga de recibir la palabra a adivinar, la cual es procesada para realizar el juego del
    ahorcado.
    :param palabra_a_adivinar:
    :return:
    '''
    intentos = 6
    letras_usadas = []
    palabra_en_guiones = []
    for i in range(len(palabra_a_adivinar)):
        if palabra_a_adivinar[i] != ' ':
            palabra_en_guiones.append('__ ')
        else:
            palabra_en_guiones.append('  ')
    while True:
        print(rojo+'Intentos restantes:'+endcolor,intentos)
        print('\n\33[44m'+'Letras/Dígitos utilizados:'+endcolor,', '.join(letras_usadas))
        print(verde+'\nPalabra:'+endcolor,''.join(palabra_en_guiones))
        print(mono_ahocardo[intentos])
        letra_usuario = input('Ingrese una letra/dígito: ')
        while len(letra_usuario) != 1:
            print('Ingrese una letra o digito válido.')
            letra_usuario = input('Ingrese una letra/dígito: ')
        while letra_usuario in letras_usadas:
            letra_usuario = input('Ingrese una letra diferente: ')

        letras_usadas.append(letra_usuario)

        if letra_usuario.lower() in palabra_a_adivinar or letra_usuario.upper() in palabra_a_adivinar:
            for letra in range(len(palabra_a_adivinar)):
                if letra_usuario.lower() == palabra_a_adivinar[letra].lower():
                    palabra_en_guiones[letra] = palabra_a_adivinar[letra]+' '
        else:
            intentos -= 1
        clear()
        if '__' not in ''.join(palabra_en_guiones):
            print(rojo+'\nPalabra:'+endcolor, ''.join(palabra_en_guiones))
            print(mono_ahocardo[intentos])
            print(verde+'¡Felicidades, haz ganado. La palabra era:'+endcolor, ''.join(palabra_a_adivinar))
            return '1'

        elif intentos == 0:
            print(rojo+'\nPalabra:'+endcolor, ''.join(palabra_en_guiones))
            print(mono_ahocardo[intentos])
            print(salmon+'¡Se te han acabado los intentos!. Suerte para la próxima. La palabra era:'+endcolor,''.join(palabra_a_adivinar))
            return '0'

def ahorcado_vs_pc(categoria,dificultad):
    '''
    Esta funcion recibe los parametros de categoria y dificultad, los cuales provienen de funciones anteriores,
    para posteriormente procesarlas indefinidamente hasta que se termine manualmente.
    :param categoria:
    :param dificultad:
    :return:
    '''
    volver_a_jugar = 'si'
    while volver_a_jugar.lower() == 'si':
        while dificultad == 4:
            seleccion_categoria()
        else:
            print('Ha seleccionado la dificultad:', lista_dificultad[int(dificultad) - 1])
            clear()

        palabra_a_adivinar = acertijos[categoria - 1][dificultad - 1]\
                            [random.randint(0, len(acertijos[categoria - 1][dificultad - 1]) - 1)]
        print('Ha seleccionado la categoria de:', lista_categorias[int(categoria) - 1])
        ahorcado(palabra_a_adivinar)

        volver_a_jugar = input('¿Desea volver a jugar? (Si/No): ')
        clear()
        if volver_a_jugar.lower() == 'si':
            ahorcado_vs_pc(seleccion_categoria(),seleccion_dificultad())

        while volver_a_jugar.lower() != 'si' and volver_a_jugar.lower() != 'no':
            volver_a_jugar = input('''
Ingrese una opción válida.
¿Desea volver a jugar? (Si/No): ''')

    menu_general()

def ahorcado_vs_humano():
    '''
    Esta funcion se encarga de implementar el juego del ahorcado para 2 humanos, mediante la implementacion
    de la funcion ahorcado() y se procesa indefinidamente hasta que se le indique.
    :return:
    '''
    jugadores = [1, 1]
    jugadores.insert(0, input(rojo+'Nombre de jugador 1: '+endcolor))
    jugadores.insert(2, input('\33[34m'+'Nombre de jugador 2: '+endcolor))
    pasar_siguiente_ronda = 'si'

    while pasar_siguiente_ronda.lower() == 'si':
        marcador_jugador_1 = jugadores[1]
        marcador_jugador_2 = jugadores[3]
        clear()
        print('\33[42m'+'Marcador:\n')
        print('\33[101m'+jugadores[0]+':'+endcolor,str(marcador_jugador_1-1))
        print('\33[104m'+jugadores[2]+':'+endcolor,str(marcador_jugador_2-1))

        print('\nTurno del jugador:',jugadores[((marcador_jugador_1+marcador_jugador_2)%2)*2])

        palabra_a_adivinar = input('Ingrese palabra a adivinar por '+jugadores[((marcador_jugador_1+marcador_jugador_2+1)%2)*2]+': ')
        clear()
        if ahorcado(palabra_a_adivinar) == '1':
            jugadores[(((marcador_jugador_1 + marcador_jugador_2 + 1) % 2) * 2) + 1] += 1
        else:
            jugadores[(((marcador_jugador_1 + marcador_jugador_2) % 2) * 2) + 1] += 1

        pasar_siguiente_ronda = input('¿Desea pasar a la siguiente ronda? (Si/No): ')
        while pasar_siguiente_ronda.lower() != 'si' and pasar_siguiente_ronda.lower() != 'no':
            pasar_siguiente_ronda = input('''

Ingrese una opción válida.
¿Desea pasar a la siguiente ronda? (Si/No): ''')

        clear()

    print('Gracias por jugar. Vuelvan pronto.')
    menu_general()


def instrucciones():
    '''
    En esta funcion se encuentran las instrucciones generales del juego del ahorcado.
    :return:
    '''
    instrucciones = ('''
    
    INSTRUCCIONES:
    
    1.- Jugar contra PC
        
        -Seleccione la categoria que desea y su respectiva dificultad.
        -Ingrese cualquier letra, numero o caracter.
        -Sólo tendra 6 intentos para lograr adivinar la palabra
        -Cuando se terminen los intentos o adivine la palabra, tendrá la opcion de seleccionar si desea jugar
          otra vez.
          
    2.- Jugar contra humano
        
        -Ingresen el nombre de los 2 jugadores.
        -Ingrese el jugador correspondiente cualquier letra, numero o caracter.
        -Sólo tendra 6 intentos para lograr adivinar la palabra
        -Cuando se terminen los intentos o adivine la palabra, tendrá la opcion de seleccionar si desea
          pasar a la siguiente ronda del juego.
    ''')
    print(instrucciones)

    if input('Presione ENTER para volver al menu principal: ') == '':
        menu_general()

def menu_general():
    '''
    Esta es la funcion del menu principal, donde selecciona que funcion se va a ejecutar a partir de
    la opcion que se le proporciona.
    :return:
    '''
    clear()
    opcion_menu_general = 0
    print('')
    while opcion_menu_general != 4:
        print('\33[31m' + '''                                                                                      
                                                                                                               v1.0

               ▄████████     ▄█    █▄      ▄██████▄    ████████▄   ▄████████     ▄████████   ████████▄    ▄██████▄
              ███    ███    ███    ███    ███    ███   ███    ███  ███    ███    ███    ███  ███   ▀███  ███    ███
              ███    ███    ███    ███    ███    ███   ███    ███  ███    █▀     ███    ███  ███    ███  ███    ███
              ███    ███   ▄███▄▄▄▄███▄▄  ███    ███   ███    █▀   ███           ███    ███  ███    ███  ███    ███
            ▀███████████  ▀▀███▀▀▀▀███▀   ███    ███   ████████    ███         ▀███████████  ███    ███  ███    ███
              ███    ███    ███    ███    ███    ███   ███    ██▄  ███    █▄     ███    ███  ███    ███  ███    ███
              ███    ███    ███    ███    ███    ███   ███    ███  ███    ███    ███    ███  ███   ▄███  ███    ███
              ███    █▀     ███    █▀      ▀██████▀    ███    ███  ████████▀     ███    █▀   ████████▀    ▀██████▀
              '''+'\33[3m'+'\33[33m'+'''                                                                                
                                                                                                by Agustin Quintanar
             ''' +endcolor+'\33[36m'+'''
                                                                 |/| /¯)
                                                                 |/|/\/
                                                                 |/|\/
                                                                (¯¯¯)
                                                                (¯¯¯)
                                                                /¯¯/\\
                                                               / ,^./\\
                                                              / /   \/\\
                                                             / /     \/\                                                      
                                                             \ \     / /
                                                              \ `---' /
                                                               `-----'                 
        ''' + endcolor +
      '\n\n'+'                                                        '+'\33[104m'+'[1]'+ endcolor + ' Jugar contra PC'+
        '\n'+'                                                        '+'\33'+'[104m'+'[2]'+ endcolor + ' Jugar contra humano'+
        '\n'+'                                                        '+'\33'+'[104m'+'[3]'+ endcolor + ' Instrucciones'+
                                                                             
      '\n\n'+'                                                        '+'\33'+'[45m'+'[4]' + endcolor +' Salir\n'
                                                                                                                                               
             + endcolor)

        opcion_menu_general = validacion_menu_principal(input(verde+'Ingrese opción a ejecutar'+'\33[5m'+': '+endcolor))

        if opcion_menu_general == 1:
            clear()
            ahorcado_vs_pc(seleccion_categoria(),seleccion_dificultad())
        elif opcion_menu_general == 2:
            clear()
            ahorcado_vs_humano()
        elif opcion_menu_general == 3:
            clear()
            print(instrucciones())
        else:
            clear()
            print('''
Finalizado exitosamente.
Vuelva pronto''')
        break


menu_general()


