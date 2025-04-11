#!/usr/bin/env python 
import rospy 
from sensor_msgs.msg import LaserScan

def callback(data):
	rospy.loginfo("Distanta in fata : %gf" , data.ranges[len(data.ranges)//2])

def listener():
	rospy.init_node('Warthog' , anonymous = True)
	rospy.Subscriber('/scan' , LaserScan , callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
