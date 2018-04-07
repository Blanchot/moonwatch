#!/usr/bin/python
# moonTest.py for testing and calibration

import sys, time
import RPi.GPIO as GPIO

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define BCM GPIO references as follows
#StepPins = [17,18,27,22] #for M0 (alt-1)
#StepPins = [23,24,25,04] #for M1 (az-1)
#StepPins = [13,12,6,5] #for M2 (az-2)
#StepPins = [20,26,16,19] #for M3 (alt-2)

StepPins = [20,26,16,19] #for M3 (alt-2)

# Set all pins as output
for pin in StepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

# Define advanced sequence as shown in manufacturers datasheet
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]

StepCount = len(Seq)
StepDir = -1 # Set to 1 or 2 for anti-clockwise (spindle up) 
             # Set to -1 or -2 for clockwise (spindle up) 

# Initialise variables
StepCounter = 0
TotalSteps = 0
numSteps = 100

# Start main loop
#while TotalSteps <= 4100: #roughly num steps for 360

def run():
  while TotalSteps <= 100:
  for pin in range(0,4):
    xpin=StepPins[pin]# Get GPIO
    if Seq[StepCounter][pin]!=0:
      GPIO.output(xpin, True)
    else:
      GPIO.output(xpin, False)

  StepCounter += StepDir
  TotalSteps += 1 #total step counter
  #print(TotalSteps)

  # If we reach the end of the sequence start again
  if (StepCounter>=StepCount):
    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount+StepDir

  # Wait before moving on
  WaitTime = 10/float(1000)
  time.sleep(WaitTime)

# Will this work here?
GPIO.cleanup()

''' # Weirdly this isn't working but I can set this from the CL
def dir(n):
  global StepDir
  if n == -1:
    StepDir = -1
    print('StepDir = -1 (clockwise)')
  elif n == 1:
    StepDir = 1
    print('StepDir = 1 (anti-clockwise)')
  else:
    print('Param must be either -1 or 1')
    pass
'''
