# one vacuum and one pressure source

"""The pump is creating the  pressure into the air receiver.
Vacuum is created in the other tank.
The vacuum supply hose plays the role of a spring.
The force created by the air pressure must overcome the spring resistance and frictional forces.
 In turn, tensile force is added to the frictional forces as the entire bracelet
  expands and stretches the edges of the medical glove. """


from wrist import Male_wrst, Female_wrst
from math import sqrt
from scipy.constants import atm, pi  # R , g, k, golden
from valve_force import InDim


class Const:
    k = 1.4  # adiabatic exponent  https://en.wikipedia.org/wiki/Heat_capacity_ratio
    Tk = 273  # T kelvin temperature 0 Tc
    Ra = 287  # R_atm  air constant
    ro = 1.205  # kg/m3
    v = 0.816  # m3/kg
    a = 343  # m/sec
    plpr = 1e9  # polypropylene
    plt = 117e6  # polyethylene
    h_chamb = 0.02
    ln_chamb = 0.02


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

    def __init__(self, x, g):
        self.wrst = x/1000  # mm to m
        self.wrst_inf = self.wrst * 2
        self.n_modl = 12
        self.n_pill = 3
        self.d_pill = 0.009
        self.h_chamb = Const.h_chamb
        self.ln_chamb = Const.ln_chamb
        self.mg = g  # shear module
        self.ln_p = 0.002  # connecting tube length
        self.h_p = 0.001  # connection tube height

    def compress_ring(self):
        return self.wrst + 2 * self.h_chamb * pi

    def top_ring(self):
        return self.wrst_inf + 2 * self.h_chamb * pi

    def w_chamb(self):
        return self.top_ring() / self.n_modl - self.d_pill * self.n_pill

    def f_spring(self):
        # Fspr = k*L H/m
        # k=G*d**4/8*D**3*n
        l_dspr = self.top_ring() - self.compress_ring()
        d_coil = 0.01
        d_wr = 0.002
        k_spr = self.mg * d_wr**4/(8 * d_coil**3 * self.n_modl)
        f_spr = k_spr * l_dspr
        return f_spr / (pa.w_chamb() * pa.d_pill * pa.n_modl)

    def v_ring(self):
        act = (self.d_pill/2)**2 * pi * self.ln_chamb * self.n_pill
        chamb_pip = self.w_chamb() * self.ln_p * self.h_p
        return (act + chamb_pip) * self.n_modl

    def v_compress_ring(self):
        w_pip = (self.compress_ring()/12 - self.w_chamb()) / self.n_pill
        cact = (w_pip/2) * (self.d_pill/2) * pi * self.ln_chamb * self.n_pill
        chamb_pip = self.w_chamb() * self.ln_p * self.h_p
        return (cact + chamb_pip) * self.n_modl


class VacuumChamber:
    def __init__(self, w, wsl):
        self.w_chamb = w
        self.h_chamb = Const.h_chamb
        self.ln_chamb = Const.ln_chamb
        self.shell = 0.001
        self.wsl = wsl
        self.suct_cup = InDim.suct_rad

    def v_solenoid(self):
        lnsl = self.w_chamb - self.shell * 2
        sch = self.suct_cup + self.shell  # suction cup height
        hsl = self.h_chamb - (sch + self.shell * 2)
        return lnsl * hsl * self.wsl

    def free_v_chamb(self):
        ins_h = self.h_chamb - self.shell
        ins_ln = self.ln_chamb - self.shell
        ins_w = self.w_chamb - self.shell
        return ins_h * ins_ln * ins_w - self.v_solenoid()

    def work_suct_cup(self):
        return (4 * pi * self.suct_cup**3) / 6


pa = PneumAct(Male_wrst, Const.plpr)
pa2 = PneumAct(Female_wrst, Const.plpr)
efts2 = GasFlow(1.2, 0.001)
vch = VacuumChamber(pa.w_chamb(), 0.005)

if __name__ == "__main__":
    print(f"vacuum chamber width {round((pa.w_chamb()) * 1000, 2)} mm")
    print(f"free space in the vacuum chamber {round(vch.free_v_chamb() * 1e6,2)} sm3,"
          f" cup {round(vch.work_suct_cup() * 1e6,2)} sm3")
    print(f" pressure relief {round(efts2.gf2() * 1000,5)} g/s"
          f" {round((pa.v_ring() - pa.v_compress_ring()) * Const.ro/efts2.gf2(), 4)} sec")
    print(f" spring back pressure {round(pa.f_spring()/ 1000, 3)} kPa")
    print(f"V ring: max{round(pa.v_ring() * 1e6,1)}, min{round(pa.v_compress_ring() * 1e6,1)} cm3 ")

    # for i in range(30, 40, 1):
    #     d_choke = 0.001  # 1 mm hole in choke
    #     i01 = i / 10
    #     efts = GasFlow(i01, d_choke, atm+pa.f_spring())
    #     print(f" fwp {round(efts.gf1() * 1000, 5)},beta* {round(efts.gf2() * 1000, 5)} g/s"
    #           f"  V fill {round((pa.v_ring() - pa.v_compress_ring()) * Const.ro/efts.gf2(), 4)} sec, {i01} atm")
