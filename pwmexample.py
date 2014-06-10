#!/usr/bin/env python

## This is a modified version of one of the PWM examples provided as part of the RPi.GPIO project
## Can't find original source at the moment - but I'll update when I track it down - David L

import time
import RPi.GPIO as GPIO

pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 50) 
p.start(0)
try:
    while 1:
	## this loop increases the duty cycle in increments of 5
	## as the duty cycle increases the pin stays high for longer
	## this makes the LED gradually brighten
        for dc in range(0, 101, 5):
            print dc
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
	## this loop does the opposite
	## it decrements the duty cycle by 5 for each pass through the loop
	## as the duty cycle decreases the pin stays high for a shorter period
	## this makes the LED gradually dim
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
