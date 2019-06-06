# -*- coding: utf-8 -*-
#FUNCIONES

'''
DEFINICIÓN DE FUNCION:
En Python, la definición de funciones se realiza mediante la instrucción def más un nombre de función descriptivo -para el cuál, aplican las mismas reglas que para el nombre de las variables- seguido de paréntesis de apertura y cierre. Como toda estructura de control en Python, la definición de la función finaliza con dos puntos (:) y el algoritmo que la compone, irá identado con 4 espacios.

PARAMETROS
Un parámetro es un valor que la función espera recibir cuando sea llamada (invocada), a fin de ejecutar acciones en base al mismo. Una función puede esperar uno o más parámetros (que irán separados por una coma) o ninguno.

    * siempre se le deben pasar sus argumentos en el mismo orden en el que los espera
    
LLAMADAS DE RETORNO
    En Python, es posible llamar a una función dentro de otra, de forma fija y de la misma manera que se la llamaría, desde fuera de dicha función.
    
COMPROBAR QUE EXISTE UNA FUNCIÓN
    
    Durante una llamada de retorno, el nombre de la función, puede no ser el indicado. Entonces, siempre que se deba realizar una llamada de retorno, es necesario comprobar que ésta exista y pueda ser llamada.
    
    Ejemplo:
        if nombre_de_la_funcion in locals():
        if callable(locals()[nombre_de_la_funcion]):
        print locals()[nombre_de_la_funcion]("Emilse")
    
LLAMADAS RECURSIVAS
    Se denomina llamada recursiva (o recursividad), a aquellas funciones que en su algoritmo, hacen referencia sí misma.
    
    Las llamadas recursivas suelen ser muy útiles en casos muy puntuales, pero debido a su gran factibilidad de caer en iteraciones infinitas, deben extremarse las medidas preventivas adecuadas y, solo utilizarse cuando sea estrictamente necesario y no exista una forma alternativa viable, que resuelva el problema evitando la recursividad.
    '''
#EJEMPLOS

def mi_funcion():
    print ('Curso Python')

mi_funcion()

#--------------------------------------------------------------------------------------------------------
print ("..................................................................................................")

def mi_funcion_2(name):
    print ('hola',name)

mi_funcion_2("Oscar")

#--------------------------------------------------------------------------------------------------------
print ("..................................................................................................")


def mi_funcion_3(name2='anonimo'):
    print ('hola',name2)

mi_funcion_3()

#--------------------------------------------------------------------------------------------------------
print ("..................................................................................................")

def suma_fracciones(n1,d1,n2,d2):

    rn = (n1*d2) + (n2*d1)
    rd = d1*d2

    print (str(rn),"/",str(rd))

n1 = int(input("Ingrese el numerador de la primera fraccion "))
d1 = int(input("Ingrese el denumerador de la primera fraccion "))
n2 = int(input("Ingrese el numerador de la segunda fraccion "))
d2 = int(input("Ingrese el denumerador de la segunda fraccion "))

suma_fracciones(n1,d1,n2,d2)

#--------------------------------------------------------------------------------------------------------
print ("..................................................................................................")

def contar(cadena):

    cadena1=str(cadena.lower())

    a = cadena1.('a')
    e = cadena1.count('e')
    i = cadena1.count('i')
    o = cadena1.count('o')
    u = cadena1.count('u')


    if a > e and a > i and a > o and a > u:
        print ("La a se repite mas veces")

    elif e > a and e > i and e > o and e > u:
        print ("La e se repite mas veces")

    elif i > a and i > e and i > o and i > u:
        print ("La i se repite mas veces")

    elif o > a and o > e and o > i and o > u:
        print ("La o se repite mas veces")

    elif u > a and u > e and u > i and u > o:
        print ("La u se repite mas veces")

    else:
        print ("Ninguna tiene mayor repeticion")


cadena = input("Ingrese su cadena ")
contar(str(cadena))

#--------------------------------------------------------------------------------------------------------
print ("..................................................................................................")

# ord('á') Obtiene el valor ASCCI del valor dado
# chr(64) Obtiene el caracter


def suma_n_numeros(n);

    a = n.split('+')
    print (n + ' = ' + str(eval('+'.join(a))))

b=input("Ingrese la suma de n numeros separados por (+): ")
suma_n_numeros(b)

#--------------------------------------------------------------------------------------------------------
print ("..................................................................................................")


def suma_n_numeros_pro(*numeros) #El asterisco simboliza n
    sum=0
    for x in numeros:
        sum += x
    print (sum)

suma_n_numeros_pro(1,2,3,4,5)

#--------------------------------------------------------------------------------------------------------
print ("..................................................................................................")

#Fuciones lambda (Son funciones anonimas)
print ("Funciones Lambda")
print ('')

myfunc = lambda i: i*2
print (myfunc(2))

myfunc2 = lambda i,j: i*j
print (myfunc2(5,3))

print ("")
print ("try: Dentro del bloque try se ubica todo el código que pueda llegar a levantar una excepcion, se utiliza el termino levantar para referirse a la accion de generar una excepción")
print ('Finally: Puede ubicarse un bloque finally donde se escriben las sentencias de finalizacion, que son  tipicamente acciones de limpieza.')
print ('Permite ejecutar algo si se produce un error como print')



print (6/6)
print (0/5)

try:
    5/0
except:
    print ("No se permite division entre cero")



a = float(input("Ingrese el dividendo: "))
b = float(input('Ingrese el divisor: '))

try:
    a/b
except:
    print ('No se puede dividir entre 0')

#FUENTES

'''
    Apuntes de curso Python de Tec Gurus
    https://librosweb.es/libro/python/capitulo-4/definiendo-funciones.html
    https://librosweb.es/libro/python/capitulo-4/llamadas-de-retorno.html
    https://librosweb.es/libro/python/capitulo-4/llamadas-recursivas.html
    https://librosweb.es/libro/python/capitulo-4/sobre-la-finalidad-de-las-funciones.html
    













