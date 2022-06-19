import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)

def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN,old_settings)
    return ch

#Motor 1 or Left Motor
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
#Motor 2 or Right Motor
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)

#Turning Right
def right():
    GPIO.output(20,GPIO.LOW)
    GPIO.output(21,GPIO.HIGH)
    GPIO.output(2,GPIO.LOW)
    GPIO.output(3,GPIO.LOW)
    time.sleep(1)

#Turning Left
def left():
    GPIO.output(2,GPIO.LOW)
    GPIO.output(3,GPIO.HIGH)
    GPIO.output(20,GPIO.LOW)
    GPIO.output(21,GPIO.LOW)
    time.sleep(1)

#Going strait
def strait():
    GPIO.output(21,GPIO.HIGH)
    GPIO.output(20,GPIO.LOW)
    GPIO.output(3,GPIO.HIGH)
    GPIO.output(2,GPIO.LOW)
    time.sleep(1)

#Going reverse
def reverse():
    GPIO.output(20,GPIO.HIGH)
    GPIO.output(21,GPIO.LOW)
    GPIO.output(2,GPIO.HIGH)
    GPIO.output(3,GPIO.LOW)
    time.sleep(1)

#Stop
def stop():
    GPIO.output(20,GPIO.HIGH)
    GPIO.output(21,GPIO.HIGH)
    GPIO.output(2,GPIO.HIGH)
    GPIO.output(3,GPIO.HIGH)
    time.sleep(1)
