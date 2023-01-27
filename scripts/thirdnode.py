#!/usr/bin/env python3
# importing some libraries

from std_srvs.srv import Empty,EmptyResponse
import assignment_2_2022.msg

import rospy

reaching_times =0
cancelation_times = 0

#this function is called if the service is called
#it prints the current values of "cancelation_times" and "reaching_times" and sends an empty response.

def cl_bck(req):
    global cancelation_times,reaching_times
    print(f"Canceled Objective's times {cancelation_times} , Reached Objective's times: {reaching_times}")
    return EmptyResponse()

def cl_bck_sub(data):


    if data.status.status == 2:

        global cancelation_times
        cancelation_times += 1
    
    elif data.status.status == 3:

        global reaching_times
        reaching_times += 1


#This code is the main function of the ROS node
#It specifies that when a message is received, the function cl_bck_sub should be called to handle the message
#it calls rospy.spin() which keeps the node running and listening for new messages or service calls
if __name__ == "__main__":

    rospy.logwarn("You have started the Code")

    rospy.init_node('reach_cancel_node')

    rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, cl_bck_sub)

    rospy.Service('reach_cancel_ints', Empty, cl_bck)

    rospy.spin()
