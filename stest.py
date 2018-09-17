#!/usr/bin/env python
import time
import PID
import serial
import matplotlib.pyplot as plt
from drawnow import *
from time import sleep
values = []


ser = serial.Serial(
 port='/dev/ttyACM0',
 baudrate = 9600,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=0.4
)

plt.ion()
cnt=0.0	
count = 1
pid = PID.PID(0.8, 0.1, 0.0002)
pid.SetPoint=25.0
pid.setSampleTime(0.1)
output = 0.0
for i in range(0,2):
	values.append(0.0)
def plotValues():
    plt.title('Serial value from Nucleo')
    plt.grid(True)
    plt.ylabel('Values')
    plt.plot(values, 'rx-', label='values')
    plt.legend(loc='upper right')
    plt.ylim(0, 80) 

	
while 1:
	x=ser.readline()
	
	cnt = float(x)
	pid.update(cnt)
	output = pid.output
	  
	cnt +=  (output)
	print x + " : " + str(cnt)
	values.append(cnt)
	values.pop(0)
	count += 1
	#drawnow(plotValues)


	
	        
	