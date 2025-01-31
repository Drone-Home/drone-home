import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

import board
import busio
import struct  # For unpacking binary data
import math

class PWMPublisher(Node):

    def __init__(self):
        super().__init__('i2c_publisher')

        # Initialize I2C
        self.i2c = busio.I2C(board.SCL, board.SDA)

        # Set the I2C address of the Arduino Nano
        self.I2C_ADDRESS = 0x08

        # Wait for the I2C bus to be ready
        while not self.i2c.try_lock():
            pass

        # Publisher for AckermannDrive
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'vehicle/pwm_controller_drive', 10)
        
        # I2C read timer
        timer_period = 1/20 # 20 hz
        self.timer = self.create_timer(timer_period, self.i2c_read)

        # Defult channel values
        self.channel0 = 0
        self.channel1 = 1500 # defult values when off

        # Constant limits
        self.CH0MIN = 1150
        self.CH0MAX = 1800
        self.CH1MIN = 920
        self.CH1MAX = 2000
        

    def i2c_read(self):
        
        # Read 4 bytes from the Arduino (2 bytes for each PWM value)
        result = bytearray(4)  # Expect 4 bytes
        self.i2c.readfrom_into(self.I2C_ADDRESS, result)
        
        # Unpack the data into two 16-bit integers
        pwm0, pwm1 = struct.unpack('<HH', result)  # '<HH' = little-endian, 2 unsigned shorts
        #print(f"PWM 1: {pwm0}, PWM 2: {pwm1}")

        # Defaut zero values
        steering_angle = -1.0 # TODO replace with constants
        drive_speed = 0.0

        if pwm0 == 0:
            print("Radio is off or out of range")
        else:
            # Map values to drive values. pwm0 is steering pwm1 is drive
            steering_angle = self.map_value(pwm0, self.CH0MIN, self.CH0MAX, -math.pi/4, math.pi/4)
            drive_speed = self.map_value(pwm1, self.CH1MIN, self.CH1MAX, -1, 1)
        
        #print(f"Steering: {steering_angle}, Drive: {drive_speed}")

        # Create and publish AckermannDrive message
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
    rclpy.init(args=args)
    pwm_publisher = PWMPublisher()
    rclpy.spin(pwm_publisher)
    # unlock i2c
    pwm_publisher.i2c.unlock()
    pwm_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
