# calculation of the dimensions and shape of the upper waste bin for medical gloves

from scipy.constants import atm, pi, golden_ratio
from wrist import Male_wrst, Female_wrst
from bt_mech_equation import Bracelet_inf, Const, spring_f


class FaceSlot:
    def __init__(self, k, p):
        self.shape = k  # k = h/ln
        self.per = p  # perimetr

    def h_slot(self):
        return self.per / (pi + 2 / self.shape - 2)

    def w_slot(self):
        return (self.h_slot() * (1 - self.shape)) / self.shape + self.h_slot()


class VacuumChamber:
    def __init__(self, x=0):
        self.wall = 15
        self.bracket = 20
        self.suction_cup = 5
        self.spring_gap = x

    def full_size_m(self):
        return Male_wrst + pi * (self.wall + self.bracket + self.suction_cup) + self.spring_gap

    def full_size_f(self):
        return Female_wrst + pi * (self.wall + self.bracket + self.suction_cup) + self.spring_gap


class WeightAndForce:
    def __init__(self, d, r, p):
        self.density = d
        self.spring_rad = r
        self.p_act = p
        self.net_weight = 130  # mm
        self.spring_ln_part = 200  # mm
        self.part = 12
        self.stl_shear_mod = Const.stl

    def gross_weight(self):
        spr_v = self.spring_rad**2 * pi * self.spring_ln_part
        d_mm3 = self.density/1000
        spr_w = spr_v * d_mm3 * self.part
        return f"{round((spr_w + self.net_weight),1)} g bracelet  weight"

    def spring_ring_f(self):
        el_2_ring = self.spring_ln_part / (2*pi * 1000)  # mm to m
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
    for i2 in range(3, 28):
        i3 = i2 * 0.001
        waf2 = WeightAndForce(8, 0.75, i3)
        sprf2 = waf2.spring_ring_f()
        psf2 = waf2.piston_f()
        print(f" ln {round(i2, 2)} mm,  force{round(sprf2,2)} N/m, {round(psf2/atm,2)} atm")
