import board
import busio
import struct  # For unpacking binary data
from time import sleep

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Set the I2C address of the Arduino Nano
I2C_ADDRESS = 0x08

# Wait for the I2C bus to be ready
while not i2c.try_lock():
    pass

try:
    while True:
        # Read 4 bytes from the Arduino (2 bytes for each PWM value)
        result = bytearray(4)  # Expect 4 bytes
        i2c.readfrom_into(I2C_ADDRESS, result)
        
        # Unpack the data into two 16-bit integers
        pwm1, pwm2 = struct.unpack('<HH', result)  # '<HH' = little-endian, 2 unsigned shorts
        print(f"PWM 1: {pwm1}, PWM 2: {pwm2}")
        sleep(.1)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    i2c.unlock()
