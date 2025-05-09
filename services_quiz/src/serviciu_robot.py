#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist

from services_quiz.srv import CustomSerMess, CustomSerMessResponse 


def handle_circle(req):

    rospy.loginfo(f"Fac cerc cu raza ")

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    vel_msg = Twist()

    vel_msg.linear.x = req.side   

    vel_msg.angular.z = 1.0       

    rate = rospy.Rate(10)

 

 

    


def circle_service_server():

    rospy.init_node('circle_service_server')

    s = rospy.Service('circle_move', CustomSerMess, handle_circle)

    rospy.loginfo("Service pentru cerc pornit.")

    rospy.spin()

if __name__ == "__main__":

    circle_service_server()
 
response = CustomServMessResponse()
response.success=True
return EmptyResponse()
