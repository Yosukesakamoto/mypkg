import rclpy
from rclpy.node import Node
from person_msg.msg import Person

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "Person", 10)
n = 0

def cb():
    global n
    msg = Person()
    msg.name = "坂本耀介"
    msg.age = n
    pub.publish(msg)
    n += 1

node.create_timer(0.5, cb)
rclpy.spin(node)

