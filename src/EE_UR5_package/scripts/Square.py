#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

def square_trajectory():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('moveit_square_trajectory', anonymous=True)

    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "manipulator"  # You may need to change this to match your group name
    move_group = moveit_commander.MoveGroupCommander(group_name)

    current_pose = move_group.get_current_pose().pose
    print("Current Pose:")
    print("Position: ", current_pose.position)
    print("Orientation: ", current_pose.orientation)
    # Define the waypoints of the square trajectory
    waypoints = []


    pose_target = geometry_msgs.msg.Pose()

    pose_target.orientation.x = 8.79826380003957e-05
    pose_target.orientation.y = 0.9997565979554529
    pose_target.orientation.z = 0.022061466060195056
    pose_target.orientation.w = 0.00016976121192795304

#     # Setting initial position
    pose_target.position.x = 0.3
    pose_target.position.y = 0.0
    pose_target.position.z = 0.0

    waypoints.append(copy.deepcopy(pose_target))

     # Define the four corners of the square
    corners = [copy.deepcopy(pose_target) for _ in range(4)]

    # Update the position of the corners
    # Replace these with appropriate values for your specific setup
    corners[0].position.x += 0.2
    corners[1].position.x += 0.2
    corners[1].position.y += 0.2
    corners[2].position.y += 0.2

    # Add the corners to the waypoints
    for corner in corners:
        waypoints.append(corner)

    # We want the EE to follow the trajectory exactly
    move_group.set_pose_target(waypoints[-1])  # Set the pose target to the last waypoint
    (plan, fraction) = move_group.compute_cartesian_path(
        waypoints,  # waypoints to follow
        0.01,  # eef_step: set to a small non-zero value (meters)
        0.0,  # jump_threshold: disable "jump" prevention
    )

    # Execute the plan
    move_group.execute(plan)


    moveit_commander.roscpp_shutdown()

if __name__ == "__main__":
    try:
        square_trajectory()
        
    except rospy.ROSInterruptException:
        pass
