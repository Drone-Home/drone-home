import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from ackermann_msgs.msg import AckermannDriveStamped
from .servo_jetson import ServoController
from custom_messages.srv import SetMode 
from custom_messages.msg import ServoCommand 
from math import degrees, radians


class DriveSubscriber(Node):
    # Subscribes to computer vision, gps, pwm, and web control signals. Based on signal activity and the current drive mode it chooses which control is active. Initializes servo class and sends commands
    # Subscribes to charger servo information, moves servos
    # Hosts a service to change the drive mode
    # Publishes drive status information

    def __init__(self):
        super().__init__('drive_subscriber')
        
        # Initialize the ServoController
        self.servo_controller = ServoController(debug=True)

        # Service to set the drive mode
        self.srv = self.create_service(SetMode, 'set_control_mode', self.set_control_mode_callback)
        self.drive_mode = "manual" # TODO load to and from file on change or in web_support
        
        self.subscriptions_list = [
            # Drive
            self.create_subscription(AckermannDriveStamped, 'vehicle/cv_controller_drive', self.cv_controller_callback, 10),
            self.create_subscription(AckermannDriveStamped, 'vehicle/auto_controller_drive', self.auto_controller_callback, 10),
            self.create_subscription(AckermannDriveStamped, 'vehicle/pwm_controller_drive', self.pwm_controller_callback, 10),
            self.create_subscription(AckermannDriveStamped, 'vehicle/web_controller_drive', self.web_controller_callback, 10),

            # Servo
            self.create_subscription(ServoCommand, 'vehicle/web_controller_charger', self.web_controller_charger_callback, 10),
        ]

        # Drive subscriptions defaults
        self.cv_controller_drive = AckermannDriveStamped()
        self.auto_controller_drive = AckermannDriveStamped()
        self.pwm_controller_drive = AckermannDriveStamped()
        self.web_controller_drive = AckermannDriveStamped()

        # Servo charger defaults
        self.web_controller_charger = ServoCommand(servo_ids=[0,1], positions=[0,0])

        # Timer
        timer_period = 1/20 # 20 hz # TODO tune timing
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        # Status publisher
        self.status_publisher = self.create_publisher(String, 'vehicle/drive_status', 10)

    def set_control_mode_callback(self, request, response):
        response.success = True
        self.get_logger().info(f"Service request to change drive mode {request}")
        self.drive_mode = request.mode
        self.get_logger().info(f"Drive mode now: {self.drive_mode}")
        return response
    
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
        NO_CONTROLLER_MODE = False # allow for no RC controller to be used for debugging
        pwm_drive_active = not NO_CONTROLLER_MODE and (drive_power_pwm > .2 or drive_power_pwm < -.2)
        pwm_steering_active = not NO_CONTROLLER_MODE and (steering_angle_pwm > radians(4.0) or steering_angle_pwm < radians(-4.0))
        web_drive_active = drive_power_web != 0
        web_steering_active = steering_angle_web != 0
        controller_disconnected = not NO_CONTROLLER_MODE and (steering_angle_pwm == -1.0 or steering_angle_pwm == 1.0)
        manual_drive_mode = self.drive_mode == "manual"

        cv_drive_active = steering_angle_cv != -1.0 # if cv_controller returns -1.0 steering then there are no recent frames
        cv_drive_active = True

        # Defult is cv controller TODO multiplex cv and GPS
        if(not manual_drive_mode): # If mode is manual then do not use any of the automatic controllers
            if (cv_drive_active):
                # cv drive has frames. THRESHOLD seconds in cv_controller
                steering_angle = steering_angle_cv
                drive_power = drive_power_cv
                info = "CV drive active"
            else:
                # gps if no cv detections and auto drive on
                steering_angle = steering_angle_auto
                drive_power = drive_power_auto
                info = "GPS drive active"
        else:
            steering_angle = 0
            drive_power = 0
            info = "No control input"

        # if the pwm controller is active
        if pwm_drive_active:
            # Use the pwm drive power
            drive_power = drive_power_pwm
            info = "PWM drive active"
        if pwm_steering_active:
            # Use the pwm steering
            steering_angle = steering_angle_pwm
            info = "PWM drive active"
        # if web controller if active use it
        if web_drive_active:
            drive_power = drive_power_web
            info = "Web drive active"
        if web_steering_active:
            steering_angle = steering_angle_web
            info = "Web steer active"
        # if the controller disconnects
        if controller_disconnected:
            # Use default 0 values
            steering_angle = 0
            drive_power = 0
            info = "Controller off or out of range"
        
        # Publish status info
        self.status_publisher.publish(String(data = info))
        #self.get_logger().info(f"{info}")

        # Charger commands
        charge_x_axis = self.web_controller_charger.positions[0]
        charge_y_axis = self.web_controller_charger.positions[1]
        
        # Send commands to servos
        self.servo_controller.set_steering_angle_radians_virtual(steering_angle)
        self.servo_controller.set_drive_speed_mapped(drive_power)
        self.servo_controller.set_charger_position_mapped(charge_x_axis, charge_y_axis)

        self.i += 1

    def cv_controller_callback(self, msg):
        self.cv_controller_drive = msg
    def auto_controller_callback(self, msg):
        self.auto_controller_drive = msg
    def pwm_controller_callback(self, msg):
        self.pwm_controller_drive = msg
    def web_controller_callback(self, msg):
        self.web_controller_drive = msg
    def web_controller_charger_callback(self, msg):
        self.web_controller_charger = msg

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