n = int(input('Ingrese el limite (n): '))
suma = 0
if n > 0:
    for x in range (1,n+1):
        suma += x * (-1) ** x

    print(suma)