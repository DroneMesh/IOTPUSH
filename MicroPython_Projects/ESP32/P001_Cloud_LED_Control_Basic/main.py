# Project #1 LED Cloud Control With IOTPUSH

import network
from machine import Pin
import uwebsockets.client
from machine import Pin, PWM
import json 
import time

#  WIFI ROUTER INFORMATION
ssid = "YOUR_SSID"
password =  "YOUR_PASSWORD"


# Token HERE 
#  You can get it from here https://iotpush.app/get-token
token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# ID You Created Here 
# https://iotpush.app/create-sensor-switch
id = 'LED'

# Pin we want to control is pin 2 and se set it as an OUTPUT to Turn on the Built in LED
led = Pin(2, Pin.OUT)


#  Wifi Connection No Need To Touch This
station = network.WLAN(network.STA_IF)
if station.isconnected() == True:
    print("Already connected")
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
    pass
print("Connection successful")
print(station.ifconfig())



def receive():
    URL = "ws://iotpush.app:8888/basic/"+token+'/'
    with uwebsockets.client.connect(URL) as websocket:
        print('Connected')

        while True:
            # Here we listen for data from the server
            command = websocket.recv()
            
            # Once we get data we convert it to json 
            # Make our life easier
            text_data_json = json.loads(command)

            # Here we Print Out the Data from server 
            print(text_data_json)

            # Take the ID from the data and name it recv_id
            recv_id = text_data_json['id'] 

            # Take the message from data that is in charge of our control
            message = text_data_json['message']


            # Check if the ID received is the Same as device ID 
            # We do this because we will be adding more devices here
            # This way each device can listen to its command
            if recv_id == id:
                
                # If recv_id matches this device id we read the message
                # The app in this mode will only send 1 or 0
                # So if message is 0 we want to turn on the led
                if message == '0':
                    led.off()
                
                # If message is 1 we want to turn on the led
                elif message == '1':
                    led.on()



# Keeps this script running in a loop forever
if __name__ == '__main__':
    print('SLEEPING 2 Seconds')
    # Loop forever
    while True:
        time.sleep(2)
        try:
            print('Connecting')
            #  We call the receive funtion that controls the LED
            receive()
        except: 
            # On any error print this message and restart loop
            print('Lost Connection')
            continue