import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped
from geometry_msgs.msg import Quaternion, PoseStamped
from sensor_msgs.msg import NavSatFix, NavSatStatus
import tf2_ros
import math
import time
from math import degrees, radians
from .geo_tools import GeoTools

class Controller(Node):

    def __init__(self):
        super().__init__('controller')

        self.waypoints = [
        (29.6396803, -82.3612485),  # 1
        (29.6399049, -82.3612544),  # 2
        (29.6399106, -82.3614452),  # 3
        (29.6396941, -82.3614379),  # 4
        ]
        self.current_waypoint_index = 0  # Start with the first waypoint
        self.distance_threshold = 5.0  # Distance threshold in meters to switch waypoints

        # Publisher for AckermannDrive
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'vehicle/drive', 10)
        
        # Subscriber for vehicle's orientation (Pose with Quaternion) and GPS
        self.pose_subscriber = self.create_subscription(PoseStamped, 'vehicle/pose', self.pose_callback, 10)
        self.gps_subscriber = self.create_subscription(NavSatFix, 'gps/fix', self.gps_callback, 10)


        # Set target heading # Note the yaw on the car is set to be the roll in quaternion TODO transform quaternion to make them correct
        # For now just set the target roll instead of yaw and read the roll instead of yaw in self.euler_from_quaternion(current_quaternion)[0]
        target_yaw = math.radians(0.0)
        self.target_quaternion = self.euler_to_quaternion(0.0, 0.0, target_yaw)

        # Control loop timer
        self.timer = self.create_timer(0.05, self.control_loop)

        # current quaternion (updated from subscriber)
        self.current_quaternion = Quaternion(x=0.0, y=0.0, z=0.0, w=0.0)
        self.current_position = NavSatFix(latitude = -1.0, longitude = -1.0)

        self.get_logger().info(f"Controller running")

    def pose_callback(self, msg):
        # Update the current quaternion from the PoseStamped message
        self.current_quaternion = msg.pose.orientation
    
    def gps_callback(self, msg):
        # Update the current GPS location from NavSatFix message
        self.current_position = msg

    def control_loop(self):
        current_quaternion = self.current_quaternion
        if current_quaternion == Quaternion(x=0.0, y=0.0, z=0.0, w=0.0) or self.current_position.latitude == -1.0: # TODO add check for GPS later
            # Not calibrated yet
            #self.get_logger().info(f"Not calibrated yet")
            return
        
        # Calculate the proportional steering angle based on heading difference
        steering_angle = self.calculate_steering_angle(current_quaternion)
        
        # Limit steering angle to -pi/4 to pi/4
        if steering_angle > math.pi/4:
            steering_angle = math.pi/4
        elif steering_angle < -math.pi/4:
            steering_angle = -math.pi/4

        #self.get_logger().info(f"Steering angle: {degrees(steering_angle)}")

        # target GPS
        lat1, lon1 = self.current_position.latitude, self.current_position.longitude   # New York
        lat2, lon2 = self.waypoints[self.current_waypoint_index]
        #lat2, lon2 = 29.6337427, -82.3609089 # country village  # 29.6337850, -82.3609108 - arrow

        bearing = GeoTools.get_bearing(lat1, lon1, lat2, lon2)
        distance = GeoTools.geo_distance(lat1, lon1, lat2, lon2)

        # waypoint system
        if distance < self.distance_threshold:
            # Move to the next waypoint if there are more waypoints
            if self.current_waypoint_index < len(self.waypoints) - 1:
                self.current_waypoint_index += 1
                self.get_logger().info(f"Switching to next waypoint: {self.waypoints[self.current_waypoint_index]}")
                time.sleep(1)
            else:
                self.get_logger().info("All waypoints reached!")
                self.current_waypoint_index = 0
        
        #self.get_logger().info((f"Bearing: {bearing:.2f}°"))
        self.get_logger().info((f"Going to {self.current_waypoint_index+1}: {distance:.2f} meters"))

        self.target_quaternion = self.euler_to_quaternion(0.0, 0.0, radians(bearing))


        # Create and publish AckermannDrive message
        drive_msg = AckermannDriveStamped()
        drive_msg.drive.steering_angle = -steering_angle
        drive_msg.drive.speed = 0.0  # TODO speed later
        self.publisher_.publish(drive_msg)

    def calculate_steering_angle(self, current_quaternion):
        # Convert current and target quaternions to yaw
        current_yaw = self.euler_from_quaternion(current_quaternion)[2]
        target_yaw = self.euler_from_quaternion(self.target_quaternion)[2] #self.quaternion_to_yaw(self.target_quaternion)
        
        diff = self.quaternion_multiply(self.quaternion_conjugate(current_quaternion), self.target_quaternion)
    
        self.get_logger().info(f"Current Yaw: {degrees(current_yaw)}, target = {degrees(target_yaw)}")
        self.get_logger().info(f"CurrentDiff: {degrees(self.euler_from_quaternion(diff)[2])}")
        

        # Calculate proportional control for heading
        heading_error = self.euler_from_quaternion(diff)[2]
        proportional_gain = 1.5
        return proportional_gain * heading_error

        

    def euler_to_quaternion(self, roll, pitch, yaw):
        # Converts Euler angles (in radians) to a Quaternion message
        q = Quaternion()
        q.x = math.sin(roll / 2) * math.cos(pitch / 2) * math.cos(yaw / 2) - math.cos(roll / 2) * math.sin(pitch / 2) * math.sin(yaw / 2)
        q.y = math.cos(roll / 2) * math.sin(pitch / 2) * math.cos(yaw / 2) + math.sin(roll / 2) * math.cos(pitch / 2) * math.sin(yaw / 2)
        q.z = math.cos(roll / 2) * math.cos(pitch / 2) * math.sin(yaw / 2) - math.sin(roll / 2) * math.sin(pitch / 2) * math.cos(yaw / 2)
        q.w = math.cos(roll / 2) * math.cos(pitch / 2) * math.cos(yaw / 2) + math.sin(roll / 2) * math.sin(pitch / 2) * math.sin(yaw / 2)
        return q
    
    def get_quaternion_from_euler(roll, pitch, yaw):
        q = Quaternion()
        q.x = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
        q.y = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
        q.z = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
        q.w = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
        
        return q

    def quaternion_to_yaw(self, quaternion):
        # Converts a Quaternion message to yaw (in radians)
        siny_cosp = 2 * (quaternion.w * quaternion.z + quaternion.x * quaternion.y)
        cosy_cosp = 1 - 2 * (quaternion.y**2 + quaternion.z**2)
        return math.atan2(siny_cosp, cosy_cosp)

    def euler_from_quaternion(self, quaternion):
        w = quaternion.w
        z = quaternion.z
        x = quaternion.x
        y = quaternion.y

        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
     
        return roll_x, pitch_y, yaw_z # in radians
    
    def quaternion_conjugate(self, quaternion):
        # Conjugate of a quaternion inverts the x, y, z components
        return Quaternion(
            x=-quaternion.x,
            y=-quaternion.y,
            z=-quaternion.z,
            w=quaternion.w
        )

    def quaternion_multiply(self, q1, q2):
        # Multiplies two quaternions q1 and q2
        return Quaternion(
            w=q1.w * q2.w - q1.x * q2.x - q1.y * q2.y - q1.z * q2.z,
            x=q1.w * q2.x + q1.x * q2.w + q1.y * q2.z - q1.z * q2.y,
            y=q1.w * q2.y - q1.x * q2.z + q1.y * q2.w + q1.z * q2.x,
            z=q1.w * q2.z + q1.x * q2.y - q1.y * q2.x + q1.z * q2.w
        )

def main(args=None):
    rclpy.init(args=args)
    controller = Controller()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
