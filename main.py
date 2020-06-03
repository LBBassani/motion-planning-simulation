

from srimulatorcore.rimulators_samples.rimulator import Rimulator
from srimulatorcore.sobots_samples.kheperaiii.kheperaiii import Kheperaiii
from srimulatorgtk.window import SobotRimulatorWindow

rimulator = Rimulator([(Kheperaiii, (0.5, 0.3)), (Kheperaiii, (-0.5, -0.3)) ])
rimulator.add_robot((Kheperaiii, (0,0)))
window = SobotRimulatorWindow(rimulator)
window.start_sobot_rimulator()