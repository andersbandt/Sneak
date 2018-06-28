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

#INFO FOR SENDING TEXT METHOD
me = "your email"
to = ""your phone number"@vtext.com"
login = "your gmail address"
password = "your password"
smptserver = "smtp.gmail.com:587"

#SENDING TEXT METHOD
def sendemail(sender, to, message, login, password, smptserver):
	server = smtplib.SMTP(smptserver)
	server.starttls()
	server.login(login,password)
	problems = server.sendmail(sender, to, message) 

message1 = "g"
    
    
while True: 
    oldIsOpen = isOpen 
    isOpen = GPIO.input(DOOR_SENSOR_PIN)  
    if (isOpen and (isOpen != oldIsOpen)):  
        print "Door has opened!"  
        sendemail(me, to, message, login, password, smptserver)
    elif (isOpen != oldIsOpen):  
        print "Door has closed"  
        GPIO.output(GREEN_LIGHT, False)  
        GPIO.output(RED_LIGHT, True)  
    time.sleep(0.1)
