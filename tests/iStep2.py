#iStep2.py
#Code from here: http://ingeniapp.com/en/stepper-motor-control-with-raspberry-pi/
#Added count for m1

import time
import sys
import RPi.GPIO as GPIO

pas = 1
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
  print(value)
  global pas
  if(value<0):
    for i in range (0,abs(value)):
      m0step_8(pas)
      time.sleep(0.01)
      pas+=1
      if(pas>=9):
        pas=1;
  else:
    for i in range (0,abs(value)):
      m0step_8(pas)
      time.sleep(0.01)
      if(pas==1):
        pas=9;
      pas-=1
  m0step_8(0)

def m1steps_8(value):
  print(value)
  global pas
  global m1 #m1 counter (right azimuth)
  if(value<0):
    for i in range (0,abs(value)):
      m1step_8(pas)
      time.sleep(0.01)
      m1 -= 1 #subtract 1 from counter
      pas+=1
      if(pas>=9):
        pas=1;
  else:
    for i in range (0,abs(value)):
      m1step_8(pas)
      time.sleep(0.01)
      m1 += 1 #add 1 to counter
      if(pas==1):
        pas=9;
      pas-=1
  m1step_8(0)

def m2steps_8(value):
  print(value)
  global pas 
  if(value<0):
    for i in range (0,abs(value)):
      m2step_8(pas)
      time.sleep(0.01)
      pas+=1
      if(pas>=9):
        pas=1;
  else:
    for i in range (0,abs(value)):
      m2step_8(pas)
      time.sleep(0.01)
      if(pas==1):
        pas=9;
      pas-=1
  m2step_8(0)

def m3steps_8(value):
  print(value)
  global pas 
  if(value<0):
    for i in range (0,abs(value)):
      m3step_8(pas)
      time.sleep(0.01)
      pas+=1
      if(pas>=9):
        pas=1;
  else:
    for i in range (0,abs(value)):
      m3step_8(pas)
      time.sleep(0.005)
      if(pas==1):
        pas=9;
      pas-=1
  m3step_8(0)

def watch(amount,motor):
  #pas = 1
  st = amount
  if motor == 0:
    #print("m0: right altitude")
    m0steps_8(st)
  elif motor == 1:
    #print("m1: right azimuth")
    m1steps_8(st)
  elif motor == 2:
    #print("m2: left azimuth")
    m2steps_8(st)
  elif motor == 3:
    #print("m3: left altitude")
    m3steps_8(st)
  else:
    print("motor selector out of range")
  #GPIO.cleanup()

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

