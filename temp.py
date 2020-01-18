# Loop printing measurements every second.
print('Press Ctrl-C to quit.')
while True:
	temp = sensor.readTempC()
	print('Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp, c_to_f(temp)))
	time.sleep(1.0)
