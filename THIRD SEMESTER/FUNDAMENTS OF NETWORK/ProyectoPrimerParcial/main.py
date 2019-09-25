#-*-coding:utf-8-*-

import pygame, sys, time
from pygame.locals import *
pygame.init()

sonidos = {
'INICIO':'Sonidos/InicioTransmision.mp3',
'FIN':'Sonidos/FinTransmision.mp3',
'$':'Sonidos/$Cash.mp3',
',':'Sonidos/,Gong.mp3',
'_':'Sonidos/_Espacio.mp3',
'ERROR':'Sonidos/Error.mp3',
'0':'Sonidos/0.mp3',
'1':'Sonidos/1.mp3',
'2':'Sonidos/2.mp3',
'3':'Sonidos/3.mp3',
'4':'Sonidos/4.mp3',
'5':'Sonidos/5.mp3',
'6':'Sonidos/6.mp3',
'7':'Sonidos/7.mp3',
'8':'Sonidos/8.mp3',
'9':'Sonidos/YMCA.mp3',
'A':'Sonidos/Aguila.mp3',
'B':'Sonidos/Burro.mp3',
'C':'Sonidos/Caballo.mp3',
'D':'Sonidos/Delfin.mp3',
'E':'Sonidos/Xilofono.mp3',
'F':'Sonidos/Foca.mp3',
'G':'Sonidos/Gallo.mp3',
'H':'Sonidos/Hiena.mp3',
'I':'Sonidos/IceCubes.mp3',
'J':'Sonidos/Jirafales.mp3',
'K':'Sonidos/Kiwi.mp3',
'L':'Sonidos/Ladrido.mp3',
'M':'Sonidos/Maullido.mp3',
'N':'Sonidos/Nutria.mp3',
'Ñ':'Sonidos/Ñoño.mp3',
'O':'Sonidos/Oveja.mp3',
'P':'Sonidos/Pato.mp3',
'Q':'Sonidos/Quyos.mp3',
'R':'Sonidos/Ranas.mp3',
'S':'Sonidos/Serpiente.mp3',
'T':'Sonidos/Tos.mp3',
'U':'Sonidos/Urraca.mp3',
'V':'Sonidos/Vaca.mp3',
'W':'Sonidos/Wookie.mp3',
'X':'Sonidos/Xilofono.mp3',
'Y':'Sonidos/YMCA.mp3',
'Z':'Sonidos/Zorro.mp3'
}



def reproducirSonido(sonido):
    pygame.mixer.music.load(sonido)
    pygame.mixer.music.play()
    time.sleep(2)

def reproducirCaracter(caracter):
    reproducirSonido(sonidos[caracter.upper()])

def convertirHexAChar(hex):
    return bytes.fromhex(hex).decode('utf-8')

estado = 'inicio'
contador = 1

while estado != 'fin':
    estado = input('Caracter '+str(contador)+': ')
    try:
        reproducirCaracter(estado)
        contador += 1
        if estado.upper() == 'ERROR':
            contador -= 2
    except:
        print('Caracter no valido')
