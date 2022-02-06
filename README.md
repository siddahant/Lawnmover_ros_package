# Lawnmover_ros_package

This package contain node that carry out a simulateion of Lawnmover pattern movmenet of turtle (from the package turtlesim).

The turtle ask user for start point, length and weidth for lawnmover pattern.
The turtle uses feedback control system to correct its position and orentation throughout the trajectory. At first, the turtle turns until it faces directly at the goal location and then moves toward the goal position, The loop of rotation and moves runs until the pattern finished. 

The package contains a custom velocity message containing only the planar forward and planar rotational velocities of the turtle.

```
# Create a new workspace
 mkdir -p ws/src

# clone the demonstration code
cd ws/src
git clone https://github.com/ctsaitsao/turtlesim-waypoints.git turtlesim-waypoints

# return to ws root
cd ../ 
```

```
catkin_make install
. devel/setup.bash
```

```
roslaunch Lawnmover_ros_package lawnmover.launch
```