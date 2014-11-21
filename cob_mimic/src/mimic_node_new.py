#!/usr/bin/python
#################################################################
##\file
#
# \note
# Copyright (c) 2010 \n
# Fraunhofer Institute for Manufacturing Engineering
# and Automation (IPA) \n\n
#
#################################################################
#
# \note
# Project name: Care-O-bot Research
# \note
# ROS stack name: cob_environments
# \note
# ROS package name: cob_gazebo_objects
#
# \author
# Author: Nadia Hammoudeh Garcia, email:nadia.hammoudeh.garcia@ipa.fhg.de
# \author
# Supervised by: Nadia Hammoudeh Garcia, email:nadia.hammoudeh.garcia@ipa.fhg.de
#
# \date Date of creation: Nov 2014
#
# \brief
# Implements script server functionalities.
#
#################################################################
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# - Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer. \n
# - Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution. \n
# - Neither the name of the Fraunhofer Institute for Manufacturing
# Engineering and Automation (IPA) nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission. \n
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License LGPL as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License LGPL for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License LGPL along with this program.
# If not, see < http://www.gnu.org/licenses/>.
#
#################################################################

import os
import subprocess
import rospy
import roslib
import Image
roslib.load_manifest('cob_mimic')
import pygame
from pygame.locals import *
from cob_mimic.srv import *

import time
        
def set_mimic(req):

    print "Mimic: %s" % req.mimic.data
    file_localition = roslib.packages.get_pkg_dir('cob_mimic') + '/common/' + req.mimic.data + '.gif'
    command = "animate -loop 0 %s"  % file_localition
    os.system(command)

def main():
    rospy.init_node('mimic')
    s=rospy.Service('mimic',SetMimic, set_mimic)
    rospy.spin()
    
 
if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt, e:
    pass
  print "exiting"
