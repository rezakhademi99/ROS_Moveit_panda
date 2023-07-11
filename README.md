# MoveIt Square Trajectory Project

## Overview
This repository demonstrates the use of the MoveIt library to control manipulators (Panda and UR5) in a ROS environment. It includes demonstrations of the manipulators following a square trajectory.

## Setup

### Prerequisites

- ROS (Melodic, Noetic, etc.) installed
- Basic knowledge of the ROS environment
- MoveIt installed on your ROS environment

### Installation
Firstly, we will create a workspace dedicated to MoveIt and clone this repository into the source directory:

```
mkdir -p ~/ws_moveit/src
cd ~/ws_moveit/src
git clone https://github.com/rezakhademi99/ROS_Moveit_panda.git
```
Next, we need to install any missing dependencies using rosdep:

```
cd ..
rosdep install --from-paths src --ignore-src -r -y
```

And finally, we build the workspace using catkin:

```
catkin_make
source devel/setup.bash
```


## Demonstration Steps

### MoveIt and ability to move panda manipulator using Rviz plugin

To ensure that MoveIt is installed correctly and that you're able to manipulate the Panda robot using the RViz plugin, you can use the following command:
```
roslaunch panda_moveit_config demo.launch
```
After running the above command, a RViz window will open where you can see the Panda robot. You can interact with the robot using the interactive markers. Try moving the robot around to different poses to ensure everything is working correctly.

![](https://github.com/rezakhademi99/ROS_Moveit_panda/blob/main/panda.gif)

### Movement on a square trajectory using the Panda

To demonstrate the Panda manipulator moving along a square trajectory, we provide a Python script. This script uses the MoveIt Python interface to generate a square trajectory and command the Panda manipulator to follow it. Run the following command in another terminal to start the demonstration:
```
rosrun EE_panda_package Square.py
```
You should see the Panda manipulator in the RViz window following a square trajectory.

![](https://github.com/rezakhademi99/ROS_Moveit_panda/blob/main/square_panda.gif)

### Movement on a square trajectory using UR5

Similarly, we also provide a demonstration of the UR5 manipulator following a square trajectory. This demonstration also uses the MoveIt Python interface to generate the square trajectory. First, we need to load our UR5 in the RViz:
```
roslaunch ur5_moveit_config demo.launch 
```
After running the above command, a RViz window will open where you can see the UR5 robot. You can interact with the robot using the interactive markers. Try moving the robot around to different poses to ensure everything is working correctly.

![](https://github.com/rezakhademi99/ROS_Moveit_panda/blob/main/UR5.gif)

You can start this demonstration using the following command:
```
rosrun EE_UR5_package Square.py
```
Again, you should see the UR5 manipulator in the RViz window following a square trajectory.

![](https://github.com/rezakhademi99/ROS_Moveit_panda/blob/main/Square_UR5.gif)
