#!/usr/bin/env python
import RPi.GPIO as GPIO
import sys
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
pinToWrite = int(sys.argv[1:][0])
etatToWrite = bool(int(sys.argv[1:][1]))
GPIO.setup(pinToWrite,GPIO.OUT)
try:
    GPIO.output(pinToWrite,etatToWrite)
    print "PIN "+str(pinToWrite)+" => "+str(etatToWrite)+" OK"
except KeyboardInterrupt:
    print "  Quit"
    GPIO.cleanup()