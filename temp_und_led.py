import RPi.GPIO as GPIO
from flask import Flask  
from time import sleep
from datetime import datetime


while True:
    file = open('/sys/bus/w1/devices/28-01204b476eea/w1_slave')
    content = file.read()
    file.close()
    
    pos = content.rfind('t=') + 2
    temperature_string = content[pos:]
    temperature = float(temperature_string) /1000
    print("Die Temperatur beträgt " + str(temperature) + " °C")
    sleep(2)

    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT) 
    GPIO.setup(6, GPIO.OUT) 
    GPIO.setup(22, GPIO.OUT) 
    GPIO.setup(23, GPIO.OUT) 
    GPIO.setup(24, GPIO.OUT) 
    GPIO.setup(27, GPIO.OUT) 

    GPIO.output(5, False)
    GPIO.output(6, False)
    GPIO.output(22, False)
    GPIO.output(23, False)
    GPIO.output(24, False)
    GPIO.output(27, False)


    if temperature < 10:
        GPIO.output(6, True)
       
    if temperature < 15 and temperature >= 10:
        GPIO.output(6, True)
        GPIO.output(5, True)
        
    if temperature < 20 and temperature >=15:
        GPIO.output(6, True)
        GPIO.output(5, True)
        GPIO.output(24, True)
        
    if temperature < 25 and temperature >=20:
        GPIO.output(6, True)
        GPIO.output(5, True)
        GPIO.output(24, True)
        GPIO.output(23, True)

    if temperature < 30 and temperature >=25:
        GPIO.output(6, True)
        GPIO.output(5, True)
        GPIO.output(24, True)
        GPIO.output(23, True)
        GPIO.output(27, True)
        
    if temperature >=30:
        GPIO.output(6, True)
        GPIO.output(5, True)
        GPIO.output(24, True)
        GPIO.output(23, True)
        GPIO.output(27, True)
        GPIO.output(22, True)
    
    now = datetime.now()

    timestamp = now.strftime("%H:%M:%S")
    
        # to open/create a new html file in the write mode
    f = open('../../../var/www/html/nubt_temp.html', 'w', )
      
    # the html code which will go in the file GFG.html
    html_template = """<html>
    <meta charset="utf-8">
    <head>
    <title>TT_rulez</title>
    
    <style>
      h1 {color:red;}
      p {color:blue;}
      body {text-align: center;
              background-image: linear-gradient(90deg, #228b22 10%, #32cd32 50%,#228b22 90%);}
    </style>
    
    </head>
    <body>
    
    <br><br><br><br><br><br>
    <h1 font color="blue">Welcome To Temperature Today...</h1>
      
    <p>...where the Entropy is high, and so are the developers.</p>
    <br>
    <h3>Your Temperature is:   """ + str(temperature) + """  °C</h3>
    <div>Last Update: """ + str(timestamp) + """</div><br>
    
    <p> For temperature update reload page! </p>
    <input type='button' value="Reload Page" style="background-color:red" onclick="location.reload()"  />
      
    </body>
    </html>
    """
      
    # writing the code into the file
    f.write(html_template)
      
    # close the file
    f.close()

