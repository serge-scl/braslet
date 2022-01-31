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


class PneumAct:
    def __init__(self, x):
        self.wrst = x/1000  # mm to m
        self.wrst_inf = self.wrst * golden
        self.n_modl = 12
        self.n_pill = 3
        self.d_pill = 0.009
        self.h_chamb = 0.02
        self.ln_chamb = 0.02

    def top_ring(self):
        return self.wrst_inf + self.h_chamb * 2 * pi

    def w_chamb(self):
        return self.top_ring() / self.n_modl - self.d_pill * self.n_pill

    def v_ring(self):
        ln = 0.002
        h = 0.001
        act = (self.d_pill/2)**2 * pi * self.ln_chamb * self.n_pill
        chamb_pip = self.w_chamb() * ln * h
        return (act + chamb_pip) * self.n_modl


pa = PneumAct(Male_wrst)
pa2 = PneumAct(Female_wrst)

if __name__ == "__main__":
    print(f"vacuum chamber width {round((pa.w_chamb()) * 1000, 2)} mm")
    print(f"actuator ring {round(pa.v_ring() * 10e5)} cm3 ")

    for i in range(11, 40, 1):
        d_choke = 0.001  # 1 mm hole in choke
        i01 = i / 10
        efts = GasFlow(i01, d_choke)
        print(f" fwp {round(efts.gf1() * 1000, 5)},beta* {round(efts.gf2() * 1000, 5)} g/s"
              f"  V fill {round(pa.v_ring() * Const.ro/efts.gf2(), 2)} sec, {i01} atm")
