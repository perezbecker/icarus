import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600) 

while True:
	read_serial=ser.readline()
	print read_serial
	#time.sleep(0.3)

	
