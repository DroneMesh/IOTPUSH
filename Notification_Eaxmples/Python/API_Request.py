#########    Place Top Of Python File    ###########
#  Python2 and Python3 Compatible Code
import requests

## Add Your Token Here
token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

def sendPush(title,info,color,notify):

    url = "https://iotpush.app/api/notif"
    payload='{\"ST_title\": \"'+title+ '\",\"ST_text\": \"'+info+'\",\"ST_color\": \"'+color+'\",\"BL_notify\": '+notify+'}'
    print(payload)
    headers = {
    'Authorization': 'Token '+token,
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    # If function should return status code 200
    return response.status_code

################# END OF HEADER ###################################



################# How to Run ###################################
# Now you can send notification with the below function from anywhere in your code
#
# sendPush(Param1, Param2, Param3, Param4)
#
# Param1 = This is the Title 
# Param2 = Information Body
# Param3 =  Color One of these [red,pink,green,blue,orange,purple,yellow]
# Param4 = Notify Your mobile device true or false [CASE SENSITIVE AND SPELLING MATTERS]

sendPush('Motion Sensor','Living Room Motion Detected','blue','true')

#  Its that simple I decided not to put print statements becuase I dont now if you will be running python2 or python3






