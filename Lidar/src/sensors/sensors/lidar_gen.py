#lidar sensor msgs: https://docs.ros.org/en/diamondback/api/sensor_msgs/html/__LaserScan_8py_source.html
#Lidar msg syntax: https://wiki.ros.org/laser_pipeline/Tutorials/IntroductionToWorkingWithLaserScannerData
from sensor_msgs.msg import LaserScan
import random 


def generate():
    msg=LaserScan()
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
