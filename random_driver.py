#!/usr/bin/env python
import rospy
import random
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node('random_husky_commands', anonymous=True)
    velocity_publisher = rospy.Publisher('husky_velocity_controller/cmd_vel', Twist, queue_size=10)  

    vel_msg = Twist()

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        vel_msg.linear.x = random.randrange(-2,2)
        vel_msg.angular.z = random.randrange(-3,3)
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        velocity_publisher.publish(vel_msg)
        rospy.loginfo(vel_msg)
        
        rate.sleep()

    rospy.loginfo("Goodbye :(")
