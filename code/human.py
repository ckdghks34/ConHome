#<human sensor>

import RPi.GPIO as gpio
import time
import socket
from datetime import datetime

gpio.setmode(gpio.BCM)
gpio.setup(19,gpio.IN) #SONSOR

count = 0;
cli_sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)

while True:
    startTime = datetime.now()    
    if gpio.input(19) == 0 :# find human        

        while True:
            endTime = datetime.now()
            if endTime.second - startTime.second == 20 :
                print("Time OUT")
                count = 0
                break

            

            if count == 3 :
                print("count = 3")
                #socket
                msg = "5"
                cli_sock.sendto (msg.encode (), ('210.125.30.188', 8080))
                count = 0
                break

            if gpio.input(19) == 0 :
                count += 1
                print(count)
                time.sleep(0.05)   
gpio.cleanup()
