# -*- coding: utf-8 -*-
"""
Circuito con 5 elementos en escalera
Cálculo de impedancia equivalente, Zeq
"""
# Datos:
Z0 = 20+20j # Ohm
Z1 = 0+70j # Ohm
Z2 = 15+15j # Ohm
Z3 = 10+10j # Ohm
Z4 = Z3
U = 200 # V
f = 50 # Hz

# Defino función para calcular elementos en paralelo
def  prl(x,y):
    return (x*y)/(x+y)

Zp1 = prl(Z3,Z4)
Zp2 = Zp1 + Z2
Zp3 = prl(Zp2,Z0)
Zeq = Zp3 + Z1

"""
Cálculo de potencia aparente (P), 
activa (P), reactiva (Q)
"""
# Cálculo de I
I = U/Zeq
# Cálculo de S
S = U*I.conjugate()
P = S.real
Q = S.imag

"""
Calcular el valor de la capacidad a colocar en paralelo a la fuente
para lograr un factor de potencia visto desde la fuente sea igual a
0,9 inductivo, indicando el nuevo valor de la corriente y Qc
"""
import math, cmath
fp = 0.9
phi1 = cmath.phase(I)
phi2 = math.acos(fp)

I2 = abs(I)*math.cos(phi1)/fp
S2 = U*I2
P2 = P
Q2 = S2*math.sin(phi2)
Qc = Q - Q2
C = Qc/(2*math.pi*f*U**2)

print('Resultados::')
print('Zeq = {:.0f} Ohm'.format(Zeq) )
print('|S| = %.0f VA'%(abs(S)) )
print(' P  = %.0f W'%P)
print(' Q  = %.0f VAr'%Q)
print('phi1 = %.2f°'%(math.degrees(phi1)) )
print('phi2 = %.2f°'%(math.degrees(phi2)) )
print('|I2| = %.2f A'%I2)
print('|S2| = %.0f VA'%S2)
print(' P2  = %.0f W'%P2)
print(' Q2  = %.0f VAr'%Q2)
print(' Qc  = %.0f VAr'%Qc)
print(' C   = %.2f uF'%(C*1e6) )