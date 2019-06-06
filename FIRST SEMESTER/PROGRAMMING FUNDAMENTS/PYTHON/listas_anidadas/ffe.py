def palabras_chidas(numero_palabras):
    palabras = []
    for i in range(numero_palabras):
        palabra = input('Palabra '+str(i+1)+': ')
        palabras.append(palabra)

    respuesta = ''
    palabra_ch = palabras[0]
    for j in range(len(palabras)):
        if len(palabras[j]) <= len(palabra_ch) and len(palabras[j])%2 == 0:
            palabra_ch = palabras[j]
            respuesta = 'Palabra: ' + palabra_ch + ' || Numero de caracteres: ' + str(len(palabra_ch)) + ' || Tipo: Par'
        elif len(palabras[j]) <= len(palabra_ch) and len(palabras[j])%2 != 0:
            palabra_ch = palabras[j]
            respuesta = 'Palabra: ' + palabra_ch + ' || Numero de caracteres: ' + str(len(palabra_ch)) + ' || Tipo: Impar'

    return respuesta

numero_palabras = int(input('Ingrese el numero de palabras que desea ingresar: '))
print(palabras_chidas(numero_palabras))

