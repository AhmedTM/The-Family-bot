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
       # pwm1 = GPIO.PWM(12,100)
       # pwm2 = GPIO.PWM(32,100)
        return;

''' def connect():
        HOST = '192.168.1.108' #We're keeping things local, so use localhost's IP!
        PORT = '334411' #Random port above 1024 (unprivileged). Read as EE 4 All
        
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
        return sock; '''
def mainfunk():
        host = '192.168.1.5'
        port = int(2010)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('socket created')
        s.bind((host,port))
        print('socket binded')
        s.listen(1)
        print('socket connected')

        GPIO.setwarnings(False)
        GPIO.cleanup()
        Init_Motors()
        pwm1 = GPIO.PWM(12,100)
        pwm2 = GPIO.PWM(32,100)


        while True:
                print('hello from infinite loop')
		
                while True:
                        conn, addr = s.accept()
                        print('socket accepted')
                        data = conn.recv(1024) #Grab 1024 bytes from the socket
                        print(str(data))
                        strdata = str(data)
                        #cmd = json.loads(strdata)
                        print('please let me know')
                        if (strdata == "b'end_session'"):
                            break
                        elif strdata == "b'F'" :

                           # GPIO.setmode(GPIO.BOARD)
                           # GPIO.setup(12,GPIO.OUT)
                           # GPIO.setup(32,GPIO.OUT)
                           # GPIO.setup(7,GPIO.OUT)
                           # GPIO.setup(33,GPIO.OUT)
                            GPIO.output(7,0)
                            GPIO.output(33,0)
                            pwm1.start(0)
                            pwm2.start(0)
                            time.sleep(1)
                            pwm1.start(80)
                            pwm2.start(80)

                        elif strdata == "b'B'" :
                            GPIO.output(7,1)
                            GPIO.output(33,1)
                            pwm1.start(0)
                            pwm2.start(0)
                            time.sleep(1)
                            pwm1.start(80)
                            pwm2.start(80)
                        elif strdata == "b'R'" :
                            GPIO.output(7,0)
                            GPIO.output(33,1)
                            pwm1.start(0)
                            pwm2.start(0)
                            time.sleep(1)
                            pwm1.start(80)
                            pwm2.start(80)
                        elif strdata == "b'L'" :
                            GPIO.output(7,1)
                            GPIO.output(33,0)
                            pwm1.start(0)
                            pwm2.start(0)
                            time.sleep(1)
                            pwm1.start(80)
                            pwm2.start(80)
                        elif strdata == "b'S'" :
                            pwm1.stop()
                            pwm2.stop()
                            
                        #ret_jason = jason.dumps(retval)
                        #conn.send(ret_jason)
                conn.close()

if __name__=="__main__":
        print('pyserver running directly')
        mainfunk()
