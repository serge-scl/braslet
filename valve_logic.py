# The initial pressure P0atm for the entire system is equal to atmospheric – atm.
# Working volumes are constants.
# In the case of pressure, this is the total volume of all actuators V12act,
# and in the case of vacuum chambers V12vch.
# The total Tcl runtime is the few seconds that are acceptable for the end user to remove one glove.
# The volume of the air receivers - Vrx is the unknown target.
# Pressure - Prx / Pvx (positive or negative) in the receivers is also an unknown desired value.
from scipy.constants import atm
from scipy.integrate import odeint
from bt_mech_equation import pa, vch, GasFlow, spring_f
from numpy import pi, sqrt, linspace
from bt_mech_equation import Const
import matplotlib.pyplot as plt


P0atm = atm
V12act = pa.v_ring()  # m^3
V12vch = vch.free_v_chamb() * 12


def spring_k():
    g = Const.stl  # shear modulus
    d = 0.001  # spring wire diameter
    c = (0.022 + 0.01) * 2 / pi  # spring coil diameter
    n = 24  # number of turns
    return spring_f(g, d, c, n, 1)


sp_k = spring_k()
const = sp_k/2
const2 = Const.rib_E * 0.0001 * 0.02

# P = x(m*x/t**2 + k/2 + Es ) / S
# k - spring_kx
# E Const.rib_E
# s ribbon 0.1 mm X 20 mm
# S piston 10 x 20 mm
# m 150 g

def f_dxt(x, t):
    md = 0.8
    return x(const + const2)/0.0024


x0 = 0.01
tl = linspace(0, 100)
od = odeint(f_dxt, x0, tl)
plt.plot(tl, od)
plt.show()


class VlsFlow(GasFlow):
    def gf3(self):
        uc = 1
        gm1 = uc * self.s * self.p / sqrt(self.R * (self.T + 20)) * self.beta**(1/self.k)
        gm2 = sqrt(2 * self.k / (self.k - 1)*(1 - self.beta**((self.k - 1) / self.k)))
        return gm1 * gm2


class Valve:
    def __call__(self, x):
        return x / 1000


vlv1 = Valve()


vlsflw = VlsFlow(1.2, vlv1(1))

if __name__ == "__main__":
    print(f"V act {round(V12act * 1e6,1)}cm3")
    print(f"V vacuum chamb ring{round(V12vch * 1e6, 1)}cm3")
    print(f"old eqw {round(vlsflw.gf2() * 1e3,5)} g/sec,  new eqw {round(vlsflw.gf3() * 1e3,5)} g/sec")
    print(f" spring {const}, ribbon {const2}")
