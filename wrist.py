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


class InitialSettings:
    def __init__(self, wrist_grip, number_seg):
        self.wrist_grip = wrist_grip

        self. wristH = wrist_grip / (pi + phi * 2)
        self.wrist_area = self.wristH ** 2 * (phi + 0.5 * pi)
        self.number_seg = number_seg
        self.segment_length = wrist_grip/number_seg

    def circle_segment(self):
        cs = int(self.number_seg * phi)
        if cs % 2 != 0:
            return cs + 1
        else:
            return cs

    def rectangle_side(self):
        return (self.number_seg - self.circle_segment())/2

    def apex_angle(self):
        return 180/self.circle_segment()


is1 = InitialSettings(wrist_grip=150, number_seg=10)
polygon_area = is1.segment_length * is1.circle_segment() * is1.segment_length \
               * cos(radians(is1.apex_angle()))
bracelet_area = is1.wristH * is1.rectangle_side() * is1.segment_length + polygon_area

if __name__ == "__main__":
    print(bracelet_area)
    print(is1.wrist_area)
