import time
import board
import busio
import adafruit_sgp30

# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)

import time

import Adafruit_MCP9808.MCP9808 as MCP9808


# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
	return c * 9.0 / 5.0 + 32.0

# Default constructor will use the default I2C address (0x18) and pick a default I2C bus.
#
# For the Raspberry Pi this means you should hook up to the only exposed I2C bus
# from the main GPIO header and the library will figure out the bus number based
# on the Pi's revision.
#
# For the Beaglebone Black the library will assume bus 1 by default, which is
# exposed with SCL = P9_19 and SDA = P9_20.
sensor = MCP9808.MCP9808()

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
# Optionally you can override the address and/or bus number:
#sensor = MCP9808.MCP9808(address=0x20, busnum=2)

# Initialize communication with the sensor.
sensor.begin()

sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

print("SGP30 serial #", [hex(i) for i in sgp30.serial])

sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8aae)

elapsed_sec = 0

# Loop printing measurements every second.
print('Press Ctrl-C to quit.')
while True:
	temp = sensor.readTempC()
	print('Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp, c_to_f(temp)))
	print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
    time.sleep(1)
    elapsed_sec += 1
    if elapsed_sec > 10:
        elapsed_sec = 0
        print("**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x"
              % (sgp30.baseline_eCO2, sgp30.baseline_TVOC))
