##########
# Datos:
##########
print('Ingrese los siguientes valores:')
SN = float(input('SN [VA]: '))
UN1 = float(input('UN1 [V]: '))
UN2 =  float(input('UN2 [V]: '))
print('Ensayo de vacío:')
Vo =  float(input('Vo [V]: '))
Io =  float(input('Io [A]: '))
Po =  float(input('Po [W]: '))
print('Ensayo de cortocircuito:')
Vcc = float(input('Vcc [V]: '))
Icc = float(input('Icc [A]: '))
Pcc = float(input('Pcc [W]: '))
print('Regulación:')
fp_reg = float(input('fp_reg: '))
print('Rendimiento:')
fp_rend = float(input('fp_rend: '))
print('Rendimiento máximo:')
fp_max = float(input('fp_max: '))

import numpy as np

IN1 = SN/UN1   # Corriente nominal primaria
IN2 = SN/UN2   # Corriente nominal secundaria
a = UN1/UN2    # Relación de transformación

###########################
# Ensayo de cortocircuito
###########################
Zeq1 = Vcc/Icc
# Cálculo de phi_cc
phi_cc = np.arccos(Pcc/(Icc*Vcc))

# Parámetros longitudinales
# Primario                        # Secundario
Req1 = Zeq1*np.cos(phi_cc)   ;   Req2 = Req1/a**2
Xeq1 = Zeq1*np.sin(phi_cc)   ;   Xeq2 = Xeq1/a**2

###################
# Ensayo de vacío
###################
phi_o = np.arccos(Po/(Io*Vo))
Ip = Io*np.cos(phi_o)
Im = Io*np.sin(phi_o)

# Secundario (BT)     # Primario (AT)
Rp2 = Vo/Ip     ;     Rp1 = Rp2*a**2
Xm2 = Vo/Im     ;     Xm1 = Xm2*a**2

##########################
# Cálculos de regulación
##########################
phi_reg = np.arccos(fp_reg)
I2_reg = fp_reg*IN2  ;  V20 = Vo
# Tensión de salida o aplicada a la carga:
V2_ind = V20 - I2_reg*(Req2*np.cos(phi_reg) + Xeq2*np.sin(phi_reg))
V2_cap = V20 - I2_reg*(Req2*np.cos(phi_reg) - Xeq2*np.sin(phi_reg))
# Regulación
reg_ind = (V20 - V2_ind)/V20*100
reg_cap = (V20 - V2_cap)/V20*100

###########################
# Cálculos de rendimiento
###########################
phi_rend = np.arccos(fp_rend)
I2_rend = IN2  ;  V20 = Vo
Pcu = I2_rend**2*Req2
# Rendimiento para el caso inductivo:
V2_ind = V20 - I2_rend*(Req2*np.cos(phi_rend) + Xeq2*np.sin(phi_rend))
n_ind = (V2_ind*I2_rend*np.cos(phi_rend))/(V2_ind*I2_rend*np.cos(phi_rend) + Pcu + Po) * 100
# Rendimiento para el caso capacitivo:
V2_cap = V20 - I2_rend*(Req2*np.cos(phi_rend) - Xeq2*np.sin(phi_rend))
n_cap = (V2_cap*I2_rend*np.cos(phi_rend))/(V2_cap*I2_rend*np.cos(phi_rend) + Pcu + Po) *100

# Rendimiento máximo
phi_max = np.arccos(fp_max)
I2_max = np.sqrt(Po/Req2)
Pcu_max = I2_max**2*Req2
#V2_max = V20 - I2_max*(Req2*fp_max + 0)
V2_max = UN2 - I2_max*(Req2*np.cos(phi_max) + Xeq2*np.sin(phi_max))
n_max = (V2_max*I2_max*fp_max)/(V2_max*I2_max*fp_max + Pcu_max + Po) * 100

print('Resultados:')
print()
print('###########################')
print('Corrientes nominales')
print('###########################')
print('IN1 = %.1f A'%IN1)
print('IN2 = %.1f A'%IN2)
print('a = %.2f'%a)
print()
print('###########################')
print('# Ensayo de cortocircuito')
print('###########################')
print('Zeq1 = %.3f Ohm'%Zeq1)
print('phi_cc = %.2f°'%np.rad2deg(phi_cc))
print('Parámetros longitudinales:')
print('Primario:                Secundario:')
print('Req1 = %.3f Ohm    |    Req2 = %.3f mOhm'%(Req1,Req2*1000))
print('Xeq1 = %.3f Ohm    |    Xeq2 = %.3f mOhm'%(Xeq1,Xeq2*1000))
print('###################')
print('# Ensayo de vacío')
print('###################')
print('phi_o = %.2f°'%np.rad2deg(phi_o))
print('Ip = %.2f A'%Ip)
print('Im = %.2f A'%Im)
print('Secundario (BT)         Primario (AT)')
print('Rp2 = %.2f Ohm    |    Rp1 = %.2f Ohm'%(Rp2,Rp1))
print('Xm2 = %.2f Ohm     |    Xm1 = %.2f Ohm'%(Xm2,Xm1))
print('##########################')
print('# Cálculos de regulación')
print('##########################')
print('I2 = %.2f A'%I2_reg)
print('phi_2 = %.2f°'%np.rad2deg(phi_reg))
print('# Tensión de salida o aplicada a la carga:')
print('Caso inductivo:')
print('V2_ind = %.2f V'%V2_ind)
print('reg_ind = %.2f %%'%reg_ind)
print('Caso capacitivo:')
print('V2_cap = %.2f V'%V2_cap)
print('reg_cap = %.2f %%'%reg_cap)
print('###########################')
print('# Cálculos de rendimiento')
print('###########################')
print('phi_rend = %.2f°'%np.rad2deg(phi_rend))
print()
print('Caso inductivo:')
print('fp_rend = %.2f'%fp_rend)
print('I2 = %.2f A'%I2_rend)
print('V2_ind = %.2f V'%V2_ind)
print('Pcu = %.1f W'%Pcu)
print('n_ind = %.2f %%'%n_ind)
print()
print('Caso capacitivo:')
print('fp_rend1 = %.2f'%fp_rend)
print('I2 = %.2f A'%I2_rend)
print('V2_cap1 = %.2f V'%V2_cap)
print('Pcu = %.1f W'%Pcu)
print('n_cap1 = %.2f %%'%n_cap)
print()
print('Máximo:')
print('I2_max = %.2f A'%I2_max)
print('V2_max = %.2f A'%V2_max)
print('Pcu_max = %.1f W'%Pcu_max)
print('n_max = %.2f %%'%n_max)
