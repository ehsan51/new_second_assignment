#! /usr/bin/env python3
# importing some libraries
import rospy
from nav_msgs.msg import Odometry
from rt_assignment.msg import custom_msg

#this function is called when the node receives a message from the topic of /odom
# it publishes the message of the topic of /odom as a custom message
def cl_bck(data):
# Initialize a publisher for the "chatter" topic with a custom message type "custom_msg"
    pub = rospy.Publisher('chatter', custom_msg, queue_size=50)
    # Create an instance of the custom message
    message=custom_msg()
    # Extract the position and linear velocity data from the received odometry message and assign it to the custom message
    message.x = data.pose.pose.position.x
    message.vel_x = data.twist.twist.linear.x
    message.y = data.pose.pose.position.y
    message.vel_y = data.twist.twist.linear.y
    # Print the custom message
    print(message)
    # Publish the custom message
    pub.publish(message)
   
# Initialize a new ROS node named 'secondnode' and create a Subscriber to listen to the "/odom" topic
# The Odometry message type is passed to the callback function which will
# be called everytime a new message is received on the topic    
def Initialize():
    
    rospy.init_node('secondnode')
    rospy.Subscriber("/odom", Odometry, cl_bck)

  
    rospy.spin()

# main
if __name__ == '__main__':
    Initialize()
    
