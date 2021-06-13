# calculation of the effort of the electromagnetic semi-automatic valve of the suction cup


from scipy import constants
from numpy import pi, sqrt


class InDim:
    mgcons = constants.mu_0
    sucts_in_modl = 2
    modl_ln = 0.025
    suct_rad = 0.0025
    h_glove = 0.0001
    ribbnE = 500000
    ohmmtr00005 = 0.108
    wire = 0.0001


class OutDim:
    num_suct = 6
    pump_vcm = 75000
    hole = 0.001
    gap = 0.001
    i_battr = 0.8


def z_sphere(x):
    return 0.665 * InDim.suct_rad * ((x * InDim.suct_rad) /
                                     (InDim.ribbnE * InDim.h_glove)) ** (1 / 3)


class PowValve:

    def __init__(self, p, z, h, g):

        self.pump = p
        self.zaxsph = z
        self.half = 3600
        self.hole = h
        self.gap = g
        self.suct = z * InDim.suct_rad * 2 * pi

    def diff(self):
        return (self.hole ** 2 * pi) / self.suct

    def pic_pow_f(self):
        return self.suct * self.pump * self.diff()

    def pic_pow_wt(self):
        return self.suct * self.pump * self.diff() * self.gap

    def batter(self):
        return self.pic_pow_wt() * self.half * InDim.sucts_in_modl * OutDim.num_suct


# F = (n * i)**2 * mgconst * a / (2 * gap**2)
# n = number of turns in the solenoid
# a = Area


class SolenoidValve:
    def __init__(self, g, s, h):
        self.gap = g
        self.rad_l = s
        self.rad_w = h
        self.b_sln = 0.003
        self.w_flp = 0.003
        self.w_pin = 0.001

    def pinarea(self):
        return self.w_flp * self.w_pin * 2

    def ni(self):
        zp = z_sphere(OutDim.pump_vcm)
        pw = PowValve(OutDim.pump_vcm, zp, self.rad_w, self.gap)
        fp = pw.pic_pow_f()
        ni1 = sqrt(fp / (constants.mu_0 * self.pinarea() / (2 * self.gap ** 2)))
        n2 = ni1 / OutDim.i_battr
        return n2

    def wireohm(self):
        lwr = (2 * (self.w_pin + self.w_flp)) * self.ni()
        return lwr * InDim.ohmmtr00005

    def wind_thick(self):
        row = self.ni() * InDim.wire / self.b_sln
        return row * InDim.wire


zsp = z_sphere(OutDim.pump_vcm)
pwalv = PowValve(OutDim.pump_vcm, zsp, OutDim.hole, OutDim.gap)
solval = SolenoidValve(OutDim.gap, InDim.suct_rad, OutDim.hole)


# Area = InDim.suct_rad * OutDim.hole * 2
# fup = pwalv.pic_pow_f()
# ni = sqrt(fup / (InDim.mgcons * Area / (2 * OutDim.gap**2)))

if __name__ == "__main__":
    print(f"{zsp} membrane deflection")
    print(f"{pwalv.pic_pow_wt()}watt pic power 1 sec {pwalv.batter()}watt all power in batter")
    print(f"{solval.ni()} number turns magnet winding")
    print(f"{solval.wireohm()} conductor resistance ")
    print(f"{solval.wind_thick()} winding thickness")
