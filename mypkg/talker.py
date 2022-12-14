import rclpy
from rclpy.node import Node
from std_msg.msg import Int16

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0

def cb():
    global n
    msg = Person()
    msg.name = "Int16"
    msg.age = n
    pub.publish(msg)
    n += 1

node.create_timer(0.5, cb)
rclpy.spin(node)

