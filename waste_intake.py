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


class AirReceivers:
    def __init__(self, x):
        self.pressure = x * atm


fsm = FaceSlot(1 / golden_ratio, Male_wrst)
fsf = FaceSlot(1 / golden_ratio, Female_wrst)
fsm_inf = FaceSlot(1 / golden_ratio, Male_wrst * Bracelet_inf)
fsf_inf = FaceSlot(1 / golden_ratio, Female_wrst * Bracelet_inf)
spr_mt_w_m = round((fsm_inf.w_slot() - fsm.w_slot()) / 2, 2)
spr_mt_h_m = round((fsm.w_slot()- fsm.h_slot()) / 2, 2)
spr_mt_w_f = round((fsf_inf.w_slot() - fsm.w_slot()) / 2, 2)
spr_mt_h_f = round((fsf_inf.h_slot() - fsf.h_slot()) / 2, 2)

if __name__ == "__main__":
    print(f"shrink bracelet male{round(fsm.h_slot(), 2), round(fsm.w_slot(), 2)} mm")
    print(f"shrink bracelet female{round(fsf.h_slot(), 2), round(fsf.w_slot(), 2)} mm")
    print(f"inflated bracelet male {round(fsm_inf.h_slot(), 2), round(fsm_inf.w_slot(), 2)} mm")
    print(f" inflated bracelet female {round(fsf_inf.h_slot(), 2), round(fsf_inf.w_slot(), 2)} mm")
    print(f" pass spring male {spr_mt_h_m, spr_mt_w_m} mm")
    print(f" pass spring female {spr_mt_h_f, spr_mt_w_f} mm")
