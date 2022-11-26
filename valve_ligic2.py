# The first problem arises if, when the edge of the suction cup is poorly laid, air penetrates inside.
# In order to avoid leakage of outside air into the system, a separate vacuum chamber is provided.
# The inlet and outlet of the chamber locks two valve positions.
# In the first position, the valve is pressed against the suction cup opening by a spring,
# separating the suction cup from the vacuum chamber.
# In this case, the hole from the vacuum line to the chamber is open.
# In the second position, the magnet is activated, the valve armature opens
# the connection of the vacuum chamber with the suction cup and closes the hole in line.


from valve_forceAC import F_hz  # sl
from bt_mech_equation import MyConst, spring_f
from numpy import pi, sqrt, average
from scipy import constants
# from statistics import mean


def induct(x, s):
    u0u = constants.mu_0 * MyConst.stl
    return u0u * x**2 * s / 0.025


class Valve:
    def __init__(self, x, v, ic, h, n):
        # self.p_atm = 1
        self.vacuum = x * 1000  # vacuum kPa to Pa
        self.pwm_v = v   # voltage
        self.pwm_i = ic  # current
        self.timer = h * 1000  # operating frequency kHz to Hz
        self.n_torn = n  # number of turns in a coil winding
        self.w_core = 0.01
        self.th_core = 0.001
        self.frq = F_hz

    def spring_vs_vacuum(self):
        r_hole = 0.0015
        s_hole = r_hole**2 * pi
        power_vacuum = s_hole * self.vacuum
        power_spring = spring_f(MyConst.stl, 0.0002, 0.0025, 10, 0.003)
        ratio = (power_spring - power_vacuum) / power_spring
        return 7 * ratio

    def resist_real(self):
        d = (self.w_core + self.th_core) * 2
        ln = d * self.n_torn
        return ln * 2.23  # 2.23 ohm/m copper wire 0.1 mm

    def time_s(self):
        r_real = self.resist_real()
        s_core = self.w_core * self.th_core
        ind = induct(self.n_torn, s_core)
        r_z = ind * 2 * pi * self.frq
        spring_fq = self.spring_vs_vacuum()
        return ind * spring_fq / sqrt(r_real**2 + r_z**2)

    def v_m_sec(self):
        return 0.001 / self.time_s()

    def frequent(self):
        return 1 / self.time_s()

    def equ_l(self):
        n_torn = self.n_torn
        return 2 * pi * self.frq * constants.mu_0 * self.w_core * self.th_core * 2 * n_torn**2

    def adc_v(self):
        gup_fix = 0.0001
        gup = 0.001
        if gup > gup_fix:
            step = int(self.timer / self.frequent())
            gup0 = gup / step
            middle_i = []
            for i in range(0, step):
                gup_stp = gup - gup0 * i + gup_fix
                i_s = round(gup_stp * self.pwm_v / self.equ_l(), 2)
                middle_i.append(i_s)
                # return mean(middle_i)
                return average(middle_i)

    def __call__(self, x):
        gup_fix = 0.0001
        gup = x
        if gup > gup_fix:
            step = int(self.timer / self.frequent())
            gup0 = gup / step
            for i in range(0, step):
                gup_stp = gup - gup0 * i + gup_fix
                yield round(self.equ_l() * self.adc_v() / gup_stp, 2)
            # v_open = round(self.equ_l() * self.pwm_i / gup, 2)
            # v_close = round(self.equ_l() * self.pwm_i / gup0, 2)
            # return f"{v_open}V open, {v_close}V close {step} cycle"
        else:
            yield round(self.equ_l() * self.pwm_i / (gup + gup_fix), 2)


class MicroController:
    def __init__(self, x, y):
        self.prior = x
        self.next = y

    def sensor_current(self):
        return 0

    def senosor_touch(self):
        return 1

    def sensor_hall(self):
        return 0


if __name__ == "__main__":
    adc = Valve(10, 3, 0.1, 100, 130)
    print(f" {round(adc.time_s() * 1000000, 3)} microsecond")
    print(f" {round(adc.v_m_sec(), 2)} m/sec {round(adc.v_m_sec(), 2) * 3600 / 1000} km/ch,"
          f" {round(adc.frequent() / 1000, 3)} kHz")
    # for i2 in adc.adc_v():
    #     print(f"{i2} i current")
    print(f"{adc.adc_v()} middle i")
    for i1 in adc(0.001):
        if i1 < 12:
            print(f" {i1} v to ADC  100 kHz")
        else:
            adc2 = Valve(10, 3, 0.16, 100, 30)  # switch to short winding
            for i2 in adc2(0.000005):
                print(f" {i2} v to ADC  100 kHz captcha")

    print(f"{adc.spring_vs_vacuum()/7} p/spring")
