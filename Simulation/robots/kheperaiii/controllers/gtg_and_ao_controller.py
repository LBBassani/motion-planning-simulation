# Sobot Rimulator - A Robot Programming Tool
# Copyright (C) 2013-2014 Nicholas S. D. McCrea
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# Email mccrea.engineering@gmail.com for questions, comments, or to report bugs.


from math import atan2, pi

from ....simulator.models.controllers.gtg_and_ao_controller import GTGAndAOController
from ....simulator.utils import linalg2_util as linalg
from .avoid_obstacles_controller import KheperaiiiAvoidObstaclesController
from .go_to_goal_controller import KheperaiiiGoToGoalController

class KheperaiiiGTGAndAOController(GTGAndAOController):

  def __init__( self, supervisor ):
    # bind the supervisor
    self.supervisor = supervisor

    # initialize controllers to blend
    self.go_to_goal_controller = KheperaiiiGoToGoalController( supervisor )
    self.avoid_obstacles_controller = KheperaiiiAvoidObstaclesController( supervisor )

    # sensor gains (weights)
    self.avoid_obstacles_controller.sensor_gains = [
      1.0-( (0.4*abs(p.theta)) / pi )
      for p in self.avoid_obstacles_controller.proximity_sensor_placements ]

    # blending factor
    self.alpha = 0.1  # go-to-goal heading is given this much weight, avoid-obstacles is given the remaining weight

    # control gains
    self.kP = 10.0
    self.kI = 0.0
    self.kD = 0.0
    
    # stored values - for computing next results
    self.prev_time = 0.0
    self.prev_eP = 0.0
    self.prev_eI = 0.0

    # key vectors and data (initialize to any non-zero vector)
    self.obstacle_vectors = [ [ 1.0, 0.0 ] ] * len( self.avoid_obstacles_controller.proximity_sensor_placements )
    self.ao_heading_vector = [ 1.0, 0.0 ]
    self.gtg_heading_vector = [ 1.0, 0.0 ]
    self.blended_heading_vector = [ 1.0, 0.0 ]

  def update_heading( self ):
    # generate and store the vectors generated by the two controller types
    self.gtg_heading_vector = self.go_to_goal_controller.calculate_gtg_heading_vector()
    self.ao_heading_vector, self.obstacle_vectors = self.avoid_obstacles_controller.calculate_ao_heading_vector()

    # normalize the heading vectors
    self.gtg_heading_vector = linalg.unit( self.gtg_heading_vector )
    self.ao_heading_vector = linalg.unit( self.ao_heading_vector )

    # generate the blended vector
    self.blended_heading_vector = linalg.add( linalg.scale( self.gtg_heading_vector, self.alpha ),
                                              linalg.scale( self.ao_heading_vector, 1.0 - self.alpha ) )

  def execute( self ):
    # calculate the time that has passed since the last control iteration
    current_time = self.supervisor.time()
    dt = current_time - self.prev_time

    # calculate the error terms
    theta_d = atan2( self.blended_heading_vector[1], self.blended_heading_vector[0] )
    eP = theta_d
    eI = self.prev_eI + eP*dt
    eD = ( eP - self.prev_eP ) / dt

    # calculate angular velocity
    omega = self.kP * eP + self.kI * eI + self.kD * eD
    
    # calculate translational velocity
    # velocity is v_max when omega is 0,
    # drops rapidly to zero as |omega| rises
    v = self.supervisor.v_max() / ( abs( omega ) + 1 )**1.5

    # store values for next control iteration
    self.prev_time = current_time
    self.prev_eP = eP
    self.prev_eI = eI

    self.supervisor.set_outputs( v, omega )

    # === FOR DEBUGGING ===
    # self._print_vars( eP, eI, eD, v, omega )

  def _print_vars( self, eP, eI, eD, v, omega ):
    print ("\n\n")
    print ("==============")
    print ("ERRORS:")
    print ("eP: " + str( eP ))
    print ("eI: " + str( eI ))
    print ("eD: " + str( eD ))
    print ("")
    print ("CONTROL COMPONENTS:")
    print ("kP * eP = " + str( self.kP ) + " * " + str( eP ))
    print ("= " + str( self.kP * eP ))
    print ("kI * eI = " + str( self.kI ) + " * " + str( eI ))
    print ("= " + str( self.kI * eI ))
    print ("kD * eD = " + str( self.kD ) + " * " + str( eD ))
    print ("= " + str( self.kD * eD ))
    print ("")
    print ("OUTPUTS:")
    print ("omega: " + str( omega ))
    print ("v    : " + str( v ))
