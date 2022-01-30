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


from wrist import Male_wrst, Female_wrst
from math import sqrt
from scipy.constants import atm, pi, golden  # R , g, k


Male_wrst_open = Male_wrst * golden
Frmale_wrst_open = Female_wrst * golden


class Const:
    k = 1.4  # adiabatic exponent  https://en.wikipedia.org/wiki/Heat_capacity_ratio
    Tk = 273  # T kelvin temperature 0 Tc
    Ra = 287  # R_atm  air constant
    ro = 1.205  # kg/m3
    v = 0.816  # m3/kg
    a = 343  # m/sec


class GasFlow:
    def __init__(self, p, d, pn=atm):
        self.v = Const.v
        self.p = p * atm
        self.pn = pn
        self.beta = self.pn/self.p
        self.s = (d/2)**2 * pi

    def exp_f(self):
        if self.beta <= 0.528:
            return 0.259
        elif self.beta > 0.528:
            b1 = self.beta**(2/Const.k)
            b2 = self.beta**((Const.k+1)/Const.k)
            return sqrt(b1 - b2)

    def gf1(self):
        return self.s * Const.a * Const.ro

    def gf2(self):
        return self.s * (self.p - self.pn) * sqrt((2 * Const.k) /
                                                  (Const.Ra * (Const.Tk + 20) * (Const.k - 1))) * self.exp_f()


d_hole = 0.001

eft = GasFlow(2.7, d_hole)

if __name__ == "__main__":
    print(f"{round(eft.gf1() * 1000, 5)} g/s gas flow hole D: {round(d_hole * 1000, 3)} mm, fwp")
    print(f"{round(eft.gf2() * 1000, 5)} g/s gas flow  hole D: {round(d_hole * 1000, 3)} mm, beta*")
    print(f"{round(eft.gf2() * Const.v * 10e5 , 5)} cm3/s gas flow  hole D: {round(d_hole * 1000, 3)} mm, beta*")
    for i in range(11, 40, 1):
        i01 = i / 10
        efts = GasFlow(i01, d_hole)
        print(f"{round(efts.gf1() * 1000, 5)} fwp,{round(efts.gf2() * 1000, 5)} beta g/s  {i01} atm,")
