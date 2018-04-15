#ephem2.py
#Test sunAz update

import ephem
import math
import time 

# Calculate the number of steps per degree
stepCircle = 4100 #number of steps to turn 360
steps_1_deg = stepCircle/360

old_m1_stepCount = 0 #old sunAz
cur_m1_stepCount = 0 #current sunAz

def init():
  global cur_m1_stepCount
  cur_m1_stepCount = 0 #number of steps clockwise

def m1_update(): #sunAz
  global old_m1_stepCount
  print(f'old_m1_stepCount: {old_m1_stepCount}')
  global cur_m1_stepCount
  print(f'cur_m1_stepCount: {cur_m1_stepCount}')
  #curAz = int(input('Current Azimuth: '))
  #print(f'Current Azimuth is: {curAz}')
  cur_m1_stepCount = round(sunAz * steps_1_deg)
  print(f'cur_m1_stepCount: {cur_m1_stepCount}')
  m1_takeSteps = cur_m1_stepCount - old_m1_stepCount
  print(f'm1_takeSteps: {m1_takeSteps}')
  old_m1_stepCount = cur_m1_stepCount

# Runs every 5 minutes

while True:
  # Need to create a new Observer object for each current time 
  home = ephem.Observer()
  home.lat = ephem.degrees('51:54:39')
  home.lon = ephem.degrees('4:30:1')

  sun = ephem.Sun()
  moon = ephem.Moon()
  sun.compute(home)
  moon.compute(home)
  
  # printing in radians
  #print('Sun   Azimuth:',sun.az)
  #print('Sun  Altitude:',sun.alt)
  #print('Moon  Azimuth:',moon.az)
  #print('Moon Altitude:',moon.alt)
  
  # printing in degrees
  sunAz = int(math.degrees(sun.az))
  sunAlt = int(math.degrees(sun.alt))
  moonAz = int(math.degrees(moon.az))
  moonAlt = int(math.degrees(moon.alt))
  
  print(time.ctime())
  print('Sun   Azimuth:',sunAz)
  print('Sun  Altitude:',sunAlt)
  print('Moon  Azimuth:',moonAz)
  print('Moon Altitude:',moonAlt)
  print()
  m1_update()
  
  time.sleep(300)
