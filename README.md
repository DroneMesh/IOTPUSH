# IOT PUSH Documentation
System is designed to send push notification to your IOS and or Android Device. It also saves all your notifications to view whenever you would like. You can view your notification from either the web panel and or your phone.
1. [Android APP LINK]
2. [IOS APP LINK]
3. [WEB Pannel LINK](https://iotpush.app)

Everything is sent over SSL Protocol.

## Getting Started

1. Create an account through the [Android_APP]() , [IOS_APP]() or the [WebPanel](https://iotpush.app)
2. If you would like to receive the notifiations on your phone you must have the app installed be and be logged in to your account

# Grab Your Token 

### Android & IOS Token will be available on Home Screen

<img src="./images/setup.jpg" alt="My cool logo" width="350"/>

### Web Admin Panel
Admin Panel Token will he located [HERE](https://iotpush.app/get-token)

<img src="./images/setup2.png" alt="My cool logo" width="350"/>


# How To Send The Notification ESP32 
1. Check out the examples folder [HERE](https://github.com/DroneMesh/IOTPUSH/tree/master/Examples)


# SENDING NOTIFICATIONS IS EASY

### In the ESP32_Arduino_Example file everything is described in plain english for everyone.
You will need to modify a couple lines.


## Add Your Token Here
```
char token[] = "a8d4cffa289b8979f51f02936acbed49595f26";

```

# Static Request
### Static Request Is Great For Sensors that dont relay back dynamic or changing data such as a Motion Sensor or Door Sensor
```
// ------  Static Request -------
// Title of Notification EX: Motion Sensor
char title[] = "Motion Sensor";

// Description of Notification EX: Motion Detected In Living Room
char desc[] = "Motion Detected In Living Room";

// Color of Notification: red, purple, yellow, green, blue, pink, orange
// If no color specified it will default to red
char color[] = "pink";

// Gourping Notifications in phone notification bar
// Leave it Defualt Unless you know what you are doing
char group[] = "1";

// Send Phone Push Notification Alert 
// If false it will still write the notification in the app and webapp but you will not receive notification
// If true it will notify your phone with a push notification
// "true" or "false"
/* IMPORTANT THIS MUST BE SPELLED CORRECTLY  */
/* true or false  */
char notify[] = "true";
// ------  END Static Request -------
```
## Send Static The Notification
### You will want to call this function below when for example the motion detector has been trigered and it will send the static notification you have setup above

```
sendStatic();
```

# Dynamic Request
### Dynamic Request is great if you are using something like a temprature sensor where the data is changing. To call this function it's very simple and done in one line of code
```
// sendCustom("TITLE","INFORMATION","COLOR","SEND_ALERT_TO_PHONE");
sendCustom("Temp Sensor #1","Current Temprature -5c","blue","true");
```
1. TITLE = 'Title Of Notification'
2. INFORMATION = 'THE SENSORS DATA YOU WANT SEND TO YOU'
3. COLOR = 'Colors of notification check the list below for available Colors'
4. SEND_ALERT_TO_PHONE = 'If you want your phone to get the notification alert set to true else false'




# AVAILBLE COLORS
## [red, blue, green, pink, purple, yellow, orange]
