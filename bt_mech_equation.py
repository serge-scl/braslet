# one vacuum and one pressure source

"""The pump is creating the  pressure into the air receiver.
Vacuum is created in the other tank.
The vacuum supply hose plays the role of a spring.
The force created by the air pressure must overcome the spring resistance and frictional forces.
 In turn, tensile force is added to the frictional forces as the entire bracelet
  expands and stretches the edges of the medical glove. """

# Fspr = k*L H/m
# k=G*d**4/8*D**3*n
# G shear modulus 1e9 Pa polypropylene, 117e6 Pa polyethylene
# spring D 9 - 10 mm, L 9 mm, d 1.5 - 2 mm
# D_spr = 0.01
# d_wr = 0.0015
# polypropylene = 1e9
# polyethylene = 117e6


from wrist import Male_wrst, Female_wrst, pHi
from math import sqrt
from scipy.constants import atm


Male_wrst_open = Male_wrst * pHi
Frmale_wrst_open = Female_wrst * pHi

k = 1.4  # k - adiabatic exponent (Poisson's ratio)
Tk = 273  # T kelvin temperature 0 Tc
R_atm = 287  # R_atm  air constant


# flow function for gas pressure
def exp_funct(x):
    if x <= 0.528:
        return 0.259
    elif x >= 0.528:
        b1 = x**(2/k)
        b2 = x**((k+1)/k)
        return sqrt(b1 - b2)


def pm(p):
    return p + atm


def f_beta(b):
    return atm/b


if __name__ == "__main__":
    pass
