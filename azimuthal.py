#source: http://computers.tutsplus.com/tutorials/controlling-dc-motors-using-python-with-a-raspberry-pi--cms-20051

import RPi.GPIO as GPIO
from time import sleep

AzimuthPin1 = 14
AzimuthPin2 = 15

PolarPin1 = 20
PolarPin2 = 21

CalibPin = -1 #think about this

timeOfAzimuth = 0

def calibrate(what=0):
  '''0 is both, 1 is azimuth and 2 is polar'''

def setupPins():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(AzimuthPin1,GPIO.OUT)
  GPIO.setup(AzimuthPin2,GPIO.OUT)
  GPIO.setup(PolarPin1,GPIO.OUT)
  GPIO.setup(PolarPin2,GPIO.OUT)

def fireA(mode, q):
  '''mode 0 means angle, mode 1 means time'''
  if mode is 0:
    setupPins()
    GPIO.output(AzimuthPin1,GPIO.HIGH)
    GPIO.setup(AzimuthPin2,GPIO.LOW)
    sleep(q/360.0 * timeOfAzimuth)
    GPIO.output(AzimuthPin1,GPIO.LOW)
    GPIO.setup(AzimuthPin2,GPIO.LOW)
  else:
    setupPins()
    GPIO.output(AzimuthPin1,GPIO.HIGH)
    GPIO.setup(AzimuthPin2,GPIO.LOW)
    sleep(q)
    GPIO.output(AzimuthPin1,GPIO.LOW)
    GPIO.setup(AzimuthPin2,GPIO.LOW)
  GPIO.cleanup()
  
def twos():
  setupPins()
  GPIO.output(AzimuthPin1,GPIO.HIGH)
  GPIO.setup(AzimuthPin2,GPIO.LOW)
  sleep(q/360.0 * timeOfAzimuth)
  GPIO.output(AzimuthPin1,GPIO.LOW)
  GPIO.setup(AzimuthPin2,GPIO.LOW)
  GPIO.cleanup()

def reverse_spin():
  GPIO.setmode(GPIO.BCM)
  GPIO.cleanup()
