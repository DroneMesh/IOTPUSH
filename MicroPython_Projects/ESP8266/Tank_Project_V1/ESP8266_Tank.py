from machine import Pin
import wificonnect
import uwebsockets.client
from machine import Pin, PWM
import json


# Wifi Router Information
ssid = "ROUTER_NAME_HERE"
password =  "PASSWORD_HERE"


# Your Token Found Here 
# https://iotpush.app/get-token
token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


#  You must create an ID here and Place it Below Spaces are Replaced with
# https://iotpush.app/create-sensor-control
id = 'Tank'

#  This is to Connect to Wifi
wificonnect.connect(ssid,password)


# A Function To Enable Calling The Motors Easier
class DCMotor:
    def __init__(self, pwm_pin, direction_pin1, direction_pin2):
        self.dir_pin1 = Pin(direction_pin1, mode=Pin.OUT)
        self.dir_pin2 = Pin(direction_pin2, mode=Pin.OUT)
        self.pwm_pin = Pin(pwm_pin, mode=Pin.OUT)
        self.pwm = PWM(self.pwm_pin, freq=100, duty=0)

    def forward(self):
        self.dir_pin1.on()
        self.dir_pin2.off()

    def backward(self):
        self.dir_pin1.off()
        self.dir_pin2.on()

    def stop(self):
        self.dir_pin1.off()
        self.dir_pin2.off()

    def set_speed(self, ratio):
        # Speed is from 0.0 - 1.0
        if ratio < 0:
            self.pwm.duty(0)
        elif ratio <= 1.0:
            self.pwm.duty(int(1024*ratio))
        else:
            self.pwm.duty(1024)



# Right Motor Pins For Control
# Pin 12 is for PWM / To Control Speed
# Pin 5 is to choose direction of Motor
# Pin 4 is to choose direction of Motor
# Yes we need 2 for this motor controller board
rightMotor = DCMotor(12,5,4)


# Left Motor Pins For Control
# Pin 14 is for PWM / To Control Speed
# Pin 2 is to choose direction of Motor
# Pin 13 is to choose direction of Motor
# Yes we need 2 for this motor controller board
leftMotor = DCMotor(14,2,13)



# Stop The Motors
def stop():
    rightMotor.forward()
    leftMotor.forward()
    rightMotor.set_speed(0)
    leftMotor.set_speed(0)

# Move Forward
def forward():
    rightMotor.forward()
    leftMotor.forward()
    rightMotor.set_speed(1.0)
    leftMotor.set_speed(1.0)

# Move Backward
def backward():
    rightMotor.backward()
    leftMotor.backward()
    rightMotor.set_speed(1.0)
    leftMotor.set_speed(1.0)

# Move Right
def right():
    rightMotor.backward()
    leftMotor.forward()
    rightMotor.set_speed(0.35)
    leftMotor.set_speed(0.35)     

# Move Left
def left():
    rightMotor.forward()
    leftMotor.backward()
    rightMotor.set_speed(0.35)
    leftMotor.set_speed(0.35)


# Here we connect to the server and receive the commands
def receive():
    URL = "ws://iotpush.app:8888/control/"+token+'/'+id.replace(" ",'_')
    id = id.replace(' ','_')
    print('Connected')
    with uwebsockets.client.connect(URL) as websocket:
        while True:
            command = websocket.recv()
            text_data_json = json.loads(command)
            if text_data_json['id'] == id:
                if text_data_json['message'] == '1':
                    forward()
                elif text_data_json['message'] == '2':
                    backward()
                elif text_data_json['message'] == '3':
                    left()
                elif text_data_json['message'] == '4':
                    right()
                elif text_data_json['message'] == '0':
                    stop()                




if __name__ == '__main__':
    stop()
    while True:
        try:
            print('Connecting')
            receive()
        except: 
            print('Lost Connection')
            stop()
            continue