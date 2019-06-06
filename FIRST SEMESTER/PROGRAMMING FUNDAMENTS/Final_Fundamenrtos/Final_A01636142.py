#Agustin Salvador Quintanar de la Mora  A01636142
#Examen final


def validacion(n):
    while True:
        try:
            n = float(n)
        except:
            print('Ingrese un dato válido...')
            n = input('Ingrese un nuevo número: ')
        else:
            return n

def mayor_ingresado():
    n = validacion(input('Bienvenido.\nIngrese un número: '))
    numeros_ingresados = []
    while n >= 0:
        numeros_ingresados.append(n)
        n = validacion(input('Ingrese otro número: '))
    return f'\nEl número mayor ingresado es el: {max(numeros_ingresados)}'

mayor_ingresado()
def nomenclatura(edificio,np,nd):
    return [[f'{edificio}{x}-0{y}' if y<10 else f'{edificio}{x}-{y}' for y in range(1,nd+1)] for x in range(np)]

def extension_frecuente(lista_archivos):
    extensiones = []
    for x in range(len(lista_archivos)):
        if lista_archivos[x][len(lista_archivos[x].split('.')[0]):len(lista_archivos[x])] not in extensiones:
            extensiones.append(lista_archivos[x][len(lista_archivos[x].split('.')[0]):len(lista_archivos[x])])
        lista_archivos[x] = lista_archivos[x][len(lista_archivos[x].split('.')[0]):len(lista_archivos[x])]
    ext = [lista_archivos.count(extensiones[x]) for x in range(len(extensiones))]
    return f'Extensión más repetida: {extensiones[ext.index(max(ext))]}'

def triangular(n):
    matriz = []
    for x in range(n):
        renglon = []
        for y in range(x):
            renglon.append(0)
        for z in range(n-x):
            renglon.append(1)
        matriz.append(renglon)

    for x in range(n):
        renglon = []
        for y in range(x):
            if y>0:
                renglon.append(0)
        else:
            renglon.append(1)
        matriz.append(renglon)
    return matriz
print(triangular(3))
def calcula():
    archivo = open('calificaciones.csv','r')
    semestre = open('semestreAD18.txt','w')
    semestre.write('|    Alumno    | Calificación | Leyenda     |\n')
    semestre.write(' ––––––––––––––––––––––––––––––––––––––––––– \n')
    for a in archivo:
        a1 = a.rstrip().split(',')
        if a1[1] != 'Parcial 1':
            promedio = round(float(a1[1])*.3+float(a1[2])*.35+float(a1[3])*.15+float(a1[4])*.2)
            if promedio >= 70:
                status = 'APROBADO'
            else:
                status = 'REPROBADO'
            espacios1 = (14-len(a1[0]))*' '
            espacios2 = (14-len(status))//2*' '
            semestre.write(f'|{a1[0]}{espacios1}|      {promedio}      |  {status}{espacios2}|\n')
    archivo.close()
    semestre.close()


'''
print(nomenclatura('A',3,6))
print(mayor_ingresado())
print(extension_frecuente(['hola.txt','1.txt','2.py','45.sql']))
'''