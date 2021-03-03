# Flashing MicroPython With VSCode

### All Future projects will be done with the exact products below
1. [ESP8266](https://bit.ly/3rdAgS0)
2. [ESP32](https://bit.ly/37OPvcJ)


## Software Links
1. [vscode](https://code.visualstudio.com/Download)
2. [python](https://www.python.org/downloads/release/python-377/)
3. [esp32 firmware](https://micropython.org/download/esp32/)
4. [esp8266 firmware](https://micropython.org/download/esp8266/)


# Commands After Installation and setting up Windows Enviroment Path
**FOLLOW THE VIDEO BEFORE THIS STEP**

```
pip install --user --upgrade pip
pip install esptool
```
# ESP32 Flashing Commands
```
esptool --chip esp32 --port com8 erase_flash
esptool --chip esp32 --port com8 --baud 460800 write_flash -z 0x1000 esp32.bin
```
# ESP8266 Flashing
```
esptool --port com8 erase_flash
esptool --port com8 --baud 460800 write_flash --flash_size=detect 0 esp8266.bin
```

# *** IMPORTANT STEP  ***
## If Arduino serial monitor writing wierd characters then change the bottom dropdown box to 1152000

# Video Tutorial
[VIDEO TUTORIAL LINK HERE](https://youtu.be/1R_1n0vhRxI)