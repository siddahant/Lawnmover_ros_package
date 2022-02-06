# Lawnmower_ros_package

This package contains a node that carries out a simulation of the Lawnmower pattern movement of the turtle (from the package turtlesim).

The turtle asks the user for the start point, length, and width of the lawnmower pattern.
The turtle uses a feedback control system to correct its position and orientation throughout the trajectory. At first, the turtle turns until it faces directly at the goal location and then moves toward the goal position, The loop of rotation and moves runs until the pattern is finished. 

The package contains a custom velocity message containing only the planar forward and planar rotational velocities of the turtle.

1. **Create a new workspace and clone the demonstration code.**
```
# Create a new workspace
 mkdir -p ~lawnmover_ws/src

# clone the demonstration code
cd ~lawnmover_ws/src
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
# Results 
**User inputs**

![Screenshot 2022-02-06 161902](https://user-images.githubusercontent.com/44742647/152705970-220e0305-42fd-4c5b-8461-d4de1880bf99.png)


**Completed mission**

![Screenshot 2022-02-06 162103](https://user-images.githubusercontent.com/44742647/152705979-cbaf1f2b-06a5-4f5a-a10f-587540fdcd42.png)


**User input but this time 'A' is grater than the canvas length**

![Screenshot 2022-02-06 162215](https://user-images.githubusercontent.com/44742647/152706004-c666a473-d694-4c7d-8573-6b747e2b9cb4.png)


**Path manipulation**

![Screenshot 2022-02-06 162300](https://user-images.githubusercontent.com/44742647/152706043-a70cb7aa-d43c-44e1-91d1-a668ad033a9a.png)

