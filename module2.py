# a very simple version of 12 modules with suction cups like  on the dial
# Si - spring index = D/d  d - diameter wire

from wrist import Male_wrst as Mwr
from wrist import Female_wrst as Fmwr
# from wrist import pHi
from valve_force import InDim
# from bt_mech_equation import D_spr, d_wr

exe_chamber = 0.006
# spring_ind = D_spr/d_wr
male_wrist = Mwr / 1000  # mm to m
female_wrist = Fmwr / 1000
h_suct = InDim.suct_rad * 2 + 0.001

if __name__ == "__main__":
    pass
