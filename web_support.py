# Links flask web and ROS nodes

# Collects data from multiple nodes and sends to website with ROS_TO_WEB topic
# Takes in data from website with WEB_TO_ROS topic
# Created by flask app.py
import rclpy
import threading
from time import sleep
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix, NavSatStatus


class WebSupport(Node):
    def __init__(self):
        super().__init__('web_support')
        self.gps_subscriber = self.create_subscription(NavSatFix, 'drone_home1/gps/fix', self.gps_callback, 10)
        
        self.current_position = NavSatFix()
        self.drone_position = NavSatFix()

    def gps_callback(self, msg):
        # Update the current GPS location from NavSatFix message
        self.current_position = msg
        print(self.current_position)
        
    def publish_cv_box(self, box):
        x1, y1, x2, y2 = box.xyxy[0]  # Bounding box corners
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        width = x2 - x1
        height = y2 - y1

        
        # Publish            
        # print(f"Center: ({center_x:.2f}, {center_y:.2f}), Size: ({width:.2f}, {height:.2f})")

    

def main(args=None):
    rclpy.init()
    web_support = WebSupport()
    
    def ros_spin():
        rclpy.spin(web_support) 

    threading.Thread(target=ros_spin, daemon=True).start()

    sleep(30)

if __name__ == '__main__':
    main()