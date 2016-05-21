#source: http://computers.tutsplus.com/tutorials/controlling-dc-motors-using-python-with-a-raspberry-pi--cms-20051

import RPi.GPIO as GPIO
from time import sleep

def two_second_spin():
  GPIO.setmode(GPIO.BOARD)
   
  Motor1A = 16
  Motor1B = 18
  Motor1E = 22
   
  GPIO.setup(Motor1A,GPIO.OUT)
  GPIO.setup(Motor1B,GPIO.OUT)
  GPIO.setup(Motor1E,GPIO.OUT)
   
  print "Turning motor on"
  GPIO.output(Motor1A,GPIO.HIGH)
  GPIO.output(Motor1B,GPIO.LOW)
  GPIO.output(Motor1E,GPIO.HIGH)
   
  sleep(2)
   
  print "Stopping motor"
  GPIO.output(Motor1E,GPIO.LOW)
   
  GPIO.cleanup()

def reverse_spin():
  GPIO.setmode(GPIO.BOARD)
   
  Motor1A = 16
  Motor1B = 18
  Motor1E = 22
   
  GPIO.setup(Motor1A,GPIO.OUT)
  GPIO.setup(Motor1B,GPIO.OUT)
  GPIO.setup(Motor1E,GPIO.OUT)
   
  print "Going forwards"
  GPIO.output(Motor1A,GPIO.HIGH)
  GPIO.output(Motor1B,GPIO.LOW)
  GPIO.output(Motor1E,GPIO.HIGH)
   
  sleep(2)
   
  print "Going backwards"
  GPIO.output(Motor1A,GPIO.LOW)
  GPIO.output(Motor1B,GPIO.HIGH)
  GPIO.output(Motor1E,GPIO.HIGH)
   
  sleep(2)
   
  print "Now stop"
  GPIO.output(Motor1E,GPIO.LOW)
   
  GPIO.cleanup()
