import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped
import math
import time
from math import degrees, radians
from .geo_tools import GeoTools
from custom_messages.msg import CV 

class Controller(Node):

    def __init__(self):
        super().__init__('cv_controller')

        self.cv_frame = CV()
        self.last_frame_time = time.time() # time frames to decide when data is outdated
        self.THRESHOLD = 3 # seconds before frame is considered outdated
        self.cv_active = False

        # Publisher for AckermannDrive
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'vehicle/cv_controller_drive', 10)

        # Subscibe to CV messages
        self.cv_subscriber = self.create_subscription(CV, 'vehicle/cv', self.cv_callback, 10)
    
        # Control loop timer
        self.timer = self.create_timer(0.1, self.control_loop)

        self.get_logger().info("CV Controller running")

    def cv_callback(self, msg):
        # Update the current quaternion from the PoseStamped message
        self.cv_frame = msg
        # Update timestamp on new frame
        self.last_frame_time = time.time()

    def control_loop(self):
        # if frame is outdated (no new frames)
        if time.time() - self.last_frame_time > self.THRESHOLD:
            steering_angle = -1.0
        else:
            # Calculate the proportional steering angle based on heading difference
            steering_angle = self.calculate_steering_angle(self.cv_frame)
        
            # Limit steering angle to -pi/4 to pi/4
            if steering_angle > math.pi/4:
                steering_angle = math.pi/4
            elif steering_angle < -math.pi/4:
                steering_angle = -math.pi/4

        # Create and publish AckermannDrive message
        drive_msg = AckermannDriveStamped()
        drive_msg.drive.steering_angle = steering_angle
        drive_msg.drive.speed = 0.0  # TODO speed later
        self.publisher_.publish(drive_msg)

    def calculate_steering_angle(self, computer_vision_data):

        # CV data: x and y (0 - 640 left to right) and (0 to 480 top to bottom)
        # Calculate error
        cv_error = computer_vision_data.x_pos - (640/2)
         
        # Calculate proportional control for heading
        heading_error = cv_error # TODO get error from CV
        proportional_gain = 0.005
        return proportional_gain * heading_error


def main(args=None):
    rclpy.init(args=args)
    controller = Controller()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
