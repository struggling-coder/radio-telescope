import RPi.GPIO as GPIO
from time import sleep
import smbus
import math

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

#These pins are permanent
MotorOutH = 20
MotorOutL = 21

AOutH = 23
AOutL = 24

aXoff = 0
aYoff = 0
aZoff = 0

#Initialization
bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

print "All woken up."
_spin(2, c)
p = raw_input("Spinning AOut clockwise")
if (p == 'n'):
	AOutH=24
	AOutL=23

spin(5, u)	
p = raw_input("Spinning MotorOut up")
if (p == 'n'):
	MotorOutL=20
	MotorOutH=21

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def _angle():
	
    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    ax = accel_xout / 16384.0
    ay = accel_yout / 16384.0
    az = accel_zout / 16384.0

    return math.acos(az/math.sqrt(ax**2 + ay**2 + az**2))*180/math.pi    

def angle():
		
    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    ax = (accel_xout - aXoff) / 16384.0
    ay = (accel_yout - aYoff) / 16384.0
    az = (accel_zout - aZoff) / 16384.0

    return math.acos(az/math.sqrt(ax**2 + ay**2 + az**2))*180/math.pi    


def raw():	
    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    ax = accel_xout / 16384.0
    ay = accel_yout / 16384.0
    az = accel_zout / 16384.0

    return [ax, ay, az]

def calibrate():
	print "Calibration starting"
	avg = 0
	h=20
	for j in range(1, h):
		_spin(1, c)
		sleep(2)
		q = raw()
		a = math.acos(az/math.sqrt(ax**2 + ay**2 + az**2))*180/math.pi
		aXoff += q[0]
		aYoff += q[1]
		aZoff += q[2]	
		avg += a
		print q, a

	aXoff /= h
	aYoff /= h
	aZoff /= h
	avg /= h

	print aXoff, aYoff, aZoff, avg
	return avg

def position(theta):
	k=1
	j = k * (theta - angle())
	spin(j, u)

	#set resolution > stupid mpu6050 error
	while (abs(theta - angle()) > 0.1):
		if theta > angle():
			spin(k * (theta - angle()), u)
		else:
			spin(k * (theta - angle()), d)

def spin(t, o):
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(MotorOutL,GPIO.OUT)
	GPIO.setup(MotorOutH,GPIO.OUT)

	GPIO.output(MotorOutH,GPIO.LOW)
	GPIO.output(MotorOutL,GPIO.LOW)
	
	if o=='u':
		GPIO.output(MotorOutH,GPIO.HIGH)
    	GPIO.output(MotorOutL,GPIO.LOW)
    else: 
    	GPIO.output(MotorOutL,GPIO.HIGH)
    	GPIO.output(MotorOutH,GPIO.LOW)	
    
    sleep(t)
     
    GPIO.output(MotorOutH,GPIO.LOW)
    GPIO.output(MotorOutL,GPIO.LOW)  	 

def _spin(t, o):
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(AOutL,GPIO.OUT)
	GPIO.setup(AOutH,GPIO.OUT)

	GPIO.output(AOutH,GPIO.LOW)
	GPIO.output(AOutL,GPIO.LOW)
	
	if o=='c':
		GPIO.output(AOutH,GPIO.HIGH)
    	GPIO.output(AOutL,GPIO.LOW)
    else: 
    	GPIO.output(AOutL,GPIO.HIGH)
    	GPIO.output(AOutH,GPIO.LOW)	
    
    sleep(t)
     
    GPIO.output(AOutH,GPIO.LOW)
    GPIO.output(AOutL,GPIO.LOW)   
    
