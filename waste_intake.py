# calculation of the dimensions and shape of the upper waste bin for medical gloves

from scipy.constants import atm, golden_ratio
from wrist import Male_wrst, Female_wrst
from bt_mech_equation import Bracelet_inf, Const, spring_f
import math
import matplotlib.pyplot as plt


class FaceSlot:
    def __init__(self, k, p):
        self.shape = k  # k = h/ln
        self.per = p  # perimetr

    def h_slot(self):
        return self.per / (math.pi + 2 / self.shape - 2)

    def w_slot(self):
        return (self.h_slot() * (1 - self.shape)) / self.shape + self.h_slot()


class VacuumChamber:
    def __init__(self, x=0):
        self.wall = 15
        self.bracket = 20
        self.suction_cup = 5
        self.spring_gap = x

    def full_size_m(self):
        return Male_wrst + math.pi * (self.wall + self.bracket + self.suction_cup) + self.spring_gap

    def full_size_f(self):
        return Female_wrst + math.pi * (self.wall + self.bracket + self.suction_cup) + self.spring_gap


# Conical Springs -
# formula
# G - shear modulus
# dl - spring deflection
# R2 - maximum coil average radius
# R1 - minimum coil average radius
# d - wire diameter
# n - number of coils
# Fcspr = dl(R2 - R1)Gd^4/(R2^4 - R1^4)16n
# ln = 16Fn(R2^4 - R1^4) / (Gd^4(R2 -R1))
def con_spring_f(g, r2, r1, d, n, dl):
    return dl * (r2 - r1) / (r2**4 - r1**4) * g * d**4 / (16 * n)


def con_spring_dl(g, r2, r1, d, n, f):
    return 16 * f * n * (r2**4 - r1**4) / (g * d**4 * (r2 - r1))


class WeightAndForce:
    def __init__(self, d, r, p):
        self.density = d
        self.spring_rad = r
        self.p_act = p
        self.net_weight = 130  # g
        self.spring_ln_part = 200  # mm
        self.part = 12
        self.stl_shear_mod = Const.stl

    def gross_weight(self):
        spr_v = self.spring_rad**2 * math.pi * self.spring_ln_part
        d_mm3 = self.density/1000
        spr_w = spr_v * d_mm3 * self.part
        return f"{round((spr_w + self.net_weight),1)} g bracelet  weight"

    def spring_ring_f(self):
        el_2_ring = self.spring_ln_part / (2 * math.pi * 1000)  # mm to m
        spr_d = self.spring_rad * 2 / 1000  # r to d mm to m
        ntr = 2
        srf = spring_f(self.stl_shear_mod, spr_d, el_2_ring, ntr, self.p_act)
        return srf

    def piston_f(self):
        space_p = (75 + 74 + 37) * 2 / 1e6
        contr_f = self.spring_ring_f() / space_p
        return contr_f + atm


class AirReceivers:
    def __init__(self, x):
        self.pressure = x * atm


fsm = FaceSlot(1 / golden_ratio, Male_wrst)
fsf = FaceSlot(1 / golden_ratio, Female_wrst)
fsm_inf = FaceSlot(1 / golden_ratio, Male_wrst * Bracelet_inf)
fsf_inf = FaceSlot(1 / golden_ratio, Female_wrst * Bracelet_inf)
spr_mt_w_m = round((fsm_inf.w_slot() - fsm.w_slot()) / 2, 1)
spr_mt_h_m = round((fsm_inf.h_slot() - fsm.h_slot()) / 2, 1)
spr_mt_w_f = round((fsf_inf.w_slot() - fsm.w_slot()) / 2, 1)
spr_mt_h_f = round((fsf_inf.h_slot() - fsf.h_slot()) / 2, 1)
vch = VacuumChamber()
fsm_full_m_inf = FaceSlot(1 / golden_ratio, vch.full_size_m() * Bracelet_inf)
fsm_full_f_inf = FaceSlot(1 / golden_ratio, vch.full_size_f() * Bracelet_inf)


class ConExtSprings:
    def __init__(self, x, y):
        self.pow = x
        self.con_spr_ln = y
        self.rad2 = 0.015
        self.rad1 = 0.005
        self.wire_d = 0.00065
        self.pip_d = 0.002
        self.coil_n = 7
        self.stl = Const.stl
        self.plpr = Const.plpr
        self.angle_h = math.radians(10)
        self.angle_w = math.radians(20)

    def con_spring_fs(self):
        return con_spring_f(self.stl, self.rad2, self.rad1, self.wire_d, self.coil_n, self.con_spr_ln)

    def con_spring_fp(self):
        return con_spring_f(self.plpr, self.rad2, self.rad1, self.pip_d, self.coil_n, self.con_spr_ln)

    def con_spring_dl_s(self):
        top_f = math.sin(self.angle_h) * self.pow * 2 - self.con_spring_fs()
        return con_spring_dl(Const.stl, self.rad2, self.rad1, self.wire_d, self.coil_n, top_f)


if __name__ == "__main__":
    print(f"shrink bracelet male{round(fsm.h_slot(), 1), round(fsm.w_slot(), 1)} mm")
    print(f"shrink bracelet female{round(fsf.h_slot(), 1), round(fsf.w_slot(), 1)} mm")
    print(f"inflated bracelet male {round(fsm_inf.h_slot(), 1), round(fsm_inf.w_slot(), 1)} mm")
    print(f" inflated bracelet female {round(fsf_inf.h_slot(), 1), round(fsf_inf.w_slot(), 1)} mm")
    print(f" pass spring male {spr_mt_h_m, spr_mt_w_m} mm")
    print(f" pass spring female {spr_mt_h_f, spr_mt_w_f} mm")
    print(f" space max male {round(fsm_full_m_inf.w_slot()), round(fsm_full_m_inf.h_slot())} mm")
    print(f" space max female {round(fsm_full_f_inf.w_slot()), round(fsm_full_f_inf.h_slot())} mm")

    print("select wire diameter")
    for i in range(25, 110, 5):
        i1 = 0.01 * i
        waf = WeightAndForce(8, i1, 0.025)
        gw = waf.gross_weight()
        sprf = waf.spring_ring_f()
        psf = waf.piston_f()
        print(f"{gw}, at wire D {round(i1 * 2,2)}, force {round(sprf,1)} N/m, {round(psf/atm, 3)} atm")
    print("working pressure during expansion")
    esp_con = spr_mt_h_m/1000  # mm 2 m
    i2_lst = []
    ln_ring_lst = []
    ln_rad_lst = []
    ln_h_lst = []
    nm_lst = []
    f_spr_0_lst = []
    f_pip_0_lst = []
    br_lst = []
    for i2 in range(3, 28):
        i3 = i2 * 0.001
        waf2 = WeightAndForce(8, 0.75, i3)
        sprf2 = waf2.spring_ring_f()
        psf2 = waf2.piston_f()
        ces = ConExtSprings(sprf2, esp_con)
        ln_h = round(ces.con_spring_dl_s() * 1000, 1)
        f_spr_0 = round(ces.con_spring_fs(), 2)
        f_pip_0 = round(ces.con_spring_fp(), 2)
        ln_rad = i2
        ln_ring = (ln_rad + 13) * 12
        ln_rad2 = round(ln_rad * 12 / (2 * math.pi), 1)
        nm = round(sprf2, 2)
        br = round(psf2/atm, 2)
        print(f"ring {ln_ring}mm,ring h {ln_rad2} mm, con h {ln_h} mm,"
              f" ring f {nm} N,con stl {f_spr_0}N, plp{f_pip_0} N, {br} atm ")
        esp_con = esp_con - spr_mt_h_m/25000
        i2_lst.append(i2)
        ln_ring_lst.append(ln_ring)
        ln_rad_lst.append(ln_rad2)
        ln_h_lst.append(ln_h)
        nm_lst.append(nm)
        f_spr_0_lst.append(f_spr_0)
        f_pip_0_lst.append(f_pip_0)
        br_lst.append(br)
    # plt.plot(i2_lst, ln_ring_lst)
    # plt.plot(i2_lst, ln_rad_lst)
    # plt.plot(i2_lst, ln_h_lst)
    # plt.plot(i2_lst, nm_lst)
    plt.plot(i2_lst, f_spr_0_lst)
    plt.plot(i2_lst, f_pip_0_lst)
    # plt.plot(i2_lst, br_lst)
    plt.show()
