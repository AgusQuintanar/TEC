#Ejercicio 1
s = 'aereo'
a = s.replace('e','3')
b = a.replace('o','h')
c = b.replace('a','4')
print(c)

#Ejercicio 2
s = 'hola'
a = s.replace('a','A')
b = a.replace('e','E')
c = b.replace('i','I')
d = c.replace('o','O')
e = d.replace('u','U')
print(e)

#Ejercicio 3
s = 'Hay hola'
s_may = s.upper()
print(s_may)

#Ejercicio 4
s = 'a1b2c3d4e5'
x = y = 0
while x < len(s):
    if s[x].isdigit() == True:
        y += 1
    x += 1
print(y)

#Ejercicio 5

s = 'arigarto'
x = y = 0
while x < len(s):
    if (s[x] == 'i' or s[x] == 'a' or s[x] == 'e') and s[x+1] == 'r':
        y += 1
    x += 1
print(y)