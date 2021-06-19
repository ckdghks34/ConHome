#Sever Raspberry
 
#server UDP
import socket
import RPi.GPIO as gpio
import time
from datetime import datetime
 
######################################################
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)
gpio.setup(17,gpio.OUT)
gpio.setup(27,gpio.OUT)
gpio.setup(22,gpio.OUT)
 
server_sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
server_sock.bind( ('210.125.30.188', 8080) )  # 서버 IP, 포트번호 바인딩
flag = True
while flag : 
    data, addr = server_sock.recvfrom(200)
    f = open("Log.txt", 'a')
    now = datetime.now()
    #print (now)
    #print ("Server is received data : ", data.decode() )
    print ("IP : " + addr[0])   
    if (int)(data.decode()) == 2 :
        print(str(now) + "\t BUTTON")
        f.write(str(now) + "\t" + data.decode() + "\t BUTTON\n")
    if (int)(data.decode()) == 3 :
        print(str(now) + "\t GAS")
        f.write(str(now) + "\t" + data.decode() + "\t GAS\n")
    if (int)(data.decode()) == 4 :
        print(str(now) + "\t FIRE")
        f.write(str(now) + "\t" + data.decode() + "\t FIRE\n")
    if (int)(data.decode()) == 5 :
        print(str(now) + "\t LAY")
        f.write(str(now) + "\t" + data.decode() + "\t LAY\n")
    
    
    a = (int)(data.decode());
    for i in range(0,3):
        for j in range (0, a):
            gpio.output(18, True)
            gpio.output(17,True)
            gpio.output(27,True)
            gpio.output(22,True)
            time.sleep(0.5);
            gpio.output(18, False)
            gpio.output(17,False)
            gpio.output(27,False)
            gpio.output(22,False)
            time.sleep(0.5);
        time.sleep(1);
 
    
    f.close()
gpio.cleanup()
