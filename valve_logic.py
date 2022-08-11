# The initial pressure P0atm for the entire system is equal to atmospheric – atm.
# Working volumes are constants.
# In the case of pressure, this is the total volume of all actuators V12act,
# and in the case of vacuum chambers V12vch.
# The total Tcl runtime is the few seconds that are acceptable for the end user to remove one glove.
# The volume of the air receivers - Vrx is the unknown target.
# Pressure - Prx / Pvx (positive or negative) in the receivers is also an unknown desired value.
from scipy.constants import atm
from bt_mech_equation import pa, vch

P0atm = atm
V12act = pa.v_ring()  # m^3
V12vch = vch.free_v_chamb() * 12

if __name__ == "__main__":
    print(f"V act {round(V12act * 1e6,1)}cm3")
    print(f"V vacuum chamb ring{round(V12vch * 1e6, 1)}cm3")
