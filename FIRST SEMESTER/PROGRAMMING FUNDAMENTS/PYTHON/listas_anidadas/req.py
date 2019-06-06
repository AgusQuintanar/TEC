#Ingreso de texto
def Textoo():
  global Texto
  Texto=str(input("Escribe un texto: "))

#Numero de caracteres
def CaracteresTotales (x):
  global CaracteresTotalitos
  CaracteresTotalitos=len(Texto)
  print ("")
  print ("Caracteres totales: ")
  print(CaracteresTotalitos)

#Numero de palabras
def TextoLista (x):
  global NumeroPalabras
  TextoListita=x.split()
  NumeroPalabras=len(TextoListita)
  print ("")
  print("Número de palabras: ")
  print(NumeroPalabras)

#Función para encontrar la palabras más grande entre dos palabras
def mayor2palabras(a,b):
  r1 = len(a)
  r2 = len(b)
  if(r1>r2):
    resultado = a
  else:
    resultado = b
  return resultado

#Función para definir la palabras más grande (cambio de posición)
def PalabraMasGrande(n):
  global mayor
  global TextoLista
  TextoLista=Texto.split(" ")
  palabra_menor = TextoLista[0]
  for t in range(len(TextoLista)):
      if len(TextoLista[t]) < len(palabra_menor):
          palabra_menor = TextoLista[t]
  return palabra_menor

#Funcion palabra más grande
def PalabraGrande (m):
  r = PalabraMasGrande(m)
  print ("")
  print("Una de las palabras más grandes es: ")
  print(r)

#Funcion para el conteo de letras
def abc(a):
  print ("")
  print("El desglose de letras: ")
  x = a.lower()
  ABC = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","á","é","í","ó","ú","0","1","2","3","4","5","6","7","8","9"]
  i=0
  n=len(ABC)
  veces =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  while(i<n):
    veces[i] = x.count(ABC[i])
    y=ABC[i]
    print(y,":",veces[i])
    i += 1

#Funcion para reemplazar
def remplazo(a):
  x = a
  y = x.replace("a", "*")
  z = y.replace("e", "·")
  s = z.replace("i", "#")
  k = s.replace("o", "&")
  o = k.replace("u", "!")
  t = o.replace("b","1")
  a = t.replace("c","2")
  b = a.replace("d","3")
  c = b.replace("f","=")
  d = c.replace("g","4")
  e = d.replace("h","5")
  f = e.replace("l","6")
  g = f.replace("j","7")
  h = g.replace("h","8")
  i = h.replace("j","9")
  j = i.replace("k","?")
  m = j.replace("p",";")
  print ("El texto cifrado es:")
  print(m)

  x = a
  y = x.replace("*","a")
  z = y.replace("·","e")
  s = z.replace("#","i")
  k = s.replace("&","o")
  o = k.replace("!","u")
  t = o.replace("1","b")
  a = t.replace("2","c")
  b = a.replace("3","d")
  c = b.replace("=","f")
  d = c.replace("4","g")
  e = d.replace("5","h")
  f = e.replace("6","l")
  g = f.replace("7","j")
  h = g.replace("8","h")
  i = h.replace("9","j")
  j = i.replace("?","k")
  m = j.replace(";","p")
  print ("El texto descifrado es:")
  print(m)

#Llamar función 0
Funcion0 = Textoo()

while (True):
  print ("1. Introducir texto nuevo")
  print ("2. Caracteres Totales")
  print ("3. Numero de palabras")
  print ("4. Palabra mas grande")
  print ("5. Desglose de letras")
  print ("6. Cifrar y descifrar")
  print ("7. Salir")

  opcion = int(input())
  if (opcion==1):
    #Llamar función 0
    Funcion0 = Textoo()

  if (opcion==2):
    #Llamar función 1
    Funcion1 = CaracteresTotales (Texto)

  if (opcion==3):
    #Llamar función 2
    Funcion2 = TextoLista (Texto)

  if (opcion==4):
    #Llamar función 3
    Funcion3 = PalabraGrande(Texto)

  if (opcion==5):
    #Llamar función 4
    Funcion4 = abc (Texto)

  if (opcion==6):
    Funcion5 = remplazo (Texto)
  if (opcion==7):
    break