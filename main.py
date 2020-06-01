from Simulation.simulator.rimulator import Rimulator
from Simulation.robots.kheperaiii.robot import Kheperaiii
import threading

rimulator = Rimulator([(Kheperaiii, (0.5, 0.3)), (Kheperaiii, (-0.5, -0.3)) ])
rimulator.add_robot((Kheperaiii, (0,0)))
rimulator.start_sobot_rimulator()
