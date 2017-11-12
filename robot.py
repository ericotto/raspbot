import RPi.GPIO as GPIO

class Motor:

    def __init__(self):

        self.left_pin_one = 20
        self.left_pin_two = 21
        self.right_pin_one = 23
        self.right_pin_two = 24

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left_pin_one, GPIO.OUT)
        GPIO.setup(self.left_pin_two, GPIO.OUT)
        GPIO.setup(self.right_pin_one, GPIO.OUT)
        GPIO.setup(self.right_pin_two, GPIO.OUT)

    def forward(self):
        GPIO.output(self.left_pin_one, GPIO.HIGH)
        GPIO.output(self.right_pin_one, GPIO.HIGH)

    def reverse(self):
        GPIO.output(self.left_pin_two, GPIO.HIGH)
        GPIO.output(self.right_pin_two, GPIO.HIGH)

    def right(self):
        GPIO.output(self.left_pin_one, GPIO.HIGH)
        GPIO.output(self.right_pin_two, GPIO.HIGH)

    def left(self):
        GPIO.output(self.left_pin_two, GPIO.HIGH)
        GPIO.output(self.right_pin_one, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.left_pin_one, GPIO.LOW)
        GPIO.output(self.left_pin_two, GPIO.LOW)
        GPIO.output(self.right_pin_one, GPIO.LOW)
        GPIO.output(self.right_pin_two, GPIO.LOW)
