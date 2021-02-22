/*

  Author: DroneMesh
  Original Code Source Author: Rui Santos

---------------------------------------

  This code has been modified by DroneMesh to work with the IOT notify System

---------------------------------------

  Autor of original C code
  Rui Santos
  Complete project details at Complete project details at https://RandomNerdTutorials.com/esp32-http-get-post-arduino/

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files.

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

---------------------------------------  
*/

#include <WiFi.h>
#include <HTTPClient.h>
#include <stdio.h> 
#include <string.h> 

// Wifi Information
const char* ssid = "YOUR WIFI ROUTER NAME";
const char* password = "YOUR WIFI PASSWORD";

// Place your Token Here Found in Android Or Iphone and or WebPanel https://iotpush.app/get-token
char token[] = "a8d4cffa289b8979f51f02936acbed49595f26";

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


// ---  Timer if Needed
// the following variables are unsigned longs because the time, measured in
// milliseconds, will quickly become a bigger number than can be stored in an int.
unsigned long lastTime = 0;
// Timer set to 10 minutes (600000)
//unsigned long timerDelay = 600000;
// Set timer to 10 seconds (10000)
unsigned long timerDelay = 10000;




// Dont Change Server Link
const char* serverName = "https://iotpush.app/api/notif";

// Post Array Init DONT TOUCH
char post[500];


void setup() {
  // Don't Touch This Area Unless You Need To
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
  Serial.println("Timer set to 5 seconds (timerDelay variable), it will take 5 seconds before publishing the first reading.");
}

void loop() {
  //Send an HTTP POST request every 10 minutes
  if ((millis() - lastTime) > timerDelay) {

    // Call Static will send everything you entered in the top of the file
    sendStatic();

    // Call Custom Function to send Custom sensor data
    // sendCustom("TITLE","INFORMATION","COLOR","SEND PHONE NOTIFICATION");
    sendCustom("Temp Sensor #1","Current Temprature -5c","blue","true");
    
    // Reset Timer
    lastTime = millis();
  }
}

void sendStatic(){

    if(WiFi.status()== WL_CONNECTED){
      // Preparing Data 
      // Combine Token For Header
      char tok[500] = "Token ";
      strcat(tok, token);

      // Init Http Client
      HTTPClient http;
      
      // Your Domain name with URL path or IP address with path
      http.begin(serverName);

      // Specify content-type header
      http.addHeader("Content-Type", "application/x-www-form-urlencoded");
          
      // Token Header
      http.addHeader("Authorization", tok);

      // Post Data
      strcat(post, "ST_title=");
      strcat(post, title);
      strcat(post, "&ST_text=");
      strcat(post, desc);
      strcat(post, "&ST_color=");
      strcat(post, color);
      strcat(post, "&BL_notify=");
      strcat(post, notify);
      strcat(post, "&OneID_group=");
      strcat(post, group);
      

      // Data to send with HTTP POST
      char httpRequestData[500] = "ST_title=Sensor ESP32&ST_text=KAKA MONSTER&ST_color=yellow&BL_notify=false";           
     
      // Send HTTP POST request
      int httpResponseCode = http.POST(post);

      // Response 200 Means Notification Sent
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
        
      // Free resources
      http.end();
    }
    else {
      Serial.println("WiFi Disconnected");
    }
}




void sendCustom(char title[],char desc[],char color[],char notify[]){

    if(WiFi.status()== WL_CONNECTED){
      // Preparing Data 
      // Combine Token For Header
      char tok[500] = "Token ";
      strcat(tok, token);
      
      // Init Http Client
      HTTPClient http;
      
      // Your Domain name with URL path or IP address with path
      http.begin(serverName);

      // Specify content-type header
      http.addHeader("Content-Type", "application/x-www-form-urlencoded");
          
      // Token Header
      http.addHeader("Authorization", tok);
      // Post Data
      strcat(post, "ST_title=");
      strcat(post, title);
      strcat(post, "&ST_text=");
      strcat(post, desc);
      strcat(post, "&ST_color=");
      strcat(post, color);
      strcat(post, "&BL_notify=");
      strcat(post, notify);

     
      // Send HTTP POST request
      int httpResponseCode = http.POST(post);
      
      Serial.print("HTTP Response code: ");
      // Response 200 Means Notification Sent
      Serial.println(httpResponseCode);
        
      // Free resources
      http.end();
    }
    else {
      Serial.println("WiFi Disconnected");
    }
}