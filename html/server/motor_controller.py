import RPi.GPIO as GPIO
import time
def Motors_Dir( motors, dir ):
	if dir == 12 :
		GPIO.output(motors,1)
		print('foward')
	elif dir == 21 :
		GPIO.output(motors,0)
		print('backward')
	return;
def Init_Motors():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(12,GPIO.OUT)
	GPIO.setup(32,GPIO.OUT)
	GPIO.setup(7,GPIO.OUT)
	GPIO.setup(33,GPIO.OUT)

	return;
def Motor_Run( cmd, speed ):
	MotorsR = GPIO.PWM(12,100)
	MotorsL = GPIO.PWM(32,100)
	print('pins initialized')
	Motors_Dir( 7, 12 )
	Motors_Dir( 33, 12 )
	print('direction intialized')
	MotorsR.start(0)	 
	MotorsL.start(0)
	print('pwm started dutycycle 0')
	time.sleep(1)
	
	if speed>100 :
		speed = 100
	if speed<0 :
		speed = 0
	if cmd == 8 :
		Motors_Dir( 7, 12 )
		Motors_Dir( 33, 12 )
		MotorsR.start(speed)	 
		MotorsL.start(speed)
	elif cmd == 2 :
		Motors_Dir( 7, 21 )
		Motors_Dir( 33, 21 )
		MotorsR.start(speed)	 
		MotorsL.start(speed)
	elif cmd == 6 :
		Motors_Dir( 7, 21 )
		Motors_Dir( 33, 12 )
		MotorsR.start(speed)	 
		MotorsL.start(speed)
	elif cmd == 4 :
		Motors_Dir( 7, 12 )
		Motors_Dir( 33, 21 )
		MotorsR.start(speed)	 
		MotorsL.start(speed)
	elif cmd == 5 :
		#Motors_Dir( 12, "CW" )
		#Motors_Dir( 18, "CW" )
		MotorsR.stop()	 
		MotorsL.stop()

	return;
GPIO.setwarnings(False)
GPIO.cleanup()
forw = 8
back = 2
Init_Motors()
#Motor_Run(forw,int(50))
#time.sleep(5)
#Motor_Run( "STOP", 50 )
#time.sleep(1)
#Motor_Run(back,int(50))
GPIO.output(7,0)
GPIO.output(33,0)
pwm1 = GPIO.PWM(12,100)
pwm2 = GPIO.PWM(32,100)
pwm1.start(0)
pwm2.start(0)
time.sleep(3)
pwm1.start(80)
pwm2.start(80)
time.sleep(5)
pwm1.start(0)
pwm2.start(0)
time.sleep(1)
GPIO.output(7,1)
GPIO.output(33,1)
pwm1.start(80)
pwm2.start(80)
input('Press any button to stop:')
#Motor_Run( 5, (50) )
pwm1.stop()
pwm2.stop()
GPIO.cleanup()
