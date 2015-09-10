import serial
import time
ser = serial.Serial('/dev/ttyUSB1', 9600)
while 1:
	orientation = ser.readline()
	print orientation
	
