#!/usr/bin/env python

import rospy
import time
import math
from geometry_msgs.msg import Twist
#from nav_msgs.msg import Odometry

#x_pos = 0
total_pos=0
total_angle=0
PI = math.pi

#def callback(msg):
    #global x_pos
    #x_pos = msg.pose.pose.position.x
    

if __name__ == '__main__':
    
    rospy.init_node('driving_command_interval', anonymous=True)
    velocity_publisher = rospy.Publisher('husky_velocity_controller/cmd_vel', Twist, queue_size=10)  
    #rospy.Subscriber("husky_velocity_controller/odom", Odometry, callback)
    vel_msg = Twist()
    rate = rospy.Rate(10)
    
    rospy.loginfo("Routine Starting")

    while not rospy.is_shutdown():
       
        rospy.loginfo("Waiting for 12am...")
	for x in range(5):
            rospy.loginfo(str(5-x) + " more hours to go..")
	    time.sleep(1)
        rospy.loginfo("It's 12am!! Time to get to work")
        
        while not rospy.is_shutdown():
	    distance = -3
   	    speed = -0.25
            relative_angle = -PI/2
            angular_speed =  -PI/8

	    for i in range(7):
	    	t0 = rospy.Time.now().to_sec()
 	    	current_distance = 0
    	   
 	    	current_angle = 0
            

 	    	vel_msg.linear.x = speed
	    	vel_msg.angular.z = 0
	    	vel_msg.linear.y = 0
	    	vel_msg.linear.z = 0
	    	vel_msg.angular.x = 0
	    	vel_msg.angular.y = 0
		
	    

	   	while (current_distance > distance):

   	            velocity_publisher.publish(vel_msg)
		    t1=rospy.Time.now().to_sec()
    		    current_distance = speed*(t1-t0)
                           
            
	    	#rospy.loginfo(current_distance)
	        vel_msg.linear.x = 0.0
            	velocity_publisher.publish(vel_msg)
                total_pos+=3
            	rospy.loginfo("Moved 3m backward, "+str(total_pos)+"m total")
            	rospy.loginfo("Waiting 10 minutes")
            	time.sleep(5)

    	    	
	    	

            	for i in range(4):
                    t0 = rospy.Time.now().to_sec()
   		    vel_msg.angular.z = angular_speed
		    

		    while (current_angle > relative_angle):
           
	   	    	velocity_publisher.publish(vel_msg)
		    	t1=rospy.Time.now().to_sec()
	    	    	current_angle = angular_speed*(t1-t0)
		        

		    #rospy.loginfo(current_angle)
		    vel_msg.angular.z = 0
		    
	   	    velocity_publisher.publish(vel_msg)
		    total_angle+=90
            	    
		    rospy.loginfo("Moved 90 degrees clockwise, "+str(total_angle)+" degrees total")
		    rospy.loginfo("Waiting 10 minutes")
		    time.sleep(5)
		    current_angle = 0

                total_angle=0
     		    

            
	    rospy.loginfo("Mission completed before 7am. Time is 6:40am")
	    rospy.signal_shutdown("Mission Complete")

    
