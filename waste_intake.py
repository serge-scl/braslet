# calculation of the dimensions and shape of the upper waste bin for medical gloves

from scipy.constants import atm


class FaceSlot:
    def __init__(self, x):
        self.shape = x  # x = h/ln


class AirReceivers:
    def __init__(self, x):
        self.pressure = x * atm
