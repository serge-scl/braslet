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
from scipy.constants import atm, g, pi


Male_wrst_open = Male_wrst * pHi
Frmale_wrst_open = Female_wrst * pHi


class Const:
    k = 1.4  # k - adiabatic exponent (Poisson's ratio)
    Tk = 273  # T kelvin temperature 0 Tc
    R = 287  # R_atm  air constant
    v = 0.816  # specific volume of gas


class GasFlow:
    def __init__(self, p, s, pn=atm):
        self.v = Const.v
        self.p = p * atm
        self.pn = pn
        self.beta = self.pn/self.p
        self.s = s

    def exp_f(self):
        if self.beta <= 0.528:
            return 0.259
        elif self.beta > 0.528:
            b1 = self.beta**(2/Const.k)
            b2 = self.beta**((Const.k+1)/Const.k)
            return sqrt(b1 - b2)

    def G(self):
        return self.s * sqrt(((2 * g * Const.k * self.p) /
                              ((Const.k - 1) * self.v)) * self.exp_f())


s_hole = 0.0005**2 * pi

eft = GasFlow(2, s_hole)

if __name__ == "__main__":
    print(f"{round(eft.G(), 5)} kg/s gas flow through a hole: {round(s_hole* 10e6,3)} mm2,"
          f" unverified formula")
