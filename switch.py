#github.com/markcity
#useful.website
#scan GPIO ports as a switch and report on changes
import RPi.GPIO as GPIO
import time

from datetime import datetime

GPIO.setmode(GPIO.BCM) #broadcom

def setPullDown(pin):
    GPIO.setup(pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def currentTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

#list ports to scan separated by comma
ports = [26,19,13,6,5,21]
size=len(ports)
currentState = [True]*size
previousState = [True]*size

#setup ports for pull down
for p in ports:
    print(p)
    setPullDown(p)

#main routine
while True:
    i=0
    for p in ports:
     #print(str(currentState[i]))
     #print(p)
     inputState=GPIO.input(p)
     currentState[i]=inputState
     if currentState[i] != previousState[i]:
      print("Current Time =", currentTime())
      print('Button Changed '+str(p),currentState[i])
      previousState[i]=currentState[i]
     i=i+1
    time.sleep(0.1)
