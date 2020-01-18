import busio
import adafruit_sgp30
import board

# Establish bus
i2c_bus = busio.I2C(board.SCL, board.SDA, frequency = 100000)
# pull from library
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c_bus)
# assign variables
eCO2, TVOC = sgp30.iaq_measure()
# eCO2 measured in ppm, TVOC measured in ppb
print('eCO2 = %d ppm    TVOC = %d ppb'%(eCO2, TVOC))
