# Project 001 Cloud LED Control

## [VIDEO TUTORIAL](http://youtube.com/dronemesh)

## Setup
### Add your Wifi Informationn, Token and Device ID in [main.py](main.py)
```
#  WIFI ROUTER INFORMATION
ssid = "YOUR_SSID"
password =  "YOUR_PASSWORD"


# Token HERE 
#  You can get it from here https://iotpush.app/get-token
token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# ID You Created Here 
# https://iotpush.app/create-sensor-switch
id = 'LED'
```


# Flashing the files
```
# Install Tool For flashing
pip install adafruit-ampy

# Make sure to use the correct COM Port
# If ampy.exe does not work try ampy.py

# Create Directory In ESP called uwebsockets
ampy.exe --port com3 mkdir uwebsockets

# Upload the files to ESP for websocket connections
ampy.exe --port com3 put .\uwebsockets\client.py uwebsockets/client.py
ampy.exe --port com3 put .\uwebsockets\protocol.py uwebsockets/protocol.py

# Uploading main.py when finished editing with your config
ampy.exe --port com3 put .\main.py main.py

```



