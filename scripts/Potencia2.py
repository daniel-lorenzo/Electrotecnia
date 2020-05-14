#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:01:56 2020

Indicar cómo calcular Zeq
Circuito con cuatro elementos en escalera

@author: daniel
"""

# Datos:
Z1 = 7+100j # Ohm
Z2 = 2+100j # Ohm
Z3 = 10+0j # Ohm
Z4 = Z3
U = 500 # V
f = 50 # Hz

# función que calcula elementos en paralelo
def prl(x,y):
    return (x*y)/(x + y)

# Cálculo de Zeq
Zp1 = prl(Z3,Z4)
Zp2 = Zp1 + Z2
Zeq = prl(Zp2,Z1)

## Cálculo de las potencias activa (P), reactiva (Q) y aparente (S)

# Cálculo de I1
I1 = U/Zeq
# Cálculo de potencia
S = U*I1.conjugate()
P = S.real
Q = S.imag


""" 
Calcular el valor de la capacidad a colocar en paralelo a la fuente para
que la corriente se reduzca un 90%, indicando el nuevo valor de la corriente
y Qc.
"""

I2 = abs(I1)*0.1

import cmath, math

phi1 = cmath.phase(I1)
phi2 = math.acos( abs(I1)*math.cos( phi1 )/I2 )

S2 = U*I2
Q2 = S2*math.sin(phi2)

Qc = Q - Q2

C = Qc/(2*math.pi*f*U**2)

print('Resultados:')
print('Zeq = {:.1f} Ohm'.format(Zeq))
print('|S| = %.2f VA'%(abs(S)))
print(' P  = %.2f W'%P)
print(' Q  = %.2f VAr'%Q)
print('I2 = %.1f A'%I2)
print('phi1 = %.2f°'%(math.degrees(phi1)) )
print('phi2 = %.2f°'%(math.degrees(phi2)) )
print('|S2| = %.2f VA'%S2 )
print('|Q2| = %.2f VAr'%Q2 )
print('|Qc| = %.2f VAr'%Qc )
print('C = %.2f uf'%(C*1e6))
