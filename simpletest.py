import time
import board
import busio
import adafruit_sgp30
import Adafruit_MCP9808.MCP9808 as MCP9808
import csv
from datetime import datetime
# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)

# BEGIN MCP9808 (TEMP) CODE SETUP
# /////////////////////////////////////////////////////

# Default constructor for temp sensor will use the default I2C address and pick a default I2C bus.
# Optionally you can override the address and/or bus number:
#sensor = MCP9808.MCP9808(address=0x20, busnum=2)
sensor = MCP9808.MCP9808()

# Initialize communication with the sensor.
sensor.begin()

# BEGIN SGP30 (CO2) CODE SETUP
# /////////////////////////////////////////////////////

# Default constructor for co2 sensor will use the default I2C address and pick a default I2C bus.
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

# Create sgp30 object to interface with 1c2 bus
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

# Initialize sgp30
sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8aae)

# create csv, generate name, define columns
csv_file = open('data.csv', mode='a')
fieldnames = ['Temperature', 'CO2', 'VOC', 'Time']
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
writer.writeheader()
csv_file.close()


# Loop makng measurements every second.
while True:
	temp = sensor.readTempC()
	print('Temperature: {0:0.3F}*C'.format(temp))
	print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	csv_file = open('data.csv', mode='a')
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer.writerow({'Temperature': temp, 'CO2': sgp30.eCO2, 'VOC': sgp30.TVOC, 'Time': current_time})
	csv_file.close()
	time.sleep(1)
