# # Sobot Rimulator - A Robot Programming Tool # #
# Copyright (C) 2013-2014 Nicholas S. D. McCrea
# License GNU General Public License v 3 - GPLv3

""" Nome do módulo :        Line Sensors
    Ano de criação :        2020/06
    Descrição do módulo :   Módulo que procura simular os sensores de linha utilizados no robô ERUS/palitobot3, 
                                um robô seguidor de linhas desenvolvido como terceiro protótipo no projeto 
                                ERUS/Seguidor de Linhas
                                veja mais em erus.ufes.br/
    Versão :                0.1 - Pré-Alpha
    Pré-requisitos :        Sobot Rimulator Core (srimulatorcore)
    Membros :               Lorena "Ino" Bassani
"""

from srimulatorcore.models.sensor import Sensor

class LineSensor(Sensor):

    def read(self):
        pass