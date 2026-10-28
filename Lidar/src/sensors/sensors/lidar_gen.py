#lidar sensor msgs: https://docs.ros.org/en/diamondback/api/sensor_msgs/html/__LaserScan_8py_source.html
#Lidar msg syntax: https://docs.ros.org/en/jade/api/sensor_msgs/html/msg/LaserScan.html
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Header
import rospy
import random 


def generate(frame_id="laser", num_readings=360):
    msg=LaserScan()
    LaserScan.header = Header()
    LaserScan.header.stamp = rospy.Time.now()  # Userclpy.time.Time.to_msg() for ROS 2
    LaserScan.header.frame_id = frame_id
    #LaserScan.header.
    LaserScan.angle_min = -90 
    LaserScan.angle_max = 90 
    LaserScan.angle_increment= 1
    LaserScan.time_increment=20 #(sec)
    LaserScan.range_min= 0.1 #(m)
    LaserScan.range_max= 7 #(m)
    LaserScan.ranges
    #for packing read distances
    #ranges=[]
    
    for i in 180:
        LaserScan.ranges[i] = random.randrange(0.1 , 7)

    for i in 180:
        LaserScan.intensities[i] = random.randrange(0.0 , 100.0)