#<button sensor>

import RPi.GPIO as gpio
import time
import socket

gpio.setmode(gpio.BCM)
gpio.setup(12,gpio.IN) #SONSOR

cli_sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
flag = True

while True:
    if gpio.input(12) == 0 :
        #print ("ON")
        print("ON")
        msg = "2"
        cli_sock.sendto (msg.encode(), ('210.125.30.188', 8080))
        time.sleep(1)
gpio.cleanup()
