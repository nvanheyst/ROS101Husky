#!/usr/bin/env python

import rospy
import time
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


PI = math.pi
x_pos = 0
yaw_pos = 0

def callback(msg):
    global x_pos
    global yaw_pos
    x_pos = msg.pose.pose.position.x
    yaw_pos = msg.pose.pose.orientation.z


if __name__ == '__main__':
    
    rospy.init_node('odometry_feedback_test', anonymous=True)
    velocity_publisher = rospy.Publisher('husky_velocity_controller/cmd_vel', Twist, queue_size=10)  
    rospy.Subscriber("husky_velocity_controller/odom", Odometry, callback)
    vel_msg = Twist()
    rate = rospy.Rate(10)
    

    while not rospy.is_shutdown():
        distance = 2
   	speed = 0.25
    	initial_pos=x_pos
        
        rospy.loginfo(x_pos)
        rospy.loginfo(initial_pos+distance)

    	vel_msg.linear.x = speed
    	vel_msg.angular.z = 0
    	vel_msg.linear.y = 0
    	vel_msg.linear.z = 0
    	vel_msg.angular.x = 0
    	vel_msg.angular.y = 0
	
    

   	while (x_pos < (initial_pos+distance)):

            velocity_publisher.publish(vel_msg)
	                    
    	vel_msg.linear.x = 0.0
    	velocity_publisher.publish(vel_msg)
        actual_distance=x_pos-initial_pos
    	rospy.loginfo("Tried to move "+str(distance)+"m backward, actually moved "+str(actual_distance)+"m")
    	time.sleep(2)

        angle = -PI/2
        angular_speed =  PI/4
        initial_angle = yaw_pos
       

        rospy.loginfo(yaw_pos)
        rospy.loginfo(initial_angle+angle)

	vel_msg.linear.x = 0
    	vel_msg.angular.z = angular_speed
    	vel_msg.linear.y = 0
    	vel_msg.linear.z = 0
    	vel_msg.angular.x = 0
    	vel_msg.angular.y = 0

        while (yaw_pos < (initial_angle+angle)):

            velocity_publisher.publish(vel_msg)
	                    
    	vel_msg.angular.z = 0.0
    	velocity_publisher.publish(vel_msg)
        actual_angle=yaw_pos-initial_angle
    	rospy.loginfo("Tried to rotate "+str(angle)+"rad, actually moved "+str(actual_angle)+"rad")
    	time.sleep(2)

        rate.sleep()
        

    rospy.loginfo("Mission complete")
    rospy.signal_shutdown("Mission Complete")
