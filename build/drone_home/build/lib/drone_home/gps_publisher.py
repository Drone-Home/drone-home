import rclpy
from rclpy.node import Node

import time
import serial
import serial.tools.list_ports
import adafruit_gps

from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix, NavSatStatus

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
        
        #self.gps.send_command(b"PMTK220,1000") # 1 Hz
        self.gps.send_command(b"PMTK220,100")   # 10 Hz
        
        self.last_print_time = time.monotonic()

    def has_fix(self):
        return self.gps.has_fix
        
    def update(self):
        # Update GPS data
        try:
            self.gps.update()
            return "Updated"
        except Exception as e:
            print(f"GPS Error: {e}")
            try:
                # Try to reconnect GPS on error
                time.sleep(1)
                self.__init__()
            except Exception as e:
                print(e)
                return e

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
    
    def get_navsatfix_msg(self, debug):
        # Build and return NavSatFix message
        navsat_msg = NavSatFix()
        
        # Populate GPS data
        navsat_msg.latitude = self.gps.latitude if self.gps.latitude is not None else 0.0
        navsat_msg.longitude = self.gps.longitude if self.gps.longitude is not None else 0.0
        navsat_msg.altitude = self.gps.altitude_m if self.gps.altitude_m is not None else 0.0

        if(debug):
            navsat_msg.latitude = 29.6396803
            navsat_msg.longitude = -82.3612485

        # Set NavSatStatus (GPS_FIX or no fix)
        navsat_msg.status = NavSatStatus() 
        # TODO remove after testing 
        #navsat_msg.status.status = NavSatStatus.STATUS_FIX
        #return navsat_msg
        if self.gps.has_fix or self.gps.latitude is None or self.gps.longitude is None:
            navsat_msg.status.status = NavSatStatus.STATUS_FIX
        else:
            navsat_msg.status.status = NavSatStatus.STATUS_NO_FIX
        
        satellites = int(self.gps.satellites) if self.gps.satellites is not None else 0
        navsat_msg.status.service = satellites#NavSatStatus.SERVICE_GPS # Using service message to show sattelites instead
        return navsat_msg

class GPSPublisher(Node):
    def __init__(self):
        super().__init__('gps_publisher')
        self.gps_publisher = self.create_publisher(NavSatFix, 'gps/fix', 10)
        
        # Initialize GPS
        self.gps_sensor = GPSSensor()

        # Update rate            
        timer_period = 1/10 #1.0 #0.01  # 10 hz
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        # Debug mode publishes a defined GPS points (gps still needs to be connected)
        debug = False

        # Publish GPS
        update_string = self.gps_sensor.update()
        navsat_msg = self.gps_sensor.get_navsatfix_msg(debug)
        navsat_msg.header.stamp = self.get_clock().now().to_msg()
        navsat_msg.header.frame_id = "gps_sensor"
        if navsat_msg is not None:
            self.gps_publisher.publish(navsat_msg)
            #self.get_logger().info(f"Published GPS data: {navsat_msg.status}, {navsat_msg.longitude}")

        self.i += 1

def main(args=None):
    
    rclpy.init(args=args)
    gps_publisher = GPSPublisher()
    rclpy.spin(gps_publisher)
    gps_publisher.destroy_node() # Destroy the node explicitly
    rclpy.shutdown()

if __name__ == '__main__':
    main()
