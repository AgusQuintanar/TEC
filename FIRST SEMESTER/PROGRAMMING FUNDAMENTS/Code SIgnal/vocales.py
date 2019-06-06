cadena = input('Ingrese su cadena: ')
cadena = cadena.lower()
voc = ['a','e','i','o','u']
b = 0
for x2 in voc:
    b += cadena.count(x2)
print(b)
