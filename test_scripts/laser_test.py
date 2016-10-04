#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# turn on light for 20 seconds when button pushed

# we will use the pin numbering of the SoC, so our pin numbers in the code are
# the same as the pin numbers on the gpio headers

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

GPIO.output(12, False)

try:
  GPIO.output(12, True)
  time.sleep(20)
  GPIO.output(12, False)

except KeyboardInterrupt:
  GPIO.output(12, False)
