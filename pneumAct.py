# calculation of pneumatic drive and overall result
# V = h/6×[(2a + a1)b + (2a1 + a)b1]
# flw  400 ml/min  pump air with the performance

from wrist import phi, Male_wrst, Female_wrst
from calcsegments import middlbrs


def pneum_v(x):
    a = x
    h = (x * phi)/2
    b = a/2
    a1 = a - 2 * h
    b1 = b - 2 * h
    v = (h/6 * ((2 * a + a1) * b + (2 * a1 + a) * b1)) * 2
    return v


def time_pomp(x):
    flw = 400
    return (x/flw) * 60


def middl_md(x, n):
    ml = Male_wrst
    fm = Female_wrst
    mln = int(ml/x)
    fmn = int(fm/x)
    if mln % n == 0 and fmn % n == 0:
        return True
    else:
        return False


for i in range(middlbrs, 100):
    x1 = i/10
    for i1 in range(1, 7):
        pn1 = pneum_v(x1)
        tmp1 = int(time_pomp(pn1) * i1)
        if tmp1 < 30:
            # print(tmp1)
            md = middl_md(x1, i1)
            if md is True:
                print(f"{i1} in module, width {x1}mm, time  {tmp1}sec")
