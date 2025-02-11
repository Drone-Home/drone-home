import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from ackermann_msgs.msg import AckermannDriveStamped
from .servo_jetson import ServoController
from math import degrees, radians


class DriveSubscriber(Node):

    def __init__(self):
        super().__init__('drive_subscriber')
        
        # Initialize the ServoController
        self.servo_controller = ServoController(debug=True)
        
        self.subscription = self.create_subscription(AckermannDriveStamped, 'vehicle/cv_controller_drive', self.cv_controller_callback, 10)
        self.subscription = self.create_subscription(AckermannDriveStamped, 'vehicle/auto_controller_drive', self.auto_controller_callback, 10)
        self.subscription = self.create_subscription(AckermannDriveStamped, 'vehicle/pwm_controller_drive', self.pwm_controller_callback, 10)
        self.subscription = self.create_subscription(AckermannDriveStamped, 'vehicle/web_controller_drive', self.web_controller_callback, 10)

        # Drive subscriptions
        self.cv_controller_drive = AckermannDriveStamped()
        self.auto_controller_drive = AckermannDriveStamped()
        self.pwm_controller_drive = AckermannDriveStamped()
        self.web_controller_drive = AckermannDriveStamped()

        # Timer
        timer_period = 1/20 # 20 hz # TODO tune timing
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
    
    def timer_callback(self):
        # Map the Ackermann steering angle (usually small) to the servo's range
        #self.get_logger().info(f'Angle set: {degrees(steering_angle)}')

        # Only node that calls servo class
        # Subscribes to the auto controller drive, the flask drive, and RC controller Drive. Currently it will only get drive from RC controller and steering from auto controller

        # Drive speed is mapped -1 to 1
        # Steering is mapped -pi/4 to pi/4

        # If drive speed is set to 2, the crawl function is called making the vehicle move as slow as possible

        # Map the Ackermann steering angle to the servo angle

        # TODO multiplex values from controllers based on values

        # Web controller
        drive_power_web = self.web_controller_drive.drive.speed
        steering_angle_web = self.web_controller_drive.drive.steering_angle  # in radians

        # Manual controller
        drive_power_pwm = self.pwm_controller_drive.drive.speed
        steering_angle_pwm = self.pwm_controller_drive.drive.steering_angle  # in radians
        
        # Auto controller
        drive_power_auto = self.auto_controller_drive.drive.speed
        steering_angle_auto = self.auto_controller_drive.drive.steering_angle  # in radians

        # CV controller
        drive_power_cv = self.cv_controller_drive.drive.speed
        steering_angle_cv = self.cv_controller_drive.drive.steering_angle  # in radians

        # If the pwm controller is slightly pressed it overrides manual
        # If pwm controller turns off or out of range use 0 values
        pwm_drive_active = drive_power_pwm > .2 or drive_power_pwm < -.2
        pwm_steering_active = steering_angle_pwm > radians(4.0) or steering_angle_pwm < radians(-4.0)
        web_active = drive_power_web != 0 or steering_angle_web != 0
        controller_disconnected = steering_angle_pwm == -1.0

        # Defult is cv controller TODO multiplex cv and GPS
        steering_angle = steering_angle_cv
        drive_power = drive_power_cv

        info = "cv_active"

        # if the pwm controller is active
        if pwm_drive_active:
            # Use the pwm drive power
            drive_power = drive_power_pwm
            info = "pwm_drive_active"
        if pwm_steering_active:
            # Use the pwm steering
            steering_angle = steering_angle_pwm
            info = "pwm_steering_active"
        # if web controller if active use it
        if web_active:
            drive_power = drive_power_web
            steering_angle = steering_angle_web
            info = "web_active"
        # if the controller disconnects
        if controller_disconnected:
            # Use default 0 values
            steering_angle = 0
            drive_power = 0
            info = "controller_disconnected"
        
        #self.get_logger().info(f"{info}")
        self.servo_controller.set_steering_angle_radians_virtual(steering_angle)
        self.servo_controller.set_drive_speed_mapped(drive_power)

        self.i += 1

    def cv_controller_callback(self, msg):
        self.cv_controller_drive = msg
    def auto_controller_callback(self, msg):
        self.auto_controller_drive = msg
    def pwm_controller_callback(self, msg):
        self.pwm_controller_drive = msg
    def web_controller_callback(self, msg):
        self.web_controller_drive = msg

def main(args=None):
    rclpy.init(args=args)

    drive_subscriber = DriveSubscriber()

    rclpy.spin(drive_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    drive_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()