import busio
import adafruit_sgp30
import board


i2c_bus = busio.I2C(board.SCL, board.SDA, frequency = 100000)

sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c_bus)

eCO2, TVOC = sgp30.iaq_measure()
print('eCO2 = %d ppm    TVOC = %d ppb'%(eCO2, TVOC)) 
