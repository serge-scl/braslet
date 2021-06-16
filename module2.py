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
from wrist import Female_wrst as Fmwr
from wrist import pHi
from numpy import pi, arccos, degrees
from valve_force import InDim
from bt_mech_equation import D_spr, d_wr

exe_chamber = 0.008
spring_ind = D_spr/d_wr
male_wrist = Mwr / 1000  # mm to m
female_wrist = Fmwr / 1000
nmb_s = InDim.num_suct
h_suct = InDim.suct_rad * 2 + 0.0005


def between_suct(x):
    d_wrist_a = x / pi
    h_exe_ch = h_suct + valve_force.solval.sol_h()
    d_wrist_b = d_wrist_a + 2 * h_exe_ch
    brac_b = d_wrist_b * pi / nmb_s - exe_chamber
    return brac_b


min_brc = between_suct(male_wrist)
min_brc_f = between_suct(female_wrist)
max_brs = between_suct((male_wrist * pHi))
max_brs_f = between_suct(female_wrist * pHi)


D_spr2 = round((max_brs + max_brs_f)/2, 3)  # turn diameter of vacuum supply tube
D_spr3 = 0.02

# tilt angle of the vacuum joint cup


def tilt_cup(d, l1):
    kt = l1/2
    csn = kt/d
    return int(degrees(arccos(csn)))


min_exp = tilt_cup(D_spr3, min_brc)
max_exp = tilt_cup(D_spr3, max_brs_f)
delta_angl = min_exp - max_exp

if __name__ == "__main__":
    print(f"{round(min_brc * 1000)} mm minimum  between suction cups at tube level")
    print(f"{round(min_brc_f * 1000)} mm minimum female  between suction cups at tube level")
    print(f"{round(max_brs * 1000)} mm maximum between suction cups at tube level")
    print(f"{round(max_brs_f * 1000)} mm maximum female between suction cups at tube level")
    # print(round(male_wrist * pHi * 1000))
    # print(D_spr2)
    print(f"{min_exp} at x fixing , the angles y and z axes in min expand ")
    print(f"{max_exp} at x fixing, the angles the y and z axes in max expand")
    print(delta_angl)
