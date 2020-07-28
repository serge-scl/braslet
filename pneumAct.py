# calculation of pneumatic drive and overall result
# V = h/6×[(2a + a1)b + (2a1 + a)b1]
# 400 ml/min  pump air with the performance

from wrist import phi, Male_wrst, Female_wrst
from calcsegments import middlbrs

Pumpperf = 400


def pneum_v(x):
    a = x
    h = (x * phi)/2
    b = a/2
    a1 = a - 2 * h
    b1 = b - 2 * h
    v = (h/6 * ((2 * a + a1) * b + (2 * a1 + a) * b1)) * 2
    return v


def time_pomp(x):
    return x * 60/Pumpperf


class MiddlMd:

    def __init__(self, l1, n):
        self.num_m = int(Male_wrst/l1)
        self.num_f = int(Female_wrst/l1)
        self.num_mod = n

    def middl_mod(self):
        if self.num_m % self.num_mod == 0 and self.num_f % self.num_mod == 0:
            return True
        else:
            return False


for i in range(middlbrs, 101):
    x1 = i/10
    for i1 in range(1, 4):
        pn1 = pneum_v(x1)
        tmp1 = int(time_pomp(pn1) * i1)
        if tmp1 < 50:
            # print(tmp1)
            md2 = MiddlMd(x1, i1)
            if md2.middl_mod() is True:
                print(f"{i1} in module, w {x1}mm, time  {tmp1}sec wm {md2.num_m}, wf{md2.num_f}")
