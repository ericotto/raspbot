import RPi.GPIO as GPIO
import time

ledPin = 24
buttonPin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN)

try:
    while True:
        if not GPIO.input(buttonPin):
            GPIO.output(ledPin, GPIO.HIGH)
        else:
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.2)
except:
    GPIO.cleanup()
