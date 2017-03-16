#!/usr/bin/env python

import socket
import time
import sys
import json
import RPi.GPIO as GPIO
#import motor_controller

def Init_Motors():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(12,GPIO.OUT)
	GPIO.setup(32,GPIO.OUT)
	GPIO.setup(7,GPIO.OUT)
	GPIO.setup(33,GPIO.OUT)
	pwm1 = GPIO.PWM(12,100)
        pwm2 = GPIO.PWM(32,100)
	return;
    
def connect():
    HOST = '127.0.0.1' #We're keeping things local, so use localhost's IP!
    PORT = '334411' #Random port above 1024 (unprivileged). Read as EE 4 All

    sock = None

    for result in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = result

        try: #Try to create the socket
            sock = socket.socket(af, socktype, proto)
        except socket.error, msg:
            sys.stderr.write('Socket Error Code : ' + str(msg[0]) + ' Message ' + msg[1]) #print error if it fails
            sock = None
            continue

        try: #Try to bind to the socket
            sock.bind(sa)
            sock.listen(1)
        except socket.error, msg:
            sys.stderr.write('Socket bind/listening Error Code : ' + str(msg[0]) + ' Message ' + msg[1])     
            sock.close() #close the socket
            sock = None
            continue
        break

    if sock is None:
        sys.stderr.write("could not open socket")
        sys.exit(1)

GPIO.setwarnings(False)
GPIO.cleanup()
Init_Motors()
while True:
	conn, addr = socket.accept()
	while True:
		data = conn.recv(1024) #Grab 1024 bytes from the socket
		try:
		    cmd = json.loads(data)
		except ValueError:
                    sys.stderr.write("Client sent non-json data. This may occur "+"if client closed socket without sending "+"'end_session' command")
		    break
		if (cmd == "end_session"):
                    break
                elif cmd == "FORWARD" :
                    GPIO.output(7,0)
                    GPIO.output(33,0)
                    pwm1.start(0)
                    pwm2.start(0)
                    time.sleep(1)
                    pwm1.start(80)
                    pwm2.start(80)

                elif cmd == "BACKWARD" :
                    GPIO.output(7,1)
                    GPIO.output(33,1)
                    pwm1.start(0)
                    pwm2.start(0)
                    time.sleep(1)
                    pwm1.start(80)
                    pwm2.start(80)
                elif cmd == "RIGHT" :
                    GPIO.output(7,0)
                    GPIO.output(33,1)
                    pwm1.start(0)
                    pwm2.start(0)
                    time.sleep(1)
                    pwm1.start(80)
                    pwm2.start(80)
                elif cmd == "LEFT" :
                    GPIO.output(7,1)
                    GPIO.output(33,0)
                    pwm1.start(0)
                    pwm2.start(0)
                    time.sleep(1)
                    pwm1.start(80)
                    pwm2.start(80)
                elif cmd == "STOP" :
                    pwm1.stop()
                    pwm2.stop()
                    
		ret_jason = jason.dumps(retval)
		conn.send(ret_jason)
	conn.close()
 
if __name__=="__main__":
    connect()
