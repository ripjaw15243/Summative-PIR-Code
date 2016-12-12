# Prototype
# Raspberry Pi GPIO input from PIR motion sensor
# This program will receive an input if the PIR motion sensor senses motion
# or movement and then sends the input to the raspberry pi connected with
# the camera module.

i = 0
word = ""
import RPi.GPIO as GPIO
import network
import sys
from gpiozero import MotionSensor

pir = MotionSensor(4)

def heard(phrase):
    print("Donggi: " + phrase)

if (len(sys.argv) >= 2):
    network.call(sys.argv[1], whenHearCall=heard)
else:
    network.wait(whenHearCall=heard)
    
while network.isConnected():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.IN)

    i = GPIO.input(7)

    if (i == 0):
        print ("No motion detected.")

        word = "off"

        network.say(word)
    elif (i == 1):
        print ("Motion detected!")

        word = "on"

        network.say(word)
        
    
    
            
            
