# Your code goes here
from flask import Flask, request
app = Flask(__name__)
#import <cs50.h>
#

response = ""
#///creating the methods of communiction
@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global unique  = "205"
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

        response = "CON Kindly input unique ID \n"
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
        response ="END your unique ID is " +unique+" kindly go back to main menu press yes then input the unique id "
        response += "00)main menu"

    elif text == '2*00':
        response += ussd_callback()


    elif text == '1*205*1':
        temperature = '26.5'
        response = "END Your temperature is " + temperature



    elif text == '1*205*2':
        humidity ='68.5'
        response = "END Your Humidity is " + humidity

    elif text == '1*205*3':
        lght='20%'
        response= "END Your light intensity is " +lght

    elif text == '1*205*4':
        phval='7'
        response ="END Your pH is " +phval +" .This means your soil is acidic and capable of growing crops such as tea, coffee, blueberries"

    elif text == '1*205*5':
        fertlvl='50%'
        response ="END your soil fertility level is " +fertlvl +" kindly add nitrogeneous fertilisers to make it better and also phospatic fertilisers"

    elif text == '1*205*6':
        soilmoi='20%'
        response ="END Your soil moisture content is "+soilmoi +" kindly add water"



    return response
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))


