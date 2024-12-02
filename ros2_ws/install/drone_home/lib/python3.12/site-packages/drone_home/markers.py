import rclpy
import math
from rclpy.node import Node
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion, PoseStamped
from sensor_msgs.msg import NavSatFix, NavSatStatus

from .geo_tools import GeoTools

# Produces a KML file that a python web server will host for visualization
class GPSVisualizationNode(Node):
    def __init__(self):
        super().__init__('gps_visualization_node')

        self.pose_subscriber = self.create_subscription(PoseStamped, 'vehicle/pose', self.pose_callback, 10)
        self.gps_subscriber = self.create_subscription(NavSatFix, 'gps/fix', self.gps_callback, 10)

        # timer for publishing markers
        self.timer = self.create_timer(0.25, self.publish_marker)

        # current quaternion (updated from subscriber)
        self.current_quaternion = Quaternion(x=0.0, y=0.0, z=0.0, w=0.0)
        self.current_position = NavSatFix(latitude = -1.0, longitude = -1.0)

        self.waypoints = [
        (28.069556, -82.724286),
        #(29.6404980, -82.3605938),
        #(29.6404013, -82.3605922),
        #(29.6404035, -82.3604530)
    ]
    
    def pose_callback(self, msg):
        # Update the current quaternion from the PoseStamped message
        self.current_quaternion = msg.pose.orientation
    
    def gps_callback(self, msg):
        # Update the current GPS location from NavSatFix message
        self.current_position = msg

    def publish_marker(self):
        self.get_logger().info(f"Heading {math.degrees(GeoTools.euler_from_quaternion(self.current_quaternion)[2])}")
        # Convert heading to format that google KML supports
        converted_heading = (180 - math.degrees(GeoTools.euler_from_quaternion(self.current_quaternion)[2]) + 90) % 360 # 180

        # Write the KML to a file that is hosted by a python server for google earth to connect
        GeoTools.generate_kml(self.current_position.latitude, self.current_position.longitude, self.current_position.altitude, converted_heading, self.waypoints)



def main(args=None):
    rclpy.init(args=args)
    node = GPSVisualizationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
