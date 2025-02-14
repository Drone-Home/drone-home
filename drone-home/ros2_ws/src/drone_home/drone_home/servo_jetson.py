# Class uses adafruit_motor servo library and PCA9685
# Abstracts specific servo and drive motor functionality

import time
import board
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
from math import degrees, radians
from time import sleep

class CustomServo:
    # Adds more parameters to Adafruit servo
    def __init__(self, pca, port, trim, min_angle, max_angle, actuation_range):
        self.trim = trim
        self.min_angle = min_angle + trim
        self.max_angle = max_angle + trim
        self.actuation_range = actuation_range
        self.servo = servo.Servo(pca.channels[port], actuation_range=actuation_range)
    
    def set_angle(self, angle):
        # Set the servo angle in degrees
        # steering -range/2 to range/2
        # positive is right, negative is left
        angle += self.trim # trim
        if(angle <= self.max_angle and angle >= self.min_angle):
            self.servo.angle = self.offset_center(-angle, self.actuation_range)
        else:
            print(f"Error: Input angle {angle} out of bounds. Must be within {self.min_angle} and {self.max_angle}.")
    
    @staticmethod
    def offset_center(angle, range):
        # Servo library uses 0 - range. This remaps an angle from 0 - range to -range/2 to range/2
        mapped_value = angle + range/2
        return mapped_value

class ServoController:

    def __init__(self, debug):
        # Debug prints
        self.debug = debug

        # Initialize the servo i2c device
        self.i2c = board.I2C() 
        self.pca = PCA9685(self.i2c)
        self.pca.frequency = 50

        # Initialize servos
        self.steering_servo = CustomServo(
            self.pca,
            port=0,
            trim=5,
            min_angle=-30,
            max_angle=30,
            actuation_range=210
        )
        self.drive_motor = CustomServo(
            self.pca,
            port=2,
            trim=-3,
            min_angle=-5,
            max_angle=90,
            actuation_range=180
        )
        self.charge_servo1 = CustomServo( # Left/right axix
            self.pca,
            port=4,
            trim=0,
            min_angle=-135/2,
            max_angle=135/2,
            actuation_range=135
        )
        self.charge_servo2 = CustomServo( # Up/down axis
            self.pca,
            port=6,
            trim=0,
            min_angle=-135/2,
            max_angle=135/2,
            actuation_range=135
        )

        self.neutral()

    def set_steering_angle(self, angle):
        self.steering_servo.set_angle(angle)
        if self.debug:
            print(f"Steering set to: {angle}")

    def set_drive_speed(self, angle):
        self.drive_motor.set_angle(angle)
        if self.debug:
            print(f"Drive set to: {angle}")
        
    def set_charger_angle(self, x_angle, y_angle):
        self.charge_servo1.set_angle(x_angle)
        self.charge_servo2.set_angle(y_angle)
        if self.debug:
            print(f"X angle set to: {x_angle}")
            print(f"Y angle set to: {y_angle}")

    def set_charger_position_mapped(self, x_angle, y_angle):
        # Interface for charging servos
        # Maps x_angle (left/right) and y_angle (up/down) from (-1,1) to servo range
        mapped_angle_x = self.map_value(x_angle, -1, 1, -(self.charge_servo1.min_angle-self.charge_servo1.trim), (self.charge_servo1.min_angle-self.charge_servo1.trim)) # subtract trim from min and max to get original min and max
        mapped_angle_y = self.map_value(y_angle, -1, 1, -(self.charge_servo2.min_angle-self.charge_servo2.trim), (self.charge_servo2.min_angle-self.charge_servo2.trim)) # subtract trim from min and max to get original min and max
        self.set_charger_angle(mapped_angle_x, mapped_angle_y)

    def set_drive_speed_mapped(self, angle):
        # Maps speed range of -1 to 1 to the motor range
        # 1 is forwards -1 is reverse
        mapped_angle = self.map_value(angle, -1, 1, -(self.drive_motor.min_angle-self.drive_motor.trim), (self.drive_motor.min_angle-self.drive_motor.trim)) # subtract trim from min and max to get original min and max
        if mapped_angle > 0: # reverse needs more power
            mapped_angle *= 3
        self.set_drive_speed(mapped_angle)
    
    def charge_open(self):
        self.charge_servo1.set_angle(-self.charge_servo1.max_angle)
        self.charge_servo2.set_angle(self.charge_servo2.max_angle)
    
    def charge_close(self):
        self.charge_servo1.set_angle(-self.charge_servo1.min_angle)
        self.charge_servo2.set_angle(self.charge_servo2.min_angle)

    def crawl(self):
        # Slowest possible speed for aligining. Call this in a loop
        # TODO tune timing with full setup
        servo_controller.set_drive_speed(-7) # -6.25865 min forwards
        sleep(.3)

        servo_controller.set_drive_speed(85) # braking force. Brake twice for reverse
        sleep(.8)
    
    def neutral(self):
        # Moves all to most neutral prositions
        self.set_steering_angle(0)
        self.set_drive_speed(-1)

    def kill(self):
        # Deinit servo controller
        self.neutral()
        sleep(2)
        self.pca.deinit()

    def set_steering_angle_radians_virtual(self, rad):
        # Set the servo angle in radians. -pi/4 to pi/4 mapped to real range for controller convinience 
        angle = degrees(rad)  # Convert radians to degrees
        # Check input angle to be between -45 and 45 degrees
        if angle < -45.1 or angle > 45.1: # TODO add more formal tolerance. Converting between degree and rad before makes the input fractionally smaller or larger than expected
            print(f"Error: Input angle {angle} out of bounds. Must be between -90 and 90.")
            return -1
        # Map angle from -45 to 45 to real range
        mapped_angle = self.map_value(angle, -45.1, 45.1, self.steering_servo.min_angle-self.steering_servo.trim, self.steering_servo.max_angle-self.steering_servo.trim) # subtract trim from min and max to get original min and max
        self.set_steering_angle(mapped_angle) 

    @staticmethod
    def map_value(value, from_min, from_max, to_min, to_max):
        # Map value to new range
        mapped_value = to_min + (value - from_min) * (to_max - to_min) / (from_max - from_min)
        return mapped_value

    @staticmethod
    def offset_center(angle, range):
        # Servo library uses 0 - range. This remaps an angle from 0 - range to -range/2 to range/2
        mapped_value = angle + range/2
        return mapped_value

if __name__ == "__main__":
    # tests
    servo_controller = ServoController()
    servo_controller.set_drive_speed(0)
    #servo_controller.set_drive_speed(-6.25865)
    #for i in range(200):
        #servo_controller.crawl()
    #servo_controller.charge_open()
    sleep(2)
    #servo_controller.charge_close()
    #sleep(1)
    servo_controller.set_drive_speed_mapped(.1)

    servo_controller.kill()
