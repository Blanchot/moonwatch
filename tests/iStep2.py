#iStep2.py
#Load from CLI: python3 -i iStep2.py
#To calibrate motors: calibrate(amount,motor)
#To autocalibrate: autocalibrate()
#Motor control based on code from here: 
#http://ingeniapp.com/en/stepper-motor-control-with-raspberry-pi/

#Last update: added autocalibration code

import time
import sys
import RPi.GPIO as GPIO

import ephem #for ephem code
import math #for ephem code

m0pas = 1
m1pas = 1
m2pas = 1
m3pas = 1
m0 = 0 #m0 counter (right altitude)
m1 = 0 #m1 counter (right azimuth)
m2 = 0 #m2 counter (left azimuth)
m3 = 0 #m3 counter (left altitude)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#motor 0 (m0 right altitude)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
#motor 1 (m1 right azimuth)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
#motor 2 (m2 left azimuth)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
#motor 3 (m3 left altitude)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

def m0step_8 (p):
  if p==0:
    GPIO.output(22,0)
    GPIO.output(27,0)
    GPIO.output(18,0)
    GPIO.output(17,0)
  if p==1:
    GPIO.output(22,1)
    GPIO.output(27,0)
    GPIO.output(18,0)
    GPIO.output(17,0)
  if p==2:
    GPIO.output(22,1)
    GPIO.output(27,1)
    GPIO.output(18,0)
    GPIO.output(17,0)
  if p==3:
    GPIO.output(22,0)
    GPIO.output(27,1)
    GPIO.output(18,0)
    GPIO.output(17,0)
  if p==4:
    GPIO.output(22,0)
    GPIO.output(27,1)
    GPIO.output(18,1)
    GPIO.output(17,0)
  if p==5:
    GPIO.output(22,0)
    GPIO.output(27,0)
    GPIO.output(18,1)
    GPIO.output(17,0)
  if p==6:
    GPIO.output(22,0)
    GPIO.output(27,0)
    GPIO.output(18,1)
    GPIO.output(17,1)
  if p==7:
    GPIO.output(22,0)
    GPIO.output(27,0)
    GPIO.output(18,0)
    GPIO.output(17,1)
  if p==8:
    GPIO.output(22,1)
    GPIO.output(27,0)
    GPIO.output(18,0)
    GPIO.output(17,1)

def m1step_8 (p):
  if p==0:
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,0)
    GPIO.output(4,0)
  if p==1:
    GPIO.output(23,1)
    GPIO.output(24,0)
    GPIO.output(25,0)
    GPIO.output(4,0)
  if p==2:
    GPIO.output(23,1)
    GPIO.output(24,1)
    GPIO.output(25,0)
    GPIO.output(4,0)
  if p==3:
    GPIO.output(23,0)
    GPIO.output(24,1)
    GPIO.output(25,0)
    GPIO.output(4,0)
  if p==4:
    GPIO.output(23,0)
    GPIO.output(24,1)
    GPIO.output(25,1)
    GPIO.output(4,0)
  if p==5:
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,1)
    GPIO.output(4,0)
  if p==6:
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,1)
    GPIO.output(4,1)
  if p==7:
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,0)
    GPIO.output(4,1)
  if p==8:
    GPIO.output(23,1)
    GPIO.output(24,0)
    GPIO.output(25,0)
    GPIO.output(4,1)

def m2step_8 (p):
  if p==0:
    GPIO.output(5,0)
    GPIO.output(6,0)
    GPIO.output(12,0)
    GPIO.output(13,0)
  if p==1:
    GPIO.output(5,1)
    GPIO.output(6,0)
    GPIO.output(12,0)
    GPIO.output(13,0)
  if p==2:
    GPIO.output(5,1)
    GPIO.output(6,1)
    GPIO.output(12,0)
    GPIO.output(13,0)
  if p==3:
    GPIO.output(5,0)
    GPIO.output(6,1)
    GPIO.output(12,0)
    GPIO.output(13,0)
  if p==4:
    GPIO.output(5,0)
    GPIO.output(6,1)
    GPIO.output(12,1)
    GPIO.output(13,0)
  if p==5:
    GPIO.output(5,0)
    GPIO.output(6,0)
    GPIO.output(12,1)
    GPIO.output(13,0)
  if p==6:
    GPIO.output(5,0)
    GPIO.output(6,0)
    GPIO.output(12,1)
    GPIO.output(13,1)
  if p==7:
    GPIO.output(5,0)
    GPIO.output(6,0)
    GPIO.output(12,0)
    GPIO.output(13,1)
  if p==8:
    GPIO.output(5,1)
    GPIO.output(6,0)
    GPIO.output(12,0)
    GPIO.output(13,1)

def m3step_8 (p):
  if p==0:
    GPIO.output(19,0)
    GPIO.output(16,0)
    GPIO.output(26,0)
    GPIO.output(20,0)
  if p==1:
    GPIO.output(19,1)
    GPIO.output(16,0)
    GPIO.output(26,0)
    GPIO.output(20,0)
  if p==2:
    GPIO.output(19,1)
    GPIO.output(16,1)
    GPIO.output(26,0)
    GPIO.output(20,0)
  if p==3:
    GPIO.output(19,0)
    GPIO.output(16,1)
    GPIO.output(26,0)
    GPIO.output(20,0)
  if p==4:
    GPIO.output(19,0)
    GPIO.output(16,1)
    GPIO.output(26,1)
    GPIO.output(20,0)
  if p==5:
    GPIO.output(19,0)
    GPIO.output(16,0)
    GPIO.output(26,1)
    GPIO.output(20,0)
  if p==6:
    GPIO.output(19,0)
    GPIO.output(16,0)
    GPIO.output(26,1)
    GPIO.output(20,1)
  if p==7:
    GPIO.output(19,0)
    GPIO.output(16,0)
    GPIO.output(26,0)
    GPIO.output(20,1)
  if p==8:
    GPIO.output(19,1)
    GPIO.output(16,0)
    GPIO.output(26,0)
    GPIO.output(20,1)

def m0steps_8(value):
  #print(value)
  global m0pas
  global m0 #m0 counter (right altitude)
  if(value>0): #reversed original code- was if(value<0):
    for i in range (0,abs(value)):
      m0step_8(m0pas)
      time.sleep(0.01)
      m0+=1 #add 1 to counter (reversed)
      m0pas+=1
      if(m0pas>=9):
        m0pas=1;
  else:
    for i in range (0,abs(value)):
      m0step_8(m0pas)
      time.sleep(0.01)
      m0-=1 #subtract 1 from counter (reversed)
      if(m0pas==1):
        m0pas=9;
      m0pas-=1
  m0step_8(0)

def m1steps_8(value):
  #print(value)
  global m1pas
  global m1 #m1 counter (right azimuth)
  if(value>0): #reversed original code- was if(value<0):
    for i in range (0,abs(value)):
      m1step_8(m1pas)
      time.sleep(0.01)
      m1+=1 #add 1 to counter (reversed)
      m1pas+=1
      if(m1pas>=9):
        m1pas=1;
  else:
    for i in range (0,abs(value)):
      m1step_8(m1pas)
      time.sleep(0.01)
      m1-=1 #subtract 1 from counter (reversed)
      if(m1pas==1):
        m1pas=9;
      m1pas-=1
  m1step_8(0)

def m2steps_8(value):
  #print(value)
  global m2pas
  global m2 #m2 counter (left azimuth)
  if(value>0): #reversed original code- was if(value<0):
    for i in range (0,abs(value)):
      m2step_8(m2pas)
      time.sleep(0.01)
      m2+=1 #add 1 to counter (reversed)
      m2pas+=1
      if(m2pas>=9):
        m2pas=1;
  else:
    for i in range (0,abs(value)):
      m2step_8(m2pas)
      time.sleep(0.01)
      m2-=1 #subtract 1 from counter (reversed)
      if(m2pas==1):
        m2pas=9;
      m2pas-=1
  m2step_8(0)

def m3steps_8(value):
  #print(value)
  global m3pas
  global m3 #m3 counter (left altitude)
  if(value>0): #reversed original code- was if(value<0):
    for i in range (0,abs(value)):
      m3step_8(m3pas)
      time.sleep(0.01)
      m3+=1 #add 1 to counter (reversed)
      m3pas+=1
      if(m3pas>=9):
        m3pas=1;
  else:
    for i in range (0,abs(value)):
      m3step_8(m3pas)
      time.sleep(0.005)
      m3-=1 #subtract 1 from counter (reversed)
      if(m3pas==1):
        m3pas=9;
      m3pas-=1
  m3step_8(0)

def calibrate(amount,motor): #calibrate each motor by hand
  st = amount
  if motor == 0:
    m0steps_8(st)
  elif motor == 1:
    m1steps_8(st)
  elif motor == 2:
    m2steps_8(st)
  elif motor == 3:
    m3steps_8(st)
  else:
    print("motor selector out of range")

def autocalibrate(): #reverse 'last positions' for autocalibration
  f_in = open('last_positions', 'rt') 
  read_str = f_in.read()
  f_in.close()
  
  read_pos_list = read_str.split()
  print(read_pos_list)
  # turn each element of the list into an int and reverse its sign
  recalib_m0 = (int(read_pos_list[0])) * -1
  recalib_m1 = (int(read_pos_list[1])) * -1
  recalib_m2 = (int(read_pos_list[2])) * -1
  recalib_m3 = (int(read_pos_list[3])) * -1
  m0steps_8(recalib_m0)
  m1steps_8(recalib_m1)
  m2steps_8(recalib_m2)
  m3steps_8(recalib_m3)

'''
EPHEM CALCULATIONS
'''
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

def m0_update(sunAlt): #sunAlt
  global old_m0_stepCount
  global cur_m0_stepCount
  cur_m0_stepCount = round(sunAlt * steps_1_deg)
  m0_takeSteps = cur_m0_stepCount - old_m0_stepCount
  m0steps_8(m0_takeSteps)
  print('sunAlt (m0): {}, steps (old: {}, cur: {}, dif: {})'.format(sunAlt, old_m0_stepCount,cur_m0_stepCount,m0_takeSteps))
  old_m0_stepCount = cur_m0_stepCount

def m1_update(sunAz): #sunAz
  global old_m1_stepCount
  global cur_m1_stepCount
  cur_m1_stepCount = round(sunAz * steps_1_deg)
  m1_takeSteps = cur_m1_stepCount - old_m1_stepCount
  m1steps_8(m1_takeSteps)
  print('sunAz (m1): {}, steps (old: {}, cur: {}, dif: {})'.format(sunAz, old_m1_stepCount,cur_m1_stepCount,m1_takeSteps))
  old_m1_stepCount = cur_m1_stepCount

def m2_update(moonAz): #moonAz
  global old_m2_stepCount
  global cur_m2_stepCount
  cur_m2_stepCount = round(moonAz * steps_1_deg)
  m2_takeSteps = cur_m2_stepCount - old_m2_stepCount
  m2steps_8(m2_takeSteps)
  print('moonAz (m2): {}, steps (old: {}, cur: {}, dif: {})'.format(moonAz, old_m2_stepCount,cur_m2_stepCount,m2_takeSteps))
  old_m2_stepCount = cur_m2_stepCount

def m3_update(moonAlt): #moonAlt
  global old_m3_stepCount
  global cur_m3_stepCount
  cur_m3_stepCount = round(moonAlt * steps_1_deg)
  m3_takeSteps = cur_m3_stepCount - old_m3_stepCount
  m3steps_8(m3_takeSteps)
  print('moonAlt (m3): {}, steps (old: {}, cur: {}, dif: {})'.format(moonAlt, old_m3_stepCount,cur_m3_stepCount,m3_takeSteps))
  old_m3_stepCount = cur_m3_stepCount
  

def run():
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
    
    # calculating in degrees
    sunAz = int(math.degrees(sun.az))
    sunAlt = int(math.degrees(sun.alt))
    moonAz = int(math.degrees(moon.az))
    moonAlt = int(math.degrees(moon.alt))
    
    print(time.ctime())
    #print('Sun  Altitude (m0):',sunAlt)
    #print('Sun   Azimuth (m1):',sunAz)
    #print('Moon  Azimuth (m2):',moonAz)
    #print('Moon Altitude (m3):',moonAlt)
    
    m0_update(sunAlt)
    m1_update(sunAz)
    m2_update(moonAz)
    m3_update(moonAlt)
    print() #empty line after printing update info for each motor
    
    #Code to (over)write 'last positions' to a file which
    #can be read in again as part of the calibration function
    pos_list = [str(sunAlt), str(sunAz), str(moonAz), str(moonAlt)]
    write_str = ' '.join(pos_list)
    #print(write_str)
    with open('last_positions', 'wt') as f_out:
      f_out.write(write_str)
    
    time.sleep(300)


'''  
if __name__ == "__main__":
  
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  #motor 0 (m0 right altitude)
  GPIO.setup(22, GPIO.OUT)
  GPIO.setup(27, GPIO.OUT)
  GPIO.setup(18, GPIO.OUT)
  GPIO.setup(17, GPIO.OUT)
  #motor 1 (m1 right azimuth)
  GPIO.setup(23, GPIO.OUT)
  GPIO.setup(24, GPIO.OUT)
  GPIO.setup(25, GPIO.OUT)
  GPIO.setup(4, GPIO.OUT)
  #motor 2 (m2 left azimuth)
  GPIO.setup(5, GPIO.OUT)
  GPIO.setup(6, GPIO.OUT)
  GPIO.setup(12, GPIO.OUT)
  GPIO.setup(13, GPIO.OUT)
  #motor 3 (m3 left altitude)
  GPIO.setup(19, GPIO.OUT)
  GPIO.setup(16, GPIO.OUT)
  GPIO.setup(26, GPIO.OUT)
  GPIO.setup(20, GPIO.OUT)

  #step_8(0) #changed in original code from step_4(0)
  pas=1
  print(len(sys.argv))
  if(len(sys.argv)<2):
    print("Parameter error")
    print("Usage: sudo python steeper.py val mode")
    print("val = step number >0clockwise, <0 anticlockwise ")
    print("mode = 0: 8 phase   2: 1 phase ")
  else:
    st=int(sys.argv[1])
    if(len(sys.argv)==3 and sys.argv[2]=="0"):
      print("m0: right altitude")
      m0steps_8(st)
    elif(len(sys.argv)==3 and sys.argv[2]=="1"):
      print("m1: right azimuth")
      m1steps_8(st)
    elif(len(sys.argv)==3 and sys.argv[2]=="2"):
      print("m2: left azimuth")
      m2steps_8(st)
    elif(len(sys.argv)==3 and sys.argv[2]=="3"):
      print("m3: left altitude")
      m3steps_8(st)
    else:
      print("motor selection arg out of range")
  GPIO.cleanup()
'''

