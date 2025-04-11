#!/usr/bin/env python
import rospy
from Warthog.msg import Robot1 
rospy.init_node('robot_node')

rate = rospy.Rate(2)

pub = rospy.Publisher('/topic' , Robot1 , queue_size=1)

robot=Robot1()
robot.Nume = "Warthog"
robot.Model="Renault"
robot.An_Fabricatie = 2008
robot.Greutate = 120.2

while not rospy.is_shutdown():
	print(robot.Nume,robot.Model,robot.An_Fabricatie,robot.Greutate)
	pub.publish(robot)
	rate.sleep()
