#!/usr/bin/env python

import RPi.GPIO as GPIO
import datetime
import time
import urllib2
import smtplib

GPIO.setmode(GPIO.BOARD)
###########
GPIO_PIR_3_1 = 16 #GPIO 04(pin 7)
###########
GPIO_PIEZO = 11 #GPIO 17

print "PIR Module + PIEZO (CTRL-C to exit)"


# Set pin as input
GPIO.setup(GPIO_PIEZO,GPIO.OUT)
###########
GPIO.setup(GPIO_PIR_3_1, GPIO.IN)

###########
lienGladys = 'http://192.168.0.101:80/event/create?token=f37322a66b39bc85f1227edae8f7383b72b5e8bb&code=motion-pir&house=1&user=1'

var = 1
###########
current_state_3_1 = 0
previous_state_3_1 = 0
###########
try:
    print "Waiting for PIR to settle ..."
	###########
    while GPIO.input(GPIO_PIR_3_1)==1:
        current_state_3_1  = 0
    print "  Ready PIR 1"
	###########
	# Extinction des outputs
    GPIO.output(GPIO_PIEZO,False)	
    while True:
        now = datetime.datetime.now()
        ticks = time.mktime(now.timetuple())
###################### PIR NUMERO 1 #########################
        time.sleep(0.1)
        current_state_3_1 = GPIO.input(GPIO_PIR_3_1)
        if current_state_3_1 == 1 and previous_state_3_1==0:
			##########
            print "  Motion detected! PIR 1"
            eventGladys = urllib2.urlopen(lienGladys)
            print("Alert : ")
            print(eventGladys.read())
			
            ticks_r = ticks + timing
            previous_state_3_1 = 1
			
            while var < 2:
	            GPIO.output(GPIO_PIEZO,True)
	            time.sleep(0.1)
	            var = var + 1
	            GPIO.output(GPIO_PIEZO,False)
	            time.sleep(0.05)
	elif current_state_3_1 == 0 and previous_state_3_1==1:
        GPIO.output(GPIO_PIEZO,False)
        previous_state_3_1=0
        var = 1
#############################################################
		
except KeyboardInterrupt:
    print "  Quit"
finally:
    GPIO.cleanup()
