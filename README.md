
Here I have collected calculations and drawings of a project for creating a device for removing disposable medical gloves with subsequent storage, accounting and disposal. This procedure is necessary to avoid a significant risk of infection during the work of medical staff. Various visual aids here offer a written and illustrated procedure on how to properly remove a disposable glove to avoid contact with a contaminated surface. However, the human factor suggests that sooner or later a mistake happens. This possibility is exacerbated by the factor of fatigue and stress.
The root directory contains files where I make various calculations. The earliest calculations related to the overall dimensions of the bracelet and its details relative to the size of the coverage of a man's or woman's wrist. These calculations cannot be called accurate. These are just some starting points.
Another group of calculations concerned the ability to determine the forces that a pneumatic mechanism must create for successful operation. This calculation showed that the range can vary quite widely. In the future, using differential equations will allow us to find more optimal values.
And the third type of calculation is the calculation of the solenoid valve that controls the operation of the suction cup. I tried to verify these calculations as far as possible.
The designCAD folder contains drawings in an open format. This work has not yet been completed in its entirety. So far, there are no drawings of the case, the upper and lower parts of the entire device, and it remains to be done. In the upper part there will be a working niche with a bracelet, and receivers and micropumps working with it. At the bottom there will be a negative pressure fan and storage for used gloves. So far, only part of the drawings of the bracelet have been made. This is a vacuum chamber with a solenoid valve and part of a pneumatic drive. All this is still in the form of separate parts without assembly. In the near future, we plan to complete the vacuum line and pneumatic drive.
Kicad pcb will contain two PCBs in two separate projects. This is a power control unit for the suction cup valve and a sensor unit that registers the correct touch of the hand with the glove. How the PCBs are attached can be seen in the sub_asstmbly/solenoid_in_chamb01 file. The inputs and outputs of these blocks are made in such a way that various types of microcontrollers can be connected. I did not finish the topology of the circuits, since the type of connectors may still be different.
