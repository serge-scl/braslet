# calculation of the dimensions and shape of the upper waste bin for medical gloves

from scipy.constants import atm, pi, golden_ratio
from wrist import Male_wrst, Female_wrst
from bt_mech_equation import Bracelet_inf


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
    def __init__(self, r, d):
        self.spring_rad = r
        self.density = d
        self.net_weight = 130
        self.spring_ln_part = 200
        self.part = 12

    def gross_weight(self):
        spr_v = self.spring_rad**2 * pi * self.spring_ln_part
        d_mm3 = self.density/1000
        spr_w = spr_v * d_mm3 * self.part
        return f"{round((spr_w + self.net_weight),1)} g bracelet total weight"


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
    for i in range(5, 10):
        i1 = 0.1 * i
        waf = WeightAndForce(i1, 8)
        gw = waf.gross_weight()
        print(f"{gw} at wire radius {round(i1,1)}")
