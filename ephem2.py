#ephem2.py
#Added update for all 4 motors
#String format for python 3.5

import ephem
import math
import time

counter = 1 #number of 5 minute updates

# Calculate the number of steps per degree
stepCircle = 4100 #number of steps to turn 360
steps_1_deg = stepCircle/360

old_m0_stepCount = 0 #old SunAlt
cur_m0_stepCount = 0 #current SunAlt
old_m1_stepCount = 0 #old sunAz
cur_m1_stepCount = 0 #current sunAz
old_m2_stepCount = 0 #old moonAz
cur_m2_stepCount = 0 #current moonAz
old_m3_stepCount = 0 #old moonAlt
cur_m3_stepCount = 0 #current moonAlt

def m0_update(): #sunAlt
  global old_m0_stepCount
  global cur_m0_stepCount
  cur_m0_stepCount = round(sunAlt * steps_1_deg)
  m0_takeSteps = cur_m0_stepCount - old_m0_stepCount
  print('m0 stepCount (old: {}, cur: {}, dif: {})'.format(old_m0_stepCount,cur_m0_stepCount,m0_takeSteps))
  old_m0_stepCount = cur_m0_stepCount

def m1_update(): #sunAz
  global old_m1_stepCount
  #print('old_m1_stepCount: {}'.format(old_m1_stepCount))
  global cur_m1_stepCount
  cur_m1_stepCount = round(sunAz * steps_1_deg)
  #print('cur_m1_stepCount: {}'.format(cur_m1_stepCount))
  m1_takeSteps = cur_m1_stepCount - old_m1_stepCount
  #print('m1_takeSteps: {}'.format(m1_takeSteps))
  print('m1 stepCount (old: {}, cur: {}, dif: {})'.format(old_m1_stepCount,cur_m1_stepCount,m1_takeSteps))
  old_m1_stepCount = cur_m1_stepCount

def m2_update(): #moonAz
  global old_m2_stepCount
  global cur_m2_stepCount
  cur_m2_stepCount = round(moonAz * steps_1_deg)
  m2_takeSteps = cur_m2_stepCount - old_m2_stepCount
  print('m2 stepCount (old: {}, cur: {}, dif: {})'.format(old_m2_stepCount,cur_m2_stepCount,m2_takeSteps))
  old_m2_stepCount = cur_m2_stepCount

def m3_update(): #moonAlt
  global old_m3_stepCount
  global cur_m3_stepCount
  cur_m3_stepCount = round(moonAlt * steps_1_deg)
  m3_takeSteps = cur_m3_stepCount - old_m3_stepCount
  print('m3 stepCount (old: {}, cur: {}, dif: {})'.format(old_m3_stepCount,cur_m3_stepCount,m3_takeSteps))
  old_m3_stepCount = cur_m3_stepCount

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
  print('Sun  Altitude (m0):',sunAlt)
  print('Sun   Azimuth (m1):',sunAz)
  print('Moon  Azimuth (m2):',moonAz)
  print('Moon Altitude (m3):',moonAlt)
  m0_update()
  m1_update()
  m2_update()
  m3_update()
  
  difAlt = abs(sunAlt-moonAlt)
  difAz = abs(sunAz-moonAz)
  
  print('SUN-MOON DIF: alt:',difAlt,'az:',difAz)
  print()
  
  # Write dif alt and dif az to log file every 3 hours
  dif_list = [time.ctime(), str(difAlt), str(difAz)]
  write_str = ', '.join(dif_list)
  #print(write_str)
  with open('alt_az_dif_log', 'at') as f_out:
    f_out.write(write_str)
   
  time.sleep(300)
