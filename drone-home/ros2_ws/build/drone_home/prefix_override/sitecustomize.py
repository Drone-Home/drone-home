import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/workspaces/drone_home-dev/drone-home/ros2_ws/install/drone_home'
