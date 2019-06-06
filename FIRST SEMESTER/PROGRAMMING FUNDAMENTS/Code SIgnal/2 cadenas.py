cadena1 = input('Ingrese su cadena 1: ')
cadena1 = cadena1.lower()
cadena2 = input('Ingrese su cadena 2: ')
cadena2 = cadena2.lower()

voc = ['a','e','i','o','u']
c1 = 0
c2 = 0
for x2 in voc:
    c1 += cadena1.count(x2)
    c2 += cadena2.count(x2)

if c1 > c2:
     print('La cadena uno tiene más vocales')
elif c2 > c1:
    print('La cadena dos tiene más vocales')
else:
    print('Tiene la misma cantidad de vocales')