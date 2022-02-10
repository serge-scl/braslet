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


v_spr = ValveSpring(10, 0.005)

if __name__ == "__main__":
    for i in range(1, 15):
        i1 = i * 1000.0
        print(f"{v_spr(i1)} in vacuum: {i} - kPa ")
