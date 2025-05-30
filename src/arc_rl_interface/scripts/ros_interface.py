#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class RosCarInterface:
    def __init__(self):
        rospy.init_node('arc_rl_interface', anonymous=True)
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.position = (0.0, 0.0)

    def odom_callback(self, msg):
        pos = msg.pose.pose.position
        self.position = (pos.x, pos.y)

    def send_command(self, action):
        twist = Twist()
        if action == 1: # Accelerate
            twist.linear.x = 0.3
        elif action == 2: # Brake
            twist.linear.x = -0.3
        elif action == 3: # Left
            twist.angular.z = 0.5
        elif action == 4: # Right
            twist.angular.z = -0.5
        # 0: Hold -> no movement
        self.cmd_pub.publish(twist)

    def get_position(self):
        return self.position

if __name__ == "__main__":
    interface = RosCarInterface()
    rospy.spin()

