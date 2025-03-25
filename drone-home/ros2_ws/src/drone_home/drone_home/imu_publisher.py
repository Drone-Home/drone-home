import rclpy
from rclpy.node import Node
import adafruit_bno055
import board
import time

from geometry_msgs.msg import PoseStamped, Quaternion


class IMUSensor:
    def __init__(self):
        i2c = board.I2C()
        self.sensor = adafruit_bno055.BNO055_I2C(i2c)
        self.sensor.offsets_magnetometer = (-447, -896, -311) #TODO get new calibration values when mounted
        self.sensor.offsets_accelerometer = (11, -90, -29)

    def get_euler_angles(self):
        # Returns the Euler angles from the IMU sensor
        return self.sensor.euler
    
    def get_quaternion(self):
        # Get quaternion from sensor
        try:
            quaternion = self.sensor.quaternion
        except Exception as e:
            print(f"IMU error: {e}")
            quaternion = None

        # Returns zero element (undefined rotation) if error
        if quaternion is None or len(quaternion) != 4:
            quaternion = (0.0, 0.0, 0.0, 0.0)

        # Builds Quaternion object for publishing
        return Quaternion(z=quaternion[3], y=quaternion[2], x=quaternion[1], w=quaternion[0])
    
    def calibrateCheck(self):
        time.sleep(.5)
        cal = self.sensor.calibration_status
        message = f"Calibration (sys:{cal[0]}, gyro:{cal[1]}, accel:{cal[2]}, mag:{cal[3]})"
        calibrated = False
        level = -1 # 2
        if(cal[0] > level and cal[1] > level and cal[2] > level and cal[3] > level): # TODO test out different calibration methods
            calibrated = True

        return calibrated, message


    def calibrated(self):
        time.sleep(1)
        return self.sensor.calibration_status, self.sensor.offsets_magnetometer
    
    def printCalibration(self):
        time.sleep(1)
        return self.sensor.calibration_status, self.sensor.offsets_magnetometer, self.sensor.offsets_accelerometer

class IMUPublisher(Node):
    def __init__(self):
        super().__init__('imu_publisher')
        self.pose_publisher = self.create_publisher(PoseStamped, 'vehicle/pose', 10)
        
        # Initialize IMU
        self.imu_sensor = IMUSensor()

        # Wait for IMU to calibrate
        while True:
            cal = self.imu_sensor.calibrateCheck()
            self.get_logger().info(f"Calibration status: {cal}")
            if cal[0]:
                break

        timer_period = 0.05 #1.0 #0.01  # todo refert to fast seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        
        # For getting calibration values
        #self.get_logger().info(f"Calibration magnetometer, accel values: {self.imu_sensor.printCalibration()}")

        # Publish Pose. Initial position is north
        pose_msg = PoseStamped()
        quaternion = self.imu_sensor.get_quaternion()
        pose_msg.header.stamp = self.get_clock().now().to_msg()
        pose_msg.header.frame_id = "imu_frame"
        pose_msg.pose.orientation = quaternion
        self.pose_publisher.publish(pose_msg)

        #self.get_logger().info(f"Quat: {self.imu_sensor.get_euler_angles()}")

        self.i += 1

def main(args=None):
      
    rclpy.init(args=args)
    imu_publisher = IMUPublisher()
    rclpy.spin(imu_publisher)
    imu_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
