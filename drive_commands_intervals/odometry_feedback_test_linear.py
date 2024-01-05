#!/usr/bin/env python

import rospy
import time
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


#PI = math.pi
x_pos = 0
y_pos = 0
#yaw_pos = 0

def callback(msg):
    global x_pos
    global y_pos
    global yaw_pos
    x_pos = msg.pose.pose.position.x
    y_pos = msg.pose.pose.position.x
    #yaw_pos = msg.pose.pose.orientation.z


if __name__ == '__main__':
    
    rospy.init_node('odometry_feedback_test', anonymous=True)
    velocity_publisher = rospy.Publisher('husky_velocity_controller/cmd_vel', Twist, queue_size=10)  
    rospy.Subscriber("husky_velocity_controller/odom", Odometry, callback)
    vel_msg = Twist()
    rate = rospy.Rate(10)
    

    while not rospy.is_shutdown():
        distance = 2
   	speed = 0.25
    	initial_distance=math.sqrt(x_pos**2+y_pos**2)
        
        rospy.loginfo(initial_distance)
        rospy.loginfo(initial_distance+distance)

    	vel_msg.linear.x = speed
    	vel_msg.angular.z = 0
    	vel_msg.linear.y = 0
    	vel_msg.linear.z = 0
    	vel_msg.angular.x = 0
    	vel_msg.angular.y = 0
	
    

   	while (math.sqrt(x_pos**2+y_pos**2) < (initial_distance+distance)):

            velocity_publisher.publish(vel_msg)
	                    
    	vel_msg.linear.x = 0.0
    	velocity_publisher.publish(vel_msg)
        actual_distance=math.sqrt(x_pos**2+y_pos**2)-initial_distance
    	rospy.loginfo("Tried to move "+str(distance)+"m backward, actually moved "+str(actual_distance)+"m")
    	time.sleep(2)

        
        rate.sleep()
        

    rospy.loginfo("Mission complete")
    rospy.signal_shutdown("Mission Complete")
