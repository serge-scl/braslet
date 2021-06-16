# calculation of the effort of the electromagnetic semi-automatic
"""  The development here concerns the operating conditions of the suction cup valve.
In order for the vacuum in the suction cup to reliably grip the rubber of the glove
and hold it at the required tension, a semi-automatic valve is needed in the suction cup itself.
The valve opens on its own when air begins to be pumped out of the suction cup
and then closes under the action of a spring,
or if the pressure begins to increase what is inside the suction cup.
However, according to the working conditions, this valve must also be forced to open.
This is the process of returning atmospheric pressure to the inside of the suction cup
 at the end of a job, or cleaning the system before gripping.
In these two cases, the valve is driven by an electromagnet.
Here are preliminary calculations of the number of turns in the electromagnet winding,
power and, accordingly, the required dimensions.
The voltage and current applied to the electromagnet can represent a stream of pulses.
The frequency should be selected in such a way that it would be better to open the valve.
Suction cup dimensions from previous calculations, hemisphere with an inner diameter of 5 mm,
the upper hole for a valve with a diameter of 2 mm.
The pump power has been increased to -75 kPa. """


from scipy import constants
from numpy import pi, sqrt


class InDim:
    num_suct = 12
    mgcons = constants.mu_0
    suct_rad = 0.0025
    h_glove = 0.0001
    ribbnE = 500000  # Pa
    ohmmtr00005 = 9.29
    wire = 0.00005


class OutDim:
    pump_vcm = 75000
    hole = 0.001
    gap = 0.001
    i_battr = 0.2
    l_mgn = 0.005
    w_mgn = 0.003


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
        return self.pic_pow_wt() * self.half  * InDim.num_suct


# F = (n * i)**2 * mgconst * a / (2 * gap**2)
# n = number of turns in the solenoid
# a = Area


class SolenoidValve:
    def __init__(self, g, s, h):
        self.gap = g
        self.rad_l = s
        self.rad_w = h
        self.b_sln = 0.003
        self.w_flp = OutDim.w_mgn
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

    def sol_h(self):
        return 0.002 + 2 * self.wind_thick() + self.w_pin


zsp = z_sphere(OutDim.pump_vcm)
pwalv = PowValve(OutDim.pump_vcm, zsp, OutDim.hole, OutDim.gap)
solval = SolenoidValve(OutDim.gap, InDim.suct_rad, OutDim.gap)


# Area = InDim.suct_rad * OutDim.hole * 2
# fup = pwalv.pic_pow_f()
# ni = sqrt(fup / (InDim.mgcons * Area / (2 * OutDim.gap**2)))

if __name__ == "__main__":
    print(f"{round(zsp * 1000, 2)} mm membrane deflection")
    print(f"{round(pwalv.pic_pow_wt() * 1000, 2)} mwt s {round(pwalv.batter(), 2)} wt batter")
    print(f"{int(solval.ni())} turns magnet winding to {OutDim.i_battr}A")
    print(f"{round(solval.wireohm(), 2)} ohm conductor resistance ")
    print(f"{round(solval.wind_thick() * 1000, 2)} mm winding")
    print(f"magn DIM h {round(solval.sol_h() * 1000)} mm  ")
