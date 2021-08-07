# logic of operation of valves of suction cups and pneumatic actuators
import time


class SuctionCup:
    def __init__(self, x):
        self.signal = x

    def coil(self):
        pass

    def ancr_vlv(self):
        pass


class AirReceiver:
    def __init__(self, p):
        self.pump_pow = p
        self.tank = 0

    def pressure_gauge(self):
        if self.pump_pow < 10000:
            return 0
        elif self.pump_pow >= 10000:
            while self.tank < 100000:
                time.sleep(1)
                print(f"gauge {self.tank}")
                self.tank = self.tank + self.pump_pow
        print("TurnOff")
        return 0


class Pump:
    def __init__(self):
        self.pwr = int(input("click"))

    # def __call__(self, stp):
    #     self.stop = stp

    def power(self):
        if self.pwr == 0:
            return 0
        elif self.pwr == 1:
            print("Power")
            return 15000


class HandInGlove:
    pass


if __name__ == "__main__":
    pmp = Pump()
    ars = AirReceiver(pmp.power())
    ars.pressure_gauge()
