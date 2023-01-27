#!/usr/bin/env python3

# importing some libraries
from std_srvs.srv import Empty,EmptyResponse
import math
from rt_assignment.msg import custom_msg
import rospy

times =0
tmp_velocity =0
des_distance=0
avg_velcity =0
#This function is called when a message is received on the topic "/reaching_goal/result" and 
#it is a callback function that calculates some information based on the data in the message

def cl_bck_sub(value):

    global times
    global tmp_velocity
    global avg_velcity
    global des_distance
    obj_position_x = rospy.get_param("/des_pos_x")
    obj_position_y = rospy.get_param("/des_pos_y")

    position_x = value.x
    position_y = value.y

    velocity_x = value.vel_x
    velocity_y = value.vel_y


    velocity = math.sqrt((velocity_x**2)+(velocity_y**2))



    if times<7:

        tmp_velocity=tmp_velocity + velocity
        times +=1

    elif times==7:

        times=0
        tmp_velocity /= 7
        avg_velcity=tmp_velocity
        tmp_velocity=0

    des_distance= math.sqrt(((obj_position_x - position_x)**2)+((obj_position_y - position_y)**2))


#the main function of the ROS node that starts by initializing the node 
#Enters an infinite loop that will run until the ROS node is shutdown
#print out the values every 1/publisher_speed seconds
if __name__ == "__main__":

    rospy.logwarn("fourthnode started")

    rospy.init_node('fourthnode')
    
    rate = rospy.Rate(rospy.get_param("/publisher_speed"))

    rospy.Subscriber("chatter", custom_msg, cl_bck_sub)

    while not rospy.is_shutdown():

        print(f"distance to the objective:  {des_distance : .5f}")
        print(f'average velocity:           {avg_velcity: .5f}')
        print("****************************************************")
        rate.sleep()

