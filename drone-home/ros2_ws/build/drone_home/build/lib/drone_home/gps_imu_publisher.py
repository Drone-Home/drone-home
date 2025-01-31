import rclpy
from rclpy.node import Node

import adafruit_bno055
import board
import time
import serial
import serial.tools.list_ports
import adafruit_gps
import math
from math import degrees, radians

from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix, NavSatStatus
from geometry_msgs.msg import PoseStamped, Quaternion


class IMUSensor:
    def __init__(self):
        i2c = board.I2C()
        self.sensor = adafruit_bno055.BNO055_I2C(i2c)
        self.sensor.offsets_magnetometer = (-2900, -3480, -351) #(-25, -132, -330) out of box. New from in box
        self.sensor.offsets_accelerometer = (11, -90, -29)

    def get_euler_angles(self):
        # Returns the Euler angles from the IMU sensor
        return self.sensor.euler
    
    def get_quaternion(self):
        # Get quaternion from sensor
        try:
            quaternion = self.sensor.quaternion
        except:
            print(f"IMU error")
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

class GPSSensor:
    def __init__(self):
        # Get GPS device by name
        #device = "/dev/serial/by-id/usb-Silicon_Labs_CP2102N_USB_to_UART_Bridge_Controller_3a054ddbab9eec11b3a69579a29c855c-if00-port0"
        device = "/dev/ttyUSB0"
        try:
            self.uart = serial.Serial(device, baudrate=57600, timeout=10) # gps3.py on desktop chnges the baudrate from 9600 to 57600. Need to do if onbuard battery dies and resets rate
            self.gps = adafruit_gps.GPS(self.uart, debug=False)
            print(f"Connected GPS on {device}")
        except serial.SerialException:
            print(f"Could not open GPS on port {device}")

        # Set GPS update rates and output message rates
        self.gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
        # 1 Hz
        #self.gps.send_command(b"PMTK220,1000")
        # 10 Hz
        self.gps.send_command(b"PMTK220,100")
        
        self.last_print_time = time.monotonic()

    def has_fix(self):
        return self.gps.has_fix
        
    def update(self):
        # Update GPS data
        try:
            self.gps.update()
            return "Updated"
        except:
            try:
                # Try to reconnect GPS on error
                time.sleep(1)
                self.__init__()
            except Exception as e: print(e)
            return e
        
    def has_new_data(self):
        current_time = time.monotonic()
        if current_time - self.last_print_time >= 1.0:
            self.last_print_time = current_time
            return True
        return False
    

    def get_data(self):
        # Returns current GPS data. Print "Waiting for fix..." if not available
        if not self.gps.has_fix:
            return "Waiting for fix..."
        
        data = {
            "timestamp": f"{self.gps.timestamp_utc.tm_mon}/{self.gps.timestamp_utc.tm_mday}/{self.gps.timestamp_utc.tm_year} {self.gps.timestamp_utc.tm_hour:02}:{self.gps.timestamp_utc.tm_min:02}:{self.gps.timestamp_utc.tm_sec:02}",
            "latitude": self.gps.latitude,
            "longitude": self.gps.longitude,
            "satellites": self.gps.satellites,
            "altitude_m": self.gps.altitude_m,
            "speed_kmh": self.gps.speed_kmh
        }
        return data
    
    def get_navsatfix_msg(self):
        # Build and return NavSatFix message
        navsat_msg = NavSatFix()
        
        # Populate GPS data
        navsat_msg.latitude = self.gps.latitude if self.gps.latitude is not None else 0.0
        navsat_msg.longitude = self.gps.longitude if self.gps.longitude is not None else 0.0
        navsat_msg.altitude = self.gps.altitude_m if self.gps.altitude_m is not None else 0.0

        #navsat_msg.latitude = 29.6396803
        #navsat_msg.longitude = -82.3612485

        # Set NavSatStatus (GPS_FIX or no fix)
        navsat_msg.status = NavSatStatus() 
        # TODO remove after testing 
        #navsat_msg.status.status = NavSatStatus.STATUS_FIX
        #return navsat_msg
        if self.gps.has_fix or self.gps.latitude is None or self.gps.longitude is None:
            navsat_msg.status.status = NavSatStatus.STATUS_FIX
        else:
            navsat_msg.status.status = NavSatStatus.STATUS_NO_FIX

        navsat_msg.status.service = NavSatStatus.SERVICE_GPS #self.gps.satellites#NavSatStatus.SERVICE_GPS # Using service message to show sattelites instead
        return navsat_msg

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.pose_publisher = self.create_publisher(PoseStamped, 'vehicle/pose', 10)
        self.gps_publisher = self.create_publisher(NavSatFix, 'gps/fix', 10)
        
        # Initialize IMU and GPS sensors
        self.imu_sensor = IMUSensor()
        self.gps_sensor = GPSSensor()

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
        
        #self.get_logger().info(f"Calibration magnetometer values: {self.imu_sensor.calibrated()}")

        # Publish Pose. Initial position is north
        pose_msg = PoseStamped()
        quaternion = self.imu_sensor.get_quaternion()
        pose_msg.header.stamp = self.get_clock().now().to_msg()
        pose_msg.header.frame_id = "imu_frame"
        pose_msg.pose.orientation = quaternion
        self.pose_publisher.publish(pose_msg)

        #self.get_logger().info(f"Quat: {self.imu_sensor.get_euler_angles()}")


        # Publish GPS
        update_string = self.gps_sensor.update()
        navsat_msg = self.gps_sensor.get_navsatfix_msg()
        navsat_msg.header.stamp = self.get_clock().now().to_msg()
        navsat_msg.header.frame_id = "gps_sensor"
        if navsat_msg is not None:
            self.gps_publisher.publish(navsat_msg)
            #self.get_logger().info(f"Published GPS data: {navsat_msg.status}, {navsat_msg.longitude}")

        self.i += 1

def main(args=None):
    
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
