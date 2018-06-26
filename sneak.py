import RPi.GPIO as GPIO
import time
from email.mime.text import MIMEText

# Set Broadcom mode so we can address GPIO pins by number.
GPIO.setmode(GPIO.BCM) 

# This is the GPIO pin number we have one of the door sensor
# wires attached to, the other should be attached to a ground 
pin.DOOR_SENSOR_PIN = 18

#Set up the door sensor pi
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

oldIsOpen = None
isOpen = None


while True: 
    oldIsOpen = isOpen 
    isOpen = GPIO.input(DOOR_SENSOR_PIN)  
    if (isOpen and (isOpen != oldIsOpen)):  
        print "Space is unoccupied!"  
        GPIO.output(RED_LIGHT, False)  
        GPIO.output(GREEN_LIGHT, True) 
    elif (isOpen != oldIsOpen):  
        print "Space is occupied!"  
        GPIO.output(GREEN_LIGHT, False)  
        GPIO.output(RED_LIGHT, True)  
    time.sleep(0.1)
