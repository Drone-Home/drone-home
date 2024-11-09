import rclpy
from rclpy.node import Node

import adafruit_bno055
import board
import time
import serial
import serial.tools.list_ports
import adafruit_gps

from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix, NavSatStatus
from geometry_msgs.msg import PoseStamped, Quaternion


class IMUSensor:
    def __init__(self):
        i2c = board.I2C()
        self.sensor = adafruit_bno055.BNO055_I2C(i2c)

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
        return Quaternion(x=quaternion[0], y=quaternion[1], z=quaternion[2], w=quaternion[3])


class GPSSensor:
    def __init__(self):
        # Get GPS device by name
        device = "/dev/serial/by-id/usb-Silicon_Labs_CP2102N_USB_to_UART_Bridge_Controller_3a054ddbab9eec11b3a69579a29c855c-if00-port0"
        try:
            self.uart = serial.Serial(device, baudrate=9600, timeout=10)
            self.gps = adafruit_gps.GPS(self.uart, debug=False)
            print(f"Connected GPS on {device}")
        except serial.SerialException:
            print(f"Could not open GPS on port {device}")
        
        # Set GPS update rates and output message rates
        self.gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
        self.gps.send_command(b"PMTK220,1000")
        
        self.last_print_time = time.monotonic()

    def has_fix(self):
        return self.gps.has_fix
        
    def update(self):
        # Update GPS data
        try:
            self.gps.update()
        except:
            try:
                # Try to reconnect GPS on error
                time.sleep(1)
                self.__init__()
            except Exception as e: print(e)
        
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
        
        navsat_msg = NavSatFix()
        
        # Populate GPS data
        navsat_msg.latitude = self.gps.latitude if self.gps.latitude is not None else 0.0
        navsat_msg.longitude = self.gps.longitude if self.gps.longitude is not None else 0.0
        navsat_msg.altitude = self.gps.altitude_m if self.gps.altitude_m is not None else 0.0

        # Set NavSatStatus (GPS_FIX or no fix)
        navsat_msg.status = NavSatStatus()
        if self.gps.has_fix or self.gps.latitude is None or self.gps.longitude is None:
            navsat_msg.status.status = NavSatStatus.STATUS_FIX
        else:
            navsat_msg.status.status = NavSatStatus.STATUS_NO_FIX

        navsat_msg.status.service = NavSatStatus.SERVICE_GPS
        return navsat_msg


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.pose_publisher = self.create_publisher(PoseStamped, 'vehicle/pose', 10)
        self.gps_publisher = self.create_publisher(NavSatFix, 'gps/fix', 10)
        
        # Initialize IMU and GPS sensors
        self.imu_sensor = IMUSensor()
        self.gps_sensor = GPSSensor()

        
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        # Publish Pose
        pose_msg = PoseStamped()
        quaternion = self.imu_sensor.get_quaternion()
        pose_msg.header.stamp = self.get_clock().now().to_msg()
        pose_msg.pose.orientation = quaternion
        self.pose_publisher.publish(pose_msg)
        #self.get_logger().info(f"Published Pose with angles: {self.imu_sensor.get_euler_angles()}")

        # Publish GPS
        self.gps_sensor.update()
        navsat_msg = self.gps_sensor.get_navsatfix_msg()
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

def gps2():
    global last_print
    # Make sure to call gps.update() every loop iteration and at least twice
    # as fast as data comes from the GPS unit (usually every second).
    # This returns a bool that's true if it parsed new data (you can ignore it
    # though if you don't care and instead look at the has_fix property).
    gps.update()
    # Every second print out current location details if there's a fix.
    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            # Try again if we don't have a fix yet.
            print("Waiting for fix...")
            return
        # We have a fix! (gps.has_fix is true)
        # Print out details about the fix like location, date, etc.
        print("=" * 40)  # Print a separator line.
        print(
            "Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}".format(
                gps.timestamp_utc.tm_mon,  # Grab parts of the time from the
                gps.timestamp_utc.tm_mday,  # struct_time object that holds
                gps.timestamp_utc.tm_year,  # the fix time.  Note you might
                gps.timestamp_utc.tm_hour,  # not get all data like year, day,
                gps.timestamp_utc.tm_min,  # month!
                gps.timestamp_utc.tm_sec,
            )
        )
        print("Latitude: {0:.6f} degrees".format(gps.latitude))
        print("Longitude: {0:.6f} degrees".format(gps.longitude))
        print(
            "Precise Latitude: {} degs, {:2.4f} mins".format(
                gps.latitude_degrees, gps.latitude_minutes
            )
        )
        print(
            "Precise Longitude: {} degs, {:2.4f} mins".format(
                gps.longitude_degrees, gps.longitude_minutes
            )
        )
        print("Fix quality: {}".format(gps.fix_quality))
        # Some attributes beyond latitude, longitude and timestamp are optional
        # and might not be present.  Check if they're None before trying to use!
        if gps.satellites is not None:
            print("# satellites: {}".format(gps.satellites))
        if gps.altitude_m is not None:
            print("Altitude: {} meters".format(gps.altitude_m))
        if gps.speed_knots is not None:
            print("Speed: {} knots".format(gps.speed_knots))
        if gps.speed_kmh is not None:
            print("Speed: {} km/h".format(gps.speed_kmh))
        if gps.track_angle_deg is not None:
            print("Track angle: {} degrees".format(gps.track_angle_deg))
        if gps.horizontal_dilution is not None:
            print("Horizontal dilution: {}".format(gps.horizontal_dilution))
        if gps.height_geoid is not None:
            print("Height geoid: {} meters".format(gps.height_geoid))