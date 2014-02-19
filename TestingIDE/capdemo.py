#!/usr/bin/env python

import RPi.GPIO as GPIO, time

timeout = 10000
total = 0
DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

def CapRead(inPin,outPin):
    total = 0
    
    # set Send Pin Register low
    GPIO.setup(outPin, GPIO.OUT)
    GPIO.output(outPin, GPIO.LOW)
    
    # set receivePin Register low to make sure pullups are off 
    GPIO.setup(inPin, GPIO.OUT)
    GPIO.output(inPin, GPIO.LOW)
    GPIO.setup(inPin, GPIO.IN)
    
    # set send Pin High
    GPIO.output(outPin, GPIO.HIGH)
    False
    # while receive pin is LOW AND total is positive value
    while( GPIO.input(inPin) == GPIO.LOW and total < timeout ):
        total+=1
    
    if ( total > timeout ):
        return -2 # total variable over timeout
        
    # set receive pin HIGH briefly to charge up fully - because the while loop above will exit when pin is ~ 2.5V 
    GPIO.setup( inPin, GPIO.OUT )
    GPIO.output( inPin, GPIO.HIGH )
    GPIO.setup( inPin, GPIO.IN )
    
    # set send Pin LOW
    GPIO.output( outPin, GPIO.LOW ) 

    # while receive pin is HIGH  AND total is less than timeout
    while (GPIO.input(inPin)==GPIO.HIGH and total < timeout) :
        total+=1
    
    if ( total >= timeout ):
        return -2
    else:
        return total



# loop
while True:
    total = 0
    print(CapRead(15,14))
    time.sleep(0.5)
# clean before you leave
GPIO.cleanup()