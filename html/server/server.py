#!/usr/bin/python

##################################################################
# Name: pyserver.py
# Desc: Opens port 334411 on localhost and waits for connections
# Credit: Source adapted from python server on http://stackoverflow.com/questions/25787944/python-socket-server-to-php-client-socket
#       Changes made to remove logging, fix connect bug (as 
#       described at source), and print to stderr.
# Intent: Modify below to act as a python command server for 
#         your PHP website
# Author: adanowit@calpoly.edu
#################################################################

import socket
import time
import sys
import json
from gpioServer import handle_gpio
import RPi.GPIO as GPIO
import time

def set_pins(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin,GPIO.IN);
    x=GPIO.input(pin);
    GPIO.cleanup();
    return str(x);


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

    #########################################################################
    #Server handling portion
    #########################################################################
    #Wait for a socket connection from PHP
    while True:
        conn, addr = sock.accept()
    
        #Loop on requests from php. PHP can break connection with command
        #"end_session."
        while True:
            data = conn.recv(1024) #Grab 1024 bytes from the socket

            #print to the command line (debugging)
            #sys.stderr.write("\nGot data: " +str(data) + "\n")
            

            ####
            # Try to interpret command as json. If a non-json command is
            # recieved, close the connection.
            ####
            try:
                cmd = json.loads(data)
            except ValueError:
                sys.stderr.write("Client sent non-json data. This may occur "+\
                                 "if client closed socket without sending "+\
                                 "'end_session' command")
                break
            
            #If we reiceve the "end_session" close the connection
            if (cmd == "end_session"):
                break

            #Default "op failed" return value
            ret_val = set_pins(int(cmd));

            ##################################
            # Code handling: This file only takes and routes requests
            # to the appropriate python modules. Add code here to
            # accept more command types!
            ##################################
            
          
            #Convert the return value back into json
            ret_json = json.dumps(ret_val)

            #sys.stderr.write("\nSent data: " + ret_json + "\n")
            #send the return value back to the requester (php)
            conn.send(str(ret_json))
        
        # Once the client has closed its session, close the connection and
        # loop back to wait for new connection requests
        conn.close()

if __name__=="__main__":
    connect()
