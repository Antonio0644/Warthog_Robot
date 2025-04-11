#!/usr/bin/env python 

import rospy
from  Warthog.msg import Robot

rospy.init_node('Publish')

def callback(msg):
	print(msg.nume , msg.nr_roti , msg.unghi)
sub=rospy.Subscriber('/topic',Robot , callback)

rospy.spin()
