#!/usr/bin/env python

import rospy
import time
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


PI = math.pi
#x_pos = 0
yaw_pos = 0

def quaternion_to_euler_angle(w, x, y, z):
    ysqr = y * y

    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + ysqr)
    X = math.degrees(math.atan2(t0, t1))

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    Y = math.degrees(math.asin(t2))

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (ysqr + z * z)
    Z = math.degrees(math.atan2(t3, t4))

    return Z

def callback(msg):
    #global x_pos
    #global y_pos
    global yaw_pos
    #x_pos = msg.pose.pose.position.x
    #y_pos = msg.pose.pose.position.x
    yaw = quaternion_to_euler_angle(msg.pose.pose.orientation.w,msg.pose.pose.orientation.x, msg.pose.pose.orientation.y,msg.pose.pose.orientation.z)
    
    if yaw < 0:
        yaw_pos=360+yaw
    else: 
        yaw_pos=yaw

    #rospy.loginfo(yaw_pos)

if __name__ == '__main__':
    
    rospy.init_node('test', anonymous=True)
    velocity_publisher = rospy.Publisher('husky_velocity_controller/cmd_vel', Twist, queue_size=10) 
    rospy.Subscriber("husky_velocity_controller/odom", Odometry, callback)
    vel_msg = Twist()
    rate = rospy.Rate(10)
    rospy.loginfo("Node started")

    while not rospy.is_shutdown():
        rospy.loginfo("Starting 90 degree rotation")
        angle = 90
    	angular_speed =  PI/4
    	initial_angle = yaw_pos

    	vel_msg.linear.x = 0
    	vel_msg.angular.z = angular_speed
    	vel_msg.linear.y = 0
    	vel_msg.linear.z = 0
    	vel_msg.angular.x = 0
    	vel_msg.angular.y = 0

        if (initial_angle+angle)<360:
	    goal=(initial_angle+angle)
	    rospy.loginfo("Goal is " + str(goal))
	    while (yaw_pos < (goal)):

                velocity_publisher.publish(vel_msg)
	    
	else: 
	    goal=(initial_angle+angle)-360 
	    rospy.loginfo("Goal is " + str(goal))
            while (yaw_pos > 90):

                velocity_publisher.publish(vel_msg)

  	    while (yaw_pos < (goal)):

                velocity_publisher.publish(vel_msg)

    	

    	vel_msg.angular.z = 0.0
    	velocity_publisher.publish(vel_msg)
        rospy.loginfo("Tried to turn 90 degrees, actually turned" + str(yaw_pos-initial_angle))
        rospy.loginfo("Waiting")
        time.sleep(2)

    	rate.sleep()
