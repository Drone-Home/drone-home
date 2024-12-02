import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from ackermann_msgs.msg import AckermannDriveStamped
from .servo import ServoController
from .motor import MotorController
from math import degrees, radians


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        
        # Initialize the ServoController and MotorController
        self.servo_controller = ServoController()
        self.motor_controller = MotorController()
        
        self.subscription = self.create_subscription(AckermannDriveStamped, 'vehicle/drive', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        
        # Map the Ackermann steering angle to the servo angle
        steering_angle = msg.drive.steering_angle  # in radians
        drive_power = msg.drive.speed # TODO replace with drive
        
        # Map the Ackermann steering angle (usually small) to the servo's range
        #self.get_logger().info(f'Angle set: {degrees(steering_angle)}')
        self.servo_controller.set_angle_radians_virtual(steering_angle)
        self.motor_controller.set_angle_radians_virtual(drive_power)
        
def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()