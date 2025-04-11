#!/usr/bin/env python 
import rospy 
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import LaserScan

def callback(scan_robot):
	inainte=scan_robot.ranges[359]
	dreapta=scan_robot.ranges[0]
	stanga=scan_robot.ranges[180]
	
	move=Twist()
	if inainte >1.0:
		move.linear.x=0.5
		move.angular.z=0.0
	elif inainte >1.0:
		move.linear.x=0.0
		move.angular.z=0.5
	elif dreapta <1.0:
		move.linear.x=0.0
		move.angular.z=0.5
	elif stanga<1.0:
		move.linear.x=0.0
		move.angular.z=-0.5
	else:
		move.linear.x=0
		move.angular.z=0
	
	pub.publish(move)
	



rospy.init_node('miscare_nod')


pub=rospy.Publisher('/cmd_vel' ,Twist , queue_size=1)
sub =rospy.Subscriber('/scan',LaserScan,callback)
rospy.spin()

print(len(scan_robot.ranges))
