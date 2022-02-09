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


class ValveSpring:

    def __init__(self, n, dl):
        self.nc = n
        self.dln = dl
        # self.spf = spring_f(MyConst.stl, 0.0005, 0.005, n, dl)

    def __call__(self, v):
        spf = spring_f(MyConst.stl, 0.0002, 0.0025, self.nc, self.dln)
        hbbl = z_sphere(v)
        sholl = MyConst.suct_rad**2 * pi
        # return spf, hbbl, sholl
        if hbbl < 0.002:
            return f"{hbbl * 1000} mm h sphere "
        else:
            return f"{spf / (v * sholl)} spring/valve air power "


v_spr = ValveSpring(10, 0.005)

if __name__ == "__main__":
    for i in range(1, 20):
        i1 = i * 1000
        print(f"{v_spr(i1)} in vacuum {i} - kPa ")
