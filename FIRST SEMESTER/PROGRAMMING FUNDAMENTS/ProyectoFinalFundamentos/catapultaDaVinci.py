#-*- coding:utf-8 -*-
import math as m

#Constantes y variables
g = -9.81
m_p = 0.0037 #Masa del proyectil
m_b = 0.01145 #Masa de la barra
m_c = 0.02629 #Masa del cilindro
m_d = 0.0128 #Masa del disco
R_d = 0.0341 #Radio del disco
R_c = 0.01195 #Radio del cilindro
l = 0.2698 #Largo del brazo
L = 0.12 #Elongacion final
a0 = float(input('Ingrese el angulo inicial: ')) #Angulo inicial
L0 = (((12-10.3)/76)*(a0+24)+10.3)/100  #Elongacion inicial
h_total = .335 #Altura total
m_equilibrio = 0.0453 #kg
k = 170
d_h = l*(m.sin(52*m.pi/180)-m.sin(a0*m.pi/180)) #Delta altura

w_chida = m.sqrt((6*(k*((L-L0)**2)-g*d_h*(2*m_p+m_b)))/(3*m_d*(R_d**2)+3*m_c*(R_c**2)+2*(l**2)*(m_b+3*m_p)))



def formgen (a, b, c):
    d = (b**2)-(4*a*c)
    if d == 0:
        r1 = -b/(2*a)
        r2 = -b/(2*a)
    elif d > 0:
        r1 = (-b+(d**0.5))/(2*a)
        r2 = (-b-(d**0.5))/(2*a)
    else:
        r1 = str((-b/(2*a))+(((d**2)**0.5)**0.5)/(2*a)) + " i"
        r2 = str((-b/(2*a))-(((d**2)**0.5)**0.5)/(2*a)) + " i"
    if r1 > 0:
        return r1
    else:
        return r2
v0 = w_chida*l
theta = 52 #Angulo de salida
y0 = h_total
t = formgen(-4.905, (m.sin(theta*m.pi/180)*v0), y0)
x = v0*m.cos(theta*m.pi/180)*t
x_ajuste = x-((x-.64)/.99)*.15
hmax = ((v0**2)*(m.sin(theta*m.pi/180))**2/(2*9.81))+y0
print(v0)
print("La altura máxima es " + str(hmax) + "m. " \
    "La distancia horizontal alcanzada es " + str(x_ajuste) + "m. "  \
    "El tiempo al impactar con el piso es " + str(t) +"s.")