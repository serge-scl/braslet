# vacuum pneumatic bracelet for replacing medical gloves
# calculation of vacuum elements min
# male wrist 180 - 200 mm
# female wrist 150 - 170 mm
# tube  1.5 diameter of medical tubes
# dif_hm 0.7  height to width ratio
# v_male_pip male bracelet tube volume
# v_female_pip female bracelet tube volume
# v_male_vcm required volume of the vacuum zone male
# v_female_vcm required volume of the vacuum zone female
# add_v_sell ratio of the vacuum zone to the shell
# v_male_sell overall volume male
# v_female_sell overall volume female
# min_male_find   minimum side of the vacuum device in the men's bracelet
# min_female_find side of the vacuum device in a women's bracelet

from math import pi, sqrt
from wrist import pHi
# from sympy import solve, Symbol


class InitSet:
    def __init__(self, male_wrist, female_wrist, tube, dif_hw, add_v_shell, kfv):
        self.male_wrist = male_wrist
        self.female_wrist = female_wrist
        self.male_wrist_opn = male_wrist * pHi
        self.female_wrist_opn = female_wrist * pHi
        self.tube = tube
        self.rad_tub = tube/2
        self.dif_hw = dif_hw
        self.add_v_shell = add_v_shell
        self.kf_v = kfv

    def min_male_fnd(self):
        v_male_tube = self.rad_tub**2 * pi * self.male_wrist * 2
        v_male_vcm = v_male_tube * self.kf_v
        v_male_sell = v_male_vcm + (v_male_vcm/self.add_v_shell)
        mmf = sqrt(v_male_sell * 3/(self.male_wrist * self.dif_hw))
        return mmf

    def min_female_fnd(self):
        v_female_tube = self.rad_tub**2 * pi * self.female_wrist * 2
        v_female_vcm = v_female_tube * self.kf_v
        v_female_sell = v_female_vcm + (v_female_vcm/self.add_v_shell)
        mff = sqrt(v_female_sell * 3/(self.female_wrist * self.dif_hw))
        return mff


is1 = InitSet(male_wrist=180, female_wrist=150, tube=1.5, dif_hw=0.7, add_v_shell=4, kfv=3)


# x = Symbol("x")
# minfndm0 = solve([(is1.male_wrist * is1.dif_hw * x ** 2) / 3 - v_male_sell], x)
# minfndf0 = solve([(is1.female_wrist * is1.dif_hw * x ** 2) / 3 - v_female_sell], x)

# print(minfndm0)
# print(minfndf0)
if __name__ == "__main__":
    print(is1.min_male_fnd())
    print(is1.min_female_fnd())
