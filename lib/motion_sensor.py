#!/usr/bin/env python

import RPi.GPIO as GPIO
import datetime
import time
import urllib2
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

GPIO.setmode(GPIO.BOARD)
# Define GPIO to use on Pi

###########
GPIO_PIR_3_1 = 16 #GPIO 04(pin 7)
GPIO_PIR_3_2 = 15 #GPIO 22(pin 15)
###########
GPIO_RELAIS = 13 #GPIO 27
GPIO_PIEZO = 11 #GPIO 17

print "PIR Module + PIEZO (CTRL-C to exit)"


# Set pin as input
GPIO.setup(GPIO_PIEZO,GPIO.OUT)
GPIO.setup(GPIO_RELAIS,GPIO.OUT)
###########
GPIO.setup(GPIO_PIR_3_1, GPIO.IN)
GPIO.setup(GPIO_PIR_3_2, GPIO.IN)
###########
lienGladys = 'http://192.168.0.101:80/event/create?token=f37322a66b39bc85f1227edae8f7383b72b5e8bb&code=motion-pir&house=1&user=1'
# lien_ispy = 'http://192.168.0.100:8080/'
# lien_web = 'http://192.168.0.100/'

oid_1 = '0'
oid_2 = '0'

oid_1 = '3'
oid_2 = '3'

var = 1
timing = 120
timing_relais = 120
h_start_relais = 18 # 18h debut
h_stop_relais = 6 # 6h fin

current_state_RELAIS = 0

###########
current_state_3_1 = 0
previous_state_3_1 = 0
###########

ticks_r = 0
ticks_relais = 0
relais = False
record = False

def start_relais():
	GPIO.output(GPIO_RELAIS,True)
	return("Start Relais...OK.")
def stop_relais():
	GPIO.output(GPIO_RELAIS,False)
	return("Stop Relais...OK.")
def send_mail(name,time):
	fromaddr = "swager974@gmail.com"
	toaddr = "swager974@gmail.com"
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = str(time) + "ALERT PIR SENSOR " + name
	body = str(time) + "Detecteur de mouvement PIR " + name
	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "zzbjoqhasagggsdz")
	text = msg.as_string()
	sending = server.sendmail(fromaddr, toaddr, text)
	server.quit()
	return sending
try:
    print "Waiting for PIR to settle ..."
	###########
    while GPIO.input(GPIO_PIR_3_1)==1:
        current_state_3_1  = 0
    print "  Ready PIR 1"
	###########
    send_mail("INITIALISATION DU SCRIPT...",datetime.datetime.now())
	# Extinction des outputs
    GPIO.output(GPIO_PIEZO,False)
   	# Loop until users quits with CTRL-C
	
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
            send_mail("PIR 1 ENTJUL",now)
	elif current_state_3_1 == 0 and previous_state_3_1==1:
             GPIO.output(GPIO_PIEZO,False)
             previous_state_3_1=0
             var = 1
#############################################################
		
except KeyboardInterrupt:
    print "  Quit"
finally:
    GPIO.cleanup()
