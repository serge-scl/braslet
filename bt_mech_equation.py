"""The pump is creating the maximum pressure into the air receiver.
Then, on a signal, the valve opens and air pressure flows through the throttle into the hose.
The pressure is transferred through the hose to the chamber of the pneumatic drive.
 The chamber consists of nine spherical containers in the form of a 3X3 matrix
interconnected and compressed by a spring mechanism.
The air supply hose plays the role of a spring.
When the air pressure supplied to the compressed balls reaches a threshold value,
the balls begin to take their shape, pushing the mechanism apart.
The force created by the air pressure must overcome the spring resistance and frictional forces.
 In this case, the opposite compression force of the chamber (balls)
 of the pneumatic drive is subtracted from the spring force.
 In turn, radial force is added to the frictional forces as the entire bracelet
  expands and stretches the edges of the medical glove. """


# dim receiver pressure 13X10X4
# act boll 3.5 X 9
# pz pump typ. volume flow v̇ (p=0) 20 ml/min (300 Hz)
# typ. back pressure p (v̇ =0) 100 mbar (300 Hz)
# m * (dv/dt) = P * S - Fspr + F3 - F3
# Fspr = k*L H/m


from wrist import Male_wrst, Female_wrst, pHi
from math import sqrt, pi
from scipy import constants

Male_wrst_open = Male_wrst * pHi
Frmale_wrst_open = Female_wrst * pHi

k = 1.4  # k - adiabatic exponent (Poisson's ratio)
Tm = 293  # T kelvin temperature
R_atm = 287  # R_atm  air constant
Pip_resist = 30

# flow function for gas pressure
# def exp_funct(x):
#     if x <= 0.528:
#         return 0.259
#     elif x >= 0.528:
#         b1 = x**(2/k)
#         b2 = x**((k+1)/k)
#         return sqrt(b1 - b2)


def pm(p):
    return p + constants.atm


def f_beta(b):
    return constants.atm/b


def f_p(d):
    d1 = d/1000
    return pi * d1**2/4

# def exp_funct_resist(x):
#     rt = (1/sqrt(Pipres)) * (sqrt(1 - x**2))
#     return rt


def gas_f_rate(f, p):
    pm0 = pm(p)
    g_kg = (f * 30000) / sqrt(Tm * R_atm * Pip_resist) * sqrt(1 - (f_beta(pm0)) ** 2)
    return g_kg / 1.205


def res_vs_act():
    dr = 12.5 * 9.5 * 3.5
    boll = 4/3 * pi * 1.5**3
    actuatr = boll * 0.7 * 6
    rat = dr/actuatr
    return rat


# k=G*d**4/8*D**3*n
# spring D 9 - 10 mm, L 9 mm, d 1.5 - 2 mm
# G shear modulus 1e9 Pa polypropylene, 117e6 Pa polyethylene


def stiffness_coefficient(g):
    k_h_sp = g * 0.0015**4/(8 * 0.01**3)
    return k_h_sp


f_act = 0.0018**2 * pi * 3 * 60000


fp = f_p(0.5)
pm1 = pm(30000)
gfr = gas_f_rate(fp, 30e3)
plast1 = stiffness_coefficient(1e9)
plast2 = stiffness_coefficient(117e6)


# print(res_vs_act())
print(plast1 * 0.005 * 0.5)
print(plast2 * 0.005 * 0.5)
print(f_act)
# print(gfr * (100**3))
