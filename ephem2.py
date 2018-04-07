# ephem2.py
# Runs every 5 minutes

import ephem
import math
import time 

home = ephem.Observer()
home.lat = ephem.degrees('51:54:39')
home.lon = ephem.degrees('4:30:1')

while True:
  sun = ephem.Sun()
  moon = ephem.Moon()
  sun.compute(home)
  moon.compute(home)
  
  # printing in radians
  #print('Sun   Azimuth:',sun.az)
  #print('Sun  Altitude:',sun.alt)
  #print('Moon  Azimuth:',moon.az)
  #print('Moon Altitude:',moon.alt)
  
  sunAz = int(math.degrees(sun.az))
  sunAlt = int(math.degrees(sun.alt))
  moonAz = int(math.degrees(moon.az))
  moonAlt = int(math.degrees(moon.alt))
  
  print('Sun   Azimuth:',sunAz)
  print('Sun  Altitude:',sunAlt)
  print('Moon  Azimuth:',moonAz)
  print('Moon Altitude:',moonAlt)

  time.sleep(30)

