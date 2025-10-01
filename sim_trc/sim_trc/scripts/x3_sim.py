#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist



class X3_Sim(Node):
    def __init__(self):
        super().__init__("X3_Sim")

        self.cmd_vel_sub = self.create_subscription(Twist,"cmd_vel", self.cmd_vel_callback, 10)
        self.x3_cmd_vel_pub = self.create_publisher(Twist, "/x3_sim/cmd_vel", 10)

    def cmd_vel_callback(self, cmd_msg):
        x3_cmd = Twist()
        x3_cmd.linear.x = cmd_msg.linear.x
        x3_cmd.linear.y = cmd_msg.linear.y
        x3_cmd.angular.z = cmd_msg.angular.z * 1000

        self.x3_cmd_vel_pub.publish(x3_cmd)






def main(args=None):
    rclpy.init(args=args)
    node = X3_Sim()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()

if __name__=="__main__":
    main()
