#! /usr/bin/env python3
# importing some libraries
import rospy
from geometry_msgs.msg import PoseStamped
import actionlib
import actionlib.msg
import assignment_2_2022.msg
from std_srvs.srv import *
import actionlib
import assignment_2_2022.msg
import os            

# This function allows the user to enter the position of the robot's target and sends it to the action server.
def target_client():
    # the user can assign the position of the target
    
    a = input("Enter position's X:")
    b = input("Enter position's Y:")
    a = int(a)
    b = int(b)
    # printing the position with X and Y elements
    print(f'You have entered position : X:{a} Y:{b}')

    global client_A
    # defining a target and sends it to the action server
    client_A = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction )

    # Waiting until the action server is started 
    print("\nPlease Wait until connecting to ACTION SERVER")
    client_A.wait_for_server()

 # assigning the objective then send it to the action service
    Objective = PoseStamped()

    Objective.pose.position.x = a
    Objective.pose.position.y = b

    Objective = assignment_2_2022.msg.PlanningGoal(Objective)

    
    # Sends the goal to the action server.
    client_A.send_goal(Objective)
    print("\n Objective sent to the Main Sever")
    rospy.sleep(2)
 
    interface_space()

#this function sends  a cancel command to action server
def cancel_target():

    client_A.cancel_goal()
    print(f'You canceled the Program')
    # Waiting for the cancelation print
    rospy.sleep(2)
    interface_space()

# this function builds the controlling panel
# display a welcome message and a list of options the user can select from
# if the input number differs from 1,2,3 it will show the wrong error
def interface_space():
    os.system('clear')
    print("******************** Welcome ***************\n")    
    print("****** The Robot is under your Control  ****\n")
    print("Which Operation Do You Need ?\n")
    print("1:Position\n")
    print("2:Cancel\n")
    print("3:Exit\n")   
    a = input(" Enter 1 , 2 , 3 \n")
    if(a == "1"):
        target_client()
    elif (a=="2") :
            cancel_target()
    
    elif (a=="3") :
            exit()
    else :
        print(" You entered wrong number *** PLEASE WAIT***")   
    
        rospy.sleep(2)
        interface_space()
    
#checks if the script is being run as the main program or if it is being imported as a module into another script
if __name__ == '__main__':
    
    rospy.init_node('client_py')
        
    interface_space()
