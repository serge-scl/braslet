# The first problem arises if, when the edge of the suction cup is poorly laid, air penetrates inside.
# In order to avoid leakage of outside air into the system, a separate vacuum chamber is provided.
# The inlet and outlet of the chamber locks two valve positions.
# In the first position, the valve is pressed against the suction cup opening by a spring,
# separating the suction cup from the vacuum chamber.
# In this case, the hole from the vacuum line to the chamber is open.
# In the second position, the magnet is activated, the valve armature opens
# the connection of the vacuum chamber with the suction cup and closes the hole in line.


from valve_forceAC import F_hz, sl
from bt_mech_equation import MyConst, spring_f
from numpy import pi, sqrt
from scipy import constants


class Valve:
    def __init__(self, x, v, ic, h):
        self.p_atm = 1
        self.vacuum = x * 1000  # vacuum kPa to Pa
        self.pwm_v = v   # voltage
        self.pwm_i = ic  # current
        self.timer = h * 1000  # operating frequency kHz to Hz

    def spring_vs_vacuum(self):
        r_hole = 0.0005
        s_hole = r_hole**2 * pi
        power_vacuum = s_hole * self.vacuum
        power_spring = spring_f(MyConst.stl,0.0002,0.0025,10,0.003)
        ratio =  (power_spring - power_vacuum) / power_spring
        return 7 * ratio

    def time_s(self):
        r_real = sl.real_res()
        r_z = sl(MyConst.u_stl) * 2 * pi * F_hz
        spring_fq = self.spring_vs_vacuum()
        induct = round(sl(MyConst.u_stl), 6)
        return induct * spring_fq / sqrt(r_real**2 + r_z**2)

    def v_m_sec(self):
        return 0.001 / self.time_s()

    def frequent(self):
        return 1 / self.time_s()

    def equ_l(self):
        frq = F_hz
        n_torn = 127
        s_core = 0.01 * 0.001
        mu_0 = constants.mu_0
        return 2 * pi * frq * mu_0 * s_core * n_torn**2

    def adc_v(self):
        if self.pwm_i == 0.1:
            step = int(self.timer / self.frequent())
            gup = MyConst.mt_valve
            gup0 = gup / step
            for i in range(0, step):
                gup_stp = gup - gup0 * i
                yield round(self.equ_l() * self.pwm_i / gup_stp, 2)
            # v_open = round(self.equ_l() * self.pwm_i / gup, 2)
            # v_close = round(self.equ_l() * self.pwm_i / gup0, 2)
            # return f"{v_open}V open, {v_close}V close {step} cycle"


if __name__ == "__main__":
    vlv = Valve(10, 12, 0.1, 100)
    print(f" {round(vlv.time_s() * 1000000, 3)} microsecond")
    print(f" {round(vlv.v_m_sec(),2)} m/sec {round(vlv.v_m_sec(),2) * 3600 / 1000} km/ch,"
          f" {round(vlv.frequent() /1000,3)} kHz")
    for i1 in vlv.adc_v():
        print(f" {i1} v to ADC sampling 100 kHz")
    # print(f"{vlv.spring_vs_vacuum()} ratio power spring  that power  vacuum")
