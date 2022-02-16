# use alternating current to power the electromagnet
"""In addition to alternating current, the solution is supposed to use a metal spring in the valve.
his will greatly simplify the design.
The spring should be mounted inside the horseshoe of the solenoid core
and act back when the valve is lifted by the electromagnet.
In this case, the valve will perform the OR function between the vacuum line and the suction cup.
The Hall sensor will be replaced by current measurement in the solenoid circuit.
To the solenoid coil itself will be added a parallel capacitor with an appropriately selected impedance.
"""

from bt_mech_equation import MyConst
from bt_mech_equation import spring_f
from valve_force import z_sphere
from math import pi
from wrist import Male_wrst
from bt_mech_equation import PneumAct
from scipy import constants


class ValveSpring:

    def __init__(self, n, dl):
        self.nc = n  # number of turns
        self.dln = dl  # and delta of spring compression
        self.d_wire = 0.0002  # spring wire diameter
        self.d_coil = 0.0025  # spring coil diameter

    def __call__(self, v):
        spf = spring_f(MyConst.stl, self.d_wire, self.d_coil, self.nc, self.dln)
        hbbl = z_sphere(v)
        sholl = MyConst.suct_rad**2 * pi
        if hbbl < 0.002:
            return f"{round(hbbl * 1000, 3)} mm H deformation, {round(spf, 3)} N spring force "
        else:
            return f"{round(spf / (v * sholl), 3)} spring/valve air power "


class SpringPressH(ValveSpring):
    def h_pr(self):
        return self.nc * self.d_wire * 1.1


pa3 = PneumAct(Male_wrst, MyConst.plt)
v_spr = ValveSpring(10, 0.005)
sp = SpringPressH(10, 0.005)


class Solenoid:
    def __init__(self, x, y):
        self.sp_pr = sp.h_pr()
        self.wall = MyConst.vcht
        self.h_ch = MyConst.h_chamb
        self.core_w = MyConst.scw
        self.s_r = MyConst.suct_rad
        self.mt_valve = MyConst.mt_valve
        self.core_thick = x  # magnetic core body thickness
        self.d_wire = y   # solenoid wire diameter
        self.cu_res = MyConst.cu_res

    def chamb_h(self):
        top_btm = self.s_r + self.wall * 2
        return self.h_ch - top_btm

    def core_ln(self):
        return pa3.w_chamb() - self.wall * 2

    def inner_space(self):
        bend = 0.001  # core bend
        flange = 0.001  # suction cup flange
        vl_th = 0.0005  # valve thickness
        arm_core = 0.001  # magnet fastener
        msc = self.mt_valve + self.core_thick
        return self.chamb_h() - (bend + flange + msc + vl_th + arm_core)

    def spring_washer(self):
        return self.inner_space() - sp.h_pr() + 0.001

    def num_torn(self):
        return int(self.inner_space() / self.d_wire)

    def real_res(self):
        insulation_coil = 0.0005
        perm = (self.core_thick + insulation_coil) * 2 + (self.core_w + insulation_coil) * 2
        wire_a = perm * self.num_torn()
        d_wire_cu = 0.1  # mm
        return round(4 * self.cu_res * wire_a / (pi * d_wire_cu**2), 1)
        # R = 4 * p * a / (pi * d ** 2)

    def __call__(self, u):
        s_core = self.core_thick * self.core_w
        return constants.mu_0 * u * self.num_torn()**2 * s_core / self.inner_space()
        # L = (μ0μ * N ** 2 * S) / ln https://en.wikipedia.org/wiki/Inductance


sl = Solenoid(0.001, 0.00013)

if __name__ == "__main__":
    print(f"{sl(100)} H solenoid inductance")
    print(f"{sl.real_res()} ohm - coil winding resistance real")
    print(f"{int(sl.spring_washer() * 1000)} mm spring washer height")
    print(f"{sl.num_torn()} number of turns of the solenoid winding")
    for i in range(1, 15):
        i1 = i * 1000.0
        print(f"{v_spr(i1)} in vacuum: {i} - kPa ")
