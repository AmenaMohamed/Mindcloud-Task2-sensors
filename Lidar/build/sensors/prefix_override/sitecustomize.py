import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/mnt/c/Users/Owner/Amena/engineering/mindcloud/Tasks/Nav-training/Task2-sensors/Task2-sensor/Mindcloud-Task2-sensors/Lidar/install/sensors'
