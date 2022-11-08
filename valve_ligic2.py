# The first problem arises if, when the edge of the suction cup is poorly laid, air penetrates inside.
# In order to avoid leakage of outside air into the system, a separate vacuum chamber is provided.
# The inlet and outlet of the chamber locks two valve positions.
# In the first position, the valve is pressed against the suction cup opening by a spring,
# separating the suction cup from the vacuum chamber.
# In this case, the hole from the vacuum line to the chamber is open.
# In the second position, the magnet is activated, the valve armature opens
# the connection of the vacuum chamber with the suction cup and closes the hole in line.


from valve_forceAC import F_hz, sl
from bt_mech_equation import MyConst
from numpy import pi, sqrt
from scipy import constants


class Valve:
    def __init__(self, x, v, i):
        self.p_atm = 1
        self.vacuum = x
        self.pwm_v = v
        self.pwm_i = i
        self.fr = F_hz
        self.induct = round(sl(MyConst.u_stl), 6)

    def time_s(self):
        r_real = sl.real_res()
        r_z = sl(MyConst.u_stl) * 2 * pi * F_hz
        spring_f = 7
        return self.induct * spring_f / sqrt(r_real**2 + r_z**2)

    def v_m_sec(self):
        return 0.001 / self.time_s()

    def equ_l(self):
        n_torn = 70
        s_core = 0.01 * 0.001
        mu_0 = constants.mu_0
        return 2 * pi * self.fr * mu_0 * s_core * n_torn**2

    def adc_v(self):
        if self.pwm_i == 0.1:
            step = 100
            gup = MyConst.mt_valve
            gup0 = gup / step
            v_open = self.equ_l() * self.pwm_i / gup
            v_close = self.equ_l() * self.pwm_i / gup0
            return f"{v_open} open, {v_close} close"
        else:
            return "power off"


if __name__ == "__main__":
    vlv = Valve(23, 12, 1)
    print(f" {round(vlv.time_s() * 1000000, 6)} microsecond")
    print(f" {round(vlv.v_m_sec(),2)} m/sec {round(vlv.v_m_sec(),2) * 3600 / 1000} km/ch")
    print(vlv.adc_v())
