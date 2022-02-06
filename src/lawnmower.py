#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from math import pow, atan2, sqrt
from turtlesim.msg import Pose


class lawnmover:
    def __init__(self):
        rospy.init_node('lawnmover_controller',anonymous=True)
        self.velocity_publisher= rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose, self.update_pose)                                   
        self.pose=Pose()
        self.rate=rospy.Rate(10)
        
    def update_pose(self,data):
        self.pose=data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
        self.pose.theta=round(self.pose.theta,4)

    def distance(self,goal_pose):
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def distance_check(self,goal_pose):
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))


    def steering_angle(self,goal_pose):
        angle= atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)
        return  angle

    def steering_PD_contoller(self,goal_pose):
        return 1*(self.steering_angle(goal_pose)-self.pose.theta)


    def velocity_PD_contoller(self,goal_pose):
        if  self.distance(goal_pose)<1:
            return 1*self.distance(goal_pose)
        else:
            return 1

    def rotate(self,X,Y):
        goal_pose=Pose()
        goal_pose.x=  X
        goal_pose.y = Y
        angle_tolerance = 0.002
        vel_msg = Twist() 
        while abs(self.steering_angle(goal_pose)-(self.pose.theta)) >= angle_tolerance:
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.steering_PD_contoller(goal_pose)
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
   
    def move(self,X,Y):
        goal_pose=Pose()
        goal_pose.x=  X
        goal_pose.y = Y
        distance_tolerance = 0.02
        vel_msg = Twist()
        while self.distance(goal_pose) >= distance_tolerance:
            if (self.pose.x < 0 or self.pose.x > 11-0.08 or self.pose.y < 0 or self.pose.y > 11-0.08):
                print("Oh no! I am hitting the wall! I am manipulating my path")
                
            vel_msg.linear.x = self.velocity_PD_contoller(goal_pose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.steering_PD_contoller(goal_pose)
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
       
                                                      
if __name__ == '__main__':
    try:
        x = lawnmover()
        #move stat point
        X=float(input("Start position X: "))
        Y=float(input("Start position Y: "))
        while 0>X or X>11 or  0>Y or Y>11:
            print("oops please make sure your start point should be in the boundary range(0 to 11)")
            X=float(input("Start position X: "))
            Y=float(input("Start position Y: "))
        A=float(input("length A: "))
        B=float(input("width B: "))
        loops= 1
        print("mission started.")
        x_max=11
        x_min=0
        y_max=11
        y_min=0
        x.rotate(X,Y)
        x.move(X,Y)
        lengthA=X+A
        
        if lengthA>x_max:
            A=A-(lengthA-x_max)
            lengthA=X+A
            # print("oh no! I  feel I will hit the wall, but do not worry i can make some adjustments")
        lengthB=Y
        count=0
        while count<loops:
           
            if lengthB>y_max:
                lengthB=y_max
                # print("oh no! I  feel I will hit the wall, but do not worry i can make some adjustments")

            x.rotate(lengthA,lengthB)
            x.move(lengthA,lengthB)
            

            lengthB=lengthB+B
            if lengthB>y_max:
                lengthB=y_max
                # print("oh no! I  feel I will hit the wall, but do not worry i can make some adjustments")

            x.rotate(lengthA,lengthB)
            x.move(lengthA,lengthB)

            x.rotate(lengthA-A,lengthB)
            x.move(lengthA-A,lengthB)
            
            lengthB=lengthB+B

            if lengthB>y_max:
                lengthB=y_max
                # print("oh no! I  feel I will hit the wall, but do not worry i can make some adjustments")

            x.rotate(lengthA-A,lengthB)
            x.move(lengthA-A,lengthB)
            count=count+1

        if lengthB<y_max or loops==1:
            x.rotate(lengthA,lengthB)
            x.move(lengthA,lengthB)
        else:
            pass
            print("I was not found a new way to go, so now i am going back to home.")
        x.rotate(5.5,5.5)
        x.move(5.5,5.5)
        x.rotate(10,5.5)
        print("Ahh finally! reached home.")

    except rospy.ROSInterruptException:
        pass


