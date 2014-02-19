#!/usr/bin/env python
import RPi.GPIO as GPIO
import os
import time

inPort = 0
ledPort = 1
sonarTrigPort = 4
sonarEchoPort = 17
lastState = False

# Setup pin numbering according to broadcom pin specs. 
# Alternatively use GPIO.BOARD to use board pin numbering
GPIO.setmode(GPIO.BCM)

# Select if pins ar input or output
GPIO.setup(inPort, GPIO.IN)
GPIO.setup(ledPort, GPIO.OUT)
GPIO.setup(sonarTrigPort, GPIO.OUT)
GPIO.setup(sonarEchoPort,GPIO.IN)
GPIO.output(sonarTrigPort,GPIO.LOW)

# Sonar might require this sleep time to start properly
#time.sleep(0.3)

while True:
    # Button/LED handling
    state = GPIO.input(inPort)
    if (state == False):
        if (state != lastState):
            print("pushed")
        GPIO.output(ledPort, GPIO.HIGH)
        lastState = False
    else: 
        if (state != lastState):
            print("Released")
            GPIO.output(ledPort, GPIO.LOW)
            lastState = True

    # Sonar handling
    timeOn = 0
    timeOff = 0
    intTimeout = 2100
    
    # Set sonar trigpin high for 10 us
    GPIO.output(sonarTrigPort,GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(sonarTrigPort,False)
    
    # Wait for echo pin to go low, then start timer
    while GPIO.input(sonarEchoPort) == GPIO.LOW and intTimeout > 0:
        intTimeout = intTimeout - 1
    timeOn = time.time()
    
    # Enter here if timeout has not occured
    if intTimeout > 0:
        intTimeout = 2100
        # Wait for echo pin to go high. Then stop timer.
        while GPIO.input(sonarEchoPort) == GPIO.HIGH and intTimeout > 0:
            intTimeout = intTimeout - 1
        timeOff = time.time()
    
        if intTimeout > 0: 
            elapsed = timeOff-timeOn
            distance = (elapsed * 34000)/2;
            print(distance)
            
            if distance > 5:
                GPIO.output(ledPort, GPIO.HIGH)
            else: 
                GPIO.output(ledPort, GPIO.LOW)
        time.sleep(0.2)