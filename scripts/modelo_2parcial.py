#################################
# Modelo 2do parcial
#################################

import numpy as np
print('#####################')
print('Modelo 2do parcial:')
print('#####################')
print('Datos:')
print('')
print('Ingrese los siguientes valores:')
SN = float(input('SN (potencia nominal) [VA]: ')) # VA
VN1 = float(input('VN1 (voltaje nominal primario) [V]: ')) # V
VN2 =  float(input('VN2 (voltaje nominal secundario) [V]: ')) # V
print('Ensayo de vacío:' )
Po = float(input('Po [W]: '))  ;   
Io = float(input('Io [A]: '))  ;   
Vo = float(input('Vo [V]: '))  ;   
print('Ensayo de cortocircuito:')
Pcc = float(input('Pcc [W]: ')) # W
Icc = float(input('Icc [A]: '))  # A
Vcc = float(input('Vcc [V]: '))  # V
print('Rendimiento:')
fp = float(input('fp (factor de potencia): '))
print('Rendimiento máximo: ')
fp_max = float(input('fp_max (factor de potencia máximo): '))

#########################
# Corrientes nominales:
#########################

IN1 = SN/VN1
IN2 = SN/VN2
a = VN1/VN2

##########
# Vacío:
##########

phi_o = np.arccos(Po/(Io*Vo))
Ip = Io*np.cos(phi_o)
Im = Io*np.sin(phi_o)
# Secundario (BT):     # Primario (AT):
Rp2 = Vo/Ip          ;   Rp1 = Rp2*a**2
Xm2 = Vo/Im          ;   Xm1 = Xm2*a**2

##################
# Cortocircuito:
##################

phi_cc = np.arccos(Pcc/(Vcc*Icc))
Zeq1 = Vcc/Icc       ;   Zeq2 = Zeq1/a**2
# Parámetros longitudinales
# Primario:                     # Secundario:
Req1 = Zeq1*np.cos(phi_cc)   ;   Req2 = Zeq2*np.cos(phi_cc)
Xeq1 = Zeq1*np.sin(phi_cc)   ;   Xeq2 = Zeq2*np.sin(phi_cc)

################
# Rendimiento:
################

I2 = fp*IN2         # condición del problema
phi_fp = np.arccos(fp)
Pcu = I2**2 * Req2
V2 = VN2 - I2*(Req2*np.cos(phi_fp) + Xeq2*np.sin(phi_fp))

n = (V2*I2*np.cos(phi_fp))/(V2*I2*np.cos(phi_fp) + Po + Pcu)

######################
# Rendimiento máximo
######################

Pcu = Po
phi_max = np.arccos(fp_max)
I2_nmax = np.sqrt(Po/Req2)
V2_nmax = VN2 - I2_nmax*(Req2*np.cos(phi_max) + Xeq2*np.sin(phi_max))

n_max = (V2_nmax*I2_nmax*fp_max)/(V2_nmax*I2_nmax*fp_max + Pcu + Po)

######################
# Imprime resultados
######################
print()
print('Resulatados:')
print('IN1 = %.2f A'%IN1)
print('IN2 = %.2f A'%IN2)
print('a = %.2f'%a)
print('------------------')
print('Vacío:')
print('------------------')
print('phi_o = %.2f°'%np.rad2deg(phi_o))
print('Ip = %.2f A'%Ip)
print('Im = %.2f A'%Im)
print('Secundario (BT):        Primario (AT):')
print('Rp2 = %.2f Ohm   |   Rp1 = %.2f Ohm'%(Rp2,Rp1))
print('Xm2 = %.2f Ohm   |   Xm1 = %.2f Ohm'%(Xm2,Xm1))
print('------------------')
print('Cortocircuito:')
print('------------------')
print('phi_cc = %.2f°'%np.rad2deg(phi_cc))
print('|Zeq1| = %.2f Ohm  |  |Zeq2| = %.2f Ohm'%(Zeq1,Zeq2))
print('Primario (AT):     |  Secundario (BT):')
print('Req1 = %.3f Ohm   |   Req2= %.3f Ohm'%(Req1,Req2))
print('Xeq1 = %.3f Ohm   |   Xeq2 = %.3f Ohm'%(Xeq1,Xeq2))
print('------------')
print('Rendimiento:')
print('------------')
print('phi_fp = %.2f°'%np.rad2deg(phi_fp))
print('Pcu = %.2f Ohm'%Pcu)
print('V2 = %.2f V'%V2)
print('n = %.4f'%n)
print('-------------------')
print('Rendimiento máximo:')
print('-------------------')
print('phi_max = %.2f°'%np.rad2deg(phi_max))
print('I2_nmax = %.2f A'%I2_nmax)
print('V2_nmax = %.2f V'%V2_nmax)
print('n_max = %.4f'%n_max)
