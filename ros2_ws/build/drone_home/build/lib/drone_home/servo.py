from gpiozero import AngularServo
from math import degrees, radians
from time import sleep

class ServoController:
    # Constants
    SERVO_MIN = -40 #bounds for steering left and right
    SERVO_MAX = 40
    SERVO_TRIM = -5.0

    def __init__(self, pin=12, min_angle=-90, max_angle=90, frame_width=0.0025):
        # Initialize the servo on pin 12 for steering
        self.servo = AngularServo(pin, min_angle=min_angle, max_angle=max_angle, frame_width=frame_width)
        self.center_servo()

    def center_servo(self):
        # Center the servo
        centered_angle = 0.0 + self.SERVO_TRIM
        self.set_angle(centered_angle)

    def set_angle(self, angle):
        # Set angle in degrees. return: 0 if angle set successfully, -1 if out of bounds
        # Left is negative right is positive

        if angle < self.SERVO_MIN or angle > self.SERVO_MAX:
            print(f"Error: Angle {angle} out of bounds. Must be between {self.SERVO_MIN} and {self.SERVO_MAX}.")
            return -1
        self.servo.angle = -angle + self.SERVO_TRIM
        print(f"Servo angle set to {angle}")
        return 0

    def set_angle_radians(self, rad):
        # Set the servo angle in radians
        angle = degrees(rad)  # Convert radians to degrees
        return self.set_angle(angle)

    def stop_servo(self):
        # Stops the servo
        self.center_servo()
        sleep(2)
        self.servo.angle = None
        print("Servo stopped.")

    def set_angle_virtual(self, angle):
        if angle < -45.1 or angle > 45.1: # TODO add more formal tolerance. Converting between degree and rad before makes the input fractionally smaller or larger than expected
            print(f"Error: Input angle {angle} out of bounds. Must be between -90 and 90.")
            return -1
        # Map the input range -45 to 45 to min and max
        mapped_angle = self.map_value(angle, -45.1, 45.1, self.SERVO_MIN, self.SERVO_MAX)
        return self.set_angle(mapped_angle)
    
    def set_angle_radians_virtual(self, rad):
        # Set the servo angle in radians. -pi/4 to pi/4 for controllerconvinience even though car only supports -25 to 25 for example

        angle = degrees(rad)  # Convert radians to degrees
        return self.set_angle_virtual(angle) 

    @staticmethod
    def map_value(value, from_min, from_max, to_min, to_max):
        # Map value to new range
        mapped_value = to_min + (value - from_min) * (to_max - to_min) / (from_max - from_min)
        return mapped_value

# Example usage:
if __name__ == "__main__":
    servo_controller = ServoController()
    # Move servo to various angles for testing
    servo_controller.set_angle_virtual(-90)
    sleep(1)
    servo_controller.set_angle_radians_virtual(3.1415/2)
    sleep(1)
    servo_controller.set_angle_virtual(0)
    sleep(2)
    servo_controller.stop_servo()
