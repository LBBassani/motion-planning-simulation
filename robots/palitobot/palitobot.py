# # Sobot Rimulator - A Robot Programming Tool # #
# Copyright (C) 2013-2014 Nicholas S. D. McCrea
# License GNU General Public License v 3 - GPLv3

""" Nome do módulo :        Palitobot
    Ano de criação :        2020/06
    Descrição do módulo :   Módulo que procura simular o robô ERUS/palitobot3, um robô seguidor de linhas
                                desenvolvido como terceiro protótipo no projeto ERUS/Seguidor de Linhas
                                veja mais em erus.ufes.br/
    Versão :                0.1 - Pré-Alpha
    Pré-requisitos :        Sobot Rimulator Core (srimulatorcore)
    Membros :               Lorena "Ino" Bassani
"""

from srimulatorcore.models.robot import Robot
from srimulatorcore.models.differential_drive_dynamics import DifferentialDriveDynamics
from srimulatorcore.models.polygon import Polygon
from srimulatorcore.models.pose import Pose
from srimulatorcore.models.robot_supervisor_interface import RobotSupervisorInterface
from srimulatorcore.models.supervisor import Supervisor
from srimulatorcore.models.wheel_encoder import WheelEncoder

class Palitobot3 (Robot):
    pass
