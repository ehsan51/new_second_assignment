# new_second_assignment

ROS

Controlling the robot in ROS

You can run the project and control the robot by following this structure:
  
Download the package from the address :   
https://github.com/ehsan51/new_second_assignment.git

Create the new package
	  catkin_create_pkg rt_assignment rospy      (in the src folder)

Update the package list by:
	  rospack profile

Clone the ' assignment_2_2022' from this address: 
https://github.com/CarmineD8/assignment_2_2022.git

In this project there are four nodes and you can run each node separately to understand the process:

First, write this command in the terminal : 
    roslaunch assignment_2_2022 assignment1.launch

then run each node separately by writing this : 
    rosrun rt-assignment [node_name.py]

The firstnode asks the user to choose the desired operation, setting the objective, canceling the process or exiting. 

The second one publishes the velocity and position of the robot 

the third one represents how many the rorbot gotten to objective or the process being cancelled by the following command

  	rosservice call /reach_cancel_ints

The last node shows the distance beween the current position and the objective,as well as the average velocity of the robot.

Note: to run this node, you should first set a value to the publisher_speed parameter by:
  	rosparam set publisher_speed [desired_value]

Otherwise, you can launch the whole of the procces by the following command:
	  roslaunch rt_assignment esi_launch.launch

The flowchart of the first and second node of the process has been represented below:![My First Board(4)](https://user-images.githubusercontent.com/52650110/214985398-9eb3dff9-b827-4f42-8332-c419052329cd.jpg)










