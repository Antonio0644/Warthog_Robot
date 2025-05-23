#!/usr/bin/env python
import rospy
import actionlib
from action_quiz.msg import DroneControlAction, DroneControlFeedback, DroneControlResult
from std_msgs.msg import Empty
class DroneControlServer(object):
   def __init__(self):
       self._as = actionlib.SimpleActionServer('drone_control', DroneControlAction, execute_cb=self.execute_cb, auto_start=False)
       self._as.start()
       self.pub_takeoff = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=1)
       self.pub_land = rospy.Publisher('/ardrone/land', Empty, queue_size=1)
   def execute_cb(self, goal):
       feedback = DroneControlFeedback()
       result = DroneControlResult()
       if goal.command == 'TAKEOFF':
           self.pub_takeoff.publish(Empty())
           while not self._as.is_preempt_requested():
               feedback.status = 'Taking off'
               self._as.publish_feedback(feedback)
               rospy.sleep(1)
           new_goal = self._as.accept_new_goal()
           if new_goal.command == 'LAND':
               self.pub_land.publish(Empty())
               for _ in range(3):
                   feedback.status = 'Landing'
                   self._as.publish_feedback(feedback)
                   rospy.sleep(1)
               self._as.set_succeeded(result)
       elif goal.command == 'LAND':
           self.pub_land.publish(Empty())
           for _ in range(3):
               feedback.status = 'Landing'
               self._as.publish_feedback(feedback)
               rospy.sleep(1)
           self._as.set_succeeded(result)
if __name__ == '__main__':
   rospy.init_node('drone_control_server')
   DroneControlServer()
   rospy.spin()
