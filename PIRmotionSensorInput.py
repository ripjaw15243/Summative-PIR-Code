# Raspberry Pi GPIO input from PIR motion sensor
# This program will receive an input if the PIR motion sensor senses motion
# or movement and then sends the input to the raspberry pi connected with
# the camera module.

import RPi.GPIO as GPIO
import time
import network
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(3, GPIO.OUT)

def heard(phrase):
    print("Donggi: " + phrase)

if (len(sys.argv) >= 2):
    network.call(sys.argv[1], whenHearCall=heard)
else:
    network.wait(whenHearCall=heard)
    
while network.isConnected():
    
    i = GPIO.input(11)

    if (i == 0):
        print ("No intruders")

        GPIO.output(3,0)
        time.sleep(1.5)

        word = "off"

        network.say(word)
    elif (i == 1):
        print ("Intruder detected")

        GPIO.output(3,1)
        time.sleep(1.5)

        word = "on"

        network.say(word)
        
    
    
            
            
