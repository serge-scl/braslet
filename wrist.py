#  wrist
#  calculation of vacuum elements min
# from sympy import *
# .......................................
# pHi = (1 + sqrt(5)) / 2 golden ratio 1
# phi = -(1 - sqrt(5)) / 2 golden ratio 2
#
# wrist_grip = 150 to 170
# number_seg = 10 min
#
# wristH = wrist_grip / (pi + phi * 2)
# wrist_area = wristH ** 2 * (phi + 0.5 * pi)
#
# segment_length = wrist_grip/number_seg
# circle_segments = int(number_seg * phi)
# rectangle_side = (number_seg - circle_segments)/2
#
# polygon_area = segment_length * circle_segments * segment_length * cos(radians(30))
# bracelet_area = wristH * rectangle_side * segment_length + polygon_area
# pain = wrist_area - bracelet_area
# print(pain)
from math import *

pHi = (1 + sqrt(5)) / 2
phi = -(1 - sqrt(5)) / 2
Male_wrst = 180
Female_wrst = 150


class InitialSettings:
    def __init__(self, wrist_grip, number_seg):
        self.wrist_grip = wrist_grip
        self. wristH = wrist_grip / (pi + phi * 2)
        self.wrist_area = self.wristH ** 2 * (phi + 0.5 * pi)
        self.number_seg = number_seg
        self.segment_length = wrist_grip/number_seg

    def circle_segment(self):
        return int(self.number_seg * 0.6)

    # def rectangle_side(self):
    #     return int(self.number_seg * 0.2)

    def apex_angle(self):
        return 180/self.circle_segment()


is1 = InitialSettings(wrist_grip=150, number_seg=10)
polygon_area = (is1.wrist_grip * 0.6) * (is1.wristH/2) * cos(radians(is1.apex_angle()))
bracelet_area = is1.wristH**2 * phi + polygon_area

for i in range(10, 25):
    is2 = InitialSettings(wrist_grip=150, number_seg=i)
    pa2 = (is2.wrist_grip*0.6) * (is2.wristH/2) * cos(radians(is2.apex_angle()))
    ba2 = is2.wristH**2 * phi + pa2
    print(ba2, is2.number_seg)
    # print(is2.wrist_area)

if __name__ == "__main__":
    print(bracelet_area)
    print(is1.wrist_area)
