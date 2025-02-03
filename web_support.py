# Links flask web and ROS nodes

# Collects data from multiple nodes and sends to website with ROS_TO_WEB topic
# Takes in data from website with WEB_TO_ROS topic
# Created by flask app.py
import rclpy
import threading
import math
from time import sleep
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix, NavSatStatus
from ackermann_msgs.msg import AckermannDriveStamped


class WebSupport(Node):
    def __init__(self):
        super().__init__('web_support')
        # For webdata
        self.gps_subscriber = self.create_subscription(NavSatFix, 'drone_home1/gps/fix', self.gps_callback, 10)

        # Publisher for web steering
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'vehicle/web_controller_drive', 10)
        
        self.current_position = NavSatFix()
        self.drone_position = NavSatFix()

        print("Web support started")

    def gps_callback(self, msg):
        # Update the current GPS location from NavSatFix message
        self.current_position = msg
        #print(self.current_position)
        
    def publish_cv_box(self, box):
        x1, y1, x2, y2 = box.xyxy[0]  # Bounding box corners
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        width = x2 - x1
        height = y2 - y1

        
        # TODO Publish            
        #print(f"Center: ({center_x:.2f}, {center_y:.2f}), Size: ({width:.2f}, {height:.2f})")

    def publish_control(self, steering, speed):
        # Map from web commands to drive commands and publish
        steering_angle = self.map_value(steering, -1, 1, -math.pi/4, math.pi/4)
        drive_speed = self.map_value(speed, -1, 1, -1, 1)

        drive_msg = AckermannDriveStamped()
        drive_msg.drive.steering_angle = -steering_angle
        drive_msg.drive.speed = drive_speed  
        self.publisher_.publish(drive_msg)

    @staticmethod
    def map_value(value, from_min, from_max, to_min, to_max):
        # Map value to new range
        mapped_value = to_min + (value - from_min) * (to_max - to_min) / (from_max - from_min)
        return float(mapped_value)
    
def main(args=None):
    rclpy.init()
    web_support = WebSupport() 
    def ros_spin():
        rclpy.spin(web_support) 
    threading.Thread(target=ros_spin, daemon=True).start()

    sleep(30)

if __name__ == '__main__':
    main()