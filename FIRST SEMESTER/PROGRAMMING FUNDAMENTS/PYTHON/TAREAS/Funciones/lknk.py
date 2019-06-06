rojo = '\033[91m'
salmon = '\033[31m'
endcolor = '\033[0m'
verde  = '\33[32m'
amarillo = '\33[33m'
azul_bajito   = '\33[96m'
azul_agua = '\033[36m'

violeta = '\33[35m'


for i in range (99):
    print(i)
    print('\033['+str(i)+'m'+'hola'+endcolor)