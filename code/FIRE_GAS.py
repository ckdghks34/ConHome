#client UDP

import socket
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(19,gpio.IN) #gas
gpio.setup(18,gpio.IN) #fire

cli_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        if gpio.input(19) == 1 : # GAS ON
            msg="3";
            #cli_sock.sendto(msg.encode(),('210.125.30.188',8080)) 
            print ("GAS")
            time.sleep(1)
        if gpio.input(19) == 0 :
        ##    print("OFF")
            time.sleep(0.5)
        if gpio.input(18) == 0 : # FIRE ON
            print("LIGHT ON")
            msg="4";
            cli_sock.sendto(msg.encode(),('210.125.30.188',8080))
            time.sleep(5)

except KeyboardInterrupt :
    gpio.cleanup()

///GAS,FIRE
