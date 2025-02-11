import time
import serial
import adafruit_bno055
import board
import adafruit_gps
from collections import namedtuple

# IMU Sensor class
class IMUSensor:
    def __init__(self):
        i2c = board.I2C()
        self.sensor = adafruit_bno055.BNO055_I2C(i2c)
        self.sensor.offsets_magnetometer = (-25, -132, -330)
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

        return quaternion
    
    def calibrateCheck(self):
        time.sleep(.5)
        cal = self.sensor.calibration_status
        message = f"Calibration (sys:{cal[0]}, gyro:{cal[1]}, accel:{cal[2]}, mag:{cal[3]})"
        calibrated = False
        if(cal[0] > -1 and cal[1] > -1 and cal[2] > -1 and cal[3] > -1):
            calibrated = True

        return calibrated, message


# GPS Sensor class
class GPSSensor:
    def __init__(self):
        # Get GPS device by name
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


def main():
    # Initialize IMU and GPS sensors
    imu_sensor = IMUSensor()
    gps_sensor = GPSSensor()

    # Wait for IMU to calibrate
    while True:
        calibrated, cal_message = imu_sensor.calibrateCheck()
        print(f"Calibration status: {cal_message}")
        if calibrated:
            break
        time.sleep(1)

    # Main loop to continuously get sensor data
    i = 0
    while True:
        # Update GPS data
        gps_sensor.update()
        
        # Print IMU data (Euler angles and quaternion)
        euler_angles = imu_sensor.get_euler_angles()
        quaternion = imu_sensor.get_quaternion()
        print(f"IMU - Euler Angles: {euler_angles}")
        print(f"IMU - Quaternion: {quaternion}")
        
        # Print GPS data
        if gps_sensor.has_new_data():
            gps_data = gps_sensor.get_data()
            print(f"GPS Data: {gps_data} {i}")
            i += 1

        time.sleep(1)  # Delay to control the polling frequency


if __name__ == "__main__":
    main()
