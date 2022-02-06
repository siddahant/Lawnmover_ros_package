# Lawnmower_ros_package

This package contain node that carry out a simulation of Lawnmower pattern movmenet of turtle (from the package turtlesim).

The turtle ask user for start point, length and weidth for lawnmover pattern.
The turtle uses feedback control system to correct its position and orentation throughout the trajectory. At first, the turtle turns until it faces directly at the goal location and then moves toward the goal position, The loop of rotation and moves runs until the pattern finished. 

The package contains a custom velocity message containing only the planar forward and planar rotational velocities of the turtle.

1. **Create a new workspace and clone the demonstration code.**
```
# Create a new workspace
 mkdir -p ~lawnmover_ws/src

# clone the demonstration code
cd lawnmover_ws/src
catkin_init_workspace
git clone https://github.com/siddahant/Lawnmover_ros_package.git

# return to lawnmover_ws root
cd ../ 
```
2. **Build the workspace and activate it.**
```
catkin_make
source devel/setup.bash
```
3. **Launch the node.**
```
roslaunch Lawnmover_ros_package lawnmower.launch
```
