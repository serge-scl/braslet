# logic of operation of valves of suction cups and pneumatic actuators
import time


class SuctionCup:
    def __init__(self, x):
        self.frequent = x

    def valve(self):
        pass

    def hall_sensor(self):
        pass


class PulseGen:
    pass


class Valve:
    def __init__(self, x, p):
        self.signal = x
        self.press_gg = p
        self.press_min = 10000

    def valve_in(self):
        if self.press_gg == 0:
            return 0
        elif self.press_gg > self.press_min:
            return 1

    def valve_out1(self):
        if self.signal == 1 and self.valve_in() == 1:
            return 1
        elif self.signal == 4:
            return 0
        else:
            return 0

    def valve_out2(self):
        if self.signal == 2 and self.valve_in() == 1:
            return 1
        elif self.signal == 4:
            return 0
        else:
            return 0

    def valve_res(self):
        if self.signal == 3 and self.valve_in() == 1:
            return 1
        elif self.signal == 4:
            return 0
        else:
            return 0

    def valve_not(self):
        if self.signal == 4:
            return 1
        else:
            return 0


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


class SensHand:

    def hall_sensor(self):
        pass

    def cap_touch(self):
        pass

    def voltmeter(self):
        pass

    def proximity_sensor(self):
        pass


class HandInGlove:
    pass


class ModulePress:

    class SuctCupR(SuctionCup):
        pass


    class SuctCupL(SuctionCup):
        pass


class ModuleSense:
    pass


if __name__ == "__main__":
    pmp = Pump()
    ars = AirReceiver(pmp.power())
    ars.pressure_gauge()
