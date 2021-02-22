# SENDING NOTIFICATIONS IS EASY

### In the ESP32_Arduino_Example file everything is described in plain english for everyone.
You will need to modify a couple lines.


## Add Your Token Here
```
char token[] = "a8d4cffa289b8979f51f02936acbed49595f26";

```

## Static Request
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
