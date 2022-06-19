import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)#green1
GPIO.setup(20,GPIO.OUT)#yellow1
GPIO.setup(16,GPIO.OUT)#red1

GPIO.setup(26,GPIO.OUT)#red2
GPIO.setup(13,GPIO.OUT)#yellow2
GPIO.setup(19,GPIO.OUT)#green2

GPIO.setup(6,GPIO.IN)
while 1:
    a=GPIO.input(6)
    print(a)
    

    if a==0:        
        GPIO.output(21,GPIO.HIGH)
        GPIO.output(26,GPIO.HIGH)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(19,GPIO.LOW) 
    elif a==1:
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)
        GPIO.output(21,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
