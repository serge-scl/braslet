# second version of the module for the container for used medical gloves
# new number of suction cups in one module - 2
# one receiver serves two modules
# half of the modules are power, the other is equipped with sensors
# male module 30mm female 25 mm - now both male and female bracelets consist of six modules each
# execution chamber bottom 8X8 mm
# to determine incline in  X,Y, Z  tubes " across (s/2)/D "  s shear modulus  D  diameter
# beta = (20.8 * Si**3 * n * f) / (E * d)
# Si - spring index = D/d  d - diameter wire
import valve_force
from wrist import Male_wrst as Mwr
from wrist import pHi
from numpy import pi
from valve_force import InDim
from bt_mech_equation import D_spr, d_wr

exe_chamber = 0.008
spring_ind = D_spr/d_wr
male_wrst = Mwr / 1000  # mm to m
nmb_s = InDim.num_suct
h_suct = InDim.suct_rad * 2 + 0.0005


def between_suct(x):
    d_wrist_a = x / pi
    h_exe_ch = h_suct + valve_force.solval.sol_h()
    d_wrist_b = d_wrist_a + 2 * h_exe_ch
    brac_b = d_wrist_b * pi / nmb_s - exe_chamber
    return brac_b


min_brc = between_suct(male_wrst)
max_brs = between_suct((male_wrst * pHi))


if __name__ == "__main__":
    print(min_brc)
    print(max_brs)
