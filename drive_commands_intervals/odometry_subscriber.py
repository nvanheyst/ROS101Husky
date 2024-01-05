#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry




def callback(msg):
    rospy.loginfo(msg)


if __name__ == '__main__':
    
    rospy.init_node('odometry_subscriber', anonymous=True)
    rospy.Subscriber("husky_velocity_controller/odom", Odometry, callback)
    rospy.spin()
