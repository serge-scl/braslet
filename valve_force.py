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
    ohmmtr005 = 0.108


class OutDim:
    num_suct = 6
    pump_vcm = 75000
    hole = 0.001
    gap = 0.001


def z_sphere(x):
    return 0.665 * InDim.suct_rad * ((x * InDim.suct_rad) /
                                     (InDim.ribbnE * InDim.h_glove)) ** (1 / 3)


zsp = z_sphere(OutDim.pump_vcm)


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


pwalv = PowValve(OutDim.pump_vcm, zsp, OutDim.hole, OutDim.gap)

# F = (n * i)**2 * mgconst * a / (2 * gap**2)
# n = number of turns in the solenoid
# a = Area


class SolenoidValve:
    def __init__(self, g, s, h):
        self.gap = g
        self.rad_l = s
        self.rad_w = h

    def area(self):
        return self.rad_l * self.rad_w * 2

    def ni(self):
        fup = pwalv.pic_pow_f()
        ni1 = sqrt(fup / (constants.mu_0 * self.area() / (2 * self.gap**2)))
        return ni1

    def wireohm(self):
        lwr = (2 * self.rad_w + self.rad_l) * self.ni()
        return lwr * InDim.ohmmtr005


solval = SolenoidValve(OutDim.gap, InDim.suct_rad, OutDim.hole)


# Area = InDim.suct_rad * OutDim.hole * 2
# fup = pwalv.pic_pow_f()
# ni = sqrt(fup / (InDim.mgcons * Area / (2 * OutDim.gap**2)))

if __name__ == "__main__":
    print(f"{zsp} membrane deflection")
    print(f"{pwalv.pic_pow_wt()}watt pic power 1 sec {pwalv.batter()}watt all power in batter")
    print(solval.ni())
    print(solval.wireohm())
