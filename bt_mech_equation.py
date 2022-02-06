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
from valve_force import InDim  # z_sphere


class Const:
    k = 1.4  # adiabatic exponent  https://en.wikipedia.org/wiki/Heat_capacity_ratio
    Tk = 273  # T kelvin temperature 0 Tc
    Ra = 287  # R_atm  air constant
    ro = 1.205  # kg/m3 air
    v = 0.816  # m3/kg air
    a = 343  # m/sec sound
    plpr = 1e9  # polypropylene
    plt = 117e6  # polyethylene
    cr_beta = 0.526  # critical σ*
    cr_beta_f = 0.259  # flow rate function φ(σ)*


class GasFlow:
    def __init__(self, p, d, pn=atm):
        self.v = Const.v
        self.p = p * atm
        self.pn = pn
        self.beta = self.pn/self.p
        self.s = (d/2)**2 * pi

    def exp_f(self):
        if self.beta <= Const.cr_beta:
            return Const.cr_beta_f
        elif self.beta > Const.cr_beta:
            b1 = self.beta**(2/Const.k)
            b2 = self.beta**((Const.k+1)/Const.k)
            return sqrt(b1 - b2)

    def gf1(self):
        return self.s * Const.a * Const.ro

    def gf2(self):
        return self.s * (self.p - self.pn) * sqrt((2 * Const.k) /
                                                  (Const.Ra * (Const.Tk + 20) * (Const.k - 1))) * self.exp_f()


class MyConst(Const):
    h_chamb = 0.02  # vacuum chamber height
    ln_chamb = 0.02  # length of the v chamber along the arm axis
    vlcd = 0.01  # vacuum line coil diameter
    vltd = 0.001  # vacuum line tube diameter
    dpsh = 0.009  # diameter of the pneumatic drive section of the pill shape
    nsom = 3  # number of sections in one module
    nofm = InDim.num_suct  # number of modules
    wcht = 0.001  # vacuum chamber wall thickness
    acth = 0.001  # actuator connection tube height
    actw = 0.002  # actuator connection tube width
    scw = 0.005  # solenoid core width
    dpsr = 0.001  # diameter of the pressure supply pipe from the receiver


class PneumAct:

    def __init__(self, x, g):
        self.wrst = x/1000  # mm to m
        self.wrst_inf = self.wrst * 2
        self.n_modl = MyConst.nofm
        self.n_pill = MyConst.nsom
        self.d_pill = MyConst.dpsh
        self.h_chamb = MyConst.h_chamb
        self.ln_chamb = MyConst.ln_chamb
        self.mg = g  # shear module
        self.ln_p = MyConst.actw
        self.h_p = MyConst.acth

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
        d_coil = MyConst.vlcd
        d_wr = MyConst.vltd
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
        self.h_chamb = MyConst.h_chamb
        self.ln_chamb = MyConst.ln_chamb
        self.shell = MyConst.wcht
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

    def suction_cup_ratio(self):
        v_cup = (4 * pi * self.suct_cup**3) / 6
        return v_cup / self.free_v_chamb()


pa = PneumAct(Male_wrst, Const.plpr)
pa2 = PneumAct(Female_wrst, Const.plpr)
efts2 = GasFlow(1.2, MyConst.dpsr)
vch = VacuumChamber(pa.w_chamb(), MyConst.scw)

if __name__ == "__main__":
    print(f"vacuum chamber width {round((pa.w_chamb()) * 1000, 2)} mm")
    print(f"free space in the vacuum chamber {round(vch.free_v_chamb() * 1e6,2)} sm3,"
          f" cup ratio {round(vch.suction_cup_ratio(),3)}")
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
