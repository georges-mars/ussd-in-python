<?php
// Read the variables sent via POST from our API
$sessionId   = $_POST["sessionId"];
$serviceCode = $_POST["serviceCode"];
$phoneNumber = $_POST["phoneNumber"];
$text        = $_POST["text"];
$unique ="205";
if ($text == "") {
    // This is the first request. Note how we start the response with CON
    $response  = "CON Hello and welcome to E-shamba. Are you an active user? \n";
    $response .= "1. YES \n";
    $response .= "2. no\n";

} else if ($text == "1*205") {
    // Business logic for first level response
    $response = "CON Hello and Welcome " .$unique . " what do you want to access?";
    $response .= "1.Current temp";
    $response .= "2.Current humidity";
    $response .= "3.Current light intensity";
    $response .= "4.Current pH Level";
    $response .= "5.Current fertility level";
    $response .= "6.Current soil moisture content";
   
} else if ($text == "2") {
    // Business logic for first level response
    // This is a terminal request. Note how we start the response with END
    $response ="END your unique ID is " .$unique . " kindly go back to main menu press yes then input the unique id\n ";
    
} else if  ($text == "1*205*1"){
    $temperature = "26.5";
    $response = "END Your temperature is " .$temperature;
       

} else if  ($text == "1*205*2"){
    $humidity = "65.0";
    $response = "END Your humidity is " .$humidity;

} else if  ($text == "1*205*3"){
    $lght = "20%";
    $response = "END Your lght is " .$lght;      

} else if  ($text == "1*205*4"){
    $phval = "3";
    $response = "END Your soil pH is " .$phval . ".This means that your soil is acidic and capable of growing crops such as tea, blueberries,coffe and canberries";

} else if  ($text == "1*205*5"){
    $fertilitylvl = "50%";
    $response = "END Your soil fertility level is " .$fertilitylvl . " Kindly add nitrogeneous and phospatic fertilisers to make it better.";      

} else if  ($text == "1*205*6"){
    $soilmoisture = "20%";
    $response = "END Your soil moisture content is " .$humidity . " .Kindly add more water to the soil";

}

// Echo the response back to the API
header('Content-type: text/plain');
echo $response;