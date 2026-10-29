#lidar sensor msgs: https://docs.ros.org/en/diamondback/api/sensor_msgs/html/__LaserScan_8py_source.html
#Lidar msg syntax: https://docs.ros.org/en/jade/api/sensor_msgs/html/msg/LaserScan.html
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Header
import random 
import math 


def generate(timestamp_msg):
    msg=LaserScan()
    msg.header = Header()
    msg.header.stamp = timestamp_msg  # Userclpy.time.Time.to_msg() for ROS 2
    msg.header.frame_id = "laser"
    #LaserScan.header.
    msg.angle_min = math.radians(-180)
    msg.angle_max = math.radians(180)
    msg.angle_increment = 0.017
    msg.time_increment = 0.0  
    msg.scan_time = 0.01      
    msg.range_min = 0.1
    msg.range_max = 10.0
    #for packing read distances
    ranges=[]
    
    for i in range(180):
        if 90 <= i <= 110:
            ranges.append(1.0)
        elif 250 <= i <= 270:
            ranges.append(2.0)
        else:
            ranges.append(5.0)
            
    msg.ranges = ranges
    
    inten=[]
    for i in range(180):
        inten.append(random.uniform(0.0 , 100.0) )

    msg.intensities=inten
    return msg