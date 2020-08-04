# calculation of pneumatic drive and overall result
# V = h/6×[(2a + a1)b + (2a1 + a)b1]
# 400 ml/min  pump air with the performance
# backpressure ability of up to 30 kPa

from wrist import phi, Male_wrst, Female_wrst
# from calcsegments import middlbrs


Pumpperf = 400/60  # sec
Backpress = 30
Node_W = 8.3


def pneum_v(x):
    a = x
    h = (x * phi)/2
    b = a/2
    a1 = a - 2 * h
    b1 = b - 2 * h
    v = (h/6 * ((2 * a + a1) * b + (2 * a1 + a) * b1)) * 2
    return v


def time_pomp(x):
    return x/Pumpperf


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


def vcupsuch(min0, max1):

    for i in range(min0, max1):
        x1 = i/10
        for i1 in range(1, 4):
            pn1 = pneum_v(x1)
            tmp1 = int(time_pomp(pn1) * i1)
            if tmp1 < 50:
                # print(tmp1)
                md2 = MiddlMd(x1, i1)
                if md2.middl_mod() is True:
                    yield f"{i1} in module, w {x1}mm, time  {tmp1}sec wm {md2.num_m}, wf{md2.num_f}"


def l_buff_tank(h, w_fix, sec):

    node_v = pneum_v(Node_W)
    module_v = node_v * 3
    module_w = Node_W * 3
    w_buff_tank = (module_w - w_fix)/2
    h_buff_tank = h
    v_buff_tank = module_v * (100/Backpress) - Pumpperf * sec
    lbtk = v_buff_tank/(w_buff_tank * h_buff_tank)
    return lbtk


def buff_tank(h, fx):

    for i2 in range(1,h):
        for i3 in range(1, fx):
            lbt2 = l_buff_tank(i2, i3, 1)
            yield f"l buff {lbt2} h buuf {i2} w buff {(25 - i3)/2} w fix {i3}"


vcps = vcupsuch(75, 101)
bft = buff_tank(7, 5)
for i in bft:
    print(i)
