import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from lidar_gen import generate
#sensor_msgs/msg/LaserScan 


class LidarPub(Node):

    def __init__(self):
        super().__init__('pub_Lidar')
        self.publisher_ = self.create_publisher(LaserScan, '/scan', 10)
        timer_period = 0.1  # seconds (10HZ)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):

        msg = generate()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Lidar Data: "%s"' % msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    publisher = LidarPub()

    rclpy.spin(publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()