def connect(ssid,password):
    import network
    # ssid = "ROUTER_NAME_HERE"
    # password =  "PASSWORD_HERE"

    
    station = network.WLAN(network.STA_IF)
    if station.isconnected() == True:
        print("Already connected")
        return
    station.active(True)
    station.connect(ssid, password)
    while station.isconnected() == False:
        pass
    print("Connection successful")
    print(station.ifconfig())