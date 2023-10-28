# Your code goes here
from flask import Flask, request
app = Flask(__name__)

import os

response = ""
#///creating the methods of communiction
@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    unique = "205"
    global response
    session_id = request.values.get("sessionId", None)#/////getting the session id
    service_code = request.values.get("serviceCode", None)#//////////getting the service code
    #phone_number = request.values.get("phoneNumber", None)#getting the phone number that requested
    text = request.values.get("text", "default")#getting the request

#if their is no request/response it means he/she is in the main menu
    if text == '':
        response  = "CON Hello and welcome to E-shamba. Are you an active user? \n"
        response += "1. YES"
        response += "2. NO"


    elif text == '1':

        response = "CON Kindly input unique ID located on the left hand side of your device\n"
        response += "Unique ID \n"




    elif text == '1* 205':
        response = "CON Hello and Welcome " +unique +" what do you want to access?"
        response += "1.Current temp"
        response += "2.Current humidity"
        response += "3.Current light intensity"
        response += "4.Current pH Level"
        response += "5.Current fertility level"
        response += "6.Current soil moisture content"

    elif text == '2':
        response ="END your unique ID is located on the Left hand side of your device. Kindly go back to the main menu And input yes then insert that unique ID "
        

    elif text == '1*205*1':
        temperature = '26.5'
        response = "END Your temperature is " + temperature +" This temperature can sustain your crop and also support crops such as grapes, sukumawiki, sweatpotatoes, peanut"



    elif text == '1*205*2':
        humidity ='68.5'
        response = "END Your Humidity is " + humidity+" This humidity is too low for your plants. We suggest you set up a green house around the plant or switch to crops such as fruitnuts, watermellon which can thrive perfectly in our farm under this humidity."

    elif text == '1*205*3':
        lght='20%'
        response= "END Your light intensity is " +lght

    elif text == '1*205*4':
        phval='7'
        response ="END Your pH is " +phval +" .This means your soil is basic and capable of growing crops such as tea, coffee, blueberries"

    elif text == '1*205*5':
        fertlvl='50%'
        response ="END your soil fertility level is " +fertlvl +" kindly add nitrogeneous fertilisers to make it better and also phospatic fertilisers"

    elif text == '1*205*6':
        soilmoi='20%'
        response ="END Your soil moisture content is "+soilmoi +" kindly add water"



    return response

#Receive response from africas talking
@app.route('/call', methods=['POST'])
def call_back_client():
    return '<Response> <Dial phoneNumbers="" maxDuration="5"/></Response>'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))


